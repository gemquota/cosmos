#!/usr/bin/env python3
"""Build the Stub Auditor SPA (stub-audit.html).

Scans components/mykb/wiki for stub articles (status: stub, or sub-320 body
words) and emits a self-contained HTML review tool with options Keep /
Enrich / Categorize / Archive / Delete, plus the existing wiki directory
structure so Categorize can propose valid targets.

Usage: python3 .wiki-daemon/build_stub_audit.py
"""
import glob
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WIKI = os.path.join(ROOT, 'wiki')

FM_RE = re.compile(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', re.DOTALL)
KEY_RE = re.compile(r'^(\w+):\s*(.*)$', re.M)
LIST_RE = re.compile(r'^\[(.*)\]$', re.DOTALL)
WIKILINK_RE = re.compile(r'\[\[[^\]]+\]\]')

TEMPLATE = os.path.join(HERE, 'stub_audit_template.html')
OUT = os.path.join(ROOT, 'stub-audit.html')


def parse_fm(text):
    fm = {}
    m = FM_RE.match(text)
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        v = v.strip().strip('"').strip("'")
        lm = LIST_RE.match(v)
        fm[k] = [x.strip().strip('"').strip("'")
                 for x in lm.group(1).split(',') if x.strip()] if lm else v
    return fm


def body_words(text):
    return len(re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL).split())


def first_add_dates():
    """Best-effort map wiki-relative path -> first commit date (YYYY-MM-DD).

    Uses a single git log pass over the wiki tree (oldest-first) so "sort by
    oldest" works even though only a handful of files carry frontmatter dates.
    """
    dates = {}
    try:
        out = subprocess.run(
            ['git', 'log', '--reverse', '--format=%x1e%aI', '--name-only',
             '--diff-filter=A', '--', 'wiki'],
            capture_output=True, text=True, cwd=ROOT, timeout=120).stdout
    except Exception:
        return dates
    # NOTE: split on the record separator directly; str.splitlines() treats
    # \x1e as a line boundary and would swallow the date lines.
    for chunk in out.split('\x1e'):
        lines = chunk.split('\n')
        cur = lines[0].strip()[:10]
        if not cur:
            continue
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            rel = line.replace(os.sep, '/')
            marker = '/wiki/'
            if marker in rel:
                rel = rel.split(marker, 1)[1]
            if rel not in dates:
                dates[rel] = cur
    return dates


def main():
    items, n = [], 0
    dirs, areas = set(), set()
    created_map = first_add_dates()
    for p in sorted(glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(p, WIKI).replace(os.sep, '/')
        if rel == 'log.md' or rel == 'index.md' or rel.endswith('/index.md'):
            continue
        if '/raw/archive/' in rel:
            continue
        text = open(p, encoding='utf-8', errors='ignore').read()
        fm = parse_fm(text)
        if str(fm.get('hub', '')).lower() == 'true' or fm.get('type') == 'index':
            continue
        w = body_words(text)
        if fm.get('status') != 'stub' and w >= 320:
            continue
        n += 1
        title = fm.get('title') or rel.rsplit('/', 1)[-1][:-3].replace('-', ' ').title()
        snip = re.sub(r'\s+', ' ', re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL)).strip()
        body = re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL)
        items.append({
            'n': n, 't': title, 'p': rel, 'w': w,
            's': fm.get('status', 'none'),
            'c': fm.get('created') or created_map.get(rel, ''),
            'l': len(WIKILINK_RE.findall(body)),
            'd': fm.get('description', '')[:160],
            'x': snip[:300],
        })
        parts = rel.split('/')
        dirs.add('/'.join(parts[:-1]))
        areas.add(parts[0])
    dirs = sorted(d for d in dirs if d)
    areas = sorted(areas)

    data = {'items': items, 'dirs': dirs, 'areas': areas, 'built': '2026-08-04'}
    payload = json.dumps(data, ensure_ascii=False)
    html = open(TEMPLATE, encoding='utf-8').read()
    html = html.replace('/*__DATA__*/', payload.replace('</', '<\\/'))
    open(OUT, 'w', encoding='utf-8').write(html)
    print(f'stub-audit.html written: {len(items)} stub files, {len(areas)} areas, {len(dirs)} dirs')


if __name__ == '__main__':
    main()
