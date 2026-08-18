# -*- coding: utf-8 -*-
"""Compile all authored content modules into data/processes.json."""
import importlib, json, os, pkgutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import content_lib
from taxonomy import all_processes

CONTENT_DIR = os.path.join(HERE, "content")


def main():
    mods = sorted(m.name for m in pkgutil.iter_modules([CONTENT_DIR]))
    for name in mods:
        importlib.import_module(f"content.{name}")

    valid = {p["pid"]: p for p in all_processes()}
    unknown = [pid for pid in content_lib.REGISTRY if pid not in valid]
    if unknown:
        raise SystemExit(f"ERROR: content authored for PIDs not in the taxonomy: {unknown}")

    out = os.path.join(ROOT, "data", "processes.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(content_lib.REGISTRY, f, ensure_ascii=False, indent=1)

    n = len(content_lib.REGISTRY)
    steps = sum(len(v["l4_steps"]) for v in content_lib.REGISTRY.values())
    print(f"Compiled {n} processes from {len(mods)} module(s): {', '.join(mods)}")
    print(f"  {steps} L4 steps, {n} Mermaid diagrams (all validated)")
    print(f"  {n}/{len(valid)} of the taxonomy documented")
    print(f"  -> data/processes.json ({os.path.getsize(out)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
