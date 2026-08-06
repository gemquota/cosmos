#!/usr/bin/env python3
"""Check wikilink + markdown-link integrity across the mykb wiki.

Resolves every [[...]] wikilink and [text](path.md) link to a real file on
disk, using the same rules as the app (resolveWikiPath): `../` is resolved
against the source file's directory, `wiki/` prefixes and `.md` suffixes
normalize, and a unique-basename fallback handles moved/archived pages.
Inline code spans and fenced code blocks are ignored (syntax examples are
not links). The default scope is `wiki/` (actionable content); `--all`
includes raw archives (historical, expected to have stale links).

Usage: python3 .wiki-daemon/link_check.py [--limit N] [--all]
"""
import os, re, sys
from collections import Counter

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(DIR, 'wiki')

WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
MDLINK = re.compile(r'\[[^\]]*\]\(([^)#]+\.md)(?:[#)][^)]*)?\)')
CODE_BLOCK = re.compile(r'```.*?```', re.DOTALL)
CODE_SPAN = re.compile(r'``[^`]*``|`[^`]*`')
FRONTMATTER = re.compile(r'^---\s*\n.*?\n(?:---|\.\.\.)', re.DOTALL)


def dotseg(path):
    out = []
    for seg in path.split('/'):
        if seg == '..':
            if out:
                out.pop()
        elif seg in ('.', ''):
            continue
        else:
            out.append(seg)
    return '/'.join(out)


class Resolver:
    def __init__(self):
        self.ids = set()
        self.base = {}
        for root, dirs, files in os.walk(DIR):
            dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian', '.wiki-daemon')]
            for fn in files:
                if not fn.endswith('.md'):
                    continue
                rel = os.path.relpath(os.path.join(root, fn), DIR).replace(os.sep, '/')
                self.ids.add(rel)
                self.ids.add(rel[:-3])
                self.base.setdefault(fn[:-3].lower(), []).append(rel)

    def resolves(self, target, srcdir):
        t = target.strip()
        t = re.sub(r'^\./', '', t)  # strip one leading ./, keep ../ for relative
        if t.endswith('.md'):
            t = t[:-3]
        if not t or t.startswith(('#', 'http')):
            return True
        cands = set()
        if t.startswith('../'):
            rel = dotseg((srcdir + '/' if srcdir else '') + t)
            cands.add(rel)
            cands.add('wiki/' + rel)
        elif srcdir:
            cands.add(srcdir + '/' + t)
            cands.add('wiki/' + srcdir + '/' + t)
        cands.add(t)
        cands.add('wiki/' + t)
        if t.startswith('wiki/'):
            cands.add(t[5:])
        if t.startswith('wiki/wiki/'):
            cands.add(t[10:])
        for c in cands:
            for form in (c, c + '.md'):
                if form in self.ids or form.lstrip('/') in self.ids:
                    return True
        b = t.split('/')[-1].lower()
        hits = self.base.get(b, [])
        if len(hits) == 1:
            return True
        wiki_hits = [h for h in hits if h.startswith('wiki/')]
        if len(wiki_hits) == 1:
            return True
        return False


def main():
    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])
    scope_all = '--all' in sys.argv
    roots = [WIKI] if not scope_all else [DIR]
    skip_dirs = set(('.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian', '.wiki-daemon'))
    r = Resolver()
    broken = {}
    checked = 0
    for root in roots:
        for cur, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if d not in skip_dirs]
            for fn in files:
                if not fn.endswith('.md'):
                    continue
                full = os.path.join(cur, fn)
                rel = os.path.relpath(full, DIR).replace(os.sep, '/')
                srcdir = rel.rsplit('/', 1)[0] if '/' in rel else ''
                text = open(full, encoding='utf-8').read()
                text = FRONTMATTER.sub('', text, count=1)
                text = CODE_BLOCK.sub(' ', text)
                text = CODE_SPAN.sub(' ', text)
                checked += 1
                for m in WIKILINK.finditer(text):
                    t = m.group(1).strip()
                    if not r.resolves(t, srcdir):
                        broken.setdefault(rel, []).append('[[%s]]' % t)
                for m in MDLINK.finditer(text):
                    t = m.group(1).strip()
                    if not r.resolves(t, srcdir):
                        broken.setdefault(rel, []).append('(%s)' % t)

    total = sum(len(v) for v in broken.values())
    scope = 'wiki' if not scope_all else 'bundle'
    print(f'checked {checked} files ({scope}); {total} unresolved links in {len(broken)} files')
    for src in sorted(broken)[:limit or len(broken)]:
        print(f'  {src}:')
        for l in broken[src][:8]:
            print(f'    {l}')
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
