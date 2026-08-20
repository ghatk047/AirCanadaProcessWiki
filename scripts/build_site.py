# -*- coding: utf-8 -*-
"""
Static site generator for the Air Canada Process Wiki.

Renders:
  index.html                              depth 0
  {l1}/index.html                         depth 1
  {l1}/{l2}/index.html                    depth 2
  {l1}/{l2}/{pid}/index.html              depth 3
  ea-diagrams/index.html                  depth 1
  ea-diagrams/{slug}/index.html           depth 2
  assets/js/search-index.json

The sidebar is static HTML baked into every page -- never JavaScript-rendered.
Asset paths are depth-derived; see PREFIX below.
"""
import json, os, re, sys, html, datetime
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from taxonomy import DOMAINS, all_processes, slugify
import ac_systems

DATA = os.path.join(ROOT, "data", "processes.json")
EA_DATA = os.path.join(ROOT, "data", "ea.json")
BUILD_DATE = datetime.date.today().isoformat()

E = lambda s: html.escape(str(s if s is not None else ""), quote=True)


def prefix(depth):
    """Relative prefix from a page at `depth` back to the site root."""
    return "../" * depth


# ---------------------------------------------------------------- data load
def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- fragments
def sys_tag(name):
    canon, cls, tip, tier, vendor = ac_systems.resolve(name)
    tip_full = f"{tip} [{vendor} - evidence {tier}]" if vendor != "UNKNOWN" else tip
    return (f'<span class="tag {cls}" data-tooltip="{E(tip_full)}">{E(canon)}'
            f'<span class="tier tier-{tier}" title="{E(ac_systems.TIER_LABEL[tier])}">{tier}</span></span>')


def sys_tags(names):
    return "".join(sys_tag(n) for n in (names or []))


TIER_LEGEND = (
    '<div class="tier-legend">'
    '<span><b>Evidence tier</b></span>'
    '<span><span class="tier tier-A">A</span> Confirmed - public AC or vendor source</span>'
    '<span><span class="tier tier-B">B</span> Indicated - postings, technographics, trade press</span>'
    '<span><span class="tier tier-C">C</span> Industry pattern - not evidenced for AC</span>'
    '<span><span class="tier tier-U">U</span> Unknown - open discovery question</span>'
    "</div>"
)


EA_COUNT = 0


def build_sidebar(depth, active_l1=None, active_l2=None, active_pid=None, procs_by_group=None):
    """
    Static nav. All 12 L1 and all 48 L2 always present; the L3 list is emitted
    only for the active L2 group, which keeps every page's nav payload small.

    L2 groups are keyed on the composite l1_code::l2_code -- keying on slug
    alone collapses distinct groups that happen to share a slug
    (e.g. CX Contact Centre and CM Crew Compliance both slug to a 'cc' code).
    """
    p = prefix(depth)
    out = ['<aside class="sidebar" id="sidebar">',
           '<div class="sb-head">',
           '<button class="sb-toggle" id="sb-toggle" title="Toggle sidebar  [" aria-label="Toggle sidebar">&#9776;</button>',
           '<span class="sb-title">Process Domains</span>',
           "</div>", "<nav>"]

    for d in DOMAINS:
        l1s = slugify(d["name"])
        n = sum(len(g["p"]) for g in d["l2"])
        act = " active" if d["code"] == active_l1 else ""
        out.append(
            f'<div class="l1-block"><a class="l1-link{act}" href="{p}{l1s}/">'
            f'<span class="ic">{d["icon"]}</span>'
            f'<span class="sb-label">{E(d["name"])}</span>'
            f'<span class="cnt">{n}</span></a>'
        )
        out.append('<div class="l2-block">')
        for g in d["l2"]:
            l2s = slugify(g["name"])
            key = f'{d["code"]}::{g["code"]}'
            gact = " active" if key == active_l2 else ""
            out.append(f'<a class="l2-link{gact}" href="{p}{l1s}/{l2s}/">{E(g["name"])}</a>')
            if key == active_l2 and procs_by_group:
                for pr in procs_by_group.get(key, []):
                    pact = " active" if pr["pid"] == active_pid else ""
                    out.append(
                        f'<a class="l3-link{pact}" href="{p}{l1s}/{l2s}/{pr["pid"].lower()}/">'
                        f'{E(pr["l3_name"])}</a>'
                    )
        out.append("</div></div>")

    out.append('<div class="sb-section-title">Enterprise Architecture</div>')
    out.append('<div class="l1-block">'
               f'<a class="l1-link{" active" if active_l1 == "EA" else ""}" href="{p}ea-diagrams/">'
               '<span class="ic">&#128506;</span>'
               '<span class="sb-label">EA Diagrams</span>'
               f'<span class="cnt">{EA_COUNT}</span></a></div>')
    out.append("</nav></aside>")
    return "\n".join(out)


