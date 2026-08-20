#!/usr/bin/env bash
# Run the full Ollama-driven process generation, unattended, safely.
#
# - Starts Ollama (if not already running) with single-model, no-concurrency
#   settings so it can't multiply RAM usage on a 16GB machine.
# - caffeinate keeps the Mac from sleeping for the life of the run -- sleep
#   would otherwise kill Ollama mid-generation.
# - nohup + disown detaches the pipeline from this shell, so closing the
#   terminal window (or losing the SSH session) does not stop it.
# - Everything is logged to logs/run-<timestamp>.log.
#
# Usage:
#   ./scripts/run_overnight.sh                # run everything remaining
#   ./scripts/run_overnight.sh --max 20        # just the next 20 (good for a first test)
#   ./scripts/run_overnight.sh --push-every 3  # push every 3 processes instead of every 1
set -euo pipefail
cd "$(dirname "$0")/.."

LOG="logs/run-$(date +%Y%m%d-%H%M%S).log"
mkdir -p logs

echo "=== Air Canada wiki -- Ollama generation run ==="
echo "Log file: $LOG"

# --- Ollama safety: one model, no concurrent requests, on this 16GB machine ---
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_KEEP_ALIVE=30m

if curl -s -m 3 http://localhost:11434/api/version >/dev/null 2>&1; then
  echo "Ollama already running."
else
  echo "Starting Ollama..."
  nohup ollama serve > logs/ollama-serve.log 2>&1 &
  disown
  for i in $(seq 1 30); do
    if curl -s -m 3 http://localhost:11434/api/version >/dev/null 2>&1; then
      echo "Ollama ready."
      break
    fi
    sleep 1
  done
fi

if ! curl -s -m 5 http://localhost:11434/api/version >/dev/null 2>&1; then
  echo "ERROR: Ollama did not come up. Check logs/ollama-serve.log"
  exit 1
fi

echo
echo "Reminder: if you have Time Machine backing up this Mac, exclude the Ollama"
echo "model volume so a backup window doesn't compete with model loading:"
echo "  tmutil addexclusion \"$(readlink -f ~/.ollama/models 2>/dev/null || echo '~/.ollama/models')\""
echo

echo "Launching pipeline (detached) -- python3 scripts/run_ollama_pipeline.py $*"
nohup caffeinate -dimsu python3 scripts/run_ollama_pipeline.py "$@" >> "$LOG" 2>&1 &
PID=$!
disown

echo "$PID" > logs/pipeline.pid
echo
echo "=== Running in the background as PID $PID ==="
echo "You can close this terminal window now -- it will keep running."
echo
echo "Monitor with:"
echo "  tail -f $LOG"
echo "  ./scripts/check_progress.sh"
echo
echo "Live site (watch it grow):  https://ghatk047.github.io/AirCanadaProcessWiki/"
echo
echo "Stop it cleanly with:  kill -TERM $PID   (finishes the current process, then exits)"
