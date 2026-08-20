# -*- coding: utf-8 -*-
"""
Ollama-driven process content generation.

Claude's job here is the brief: real Air Canada systems (with evidence tiers),
real regulatory and operational pain points, the correct L1/L2 grounding for
each process. qwen2.5-coder:14b's job is expanding that brief into full L4
depth -- 5+ phases, 16+ steps, 6+ decision/exception gates per process.

The Mermaid diagram is never trusted from the model. Every diagram is built
deterministically from the validated step list by content_lib.build_mermaid,
the same battle-tested construction used by the hand-authored path. That
removes the entire class of raw-LLM-Mermaid failures the original pipeline
had to fight with a sanitiser.
"""
import json, os, re, sys, time, datetime, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ac_systems
from content_lib import build_mermaid, build_lanes, LANE_COLORS
from sanitise_mmd import sanitise_mermaid, validate as validate_mermaid

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
MODEL = os.environ.get("AC_MODEL", "qwen2.5-coder:14b")
SOURCE_TAG = f"ollama:{MODEL}"

MIN_PHASES, MAX_PHASES = 5, 8
MIN_STEPS, MAX_STEPS = 16, 30
MIN_GATES = 6                      # decision_point=Y or exception=Y, combined
TARGET_PHASES, TARGET_STEPS, TARGET_GATES = 6, 20, 8
# Every decision_point="Y" step must carry a branch -- not "most gates should" (too vague,
# empirically the model treats a vague quota as optional and skips it almost entirely).
# exception="Y" steps get a branch too when encouraged, but it isn't hard-required for those.

REQUEST_TIMEOUT_S = 600
MAX_ATTEMPTS = 4

# ---------------------------------------------------------------- domain hooks
# Real, evidenced Air Canada pain points, keyed by L1 domain code. Injected
# into the brief only for domains where they are genuinely relevant --
# never force-fit into a process that has nothing to do with them.
DOMAIN_HOOKS = {
 "CX": ["The CTA APPR complaint backlog runs to roughly 92,500 files; Air Canada was issued a "
        "CA$426,000 administrative monetary penalty in March 2026 for 71 violations of APPR section "
        "18(1.1); a third-party arbitration pilot covering an initial 500 cases opened in 2026.",
        "Moffatt v. Air Canada, 2024 BCCRT 149: the airline was held liable for its website chatbot's "
        "incorrect bereavement-fare guidance; the tribunal rejected the argument the bot was a separate "
        "legal entity; the bot was withdrawn around April 2024. Every customer-facing automated response "
        "now carries a human-in-loop and source-grounding obligation."],
 "FO": ["The June 2023 communicator system outage delayed or cancelled the large majority of a day's "
        "flights network-wide; there is no rehearsed manual fallback procedure for this failure mode.",
        "Air Canada Express, flown by Jazz Aviation and PAL Airlines under capacity purchase agreements, "
        "runs its own crew, ops-control and maintenance systems; disruption data crosses that boundary by "
        "phone and spreadsheet today, and a wrong reason code there becomes a downstream APPR exposure."],
 "CM": ["Four bargaining units -- ACPA (pilots), CUPE (cabin crew), Teamsters (ground), UNIFOR (airport) -- "
        "each carry distinct collective agreement rules for pairing, rostering, credit and grievance "
        "handling, all of which the crew planning system must apply correctly and consistently."],
 "GO": ["A February 2023 outage took Amadeus Altea DCS and the station intranet down at Toronto Pearson; "
        "manual check-in and boarding fallback is a real operating mode, not a theoretical one.",
        "IATA Resolution 753 requires bag-to-passenger tracking at every handling milestone."],
 "MR": ["Air Canada Technical Services runs TRAX as the maintenance and engineering core -- not AMOS, not "
        "Ramco, not IFS/Mxi Maintenix, which are competitors' installs. Naming the wrong one is disqualifying "
        "in front of an Air Canada audience."],
 "CG": ["Air Canada Cargo is mid-migration to CHAMP Cargospot neo (Airline, Handling, Mobile, Revenue "
        "Accounting); the interim period runs legacy and Cargospot in parallel with a real double-entry risk.",
        "Canada PACT (pre-load air cargo targeting) has required pre-load CBSA filing before loading since "
        "April 2025, with zero tolerance for interface downtime."],
 "IT": ["Four systems are genuine open discovery questions, not filled in: integration middleware/API "
        "gateway, SIEM and SOC tooling, workforce identity (distinct from the confirmed customer identity "
        "on SAP Customer Data Cloud), and the ITSM product. Every agentic AI use case depends on the "
        "integration layer specifically.",
        "Moffatt v. Air Canada, 2024 BCCRT 149 makes human-in-loop governance and source-grounding a hard "
        "requirement for any customer-facing AI, not an optional design choice."],
 "AP": ["Aeroplan was reacquired from Aimia for CA$450M and relaunched in-house on 8 November 2020; member "
        "identity now sits on SAP Customer Data Cloud, delivered with Trew Knowledge.",
        "The Aeroplan points liability is a material balance-sheet item, not a marketing metric, and depends "
        "on breakage assumptions that must reconcile between loyalty operations and finance."],
 "NP": ["Toronto Pearson is designed around Sixth Freedom connecting traffic between the US and Europe/Asia "
        "over Canada; bank design trades connection reliability against aircraft utilisation on tight margins.",
        "The A++ Atlantic joint venture with United and Lufthansa Group means transatlantic capacity is a "
        "joint decision, not a unilateral Air Canada one."],
 "RM": ["Air Canada is a long-tenured PROS Real-Time Dynamic Pricing customer; ATPCO fare filing latency is "
        "the slowest link in an otherwise near-real-time pricing chain."],
 "FN": ["The air traffic liability -- tickets sold but not yet flown -- is one of the largest balance sheet "
        "items an airline carries, and revenue is recognised on lift, not on sale."],
 "HR": ["The Official Languages Act creates a bilingual English/French obligation across the employee "
        "experience itself, not only customer-facing channels; four bargaining units each carry distinct "
        "rule sets that HR systems must apply correctly."],
}

