# -*- coding: utf-8 -*-
"""
Recompute the "mermaid" field for every already-generated process using the
current content_lib.build_mermaid -- no Ollama call, just re-deriving the
diagram from the step/phase data already sitting in data/processes.json.

Run this after any layout change to content_lib.build_mermaid (or the
sanitiser) so existing processes pick up the fix without burning a single
Ollama generation. render_diagrams.py's content hash will then pick up the
changed mermaid strings automatically on the next render pass.

Usage:
  python3 scripts/rebuild_diagrams.py
  python3 scripts/render_diagrams.py      # re-renders only what changed
  python3 scripts/build_site.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from content_lib import build_mermaid
from sanitise_mmd import sanitise_mermaid, validate

DATA = os.path.join(ROOT, "data", "processes.json")


def main():
    if not os.path.exists(DATA):
        print("No data/processes.json yet -- nothing to rebuild.")
        return

    with open(DATA, encoding="utf-8") as f:
        content = json.load(f)

    changed = 0
    for pid, entry in content.items():
        if "phases" not in entry or "l4_steps" not in entry:
            continue
        old = entry.get("mermaid", "")
        new = sanitise_mermaid(build_mermaid(entry["phases"], entry["l4_steps"]))
        problems = validate(new)
        if problems:
            print(f"  SKIP {pid}: new mermaid failed validation: {problems}")
            continue
        if new != old:
            entry["mermaid"] = new
            changed += 1

    tmp = DATA + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=1)
    os.replace(tmp, DATA)

    print(f"Rebuilt mermaid for {changed}/{len(content)} processes (layout/curve change).")
    print("Next: python3 scripts/render_diagrams.py   (re-renders only the changed ones)")


if __name__ == "__main__":
    main()
