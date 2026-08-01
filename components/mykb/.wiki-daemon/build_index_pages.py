#!/usr/bin/env python3
"""Refresh wiki area index pages with a Concepts listing of every article.

For each one-level subdirectory of wiki/, updates its index.md (or README.md)
so every article in that directory is reachable via a markdown link — this
satisfies okf lint's reachability rule and improves navigation.

Usage: python3 .wiki-daemon/build_index_pages.py
"""
import os, re, json, sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(DIR, 'wiki')

def frontmatter_title(path):
    text = open(path, encoding='utf-8').read()
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', text, re.DOTALL)
    if m:
        t = re.search(r'^title:\s*"([^"]+)"', m.group(1), re.MULTILINE)
        if t:
            return t.group(1).strip()
    return None

def main():
    updated = 0
    for area in sorted(os.listdir(WIKI)):
        adir = os.path.join(WIKI, area)
        if not os.path.isdir(adir) or area in ('daily',):
            continue
        idx = os.path.join(adir, 'index.md')
        if not os.path.exists(idx):
            idx = os.path.join(adir, 'README.md')
        if not os.path.exists(idx):
            continue
        entries = []
        for fn in sorted(os.listdir(adir)):
            if not fn.endswith('.md') or fn in ('index.md', 'README.md'):
                continue
            full = os.path.join(adir, fn)
            if not os.path.isfile(full):
                continue
            title = frontmatter_title(full) or fn[:-3].replace('-', ' ').title()
            slug = fn[:-3]
            entries.append((slug, title))
        if not entries:
            continue
        block = '## Concepts\n\n' + '\n'.join(
            '- [%s](%s.md) — %s' % (title, slug, title)
            for slug, title in entries
        ) + '\n'
        text = open(idx, encoding='utf-8').read()
        # Replace an existing Concepts section, else append
        pattern = re.compile(r'## Concepts\n.*?(?=\n## |\Z)', re.DOTALL)
        if pattern.search(text):
            text2 = pattern.sub(block, text, count=1)
        else:
            text2 = text.rstrip() + '\n\n' + block
        if text2 != text:
            open(idx, 'w', encoding='utf-8').write(text2)
            updated += 1
            print('updated', os.path.relpath(idx, DIR))
    print('index pages updated:', updated)

if __name__ == '__main__':
    main()
