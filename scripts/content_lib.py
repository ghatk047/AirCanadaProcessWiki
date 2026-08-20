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


def _step_sort_key(s):
    return [int(x) for x in re.findall(r"\d+", s["step"])]


def build_mermaid(phases, steps, font_size="12px"):
    """
    Deterministic flowchart: one subgraph per phase, steps chained in order,
    plus real branching where a step's data specifies one.

    Top level is LR so phases sit side by side (matching a standard BPMN swim
    diagram) and each phase stacks its steps TB internally. Phases are linked
    subgraph-to-subgraph (P1 --> P2), never node-to-node across a boundary --
    a node-to-node edge crossing INTO a subgraph makes mermaid discard that
    subgraph's own `direction`, collapsing the whole diagram onto one axis.
    Subgraph-to-subgraph edges do not trigger that bug in either orientation,
    confirmed empirically for both TB-outer/LR-inner and LR-outer/TB-inner.

    A step may carry an optional `branch` dict: {"label": "No", "to": "1.2"}.
    "to" is either another step's id (a loop-back or a forward skip -- a real
    second outgoing edge, labelled) or free text naming a new early-exit
    terminal that doesn't otherwise exist in the step list (e.g. "No action
    needed"). The step's normal, unlabelled edge to the next step in sequence
    is unaffected -- branch is additive, never a replacement.

    Styling is selective, not blanket: only Start/End/terminal nodes and
    decision/exception nodes get a colour override. Plain steps are left to
    Mermaid's own default theme, which is what gives a diagram its visual
    polish -- forcing every node into a custom classDef (the old approach)
    fights the theme instead of using it.
    """
    ordered = sorted(steps, key=_step_sort_key)
    by_phase = {}
    for s in ordered:
        by_phase.setdefault(_phase_of(s["step"]), []).append(s)
    phs = sorted(by_phase)
    first_ph, last_ph = phs[0], phs[-1]

    step_node_id = {s["step"]: _node_id(s["step"]) for s in ordered}

    # Pass 1: resolve every branch target, registering a new terminal node
    # (owned by the branching step's own phase, matching how the reference
    # convention declares an early-exit node inside the phase that exits to it)
    # for any target that isn't an existing step id.
    terminals_by_phase = {}   # phase -> [(node_id, label)]
    branch_edges = []         # (from_id, to_id, label)
    term_n = 0
    for s in ordered:
        br = s.get("branch")
        if not br or not str(br.get("to", "")).strip():
            continue
        target = str(br["to"]).strip()
        label = _label(str(br.get("label", "")) or "alt", 16)
        from_id = step_node_id[s["step"]]
        if target in step_node_id:
            to_id = step_node_id[target]
        else:
            term_n += 1
            to_id = f"T{term_n}"
            terminals_by_phase.setdefault(_phase_of(s["step"]), []).append((to_id, _label(target, 30)))
        branch_edges.append((from_id, to_id, label))

    lines = [f"%%{{init: {{'theme':'default','themeVariables':{{'fontSize':'{font_size}'}},"
             f"'flowchart':{{'curve':'basis'}}}}}}%%",
             "flowchart LR"]

    dec, exc, endpoints = [], [], []
    for ph in phs:
        pname = _label(phases[ph - 1] if ph <= len(phases) else f"Phase {ph}", 38)
        lines.append(f"subgraph P{ph} [{pname}]")
        lines.append("direction TB")
        if ph == first_ph:
            lines.append("START([Start])"); endpoints.append("START")
        for s in by_phase[ph]:
            nid = step_node_id[s["step"]]
            lbl = _label(s["name"])
            if str(s.get("decision_point", "N")).upper().startswith("Y"):
                lines.append(f"{nid}{{{lbl}}}"); dec.append(nid)
            elif str(s.get("exception", "N")).upper().startswith("Y"):
                lines.append(f"{nid}([{lbl}])"); exc.append(nid)
            else:
                lines.append(f"{nid}[{lbl}]")
        for tid, tlabel in terminals_by_phase.get(ph, []):
            lines.append(f"{tid}([{tlabel}])"); endpoints.append(tid)
        if ph == last_ph:
            lines.append("END([Complete])"); endpoints.append("END")
        lines.append("end")

    # Primary chain: within-phase sequence only, plus Start into the very
    # first step and the very last step into End. Node-to-node edges never
    # cross a subgraph boundary -- see the direction-collapse note above.
    for ph in phs:
        seq = by_phase[ph]
        chain_ids = [step_node_id[s["step"]] for s in seq]
        if ph == first_ph:
            lines.append(f"START --> {chain_ids[0]}")
        for a, b in zip(chain_ids, chain_ids[1:]):
            lines.append(f"{a} --> {b}")
        if ph == last_ph:
            lines.append(f"{chain_ids[-1]} --> END")

    for a, b in zip(phs, phs[1:]):
        lines.append(f"P{a} --> P{b}")

    # Branch edges (labelled, additive) come after the primary chain and
    # phase links so a reader's eye follows the happy path first.
    for from_id, to_id, label in branch_edges:
        lines.append(f"{from_id} -->|{label}| {to_id}")

    for ph in phs:
        lines.append(f"style P{ph} fill:#FFF0F2,stroke:#D2001F,stroke-width:2px")

    lines.append("classDef endNode fill:#1A1A1A,stroke:#1A1A1A,color:#FFFFFF,stroke-width:1px")
    lines.append("classDef decNode fill:#FFF3DA,stroke:#C9963E,stroke-width:2px,color:#1A1A1A")
    lines.append("classDef excNode fill:#FFE3E7,stroke:#D2001F,stroke-width:2px,color:#1A1A1A")
    if endpoints: lines.append("class " + ",".join(endpoints) + " endNode")
    if dec:       lines.append("class " + ",".join(dec) + " decNode")
    if exc:       lines.append("class " + ",".join(exc) + " excNode")

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
    assert 4 <= len(steps) <= 14, f"{pid}: expected 4-14 steps, got {len(steps)}"

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
