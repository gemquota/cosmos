#!/usr/bin/env python3
"""Build the stub review + guidance datasets for the mykb app.

Scans components/mykb/wiki and emits two compact datasets:

  stub-review.json  — stub articles (frontmatter status: stub) plus the
                      pre-archived junk-entities trees, for the app's stub
                      triage section.
  guidance.json     — area coverage health (pages / stubs / stub % per area),
                      a ranked focus list for where research effort should go
                      next, and a snapshot of the persisted guidance queue
                      (wanted pages, research directions, open questions, and
                      page-level feedback) from
                      .wiki-daemon/buffers/guidance-queue.json.

Live mode uses the same scans via server.py's /api/v2/stubs and
/api/v2/guidance.

Usage: python3 .wiki-daemon/build_stub_audit.py
"""
import glob
import json
import os
import re
import subprocess
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WIKI = os.path.join(ROOT, 'wiki')

FM_RE = re.compile(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', re.DOTALL)
KEY_RE = re.compile(r'^(\w+):\s*(.*)$', re.M)
LIST_RE = re.compile(r'^\[(.*)\]$', re.DOTALL)
WIKILINK_RE = re.compile(r'\[\[[^\]]+\]\]')
WIKILINK_TARGET_RE = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]')
CODE_BLOCK_RE = re.compile(r'```.*?```', re.DOTALL)
CODE_SPAN_RE = re.compile(r'`{1,3}[^`]*`{1,3}')
SAFE_TARGET_RE = re.compile(r'^[A-Za-z0-9_./-]+$')

