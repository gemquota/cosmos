#!/usr/bin/env python3
"""Build the knowledge-graph JSON for mykb.

Walks wiki/**/*.md, extracts every node (file) with its title, and creates
edges from [[wikilinks]] and markdown links to other wiki files. Also adds
"related" edges between concepts that share >= 3 tags, keeping the graph
semantically dense while staying derived from actual content.

Writes:
  components/mykb/graph.json              (static hosting / wiki browser)
  components/mykb/.wiki-daemon/graph.json (wiki daemon API)

Usage: python3 .wiki-daemon/build_graph.py
"""
import os, re, json, sys
from collections import defaultdict

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(DIR, 'wiki')
OUT_STATIC = os.path.join(DIR, 'graph.json')
OUT_DAEMON = os.path.join(DIR, '.wiki-daemon', 'graph.json')

WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
MDLINK = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:[^)]*)\)')

def read_fm_title(text):
    m = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', text, re.DOTALL)
    if m:
        t = re.search(r'^title:\s*"([^"]+)"', m.group(1), re.MULTILINE)
        if t:
            return t.group(1).strip()
    return None

def main():
    nodes = []
    bodies = {}
    titles = {}
    paths_by_basename = defaultdict(list)
    for root, dirs, files in os.walk(WIKI):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, WIKI).replace(os.sep, '/')
            node_id = 'wiki/' + rel[:-3]
            try:
                text = open(full, encoding='utf-8').read()
            except Exception:
                continue
            bodies[node_id] = text
            title = read_fm_title(text) or rel[:-3].split('/')[-1].replace('-', ' ').title()
            titles[node_id] = title
            paths_by_basename[rel[:-3].split('/')[-1].lower()].append(node_id)

    id_set = set(bodies)
    seen_edges = set()
    edges = []

    def add_edge(src, tgt):
        if src == tgt or src not in id_set or tgt not in id_set:
            return
        key = (src, tgt)
        if key not in seen_edges:
            seen_edges.add(key)
            edges.append({'source': src, 'target': tgt})

    def resolve_target(raw):
        t = raw.strip()
        if t.endswith('.md'):
            t = t[:-3]
        t = t.lstrip('./').split('#')[0]
        # Prefer the exact path: wiki/... links already carry the prefix
        cands = []
        if t.startswith('wiki/'):
            cands.append(t)
        else:
            cands.append('wiki/' + t)
        base = t.split('/')[-1].lower()
        cands += paths_by_basename.get(base, [])
        for c in cands:
            if c in id_set:
                return c
        # Obsidian-style short link without dir prefix
        return None

    for node_id, text in bodies.items():
        for m in WIKILINK.finditer(text):
            tgt = resolve_target(m.group(1))
            if tgt:
                add_edge(node_id, tgt)
        for m in MDLINK.finditer(text):
            tgt = resolve_target(m.group(1))
            if tgt:
                add_edge(node_id, tgt)

    # Semantic edges: concepts sharing >= 3 tags
    tag_of = defaultdict(set)
    for node_id, text in bodies.items():
        m = re.search(r'^tags:\s*\[(.*?)\]', text, re.DOTALL)
        if m:
            tags = re.findall(r'"([^"]+)"', m.group(1))
            tag_of[node_id] = set(tags)
    tag_nodes = sorted(node_id for node_id in id_set if len(tag_of[node_id]) >= 3)
    for i, a in enumerate(tag_nodes):
        ta = tag_of[a]
        for b in tag_nodes[i+1:]:
            if len(ta & tag_of[b]) >= 3:
                add_edge(a, b)

    g = {'nodes': [{'id': nid, 'title': titles[nid]} for nid in sorted(id_set)], 'edges': edges}

    os.makedirs(os.path.dirname(OUT_DAEMON), exist_ok=True)
    with open(OUT_STATIC, 'w', encoding='utf-8') as f:
        json.dump(g, f, ensure_ascii=False, separators=(',', ':'))
    with open(OUT_DAEMON, 'w', encoding='utf-8') as f:
        json.dump(g, f, ensure_ascii=False, separators=(',', ':'))

    print(f'graph: {len(g["nodes"])} nodes, {len(g["edges"])} edges')
    print(f'  static: {OUT_STATIC} ({os.path.getsize(OUT_STATIC)/1024:.0f} KB)')
    print(f'  daemon: {OUT_DAEMON}')

if __name__ == '__main__':
    sys.exit(main())