FEWSHOT = """{
  "description": "A representative Air Canada process description, two to three sentences, naming the actual system and the actual operational tension.",
  "trigger": "The specific event that starts this process.",
  "outcome": "The specific, verifiable state the process produces when it succeeds.",
  "ac_notes": "Two to four sentences of Air Canada-specific context: the regulatory hook, the real incident, the system integration reality, or the organisational seam that makes this process matter to a CIO reading a bid.",
  "phases": ["Phase 1 name", "Phase 2 name", "Phase 3 name", "Phase 4 name", "Phase 5 name", "Phase 6 name"],
  "l4_steps": [
    {"step":"1.1","name":"First concrete action","role":"Air Canada-specific role title","system":"Exact system name from the provided list","input":"what feeds this step","output":"what this step produces","kpi":"a measurable target with a number","decision_point":"N","exception":"N","pain_point":"a specific, real operational friction, not a generic statement"},
    {"step":"1.2","name":"A genuine decision","role":"...","system":"...","input":"...","output":"...","kpi":"...","decision_point":"Y","exception":"N","pain_point":"...","branch":{"label":"No","to":"Escalated to supervisor"}},
    {"step":"1.3","name":"Third action in phase 1 -- the path taken when the decision above is Yes","role":"...","system":"...","input":"...","output":"...","kpi":"...","decision_point":"N","exception":"N","pain_point":"..."},
    {"step":"2.1","name":"An exception step that resolves and rejoins the main flow","role":"...","system":"...","input":"...","output":"...","kpi":"...","decision_point":"N","exception":"Y","pain_point":"...","branch":{"label":"resolved","to":"2.3"}}
  ],
  "kpis": ["KPI 1 with a number", "KPI 2 with a number", "KPI 3 with a number", "KPI 4 with a number", "KPI 5 with a number"],
  "risks": ["Risk 1, specific to this process", "Risk 2", "Risk 3", "Risk 4", "Risk 5"]
}"""