OUT = os.path.join(ROOT, 'stub-review.json')
GUIDANCE_OUT = os.path.join(ROOT, 'guidance.json')
DATE_CACHE = os.path.join(HERE, 'stub_created_dates.json')
GUIDANCE_QUEUE = os.path.join(HERE, 'buffers', 'guidance-queue.json')


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
    The result is cached keyed on HEAD so live-data scans don't re-run the
    (slow) git log on every request; the cache is rebuilt when HEAD moves.
    """
    head = None
    try:
        head = subprocess.run(['git', 'rev-parse', 'HEAD'],
                              capture_output=True, text=True, cwd=ROOT,
                              timeout=10).stdout.strip()
    except Exception:
        pass
    if os.path.isfile(DATE_CACHE):
        try:
            with open(DATE_CACHE, encoding='utf-8') as fh:
                cached = json.load(fh)
            if cached.get('head') == head and isinstance(cached.get('dates'), dict):
                return cached['dates']
        except Exception:
            pass

    dates = {}
    try:
        out = subprocess.run(
            ['git', 'log', '--reverse', '--format=%x1e%aI', '--name-only',
             '--diff-filter=A', '--', 'wiki'],
            capture_output=True, text=True, cwd=ROOT, timeout=120).stdout
    except Exception:
        return dates
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
    try:
        with open(DATE_CACHE + '.tmp', 'w', encoding='utf-8') as fh:
            json.dump({'head': head, 'dates': dates}, fh)
        os.replace(DATE_CACHE + '.tmp', DATE_CACHE)
    except Exception:
        pass
    return dates


def walk_wiki():
    """Walk wiki/ once. Yields (rel, frontmatter, body_words, text) for pages.

    Excludes log.md / index pages, hub-marked entries, and anything under
    raw/archive/. Used by both the stub scan and the coverage scan so they
    share one source of truth.
    """
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
        yield rel, fm, body_words(text), text


def walk_junk():
    """Walk pre-archived junk-entities trees. Yields (rel_to_root, text)."""
    for p in sorted(glob.glob(os.path.join(ROOT, 'raw', 'archive', 'junk-entities-*', '**', '*.md'), recursive=True)):
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        text = open(p, encoding='utf-8', errors='ignore').read()
        yield rel, text


def scan_stubs():
    """Scan wiki for stub articles and return the auditor dataset.

    Also surfaces the raw/archive/junk-entities-* trees (pre-archived junk that
    the previous passes decided to remove) so they can be deleted from the same
    review UI. Junk items carry j=1 and their full bundle-relative path. Only
    frontmatter status:stub wiki pages are included; short-but-not-stub pages
    are NOT part of the review pool.

    Returns the same shape the SPA expects: items / dirs / areas / built.
    Used both by the static build and by server.py's live-data endpoint.
    """
    items, n = [], 0
    dirs, areas = set(), set()
    created_map = first_add_dates()

    def collect(rel, fm, w, text, junk):
        nonlocal n
        n += 1
        title = fm.get('title') or rel.rsplit('/', 1)[-1][:-3].replace('-', ' ').title()
        snip = re.sub(r'\s+', ' ', re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL)).strip()
        body = re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL)
        items.append({
            'n': n, 't': title, 'p': rel, 'w': w,
            's': 'junk' if junk else fm.get('status', 'none'),
            'j': 1 if junk else 0,
            'c': fm.get('created') or created_map.get(rel, ''),
            'l': len(WIKILINK_RE.findall(body)),
            'd': fm.get('description', '')[:160],
            'x': snip[:300],
        })
        if not junk:
            parts = rel.split('/')
            dirs.add('/'.join(parts[:-1]))
            areas.add(parts[0])

    for rel, fm, w, text in walk_wiki():
        if fm.get('status') != 'stub':
            continue
        collect(rel, fm, w, text, junk=False)

    for rel, text in walk_junk():
        collect(rel, parse_fm(text), body_words(text), text, junk=True)

    return {
        'items': items,
        'dirs': sorted(d for d in dirs if d),
        'areas': sorted(areas),
        'built': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }


def _load_json(path):
    try:
        with open(path, encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return None


def _slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', (s or '').lower().strip())
    return re.sub(r'-+', '-', s).strip('-')


def scan_wanted_links():
    """Find [[wikilinks]] that resolve to no existing wiki page (red links).

    A red link is a standing research signal: pages the wiki itself says are
    missing. Resolution mirrors the app's resolveWikiPath (root-relative
    paths plus a unique-basename fallback) so moved/archived pages don't show
    up as wanted. Returns ranked candidates with link counts, the areas that
    link to them, and a suggested scaffold path.
    """
    pages = {}
    base_index = {}
    for p in glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True):
        rel = os.path.relpath(p, WIKI).replace(os.sep, '/')
        pages[rel] = True
        base_index.setdefault(rel.split('/')[-1][:-3].lower(), []).append(rel)

    def resolves(target):
        t = target.strip().lstrip('./')
        if t.endswith('.md'):
            t = t[:-3]
        if not t:
            return False
        cands = []
        if '/' in t:
            cands.append(t)
            cands.append(t + '.md')
            if t.startswith('wiki/'):
                cands.append(t[5:])
                cands.append(t[5:] + '.md')
            else:
                cands.append('wiki/' + t)
                cands.append('wiki/' + t + '.md')
            if any(c in pages for c in cands):
                return True
        base = t.split('/')[-1].lower()
        hits = base_index.get(base, [])
        if len(hits) == 1:
            return True
        wiki_hits = [h for h in hits if h.startswith('wiki/')]
        if len(wiki_hits) == 1:
            return True
        return False

    missing = {}
    for rel, fm, w, text in walk_wiki():
        area = rel.split('/')[0]
        text = re.sub(r'^---\s*\n.*?\n(?:---|\.\.\.)', '', text, count=1, flags=re.DOTALL)
        text = CODE_BLOCK_RE.sub(' ', text)
        text = CODE_SPAN_RE.sub(' ', text)
        for m in WIKILINK_TARGET_RE.finditer(text):
            t = m.group(1).strip()
            if not t or t.startswith('#') or t.startswith('http') or '#' in t:
                continue
            if t.startswith('raw/') or t.startswith('file:'):
                continue
            if not SAFE_TARGET_RE.match(t):
                continue
            if resolves(t):
                continue
            key = t.lower()
            entry = missing.setdefault(key, {
                'target': t, 'links': 0, 'from': [],
            })
            entry['links'] += 1
            if area not in entry['from']:
                entry['from'].append(area)

    rows = []
    for e in missing.values():
        e['from'] = sorted(e['from'])[:4]
        t = e['target'].strip().lstrip('./')
        if t.endswith('.md'):
            t = t[:-3]
        if t.startswith('wiki/'):
            e['suggested'] = t + '.md'
        elif '/' in t:
            e['suggested'] = 'wiki/' + t + '.md'
        else:
            e['suggested'] = 'wiki/%s/%s.md' % (e['from'][0] if e['from'] else 'concepts',
                                                _slugify(t) or 'wanted-page')
        rows.append(e)
    rows.sort(key=lambda r: (-r['links'], r['target']))
    return rows[:60]


def scan_live_state():
    """Cross-component live state for the Guide (pass 9/10).

    Pulls the RSIS3 loop stack (loops.json), per-loop telemetry starts +
    tuned model params, SPACE-spec goal traces, and recent MyKB syntheses so
    the Guide renders live loop + memory state instead of static lists only.
    """
    rsis3 = os.path.normpath(os.path.join(ROOT, '..', 'rsis3'))
    live = {
        'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'loops': [],
        'telemetry': {'files': 0, 'events': 0, 'loops': {}, 'spec_traces': []},
        'memory': {'syntheses': []},
    }

    # Loop stack snapshot (dashboard loops.json: L0-L9).
    loops_data = _load_json(os.path.join(rsis3, 'dashboard', 'loops.json'))
    if isinstance(loops_data, dict) and isinstance(loops_data.get('loops'), list):
        for e in loops_data['loops']:
            if not isinstance(e, dict) or not e.get('id'):
                continue
            live['loops'].append({
                'id': e.get('id'), 'name': e.get('name'),
                'status': e.get('status'), 'runs': e.get('runs', 0),
                'last_run': e.get('last_run'),
                'cycle': e.get('cycle', 0),
                'target': e.get('target'),
                'params': e.get('params') or [],
            })

    # Telemetry: per-loop starts + L2 goals that reference a SPACE spec artifact.
    tel_dir = os.path.join(rsis3, '.rsis', 'telemetry')
    if os.path.isdir(tel_dir):
        files = sorted(glob.glob(os.path.join(tel_dir, '*.jsonl')))
        live['telemetry']['files'] = len(files)
        traces = []
        for f in files:
            for line in open(f, encoding='utf-8', errors='ignore'):
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                live['telemetry']['events'] += 1
                t = ev.get('type', '')
                m = re.match(r'^l([1-9])_start$', t)
                if m:
                    key = 'L' + m.group(1)
                    live['telemetry']['loops'][key] = (
                        live['telemetry']['loops'].get(key, 0) + 1)
                goal = ev.get('goal') or ''
                if t == 'l2_start' and 'spec artifact' in goal:
                    traces.append({
                        'goal': goal[:160],
                        'timestamp': ev.get('timestamp', ''),
                    })
        traces.sort(key=lambda r: r['timestamp'], reverse=True)
        live['telemetry']['spec_traces'] = traces[:5]

    # Memory: most recent MyKB syntheses (OKF frontmatter timestamps).
    syn_dir = os.path.join(ROOT, 'wiki', 'syntheses')
    if os.path.isdir(syn_dir):
        entries = []
        for f in sorted(glob.glob(os.path.join(syn_dir, '*.md'))):
            name = os.path.basename(f)
            if name == '00-index.md':
                continue
            fm = parse_fm(open(f, encoding='utf-8', errors='ignore').read())
            entries.append({
                'slug': name[:-3],
                'title': fm.get('title') or name[:-3].replace('-', ' ').title(),
                'tags': fm.get('tags') or [],
                'timestamp': fm.get('timestamp', ''),
            })
        entries.sort(key=lambda e: e['timestamp'], reverse=True)
        live['memory']['syntheses'] = entries[:5]

    return live


def scan_guidance():
    """Area coverage + focus ranking + persisted guidance queue.

    coverage rows: {area, pages, stubs, stub_pct, avg_words}; focus is the
    top rows ranked by stub burden (where research effort should go next).
    queue is a snapshot of .wiki-daemon/buffers/guidance-queue.json so static
    pages still see persisted wanted pages / directions / feedback.
    """
    rows = {}
    for rel, fm, w, text in walk_wiki():
        area = rel.split('/')[0] or 'wiki'
        row = rows.setdefault(area, {'area': area, 'pages': 0, 'stubs': 0, 'words': 0})
        row['pages'] += 1
        row['words'] += w
        if fm.get('status') == 'stub':
            row['stubs'] += 1
    areas = []
    for area, r in rows.items():
        r['stub_pct'] = round(r['stubs'] / r['pages'] * 100) if r['pages'] else 0
        r['avg_words'] = int(r['words'] / r['pages']) if r['pages'] else 0
        r.pop('words', None)
        areas.append(r)
    areas.sort(key=lambda r: (-r['stubs'], -r['stub_pct'], r['area']))

    def note_for(r):
        if not r['stubs']:
            return 'healthy — no stubs'
        if r['stub_pct'] >= 50:
            return 'highest stub burden — prioritize enrichment'
        return 'stub backlog — next enrichment wave'

    total_pages = sum(r['pages'] for r in areas)
    total_stubs = sum(r['stubs'] for r in areas)
    return {
        'built': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'total': {
            'pages': total_pages,
            'stubs': total_stubs,
            'stub_pct': round(total_stubs / total_pages * 100) if total_pages else 0,
        },
        'areas': areas,
        'focus': [
            {'area': r['area'], 'pages': r['pages'], 'stubs': r['stubs'],
             'stub_pct': r['stub_pct'], 'note': note_for(r)}
            for r in areas[:10]
        ],
        'wanted_links': scan_wanted_links(),
        'queue': _load_json(GUIDANCE_QUEUE),
        'live': scan_live_state(),
    }


def main():
    stubs = scan_stubs()
    open(OUT, 'w', encoding='utf-8').write(json.dumps(stubs, ensure_ascii=False))
    guidance = scan_guidance()
    json.dump(guidance, open(GUIDANCE_OUT, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'stub-review.json written: {len(stubs["items"])} stub files, {len(stubs["areas"])} areas, {len(stubs["dirs"])} dirs')
    print(f'guidance.json written: {guidance["total"]["pages"]} pages, {guidance["total"]["stubs"]} stubs, {len(guidance["areas"])} areas, {len(guidance["wanted_links"])} wanted links')


if __name__ == '__main__':
    main()
