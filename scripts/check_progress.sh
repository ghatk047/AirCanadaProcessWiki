#!/usr/bin/env bash
# Quick status check for the running (or last-run) Ollama generation pipeline.
cd "$(dirname "$0")/.."

echo "=== Process completion ==="
python3 - <<'PY'
import json, sys, os
sys.path.insert(0, "scripts")
from taxonomy import all_processes
import llm_content

procs = all_processes()
content = json.load(open("data/processes.json", encoding="utf-8")) if os.path.exists("data/processes.json") else {}
done = [p for p in procs if llm_content.is_done(content.get(p["pid"]))]
print(f"{len(done)}/{len(procs)} complete at full depth ({llm_content.MODEL})")

if os.path.exists("data/.generation_failures.json"):
    fails = json.load(open("data/.generation_failures.json", encoding="utf-8"))
    if fails:
        print(f"{len(fails)} failed after max retries: {', '.join(sorted(fails.keys()))}")

if done:
    import statistics
    steps = [len(content[p["pid"]]["l4_steps"]) for p in done]
    phases = [len(content[p["pid"]]["phases"]) for p in done]
    secs = [content[p["pid"]].get("gen_seconds", 0) for p in done]
    print(f"avg steps/process: {statistics.mean(steps):.1f}   avg phases: {statistics.mean(phases):.1f}")
    print(f"avg generation time: {statistics.mean(secs):.0f}s   "
          f"est. remaining: {statistics.mean(secs) * (len(procs)-len(done)) / 3600:.1f}h "
          f"at current pace for {len(procs)-len(done)} remaining")
PY

echo
echo "=== Pipeline process ==="
if [ -f logs/pipeline.pid ]; then
  PID=$(cat logs/pipeline.pid)
  if ps -p "$PID" > /dev/null 2>&1; then
    echo "Running as PID $PID"
  else
    echo "Not running (last PID $PID has exited)"
  fi
fi

echo
echo "=== Ollama server ==="
curl -s -m 3 http://localhost:11434/api/version 2>/dev/null && echo " -- reachable" || echo "not reachable"

echo
echo "=== Latest log lines ==="
LATEST=$(ls -t logs/run-*.log 2>/dev/null | head -1)
if [ -n "$LATEST" ]; then
  echo "($LATEST)"
  tail -15 "$LATEST"
fi

echo
echo "=== Git / GitHub Pages ==="
git log --oneline -5
echo "Live: https://ghatk047.github.io/AirCanadaProcessWiki/"
