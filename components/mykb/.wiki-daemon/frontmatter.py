"""Minimal OKF frontmatter parsing shared by the wiki index builders.

Keeps the enriched files.json entries ({path, type, title, tags}) identical
between the daemon builder (.wiki-daemon/build_files_index.py) and the
GitHub Pages snapshot (gen-static-data.py at the repo root).
"""

from __future__ import annotations

import re

FM_RE = re.compile(r'^---\s*\n(.*?)\n---', re.S)
KEY_RE = re.compile(r'^(\w+):\s*(.*)$', re.M)
LIST_RE = re.compile(r'^\[(.*)\]$', re.S)


def parse_frontmatter(text):
    """Return frontmatter fields; scalars are unquoted, lists are arrays."""
    fm = {}
    m = FM_RE.match(text or '')
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        v = v.strip().strip('"').strip("'")
        lm = LIST_RE.match(v)
        if lm:
            fm[k] = [x.strip().strip('"').strip("'")
                     for x in lm.group(1).split(',') if x.strip()]
        else:
            fm[k] = v
    return fm


def entry_for(rel, text):
    """Build one enriched files.json entry for a markdown file path."""
    fm = parse_frontmatter(text)
    title = (fm.get('title') or '').strip()
    if not title:
        name = rel.rsplit('/', 1)[-1]
        title = name[:-3].replace('-', ' ').replace('_', ' ').strip().title()
    return {
        'path': rel,
        'type': (fm.get('type') or '').strip(),
        'title': title,
        'tags': fm.get('tags', []) or [],
    }
