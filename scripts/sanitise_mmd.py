# -*- coding: utf-8 -*-
"""
Mermaid sanitiser.

Every rule here exists because it caused an mmdc render failure at some point.
Do not "simplify" it without re-running render_all.
"""
import re

INIT_LINE = "%%{init: {'theme':'base','themeVariables':{'fontSize':'13px'}}}%%"


def sanitise_mermaid(mmd: str, font_size: str = "13px") -> str:
    init = "%%{init: {'theme':'base','themeVariables':{'fontSize':'" + font_size + "'}}}%%"

    # 1. Strip markdown fences that LLM output tends to wrap around diagrams.
    mmd = re.sub(r'^```[a-z]*\n?', '', mmd, flags=re.MULTILINE)
    mmd = re.sub(r'```$', '', mmd, flags=re.MULTILINE)

    # 2. Remove YAML frontmatter -- mmdc parse-errors on line 1 if present.
    mmd = re.sub(r'^---.*?---\s*', '', mmd, flags=re.DOTALL)

    # 3. Repair HTML-encoded arrows.
    mmd = mmd.replace('--&gt;', '-->').replace('--gt', '-->')

    # 4. Node IDs must start with a letter: 1.1 -> S1_1
    mmd = re.sub(r'\b(\d+)\.(\d+)\b', r'S\1_\2', mmd)

    # 5. Strip ()&<> from inside node labels.
    def clean_label(m):
        text = re.sub(r'[()&<>]', '', m.group(2))
        text = re.sub(r'  +', ' ', text).strip()
        return f'{m.group(1)}{text}{m.group(3)}'
    mmd = re.sub(r'(\[)([^\]]+)(\])', clean_label, mmd)
    mmd = re.sub(r'(\()([^)]+)(\))', clean_label, mmd)

    # 6. Bare node label after an arrow -> wrap in [...]
    #    mmdc reports this as "Expecting SEMI".
    fixed = []
    for line in mmd.split('\n'):
        s = line.strip()
        skip = (s.startswith('%%') or s.startswith('subgraph') or
                s.startswith('end') or s.startswith('style') or
                s.startswith('classDef') or s.startswith('class ') or
                s.startswith('linkStyle') or
                s.startswith('flowchart') or s.startswith('graph') or
                '|' in s)
        if not skip:
            def _fix(m):
                nid = m.group(2)
                label = re.sub(r'[()&<>]', '', nid + ' ' + m.group(3)).strip()
                return f'{m.group(1)}{nid}[{label}]'
            line = re.sub(r'(--+>)\s*([A-Za-z]\w*)\s+([A-Za-z][^\[(\|\n][^\n]*)', _fix, line)
        fixed.append(line)   # must stay outside the `if` -- dropping lines silently breaks diagrams
    mmd = '\n'.join(fixed)

    # 7. Guarantee an %%{init}%% directive on line 1 -- only inject the
    # default if one is genuinely missing. An existing init line (e.g. one
    # a deterministic builder already produced, with its own theme/curve
    # settings) is left untouched rather than clobbered with this module's
    # hardcoded default.
    if '%%{init' not in mmd:
        mmd = init + '\n' + mmd

    # 8. No blank line between %%{init}%% and the flowchart directive.
    cleaned = []
    for line in mmd.strip().split('\n'):
        if cleaned and cleaned[-1].startswith('%%{init') and line.strip() == '':
            continue
        cleaned.append(line)
    return '\n'.join(cleaned).strip()


def svg_safe(text: str) -> str:
    """Bare & in SVG XML is a parse error."""
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9A-Fa-f]+);)', '&amp;', text)


def validate(mmd: str):
    """Cheap pre-flight checks. Returns a list of problem strings."""
    problems = []
    lines = mmd.split('\n')
    if not lines or not lines[0].startswith('%%{init'):
        problems.append("line 1 is not the %%{init}%% directive")
    if len(lines) < 2 or not re.match(r'^(flowchart|graph)\s', lines[1].strip()):
        problems.append("line 2 is not a flowchart/graph directive")
    if '--gt' in mmd or '--&gt;' in mmd:
        problems.append("encoded arrow survived sanitising")
    for i, ln in enumerate(lines, 1):
        for lbl in re.findall(r'\[([^\]]*)\]', ln):
            if re.search(r'[()&<>]', lbl):
                problems.append(f"line {i}: illegal char in label {lbl!r}")
    opens = sum(1 for ln in lines if ln.strip().startswith('subgraph'))
    ends = sum(1 for ln in lines if ln.strip() == 'end')
    if opens > ends:
        problems.append(f"{opens} subgraph vs {ends} end -- unbalanced")
    return problems


if __name__ == "__main__":
    bad = """```mermaid
---
config:
  layout: elk
---
graph LR

1.1[Start (here) & now] --gt 2.1 Do the thing
subgraph P1 [Phase One]
2.1 --> 3.1[End]
end
```"""
    out = sanitise_mermaid(bad)
    print(out)
    print("\nvalidate ->", validate(out) or "clean")