def topbar(depth):
    p = prefix(depth)
    return f"""<div id="progress-bar"></div>
<header class="topbar">
  <button class="tb-btn" id="mob-menu" style="display:none" aria-label="Menu">&#9776;</button>
  <a class="brand" href="{p}index.html"><span class="leaf">&#127809;</span>
    <span><span class="ac">Air Canada</span> Process Wiki</span></a>
  <span class="badge-aeroplan">Aeroplan</span>
  <div class="spacer"></div>
  <div class="tb-search">
    <input id="search-input" type="search" placeholder="Search processes, steps, systems&hellip;"
           autocomplete="off" spellcheck="false" aria-label="Search">
    <span class="kbd">/</span>
  </div>
  <button class="tb-btn" id="theme-btn" aria-label="Toggle theme">&#127769; <span class="lbl">Dark</span></button>
  <a class="tb-btn" href="{p}ea-diagrams/">&#128506; <span class="lbl">EA</span></a>
</header>
<div id="search-results"></div>"""


def breadcrumb(depth, trail):
    parts = []
    for i, (label, href) in enumerate(trail):
        if i:
            parts.append('<span class="sep">&rsaquo;</span>')
        if href:
            parts.append(f'<a href="{href}">{E(label)}</a>')
        else:
            parts.append(f'<span class="cur">{E(label)}</span>')
    return f'<div class="breadcrumb">{"".join(parts)}</div>'


LIGHTBOX = """<div id="lightbox" role="dialog" aria-label="Diagram viewer">
  <div class="lb-bar">
    <button id="lb-out" title="Zoom out  -">&minus;</button>
    <span id="lb-zoom-pct">100%</span>
    <button id="lb-in" title="Zoom in  +">+</button>
    <button id="lb-reset" title="Reset  0">&#8634;</button>
    <button id="lb-open" title="Open full size">&#8599;</button>
    <button id="lb-close" title="Close  Esc">&times;</button>
  </div>
  <div class="lb-stage"><img id="lb-img" alt="Diagram"></div>
  <div class="lb-title" id="lb-title"></div>
</div>
<div id="kbd-help"><div class="kh-box">
  <h3>Keyboard shortcuts</h3>
  <dl>
    <dt>/</dt><dd>Focus search</dd>
    <dt>J</dt><dd>Next process</dd>
    <dt>K</dt><dd>Previous process</dd>
    <dt>D</dt><dd>Toggle dark mode</dd>
    <dt>[</dt><dd>Collapse or expand sidebar</dd>
    <dt>P</dt><dd>Print this page</dd>
    <dt>+ &minus; 0</dt><dd>Zoom in the diagram viewer</dd>
    <dt>Esc</dt><dd>Close overlays</dd>
    <dt>?</dt><dd>This help</dd>
  </dl>
</div></div>
<button id="back-to-top" title="Back to top" aria-label="Back to top">&uarr;</button>"""


FOOT = """<div class="foot">
<b>Air Canada Process Wiki</b> &mdash; process and systems reference compiled from public sources
for IT Application Management and User Support pre-sales discovery.
Built {date}. Every system carries an evidence tier: tier C is an industry pattern and tier U is an open
question, and neither should be asserted as fact about Air Canada without confirmation in discovery.
Not affiliated with or endorsed by Air Canada. Air Canada, Aeroplan and Altitude are trademarks of Air Canada.
</div>"""


