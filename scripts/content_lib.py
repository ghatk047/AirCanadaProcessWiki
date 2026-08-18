# -*- coding: utf-8 -*-
"""
Authoring framework for process content.

Author writes semantics only. This module derives:
  * the Mermaid BPMN flowchart (from phases + steps)  -> always valid, never hand-written
  * swim lanes (from the distinct roles across steps)
  * the systems list (from the systems used by steps, plus extras)

Compile with:  python3 scripts/build_content.py
"""
import re, sys, os, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sanitise_mmd import sanitise_mermaid, validate
import ac_systems

BUILD_DATE = datetime.date.today().isoformat()

# Lane colours: Air Canada red family plus neutral supports.
LANE_COLORS = ["#D2001F", "#1A1A1A", "#C9963E", "#6B6B6B", "#A8001A",
               "#2D2D2D", "#8A5A1E", "#4A4A4A", "#E04A60", "#5A5A5A"]

REGISTRY = {}


def S(step, name, role, system, inp, out, kpi, dec="N", exc="N", pain=""):
    """One L4 step. Positional to keep authoring compact."""
    return {"step": step, "name": name, "role": role, "system": system,
            "input": inp, "output": out, "kpi": kpi,
            "decision_point": dec, "exception": exc, "pain_point": pain}


def _node_id(step):
    return "N" + re.sub(r"[^0-9]", "_", str(step))


def _label(text, limit=58):
    """Mermaid-safe node label."""
    t = re.sub(r"[()&<>\[\]{}|\"']", "", str(text))
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > limit:
        cut = t[:limit].rsplit(" ", 1)[0]
        t = (cut or t[:limit]).rstrip() + "..."
    return t


def _phase_of(step):
    m = re.match(r"^(\d+)", str(step))
    return int(m.group(1)) if m else 1


def build_mermaid(phases, steps, font_size="12px"):
    """
    Deterministic flowchart: one subgraph per phase, steps chained in order.

    Top level is TB so phases stack vertically and each phase runs LR internally.
    The reverse (LR outer / TB inner) renders as a single very wide strip because
    mermaid ignores `direction TB` inside a subgraph of an LR flowchart.
    """
    by_phase = {}
    for s in steps:
        by_phase.setdefault(_phase_of(s["step"]), []).append(s)

    lines = [f"%%{{init: {{'theme':'base','themeVariables':{{'fontSize':'{font_size}'}}}}}}%%",
             "flowchart TB"]

    dec, exc, norm = [], [], []
    for ph in sorted(by_phase):
        pname = _label(phases[ph - 1] if ph <= len(phases) else f"Phase {ph}", 38)
        lines.append(f"subgraph P{ph} [{pname}]")
        lines.append("direction LR")
        for s in by_phase[ph]:
            nid = _node_id(s["step"])
            lbl = _label(s["name"])
            if str(s.get("decision_point", "N")).upper().startswith("Y"):
                lines.append(f"{nid}{{{lbl}}}"); dec.append(nid)
            elif str(s.get("exception", "N")).upper().startswith("Y"):
                lines.append(f"{nid}([{lbl}])"); exc.append(nid)
            else:
                lines.append(f"{nid}[{lbl}]"); norm.append(nid)
        lines.append("end")

    # Chain steps WITHIN a phase only, then link phase to phase by subgraph id.
    # Node-to-node edges that cross a subgraph boundary make mermaid discard the
    # subgraph's `direction`, which collapses the whole diagram onto one axis.
    for ph in sorted(by_phase):
        seq = sorted(by_phase[ph],
                     key=lambda s: [int(x) for x in re.findall(r"\d+", s["step"])])
        for a, b in zip(seq, seq[1:]):
            lines.append(f'{_node_id(a["step"])} --> {_node_id(b["step"])}')
    phs = sorted(by_phase)
    for a, b in zip(phs, phs[1:]):
        lines.append(f"P{a} --> P{b}")

    for ph in sorted(by_phase):
        lines.append(f"style P{ph} fill:#FFF0F2,stroke:#D2001F,stroke-width:2px")

    lines.append("classDef stepNode fill:#FFFFFF,stroke:#1A1A1A,stroke-width:1px,color:#1A1A1A")
    lines.append("classDef decNode fill:#FFF8E6,stroke:#C9963E,stroke-width:2px,color:#1A1A1A")
    lines.append("classDef excNode fill:#FFE3E7,stroke:#D2001F,stroke-width:2px,color:#1A1A1A")
    if norm: lines.append("class " + ",".join(norm) + " stepNode")
    if dec:  lines.append("class " + ",".join(dec) + " decNode")
    if exc:  lines.append("class " + ",".join(exc) + " excNode")

    return "\n".join(lines)


def build_lanes(steps):
    roles, order = {}, []
    for s in steps:
        r = s["role"]
        if r not in roles:
            roles[r] = []
            order.append(r)
        roles[r].append(s["step"])
    return [{"role": r, "color": LANE_COLORS[i % len(LANE_COLORS)], "steps": roles[r]}
            for i, r in enumerate(order)]


def P(pid, desc, trig, out, note, phases, steps, kpis, risks, extra_systems=None):
    """Register one process."""
    assert pid not in REGISTRY, f"duplicate content for {pid}"
    assert 3 <= len(phases) <= 4, f"{pid}: expected 3-4 phases, got {len(phases)}"
    assert 6 <= len(steps) <= 14, f"{pid}: expected 6-14 steps, got {len(steps)}"

    seen, systems = set(), []
    for s in steps:
        canon = ac_systems.resolve(s["system"])[0]
        s["system"] = canon
        if canon not in seen:
            seen.add(canon); systems.append(canon)
    for x in (extra_systems or []):
        canon = ac_systems.resolve(x)[0]
        if canon not in seen:
            seen.add(canon); systems.append(canon)

    mmd = sanitise_mermaid(build_mermaid(phases, steps))
    problems = validate(mmd)
    assert not problems, f"{pid} mermaid: {problems}"

    REGISTRY[pid] = {
        "description": desc, "trigger": trig, "outcome": out, "ac_notes": note,
        "phases": phases, "l4_steps": steps,
        "swim_lanes": build_lanes(steps),
        "systems": systems, "kpis": kpis, "risks": risks,
        "mermaid": mmd, "updated": BUILD_DATE,
    }
    return pid
