# Air Canada Process Wiki

A business-process and systems reference for **Air Canada**, published as a static
site on GitHub Pages.

**Live site:** https://ghatk047.github.io/AirCanadaProcessWiki/

284 processes across 12 L1 domains and 48 L2 groups, mapped to 71 named systems,
with 27 enterprise-architecture diagrams. Built as a pre-sales discovery artifact
for IT Application Management and User Support work.

## Evidence tiers

Every system reference carries an evidence tier, because a process wiki aimed at an
airline CIO is only useful if it is honest about what is known:

| Tier | Meaning |
|---|---|
| **A** | Confirmed — Air Canada or vendor public source |
| **B** | Indicated — job postings, technographic data, trade press |
| **C** | Industry pattern — *not* evidenced for Air Canada |
| **U** | Unknown — an open discovery question |

The U-tier entries (integration middleware, SIEM and SOC, workforce identity, ITSM
product) are shown deliberately. They are the questions worth asking, not gaps to
paper over.

## Build

```bash
python3 scripts/build_content.py     # scripts/content/*.py -> data/processes.json
python3 scripts/render_diagrams.py   # Mermaid -> assets/img/*.png via mmdc
python3 scripts/build_site.py        # -> all HTML + search index
```

Requires Python 3, `openpyxl`, and [`mermaid-cli`](https://github.com/mermaid-js/mermaid-cli) 11.x.
`data/processes.json` is a derived artifact and is gitignored; the source of truth
for content is `scripts/content/*.py`.

## Disclaimer

Compiled from public sources. Not affiliated with, endorsed by, or authorised by Air
Canada. Air Canada, Aeroplan and Altitude are trademarks of Air Canada. Tier C and
tier U entries are explicitly *not* claims of fact about Air Canada's estate.