SYSTEM_PROMPT = f"""You are a senior SAP consultant and airline operations specialist writing internal
process documentation for Air Canada, for an audience of Air Canada's own CIO and operations leadership.
This is a pre-sales credibility artifact: every system name, role and pain point must read as something
someone who actually runs these processes at Air Canada would recognise as true, not generic airline
boilerplate.

DEPTH IS THE PRIORITY. Every process you write must have:
  - AT LEAST {MIN_PHASES} phases (target {TARGET_PHASES}), never fewer than {MIN_PHASES}
  - AT LEAST {MIN_STEPS} L4 steps total (target {TARGET_STEPS}), never fewer than {MIN_STEPS}
  - AT LEAST {MIN_GATES} steps flagged decision_point="Y" or exception="Y" combined (target {TARGET_GATES}),
    spread across different phases, not clustered in one
A shallow process with 6-8 steps and one decision point is a FAILURE. Real airline processes branch,
loop back on exception, escalate, and reconcile across systems. Show that.

BRANCHING IS MANDATORY ON EVERY decision_point="Y" STEP. This is not optional and not a "most of them"
guideline -- every single step you mark decision_point="Y" MUST carry a "branch" object naming its
alternate outcome. A diamond with no branch is not a decision, it's decoration, and will be rejected.

  "branch": {{"label": "No", "to": "1.4"}}

"label" is short (1-3 words: "No", "Escalate", "Failed", "Timeout") -- this becomes the text on the
diagram's edge. "to" is either:
  (a) another step's exact "step" id already in this process (a forward skip past intervening steps, or
      a loop BACK to an earlier step id for a genuine retry/rework cycle -- airline processes do this
      constantly: re-attempt a check, re-submit after rejection, cycle until a threshold clears), or
  (b) a short new phrase naming an early-exit outcome that doesn't otherwise exist as a step (e.g.
      "No action needed", "Request declined", "Escalated to duty manager") -- use this when the gate's
      failure path genuinely ends the process rather than rejoining it.
The step's normal path (continuing to the next step in sequence) still happens automatically -- the
branch only needs to describe the ALTERNATE outcome, never the expected one.

Vary the branch labels -- don't reuse "Not approved" for every decision. Ground each one in this
process's own subject matter (a threshold, a system result, a capacity check) rather than a generic
review/escalate template.

exception="Y" steps may also carry a branch (e.g. showing where the exception rejoins the main flow, or
where it exits early) -- this is encouraged but not mandatory the way decision_point="Y" branches are.

Every step needs a REAL, SPECIFIC pain point -- something a working analyst or agent would actually say
about their job, not a generic statement like "process can be slow" or "requires coordination". Ground it
in a genuine system limitation, a timing conflict, a regulatory constraint, or an organisational seam.

Roles must be Air Canada-specific job titles ("YYZ Operations Control Duty Manager", "APPR Adjudicator",
"Aeroplan Member Services Agent", "Cargo Compliance Agent") -- never generic ("Manager", "Analyst" alone).

Systems must be drawn from the list provided in the brief wherever the step's function matches one of
them. Only introduce a system not on that list if the step genuinely requires something the list does not
cover, and even then prefer a real, named Air Canada system over a generic placeholder.

Return ONLY a single valid JSON object, no markdown fences, no commentary before or after, matching this
exact shape:

{FEWSHOT}

Field rules:
  - "step" values must follow "{{phase_number}}.{{step_number}}" format (e.g. "1.1", "1.2", "2.1", "3.4"),
    phase_number matching the 1-indexed position of the step's phase in the "phases" array.
  - "decision_point" and "exception" are always exactly "Y" or "N".
  - "branch" is omitted entirely for a step with no alternate path -- do not write "branch": null or
    "branch": {{}}, just leave the key out.
  - "kpis" and "risks" arrays each need exactly 5 entries.
  - Every string field is plain prose -- no markdown, no bullet characters, no parentheses-heavy asides.
"""


def _domain_hooks_text(l1_code):
    hooks = DOMAIN_HOOKS.get(l1_code, [])
    if not hooks:
        return ""
    return "\nReal Air Canada context relevant to this domain (use where it genuinely applies):\n" + \
           "\n".join(f"  - {h}" for h in hooks)


