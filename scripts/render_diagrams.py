# -*- coding: utf-8 -*-
"""
Render every process Mermaid source to PNG via mmdc.

Sources are written to diagrams/ and PNGs to assets/img/. A content hash is
kept alongside each PNG so re-runs only re-render what actually changed.
"""
import argparse, hashlib, json, os, subprocess, sys, concurrent.futures as cf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

DIA = os.path.join(ROOT, "diagrams")
IMG = os.path.join(ROOT, "assets", "img")
HASHES = os.path.join(ROOT, "data", ".diagram-hashes.json")

PROC_ARGS = ["-w", "1920", "-H", "1080", "--scale", "2", "--backgroundColor", "white"]
EA_ARGS   = ["-w", "2400", "-H", "1400", "--scale", "2", "--backgroundColor", "white"]


def render_one(slug, mmd, ea=False):
    os.makedirs(DIA, exist_ok=True)
    os.makedirs(IMG, exist_ok=True)
    src = os.path.join(DIA, f"{slug}.mmd")
    png = os.path.join(IMG, f"{slug}.png")
    with open(src, "w", encoding="utf-8") as f:
        f.write(mmd)
    cmd = ["mmdc", "-i", src, "-o", png] + (EA_ARGS if ea else PROC_ARGS)
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and os.path.exists(png) and os.path.getsize(png) > 0
    return slug, ok, (r.stderr or r.stdout or "").strip().splitlines()[-1:] or [""]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-render even if unchanged")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", help="comma-separated slugs or PIDs")
    args = ap.parse_args()

    items = []
    pj = os.path.join(ROOT, "data", "processes.json")
    if os.path.exists(pj):
        for pid, c in json.load(open(pj, encoding="utf-8")).items():
            if c.get("mermaid"):
                items.append((pid.lower(), c["mermaid"], False))
    ej = os.path.join(ROOT, "data", "ea.json")
    if os.path.exists(ej):
        for d in json.load(open(ej, encoding="utf-8")).get("diagrams", []):
            if d.get("mermaid"):
                items.append((d["slug"], d["mermaid"], True))

    if args.only:
        want = {s.strip().lower() for s in args.only.split(",")}
        items = [i for i in items if i[0] in want]

    hashes = {}
    if os.path.exists(HASHES) and not args.force:
        hashes = json.load(open(HASHES, encoding="utf-8"))

    todo = []
    for slug, mmd, ea in items:
        h = hashlib.sha256(mmd.encode("utf-8")).hexdigest()[:16]
        png = os.path.join(IMG, f"{slug}.png")
        if hashes.get(slug) == h and os.path.exists(png):
            continue
        todo.append((slug, mmd, ea, h))

    print(f"{len(items)} diagrams total, {len(todo)} need rendering")
    if not todo:
        return

    ok_n, fails = 0, []
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(render_one, s, m, e): (s, h) for s, m, e, h in todo}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            slug, h = futs[fut]
            try:
                _, ok, err = fut.result()
            except Exception as exc:
                ok, err = False, [str(exc)]
            if ok:
                ok_n += 1
                hashes[slug] = h
            else:
                fails.append((slug, err))
            if i % 20 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} rendered  ({ok_n} ok, {len(fails)} failed)")

    os.makedirs(os.path.dirname(HASHES), exist_ok=True)
    json.dump(hashes, open(HASHES, "w", encoding="utf-8"))

    print(f"\n{ok_n} rendered, {len(fails)} failed")
    for slug, err in fails[:15]:
        print(f"  FAIL {slug}: {' '.join(err)}")


if __name__ == "__main__":
    main()