def page(depth, title, body, trail, active_l1=None, active_l2=None,
         active_pid=None, procs_by_group=None, nav=None, has_toc=False):
    p = prefix(depth)
    navjs = ""
    if nav:
        navjs = (f'window.AC_NAV={{prev:{json.dumps(nav.get("prev"))},'
                 f'next:{json.dumps(nav.get("next"))}}};')
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} &middot; Air Canada Process Wiki</title>
<meta name="description" content="Air Canada business process and systems reference. {E(title)}.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#127809;</text></svg>">
<link rel="stylesheet" href="{p}assets/css/wiki.css">
<script>window.AC_ROOT={json.dumps(p)};{navjs}
(function(){{try{{var t=localStorage.getItem('ac-theme');
if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body>
{topbar(depth)}
{build_sidebar(depth, active_l1, active_l2, active_pid, procs_by_group)}
{breadcrumb(depth, trail)}
<main class="content">
<div class="page{' has-toc' if has_toc else ''}">
{body}
</div>
{FOOT.format(date=BUILD_DATE)}
</main>
{LIGHTBOX}
<script src="{p}assets/js/wiki.js"></script>
</body>
</html>"""


def write(relpath, content):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------- pages
def render_home(procs, content):
    done = sum(1 for p in procs if p["pid"] in content)
    n_sys = len(ac_systems.SYSTEMS)
    tier_a = sum(1 for v in ac_systems.SYSTEMS.values() if v[2] == "A")

    cards = []
    for d in DOMAINS:
        n = sum(len(g["p"]) for g in d["l2"])
        d_done = sum(1 for p in procs if p["l1_code"] == d["code"] and p["pid"] in content)
        cards.append(f"""<a class="dcard" href="{slugify(d['name'])}/">
  <div class="dc-top"><span class="dc-ic">{d['icon']}</span>
    <span class="dc-code">{d['code']}</span><h3>{E(d['name'])}</h3></div>
  <p>{E(d['blurb'])}</p>
  <div>{sys_tags(d['systems'][:3])}</div>
  <div class="dc-foot"><span class="dc-n">{n}</span> processes
    <span>&middot;</span> {len(d['l2'])} groups
    <span>&middot;</span> {d_done} documented</div>
</a>""")

    body = f"""<h1>Air Canada Process Wiki</h1>
<p class="lede">A working reference for Air Canada's business processes and the systems that carry them &mdash;
{len(procs)} processes across {len(DOMAINS)} domains, mapped to {n_sys} named systems, with every
system claim carrying an evidence tier. Built for IT Application Management and User Support discovery.</p>

<div class="stats">
  <div class="stat"><div class="n">{len(procs)}</div><div class="l">Processes</div></div>
  <div class="stat"><div class="n">{len(DOMAINS)}</div><div class="l">L1 Domains</div></div>
  <div class="stat"><div class="n">{sum(len(d['l2']) for d in DOMAINS)}</div><div class="l">L2 Groups</div></div>
  <div class="stat"><div class="n">{n_sys}</div><div class="l">Systems</div></div>
  <div class="stat"><div class="n">{tier_a}</div><div class="l">Tier A Confirmed</div></div>
  <div class="stat"><div class="n">{EA_COUNT}</div><div class="l">EA Diagrams</div></div>
</div>

{TIER_LEGEND}

<div class="callout"><span class="ct">How to read this wiki</span>
Every system tag carries a letter badge. <b>A</b> means Air Canada or the vendor has said it publicly.
<b>B</b> means job postings, technographic data or trade press point to it. <b>C</b> is an industry pattern
that is <i>not</i> evidenced for Air Canada. <b>U</b> is a named gap we would resolve in discovery rather than
paper over. The four U-tier entries &mdash; integration middleware, SIEM and SOC, workforce identity, and the
ITSM product &mdash; are deliberately visible: they are the questions to ask, not omissions.</div>

<h2>Process Domains</h2>
<div class="grid">
{"".join(cards)}
</div>

<h2>Where the estate is under strain</h2>
<div class="grid">
  <div class="dcard" style="cursor:default">
    <div class="dc-top"><span class="dc-ic">&#9878;</span><h3>APPR complaint load</h3></div>
    <p>Air Passenger Protection Regulations entitlement is determined largely by hand from the PNR and the
    disruption reason code, then re-keyed into the case tool. The Canadian Transportation Agency backlog and
    the 2026 arbitration pilot make this a board-level process, not a back-office one.</p>
    <div class="dc-foot">See <b>CX &rsaquo; Complaints, APPR &amp; Claims</b></div>
  </div>
  <div class="dcard" style="cursor:default">
    <div class="dc-top"><span class="dc-ic">&#9889;</span><h3>Ops control resilience</h3></div>
    <p>The June 2023 communicator outage delayed or cancelled the large majority of a day's flights. Ops
    control, crew and DCS share a seam that has no documented degraded-mode operating procedure.</p>
    <div class="dc-foot">See <b>FO &rsaquo; Ops Control &amp; IRROP Recovery</b></div>
  </div>
  <div class="dcard" style="cursor:default">
    <div class="dc-top"><span class="dc-ic">&#128279;</span><h3>The Express operator seam</h3></div>
    <p>Jazz and PAL fly Air Canada Express under capacity purchase agreements on their own crew, ops and
    maintenance systems. Disruption data crosses that seam by spreadsheet and phone.</p>
    <div class="dc-foot">See <b>FO &rsaquo; Express Operator Disruption Reconciliation</b></div>
  </div>
  <div class="dcard" style="cursor:default">
    <div class="dc-top"><span class="dc-ic">&#129302;</span><h3>AI governance after Moffatt</h3></div>
    <p>A civil resolution tribunal held Air Canada liable for its website assistant's wrong advice and
    rejected the argument that the bot was a separate legal entity. Human-in-loop control is now a hard
    requirement on any customer-facing automation, not a design option.</p>
    <div class="dc-foot">See <b>IT &rsaquo; AI &amp; ML Platform</b></div>
  </div>
</div>

<h2>Documentation status</h2>
<div class="callout warn"><span class="ct">Build progress</span>
{done} of {len(procs)} processes carry full L4 step documentation.
Undocumented processes are listed and navigable but marked <b>Queued</b>.</div>
"""
    write("index.html", page(0, "Home", body, [("Home", None)]))


def render_l1(d, procs, content):
    l1s = slugify(d["name"])
    dp = [p for p in procs if p["l1_code"] == d["code"]]
    cards = []
    for g in d["l2"]:
        gp = [p for p in dp if p["l2_code"] == g["code"]]
        gd = sum(1 for p in gp if p["pid"] in content)
        cards.append(f"""<a class="dcard" href="{slugify(g['name'])}/">
  <div class="dc-top"><span class="dc-code">{d['code']}-{g['code']}</span><h3>{E(g['name'])}</h3></div>
  <p>{E(g['blurb'])}</p>
  <div class="dc-foot"><span class="dc-n">{len(gp)}</span> processes
    <span>&middot;</span> {gd} documented</div>
</a>""")

    body = f"""<h1><span class="dc-code">{d['code']}</span> {E(d['name'])}</h1>
<p class="lede">{E(d['blurb'])}</p>
<div class="card"><h3>Principal systems in this domain</h3>{sys_tags(d['systems'])}</div>
{TIER_LEGEND}
<h2>Process Groups</h2>
<div class="grid">{"".join(cards)}</div>
<h2>All {len(dp)} processes in {E(d['name'])}</h2>
<div class="plist">
{"".join(process_row(p, content, 1) for p in dp)}
</div>"""
    write(f"{l1s}/index.html",
          page(1, d["name"], body, [("Home", "../index.html"), (d["name"], None)],
               active_l1=d["code"]))


def process_row(p, content, depth):
    c = content.get(p["pid"])
    l1s, l2s = p["l1_slug"], p["l2_slug"]
    href = (f'{l1s}/{l2s}/{p["pid"].lower()}/' if depth == 1 else f'{p["pid"].lower()}/')
    tags = sys_tags((c.get("systems") or [])[:2]) if c else '<span class="tag generic">Queued</span>'
    return (f'<a class="prow" href="{href}"><span class="p-pid">{p["pid"]}</span>'
            f'<span class="p-name">{E(p["l3_name"])}</span>'
            f'<span class="p-sys">{tags}</span><span class="p-arrow">&rsaquo;</span></a>')


def render_l2(d, g, procs, content, procs_by_group):
    l1s, l2s = slugify(d["name"]), slugify(g["name"])
    gp = [p for p in procs if p["l1_code"] == d["code"] and p["l2_code"] == g["code"]]
    body = f"""<h1><span class="dc-code">{d['code']}-{g['code']}</span> {E(g['name'])}</h1>
<p class="lede">{E(g['blurb'])} &mdash; {len(gp)} processes within {E(d['name'])}.</p>
<div class="plist">
{"".join(process_row(p, content, 2) for p in gp)}
</div>"""
    write(f"{l1s}/{l2s}/index.html",
          page(2, g["name"], body,
               [("Home", "../../index.html"), (d["name"], "../"), (g["name"], None)],
               active_l1=d["code"], active_l2=f'{d["code"]}::{g["code"]}',
               procs_by_group=procs_by_group))


def phase_of(step):
    m = re.match(r"^(\d+)", str(step))
    return int(m.group(1)) if m else 1


def render_process(p, content, procs, idx, procs_by_group):
    c = content.get(p["pid"])
    l1s, l2s, pid_l = p["l1_slug"], p["l2_slug"], p["pid"].lower()
    trail = [("Home", "../../../index.html"), (p["l1_name"], "../../"),
             (p["l2_name"], "../"), (p["pid"], None)]
    nav = {"prev": None, "next": None}
    if idx > 0:
        q = procs[idx - 1]
        nav["prev"] = f'../../../{q["l1_slug"]}/{q["l2_slug"]}/{q["pid"].lower()}/'
    if idx < len(procs) - 1:
        q = procs[idx + 1]
        nav["next"] = f'../../../{q["l1_slug"]}/{q["l2_slug"]}/{q["pid"].lower()}/'

    head = f"""<div class="page-head">
  <button class="pid-badge" data-pid="{p['pid']}" title="Click to copy the process ID">
    {p['pid']}<span class="copy-ic">&#128203;</span></button>
  <span class="updated">Updated {E((c or {}).get('updated', BUILD_DATE))}</span>
</div>
<h1>{E(p['l3_name'])}</h1>"""

    if not c:
        body = head + """<div class="callout warn"><span class="ct">Queued</span>
This process is defined in the taxonomy but its L4 step documentation has not been authored yet.</div>"""
        write(f"{l1s}/{l2s}/{pid_l}/index.html",
              page(3, p["l3_name"], body, trail, active_l1=p["l1_code"],
                   active_l2=f'{p["l1_code"]}::{p["l2_code"]}', active_pid=p["pid"],
                   procs_by_group=procs_by_group, nav=nav))
        return

    steps = c.get("l4_steps", [])
    phase_names = c.get("phases", [])
    grouped = OrderedDict()
    for s in steps:
        grouped.setdefault(phase_of(s.get("step", "1.1")), []).append(s)

    phase_html = []
    for ph, sl in grouped.items():
        pname = phase_names[ph - 1] if ph <= len(phase_names) else f"Phase {ph}"
        rows = []
        for s in sl:
            dp_ = "Y" if str(s.get("decision_point", "N")).upper().startswith("Y") else "N"
            ex_ = "Y" if str(s.get("exception", "N")).upper().startswith("Y") else "N"
            rows.append(f"""<tr>
<td class="c-step">{E(s.get('step'))}</td>
<td><b>{E(s.get('name'))}</b></td>
<td>{E(s.get('role'))}</td>
<td>{sys_tag(s.get('system')) if s.get('system') else ''}</td>
<td>{E(s.get('input'))}</td>
<td>{E(s.get('output'))}</td>
<td>{E(s.get('kpi'))}</td>
<td class="c-flag"><span class="{'yes' if dp_=='Y' else 'no'}">{dp_}</span></td>
<td class="c-flag"><span class="{'yes' if ex_=='Y' else 'no'}">{ex_}</span></td>
<td>{E(s.get('pain_point'))}</td>
</tr>""")
        phase_html.append(f"""<div class="phase-group" data-phase-id="{p['pid']}-{ph}">
  <div class="phase-head"><span class="ph-chev">&#9660;</span>
    <span class="ph-name">Phase {ph} &mdash; {E(pname)}</span>
    <span class="ph-n">{len(sl)} steps</span></div>
  <div class="phase-body"><div class="tbl-wrap"><table>
  <thead><tr><th>Step</th><th>Activity</th><th>Role</th><th>System</th><th>Input</th>
  <th>Output</th><th>KPI</th><th>Dec</th><th>Exc</th><th>Pain point</th></tr></thead>
  <tbody>{"".join(rows)}</tbody></table></div></div>
</div>""")

    lanes = "".join(
        f'<div class="lane"><span class="swatch" style="background:{E(l.get("color","#D2001F"))}"></span>'
        f'<span>{E(l.get("role"))}</span>'
        f'<span class="lane-steps">{E(" ".join(l.get("steps", [])))}</span></div>'
        for l in c.get("swim_lanes", []))

    img = f"../../../assets/img/{pid_l}.png"
    img_abs = os.path.join(ROOT, "assets", "img", f"{pid_l}.png")
    if os.path.exists(img_abs):
        diagram = (f'<div class="diagram-wrap"><span class="dg-hint">Click to zoom</span>'
                   f'<img src="{img}" alt="{E(p["l3_name"])} process flow" loading="lazy"></div>')
    else:
        diagram = ('<div class="diagram-wrap"><div class="dg-missing">'
                   'BPMN diagram not yet rendered for this process.</div></div>')

    toc = """<aside class="toc">
  <div class="toc-t">On this page</div>
  <a href="#bpmn">Process flow</a>
  <a href="#steps">Process steps</a>
  <a href="#lanes">Swim lanes</a>
  <a href="#systems">Systems</a>
  <a href="#kpis">KPIs</a>
  <a href="#risks">Risks</a>
</aside>"""

    main = f"""{head}
<h2 id="bpmn">Process flow</h2>
{diagram}

<h2 id="steps">Process steps</h2>
{"".join(phase_html)}

<h2 id="lanes">Swim lanes</h2>
<div class="lanes">{lanes or '<span style="color:var(--text-muted)">Not defined.</span>'}</div>

<h2 id="systems">Systems touched</h2>
<div class="card">{sys_tags(c.get('systems'))}</div>

<h2 id="kpis">Key performance indicators</h2>
<ul class="bullets">{"".join(f"<li>{E(k)}</li>" for k in c.get('kpis', []))}</ul>

<h2 id="risks">Risks and control points</h2>
<ul class="bullets risk">{"".join(f"<li>{E(r)}</li>" for r in c.get('risks', []))}</ul>

<div class="pager">
  {f'<a class="prev" href="{nav["prev"]}"><span class="pg-l">&larr; Previous  K</span><span class="pg-n">{E(procs[idx-1]["l3_name"])}</span></a>' if nav["prev"] else '<span style="flex:1"></span>'}
  {f'<a class="next" href="{nav["next"]}"><span class="pg-l">Next  J &rarr;</span><span class="pg-n">{E(procs[idx+1]["l3_name"])}</span></a>' if nav["next"] else '<span style="flex:1"></span>'}
</div>"""

    write(f"{l1s}/{l2s}/{pid_l}/index.html",
          page(3, f'{p["pid"]} {p["l3_name"]}',
               f'<div class="page-main">{main}</div>{toc}', trail,
               active_l1=p["l1_code"], active_l2=f'{p["l1_code"]}::{p["l2_code"]}',
               active_pid=p["pid"], procs_by_group=procs_by_group, nav=nav, has_toc=True))


def render_ea(ea):
    diagrams = ea.get("diagrams", [])
    n_land = sum(1 for d in diagrams if d.get("kind") == "Domain landscape")
    n_flow = len(diagrams) - n_land
    cards = []
    for dg in diagrams:
        cards.append(f"""<a class="dcard" href="{dg['slug']}/">
  <div class="dc-top"><span class="dc-code">{E(dg['id'])}</span><h3>{E(dg['title'])}</h3></div>
  <p>{E(dg.get('blurb',''))}</p>
  <div class="dc-foot">{E(dg.get('kind','Cross-domain flow'))}</div>
</a>""")
    body = f"""<h1>Enterprise Architecture Diagrams</h1>
<p class="lede">{n_land} domain landscapes and {n_flow} cross-domain integration flows showing how Air Canada's
systems actually connect, including the seams where data is re-keyed by hand.</p>
{TIER_LEGEND}
<div class="grid">{"".join(cards) or '<p>No diagrams generated yet.</p>'}</div>"""
    write("ea-diagrams/index.html",
          page(1, "EA Diagrams", body,
               [("Home", "../index.html"), ("EA Diagrams", None)], active_l1="EA"))

    for dg in diagrams:
        img_abs = os.path.join(ROOT, "assets", "img", f"{dg['slug']}.png")
        if os.path.exists(img_abs):
            diagram = (f'<div class="diagram-wrap"><span class="dg-hint">Click to zoom</span>'
                       f'<img src="../../assets/img/{dg["slug"]}.png" alt="{E(dg["title"])}" loading="lazy"></div>')
        else:
            diagram = '<div class="diagram-wrap"><div class="dg-missing">Diagram not yet rendered.</div></div>'
        notes = "".join(f"<li>{E(n)}</li>" for n in dg.get("notes", []))
        body = f"""<div class="page-head">
  <button class="pid-badge" data-pid="{E(dg['id'])}">{E(dg['id'])}<span class="copy-ic">&#128203;</span></button>
  <span class="updated">Updated {BUILD_DATE}</span></div>
<h1>{E(dg['title'])}</h1>
<p class="lede">{E(dg.get('blurb',''))}</p>
{diagram}
<h2>Systems in this view</h2>
<div class="card">{sys_tags(dg.get('systems', []))}</div>
{f'<h2>Reading notes</h2><ul class="bullets">{notes}</ul>' if notes else ''}"""
        write(f"ea-diagrams/{dg['slug']}/index.html",
              page(2, dg["title"], body,
                   [("Home", "../../index.html"), ("EA Diagrams", "../"), (dg["title"], None)],
                   active_l1="EA"))


def build_search_index(procs, content, ea):
    docs = []
    for d in DOMAINS:
        docs.append({"t": "domain", "p": d["code"], "n": d["name"],
                     "c": "Domain", "u": f"{slugify(d['name'])}/", "s": "", "y": ""})
        for g in d["l2"]:
            docs.append({"t": "group", "p": f'{d["code"]}-{g["code"]}', "n": g["name"],
                         "c": d["name"], "u": f"{slugify(d['name'])}/{slugify(g['name'])}/",
                         "s": "", "y": ""})
    for p in procs:
        c = content.get(p["pid"], {})
        steps = " ".join(s.get("name", "") for s in c.get("l4_steps", []))
        systems = " ".join(c.get("systems", []))
        docs.append({"t": "process", "p": p["pid"], "n": p["l3_name"],
                     "c": f'{p["l1_name"]} › {p["l2_name"]}',
                     "u": f'{p["l1_slug"]}/{p["l2_slug"]}/{p["pid"].lower()}/',
                     "s": steps, "y": systems})
        for s in c.get("l4_steps", []):
            docs.append({"t": "step", "p": f'{p["pid"]}.{s.get("step","")}',
                         "n": s.get("name", ""), "c": f'Step in {p["l3_name"]}',
                         "u": f'{p["l1_slug"]}/{p["l2_slug"]}/{p["pid"].lower()}/#steps',
                         "s": s.get("role", ""), "y": s.get("system", "")})
    for dg in ea.get("diagrams", []):
        docs.append({"t": "ea", "p": dg["id"], "n": dg["title"], "c": "EA Diagram",
                     "u": f'ea-diagrams/{dg["slug"]}/', "s": "",
                     "y": " ".join(dg.get("systems", []))})
    write("assets/js/search-index.json", json.dumps({"docs": docs}, ensure_ascii=False))
    return len(docs)


def main():
    global EA_COUNT
    procs = all_processes()
    content = load_json(DATA, {})
    ea = load_json(EA_DATA, {"diagrams": []})
    EA_COUNT = len(ea.get("diagrams", []))

    procs_by_group = OrderedDict()
    for p in procs:
        procs_by_group.setdefault(f'{p["l1_code"]}::{p["l2_code"]}', []).append(p)

    render_home(procs, content)
    for d in DOMAINS:
        render_l1(d, procs, content)
        for g in d["l2"]:
            render_l2(d, g, procs, content, procs_by_group)
    for i, p in enumerate(procs):
        render_process(p, content, procs, i, procs_by_group)
    render_ea(ea)
    n_docs = build_search_index(procs, content, ea)

    open(os.path.join(ROOT, ".nojekyll"), "w").close()

    done = sum(1 for p in procs if p["pid"] in content)
    n_pages = 1 + len(DOMAINS) + sum(len(d["l2"]) for d in DOMAINS) + len(procs) + 1 + len(ea.get("diagrams", []))
    print(f"Built {n_pages} pages")
    print(f"  {len(procs)} process pages ({done} documented, {len(procs)-done} queued)")
    print(f"  {len(ea.get('diagrams', []))} EA diagram pages")
    print(f"  search index: {n_docs} documents")


if __name__ == "__main__":
    main()
