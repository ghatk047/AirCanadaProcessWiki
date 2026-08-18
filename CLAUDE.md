# Air Canada Process Wiki — agent instructions

## What this is

A GitHub Pages wiki documenting Air Canada's business processes and the systems that
carry them. It is a **pre-sales artifact** for IT Application Management and User
Support work, written to be read by an Air Canada CIO. Everything in it must survive
that reader.

## The single hard rule

**Never assert a system Air Canada does not run.** Naming a competitor's install as
theirs is disqualifying. `scripts/ac_systems.py` is the only source of truth for
system names, and every system carries an evidence tier:

| Tier | Meaning | Use in a bid |
|---|---|---|
| A | Confirmed — Air Canada or vendor public source | Assert freely |
| B | Indicated — job postings, technographics, trade press | Assert with attribution |
| C | Industry pattern — **not** evidenced for Air Canada | Never assert; frame as a question |
| U | Unknown — open discovery question | Surface as a discovery item |

The four U-tier entries (integration middleware, SIEM and SOC, workforce identity,
ITSM product) are deliberately visible. They are the questions to ask in discovery,
not gaps to paper over.

### Corrections that override common assumptions

- MRO core is **TRAX** — not AMOS, not Ramco, not IFS/Mxi Maintenix
- Cargo is **CHAMP Cargospot neo**, implementation in flight — not IBS iCargo
- Network planning, scheduling and ops control is **Lufthansa Systems NetLine**
- Crew and OCC run on **Jeppesen**
- Cloud posture is **AWS-first** — not GCP
- Analytics is the **Databricks lakehouse**, Cloudera sunsetting — not Snowflake
- Contact centre is **Amazon Connect + Salesforce Service Cloud Voice** — not Genesys
- Customer identity is **SAP Customer Data Cloud** — Okta is not evidenced

## Build pipeline

Run in this order from the repo root:

```bash
python3 scripts/build_content.py     # scripts/content/*.py -> data/processes.json
python3 scripts/render_diagrams.py   # Mermaid -> assets/img/*.png via mmdc
python3 scripts/build_site.py        # -> all HTML + assets/js/search-index.json
```

`data/processes.json` is a **derived artifact and is gitignored**. The source of
truth is `scripts/content/*.py`.

## Authoring process content

Author in `scripts/content/`, using `P()` and `S()` from `scripts/content_lib.py`.
Do **not** hand-write Mermaid or swim lanes — `content_lib` derives both from the
phases and steps, which is what keeps every diagram valid.

Each process needs: 3 phases, 8–14 steps, 5 KPIs, 5 risks. Steps carry role, system,
input, output, KPI, decision/exception flags and a **real** pain point. Roles must be
Air Canada–specific ("YYZ Operations Control Duty Manager", "APPR Adjudicator",
"Aeroplan Member Services Agent"), never generic.

Anchor content on real, evidenced pain: the CTA/APPR complaint backlog and the 2026
arbitration pilot, the June 2023 ops-control outage, the Jazz and PAL Express operator
seam, the Cargospot cutover double-entry window, and the Moffatt v. Air Canada
chatbot ruling that makes human-in-loop governance mandatory rather than optional.

## Mermaid rules (violations break mmdc)

- Line 1 must be the `%%{init}%%` directive; line 2 the flowchart directive; no blank line between
- Never use YAML frontmatter
- Node IDs start with a letter; arrows are always `-->`
- Node labels are plain text — no `( ) & < >`
- Top level is `flowchart TB` with `direction LR` inside each phase subgraph
- **Chain steps within a phase, then link phases by subgraph id (`P1 --> P2`).**
  `direction` is silently ignored if a node-to-node edge crosses a subgraph boundary,
  which collapses the whole diagram onto one axis.

## Page depth and asset paths

| Page | Depth | Prefix |
|---|---|---|
| `index.html` | 0 | `assets/` |
| `{l1}/index.html` | 1 | `../assets/` |
| `{l1}/{l2}/index.html` | 2 | `../../assets/` |
| `{l1}/{l2}/{pid}/index.html` | 3 | `../../../assets/` |
| `ea-diagrams/{slug}/index.html` | 2 | `../../assets/` |

The sidebar is static HTML baked into every page — never JavaScript-rendered.
L2 groups are keyed on the composite `{l1_code}::{l2_code}`; keying on slug alone
collapses distinct groups that share a code (CX-CC and CM-CC both slug to "cc").

## Conventions

- Air Canada red `#D2001F`, black `#1A1A1A`. Never navy or orange.
- Canadian and British spelling in prose ("optimisation", "programme", "labour")
- PID format `AC-{L1}-{L2}-{NN}`
- Prose: plain declarative sentences. No marketing register, no em dashes in
  generated content, no exclamation marks.
