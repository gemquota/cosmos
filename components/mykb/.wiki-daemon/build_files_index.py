#!/usr/bin/env python3
"""Regenerate files.json — the enriched index of every .md file in mykb.

Writes components/mykb/files.json in the format the wiki browser expects:
an array of {path, type, title, tags} entries (paths relative to the bundle
root, all markdown). The browser derives the Content/Meta split, Type
grouping, and the Types/Folders metrics from this metadata.

Usage: python3 .wiki-daemon/build_files_index.py
"""
import os, json, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from frontmatter import entry_for  # noqa: E402

DIR = os.path.dirname(HERE)
OUT = os.path.join(DIR, 'files.json')
EXCLUDE_DIRS = {'__pycache__', 'node_modules'}

files = []
for root, dirs, names in os.walk(DIR):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
    relroot = os.path.relpath(root, DIR).replace(os.sep, '/')
    for fn in sorted(names):
        if not fn.endswith('.md'):
            continue
        rel = fn if relroot == '.' else relroot + '/' + fn
        full = os.path.join(root, fn)
        try:
            with open(full, encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
        except OSError:
            text = ''
        files.append(entry_for(rel, text))

files.sort(key=lambda e: e['path'])

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(files, f, ensure_ascii=False, indent=1)

print(f'Wrote {len(files)} files to {OUT}')
