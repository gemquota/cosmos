#!/usr/bin/env python3
"""Regenerate files.json — the flat list of every .md file in the mykb bundle.

Writes components/mykb/files.json in the format the wiki browser expects
(an array of paths relative to the bundle root, all markdown).

Usage: python3 .wiki-daemon/build_files_index.py
"""
import os, json, sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(DIR, 'files.json')
EXCLUDE_DIRS = {'.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian'}
EXCLUDE_FILES = {'mykb-code.md', 'mykb-content.md'}

files = []
for root, dirs, names in os.walk(DIR):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    relroot = os.path.relpath(root, DIR).replace(os.sep, '/')
    for fn in sorted(names):
        if not fn.endswith('.md'):
            continue
        if fn in EXCLUDE_FILES:
            continue
        rel = fn if relroot == '.' else relroot + '/' + fn
        files.append(rel)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(files, f, ensure_ascii=False)

print(f'Wrote {len(files)} files to {OUT}')