def build_brief(p):
    """Assemble the per-process grounding brief from taxonomy + system registry data."""
    sys_lines = []
    for name in p["domain_systems"]:
        canon, cls, tip, tier, vendor = ac_systems.resolve(name)
        sys_lines.append(f"  - {canon} ({vendor}, evidence tier {tier}): {tip}")

    return f"""Write the full process document for:

Process ID: {p['pid']}
Process name: {p['l3_name']}
L1 domain: {p['l1_name']}
L2 group: {p['l2_name']}

Domain systems available for this process (prefer these where the step's function matches):
{chr(10).join(sys_lines)}
{_domain_hooks_text(p['l1_code'])}

Write the complete process now as a single JSON object per the schema and depth requirements in the
system prompt. Remember: at least {MIN_PHASES} phases, at least {MIN_STEPS} L4 steps, at least
{MIN_GATES} decision or exception gates, and EVERY decision_point="Y" step must carry a "branch" object
to a genuinely different step or a new early-exit outcome -- not most of them, every single one. This is
the single most important instruction -- do not undershoot it."""


def _http_post_json(path, payload):
    req = urllib.request.Request(
        OLLAMA_HOST + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT_S) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _extract_json(text):
    text = text.strip()
    text = re.sub(r'^```(?:json)?\s*', '', text)
    text = re.sub(r'```\s*$', '', text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    m = re.search(r'\{.*\}', text, re.DOTALL)
    if m:
        return json.loads(m.group(0))
    raise ValueError("no JSON object found in model output")


def _call_model(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "format": "json",
        "stream": False,
        "options": {"temperature": 0.6, "num_ctx": 12288, "num_predict": 6000},
    }
    result = _http_post_json("/api/chat", payload)
    content = result.get("message", {}).get("content", "")
    if not content:
        raise ValueError("empty response from model")
    return _extract_json(content)


def _validate_depth(data):
    """Return a list of problems; empty list means depth requirements are met."""
    problems = []
    phases = data.get("phases")
    steps = data.get("l4_steps")
    if not isinstance(phases, list) or not (MIN_PHASES <= len(phases) <= MAX_PHASES):
        problems.append(f"phases: expected {MIN_PHASES}-{MAX_PHASES}, got {len(phases) if isinstance(phases, list) else 'invalid'}")
    if not isinstance(steps, list) or not (MIN_STEPS <= len(steps) <= MAX_STEPS):
        problems.append(f"l4_steps: expected {MIN_STEPS}-{MAX_STEPS}, got {len(steps) if isinstance(steps, list) else 'invalid'}")
        return problems  # can't check gates/step-format without a valid list
    gates = sum(1 for s in steps if str(s.get("decision_point", "N")).upper().startswith("Y")
                or str(s.get("exception", "N")).upper().startswith("Y"))
    if gates < MIN_GATES:
        problems.append(f"decision/exception gates: expected >= {MIN_GATES}, got {gates}")
    unbranched_decisions = [
        s.get("step") for s in steps
        if str(s.get("decision_point", "N")).upper().startswith("Y")
        and not (isinstance(s.get("branch"), dict) and str(s["branch"].get("to", "")).strip())
    ]
    if unbranched_decisions:
        problems.append(
            f"these decision_point=\"Y\" steps are missing a required \"branch\" object: "
            f"{', '.join(unbranched_decisions)} -- every decision needs one, no exceptions")
    branch_labels = [str(s["branch"].get("label", "")).strip().lower()
                     for s in steps if isinstance(s.get("branch"), dict) and s["branch"].get("label")]
    if branch_labels:
        from collections import Counter
        label, count = Counter(branch_labels).most_common(1)[0]
        if count >= 3 and count > len(branch_labels) // 2:
            problems.append(
                f"the branch label {label!r} is reused {count} times across different decisions -- this "
                f"is the generic 'review / not approved / escalate' template, not real distinct decisions. "
                f"Rewrite so each decision asks a specific, different question with its own label")
    for s in steps:
        if not re.match(r'^\d+\.\d+$', str(s.get("step", ""))):
            problems.append(f"step id {s.get('step')!r} does not match N.N format")
            break
        for k in ("name", "role", "system", "input", "output", "kpi"):
            if not str(s.get(k, "")).strip():
                problems.append(f"step {s.get('step')} missing required field {k!r}")
                break
    if not isinstance(data.get("kpis"), list) or len(data["kpis"]) < 3:
        problems.append("kpis: need at least 3 entries")
    if not isinstance(data.get("risks"), list) or len(data["risks"]) < 3:
        problems.append("risks: need at least 3 entries")
    for k in ("description", "trigger", "outcome", "ac_notes"):
        if not str(data.get(k, "")).strip():
            problems.append(f"missing top-level field {k!r}")
    return problems


def generate_process(p, log=print):
    """Call Ollama for one process, validating and retrying on depth/format failure.
    Returns a dict ready to store in data/processes.json, or None on repeated failure."""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_brief(p)},
    ]

    last_problems = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            t0 = time.time()
            data = _call_model(messages)
            elapsed = time.time() - t0
            problems = _validate_depth(data)
            if not problems:
                return _finalise(p, data, elapsed, attempt)
            last_problems = problems
            log(f"  [{p['pid']}] attempt {attempt}: depth/format issues: {'; '.join(problems[:3])}")
            messages.append({"role": "assistant", "content": json.dumps(data)[:4000]})
            messages.append({"role": "user", "content":
                "That response did not meet the requirements: " + "; ".join(problems) +
                f". Regenerate the COMPLETE process from scratch as a single JSON object with at least "
                f"{MIN_PHASES} phases, at least {MIN_STEPS} L4 steps, at least {MIN_GATES} decision "
                f"or exception gates, and a \"branch\" object on EVERY SINGLE decision_point=\"Y\" step "
                f"listed above with no exceptions. Do not explain -- output only the corrected JSON object."})
        except urllib.error.URLError as e:
            log(f"  [{p['pid']}] attempt {attempt}: connection error: {e}")
            time.sleep(5)
        except Exception as e:
            log(f"  [{p['pid']}] attempt {attempt}: {type(e).__name__}: {e}")
            time.sleep(2)

    log(f"  [{p['pid']}] FAILED after {MAX_ATTEMPTS} attempts -- last problems: {last_problems}")
    return None


