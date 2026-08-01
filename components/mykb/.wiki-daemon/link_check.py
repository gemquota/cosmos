#!/usr/bin/env python3
"""Check wikilink integrity across the mykb bundle.

Resolves every [[...]] wikilink and markdown .md link in .md files to a real
file on disk. Reports unresolved links grouped by source file.

Usage: python3 .wiki-daemon/link_check.py [--limit N]
"""
import os, re, sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(DIR, 'wiki')

WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
MDLINK = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:[^)]*)\)')

def main():
    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])
    # Build canonical id set: path without .md, relative to bundle root
    ids = set()
    for root, dirs, files in os.walk(DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian', '.wiki-daemon')]
        for fn in files:
            if not fn.endswith('.md'):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, DIR).replace(os.sep, '/')
            ids.add(rel)
            ids.add(rel[:-3])

    broken = {}
    checked = 0
    for root, dirs, files in os.walk(DIR):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian', '.wiki-daemon')]
        for fn in files:
            if not fn.endswith('.md'):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, DIR).replace(os.sep, '/')
            text = open(full, encoding='utf-8').read()
            checked += 1
            for m in WIKILINK.finditer(text):
                t = m.group(1).strip()
                if t.endswith('.md'):
                    t = t[:-3]
                t = t.lstrip('./')
                cands = [t, t + '.md']
                ok = any(c in ids for c in cands)
                if not ok:
                    broken.setdefault(rel, []).append('[[%s]]' % t)
            for m in MDLINK.finditer(text):
                t = m.group(1).strip().lstrip('./')
                if t not in ids:
                    broken.setdefault(rel, []).append('(%s)' % t)

    total_broken = sum(len(v) for v in broken.values())
    print(f'checked {checked} files; {total_broken} unresolved links in {len(broken)} files')
    for src in sorted(broken)[:limit or len(broken)]:
        print(f'  {src}:')
        for l in broken[src][:8]:
            print(f'    {l}')
    return 1 if total_broken else 0

if __name__ == '__main__':
    sys.exit(main())
