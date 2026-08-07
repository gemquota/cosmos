#!/usr/bin/env python3
"""Build the knowledge-graph JSON for mykb.

Walks wiki/**/*.md, extracts every node (file) with its title, and creates
edges from [[wikilinks]] and markdown links to other wiki files. Also adds
"related" edges between concepts that share >= 3 tags, keeping the graph
semantically dense while staying derived from actual content.

Also emits the payload files the standalone knowledge-graph page
(okf-graph.html) lazy-loads at runtime instead of baking in:

  catalog.json — every .md in the bundle (id/title/type/description/tags),
                 so the graph app can rebuild types/tags/filters statically
  index.json   — per-directory index entries (index.md presence, listings)
  log.json     — the bundle log markdown (Files → Indexes history view)

Writes (static hosting / wiki browser, then wiki daemon API):
  components/mykb/graph.json  + catalog.json / index.json / log.json
  components/mykb/.wiki-daemon/<same>

Usage: python3 .wiki-daemon/build_graph.py
"""
import os, re, json, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from frontmatter import parse_frontmatter  # noqa: E402

DIR = os.path.dirname(HERE)
WIKI = os.path.join(DIR, 'wiki')
OUT_STATIC = os.path.join(DIR, 'graph.json')
OUT_DAEMON = os.path.join(DIR, '.wiki-daemon', 'graph.json')
EXCLUDE_DIRS = {'__pycache__', 'node_modules'}

WIKILINK = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')
MDLINK = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:[^)]*)\)')


def walk_md(base):
    """Return [(rel_path, abs_path)] for every .md under base (skip hidden)."""
    files = []
    for root, dirs, names in os.walk(base):
        dirs[:] = [d for d in dirs
                   if d not in EXCLUDE_DIRS and not d.startswith('.')]
        relroot = os.path.relpath(root, base).replace(os.sep, '/')
        for fn in sorted(names):
            if not fn.endswith('.md'):
                continue
            rel = fn if relroot == '.' else relroot + '/' + fn
            files.append((rel, os.path.join(root, fn)))
    return files


def title_from_name(rel):
    name = rel.rsplit('/', 1)[-1]
    return name[:-3].replace('-', ' ').replace('_', ' ').strip().title()


def first_paragraph(text):
    """First non-empty, non-frontmatter paragraph, trimmed to ~200 chars."""
    body = re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text or '', count=1,
                  flags=re.DOTALL)
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(('#', '>', '-', '*', '```', '|')):
            continue
        line = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', line)
        line = re.sub(r'[`*_~#]', '', line).strip()
        return line[:200]
    return ''


def catalog_entries(base):
    """Enriched catalog for every .md in the bundle (old EMBED.catalog shape)."""
    out = []
    for rel, full in walk_md(base):
        try:
            text = open(full, encoding='utf-8', errors='ignore').read()
        except OSError:
            text = ''
        fm = parse_frontmatter(text)
        nid = rel[:-3]
        d = rel.rsplit('/', 1)[0] if '/' in rel else '.'
        out.append({
            'id': nid,
            'title': fm.get('title') or title_from_name(rel),
            'type': (fm.get('type') or '').strip(),
            'description': (fm.get('description') or first_paragraph(text)).strip(),
            'tags': fm.get('tags') or [],
            'timestamp': fm.get('timestamp'),
            'status': fm.get('status'),
            'backlog_ref': None,
            'dir': d,
            'area': (d.split('/')[0] if d != '.' else '(root)'),
            'links_out': 0,
            'links_in': 0,
        })
    return out


def index_entries(catalog):
    """Per-directory index entries (old EMBED.index shape)."""
    by_dir = defaultdict(list)
    for c in catalog:
        by_dir[c['dir']].append(c)
    entries = []
    for d in sorted(by_dir):
        index_path = 'index.md' if d == '.' else d + '/index.md'
        idx_full = os.path.join(DIR, index_path)
        present = os.path.isfile(idx_full)
        listing = [{'id': c['id'], 'title': c['title'],
                    'description': c.get('description') or ''}
                   for c in by_dir[d]]
        types, tags = defaultdict(int), defaultdict(int)
        for c in by_dir[d]:
            if c.get('type'):
                types[c['type']] += 1
            for t in c.get('tags') or []:
                tags[t] += 1
        entries.append({
            'dir': d,
            'index_path': index_path,
            'present': present,
            'synthesized': not present,
            'body': open(idx_full, encoding='utf-8', errors='ignore').read()
                    if present else None,
            'count': len(by_dir[d]),
            'types': dict(types),
            'tags': dict(tags),
            'subdirs': sorted({c['dir'].split('/')[1]
                               for c in by_dir[d] if c['dir'].startswith(d + '/')}),
            'listing': listing,
        })
    return entries


def log_entries():
    """Bundle log markdown (old EMBED.logs shape)."""
    full = os.path.join(DIR, 'log.md')
    if not os.path.isfile(full):
        return []
    return [{'path': 'log.md', 'dir': '.',
             'content': open(full, encoding='utf-8', errors='ignore').read()}]


def main():
    # ── graph: wiki nodes + edges ──
    nodes = []
    bodies = {}
    titles = {}
    paths_by_basename = defaultdict(list)
    for rel, full in walk_md(WIKI):
        node_id = 'wiki/' + rel[:-3]
        try:
            text = open(full, encoding='utf-8').read()
        except Exception:
            continue
        bodies[node_id] = text
        fm = parse_frontmatter(text)
        titles[node_id] = fm.get('title') or rel[:-3].split('/')[-1].replace('-', ' ').title()
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

    # Semantic edges: concepts sharing >= 3 tags (kept identical to the
    # historic builder: frontmatter is matched from the text start, so only
    # files whose frontmatter opens with `tags:` contribute — preserves the
    # established graph edge set across regenerations).
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

    g = {'nodes': [{'id': nid, 'title': titles[nid]} for nid in sorted(id_set)],
         'edges': edges}

    # ── payloads for the standalone graph page ──
    catalog = catalog_entries(DIR)
    index = index_entries(catalog)
    logs = log_entries()
    payloads = {
        'graph.json': g,
        'catalog.json': catalog,
        'index.json': index,
        'log.json': logs,
    }

    os.makedirs(os.path.dirname(OUT_DAEMON), exist_ok=True)
    for name, obj in payloads.items():
        static = os.path.join(DIR, name)
        daemon = os.path.join(OUT_DAEMON.rsplit('/', 1)[0], name)
        with open(static, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))
        with open(daemon, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, separators=(',', ':'))

    print(f'graph: {len(g["nodes"])} nodes, {len(g["edges"])} edges')
    print(f'catalog: {len(catalog)} entries, index: {len(index)} dirs, '
          f'logs: {len(logs)}')
    print(f'  static: {os.path.join(DIR, "graph.json")} '
          f'({os.path.getsize(OUT_STATIC)/1024:.0f} KB)')
    print(f'  daemon: {OUT_DAEMON}')


if __name__ == '__main__':
    sys.exit(main())
