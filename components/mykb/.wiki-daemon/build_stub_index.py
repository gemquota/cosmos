#!/usr/bin/env python3
"""Build the stub index (stub-index.json) for the mykb app.

Scans components/mykb/wiki and lists every file whose frontmatter status is
'stub' (the only reliable stub signal), with metadata the app needs
(words, status, type, title, tags, area, inferred category path).

Usage: python3 .wiki-daemon/build_stub_index.py
"""
import datetime as _dt
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WIKI = os.path.join(ROOT, 'wiki')

FM_RE = re.compile(r'^---\s*\n(.*?)\n---', re.S)
KEY_RE = re.compile(r'^(\w+):\s*(.*)$', re.M)
LIST_RE = re.compile(r'^\[(.*)\]$', re.S)
FLOOR = 320


def parse_frontmatter(text):
    fm = {}
    m = FM_RE.match(text)
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


def body_words(text):
    body = FM_RE.sub('', text, count=1)
    return len(re.findall(r'\S+', body))


def category_path(rel):
    """Infer domain/super/category/subcategory from the path's categories/ structure."""
    parts = rel.split('/')
    out = {'domain': '', 'super': '', 'category': '', 'sub': ''}
    try:
        if 'domains' in parts:
            out['domain'] = parts[parts.index('domains') + 1]
        if 'categories' in parts:
            ci = parts.index('categories')
            if ci + 1 < len(parts) and parts[ci + 1] != 'index.md':
                out['super'] = parts[ci + 1]
        if 'subcategories' in parts:
            si = parts.index('subcategories')
            if si + 1 < len(parts) and parts[si + 1] != 'index.md':
                out['category'] = parts[si + 1]
    except ValueError:
        pass
    return out


def main():
    stubs = []
    for p in sorted(glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(p, WIKI).replace(os.sep, '/')
        if rel == 'log.md' or rel.endswith('/index.md') or rel.endswith('/00-index.md'):
            continue
        with open(p, encoding='utf-8', errors='ignore') as fh:
            text = fh.read()
        fm = parse_frontmatter(text)
        words = body_words(text)
        status = fm.get('status', 'none')
        if status == 'stub':
            base = os.path.splitext(os.path.basename(rel))[0]
            cat = category_path(rel)
            stubs.append({
                'path': 'wiki/' + rel,
                'title': fm.get('title', base.replace('-', ' ').title()),
                'words': words,
                'status': status,
                'type': fm.get('type', 'concept'),
                'tags': fm.get('tags', []),
                'area': rel.split('/')[0],
                **cat,
            })
    out = {
        'generated': _dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
        'floor': FLOOR,
        'total': len(stubs),
        'stubs': stubs,
    }
    with open(os.path.join(ROOT, 'stub-index.json'), 'w') as fh:
        json.dump(out, fh, indent=1)
    print(f'stub-index.json: {len(stubs)} stubs')


if __name__ == '__main__':
    main()