def _finalise(p, data, elapsed, attempt):
    steps = data["l4_steps"]
    seen, systems = set(), []
    for s in steps:
        canon = ac_systems.resolve(s["system"])[0]
        s["system"] = canon
        s["decision_point"] = "Y" if str(s.get("decision_point", "N")).upper().startswith("Y") else "N"
        s["exception"] = "Y" if str(s.get("exception", "N")).upper().startswith("Y") else "N"
        if canon not in seen:
            seen.add(canon); systems.append(canon)

    mmd = sanitise_mermaid(build_mermaid(data["phases"], steps))
    mmd_problems = validate_mermaid(mmd)
    if mmd_problems:
        raise ValueError(f"generated mermaid failed validation: {mmd_problems}")

    return {
        "description": data["description"], "trigger": data["trigger"], "outcome": data["outcome"],
        "ac_notes": data["ac_notes"], "phases": data["phases"], "l4_steps": steps,
        "swim_lanes": build_lanes(steps), "systems": systems,
        "kpis": data["kpis"][:8], "risks": data["risks"][:8],
        "mermaid": mmd,
        "updated": datetime.date.today().isoformat(),
        "source": SOURCE_TAG,
        "gen_seconds": round(elapsed, 1), "gen_attempts": attempt,
    }


def is_done(existing_entry):
    """A process counts as done for THIS pipeline only if it was generated by the
    current model, meets the depth floor, and every decision_point="Y" step carries
    a branch -- old Claude-authored content, a prior thin attempt, or content
    generated before the branching requirement existed does not count, and gets
    regenerated."""
    if not existing_entry:
        return False
    if existing_entry.get("source") != SOURCE_TAG:
        return False
    if not (len(existing_entry.get("phases", [])) >= MIN_PHASES and
            len(existing_entry.get("l4_steps", [])) >= MIN_STEPS):
        return False
    steps = existing_entry.get("l4_steps", [])
    for s in steps:
        if str(s.get("decision_point", "N")).upper().startswith("Y"):
            branch = s.get("branch")
            if not (isinstance(branch, dict) and str(branch.get("to", "")).strip()):
                return False
    return True
