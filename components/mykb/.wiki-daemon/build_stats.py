#!/usr/bin/env python3
"""Build the MyKB wiki stats hub (stats.html).

Scans components/mykb/wiki, aggregates frontmatter + body stats and graph
degree data, then emits a self-contained HTML page with embedded JSON that
renders ~13 Chart.js graphs.

Usage: python3 .wiki-daemon/build_stats.py
"""
import datetime as _dt
import glob
import json
import os
import re
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)            # components/mykb
WIKI = os.path.join(ROOT, 'wiki')

FM_RE = re.compile(r'^---\s*\n(.*?)\n---', re.S)
KEY_RE = re.compile(r'^(\w+):\s*(.*)$', re.M)
LIST_RE = re.compile(r'^\[(.*)\]$', re.S)
LINK_RE = re.compile(r'\[\[([^\[\]]+)\]\]')
ISO_RE = re.compile(r'(\d{4})-(\d{2})-(\d{2})')


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


def walk_md():
    for p in sorted(glob.glob(os.path.join(WIKI, '**', '*.md'), recursive=True)):
        rel = os.path.relpath(p, WIKI).replace(os.sep, '/')
        with open(p, encoding='utf-8', errors='ignore') as fh:
            text = fh.read()
        fm = parse_frontmatter(text)
        yield rel, fm, body_words(text), len(LINK_RE.findall(text))


def iso_month(ts):
    m = ISO_RE.search(ts or '')
    return f'{m.group(1)}-{m.group(2)}' if m else None


def iso_day(ts):
    m = ISO_RE.search(ts or '')
    return f'{m.group(1)}-{m.group(2)}-{m.group(3)}' if m else None


def main():
    files, total_words, total_links = [], 0, 0
    words_all, words_nd, links_all = [], [], []
    zero_links = 0
    months, daily_months = Counter(), Counter()
    days60 = Counter()
    statuses, types_, areas, tags = Counter(), Counter(), Counter(), Counter()
    area_words, month_words = Counter(), Counter()
    status_month = defaultdict(Counter)
    per_file = {}                      # rel -> (words, links, status)

    for rel, fm, words, links in walk_md():
        if rel == 'log.md' or rel == 'index.md' or rel.endswith('/index.md'):
            continue
        files.append(rel)
        total_words += words
        total_links += links
        words_all.append(words)
        links_all.append(links)
        if not rel.startswith('daily/'):
            words_nd.append(words)
        if links == 0:
            zero_links += 1
        statuses[fm.get('status', 'none')] += 1
        types_[fm.get('type', 'none')] += 1
        area = rel.split('/')[0]
        akey = area if len(rel.split('/')) > 1 else '(root)'
        areas[akey] += 1
        area_words[akey] += words
        for t in fm.get('tags', []):
            tags[t] += 1
        mo = iso_month(fm.get('timestamp'))
        if mo:
            months[mo] += 1
            month_words[mo] += words
            status_month[mo][fm.get('status', 'none')] += 1
            if rel.startswith('daily/'):
                daily_months[mo] += 1
        d = iso_day(fm.get('timestamp'))
        if d:
            days60[d] += 1
        per_file[rel] = {'w': words, 'l': links, 's': fm.get('status', 'none')}

    # graph degree
    nodes = edges = degree = links_in = None
    try:
        g = json.load(open(os.path.join(ROOT, 'graph.json')))
        nodes, edges = len(g.get('nodes', [])), len(g.get('edges', []))
        degree = Counter()
        links_in = Counter()

        def graph_ok(nid):
            return bool(nid) and nid != 'wiki/log' and nid != 'wiki/index' \
                and not nid.endswith('/index')

        for e in g.get('edges', []):
            s, t = e.get('source'), e.get('target')
            if graph_ok(s):
                degree[s] += 1
            if graph_ok(t):
                degree[t] += 1
                links_in[t] += 1
    except Exception:
        pass

    def pct(n, d):
        return round(100.0 * n / d, 1) if d else 0.0

    n = len(files)
    thresholds = [50, 100, 150, 200, 300, 400, 500, 750, 1000, 2000, 5000]
    th_all = [sum(1 for w in words_all if w >= t) for t in thresholds]
    th_nd = [sum(1 for w in words_nd if w >= t) for t in thresholds]

    buckets = ['0-49', '50-99', '100-199', '200-299', '300-399', '400-499',
               '500-749', '750-999', '1000+']
    edges_b = [0, 50, 100, 200, 300, 400, 500, 750, 1000]
    hist = [0] * len(buckets)
    for w in words_all:
        for i in range(len(edges_b) - 1):
            if edges_b[i] <= w < edges_b[i + 1]:
                hist[i] += 1
                break
        else:
            hist[-1] += 1

    link_buckets = ['0', '1', '2-3', '4-7', '8-15', '16-31', '32+']
    lb_edges = [0, 1, 2, 4, 8, 16, 32]
    links_hist = [0] * len(link_buckets)
    for l in links_all:
        for i in range(len(lb_edges) - 1):
            if lb_edges[i] <= l < lb_edges[i + 1]:
                links_hist[i] += 1
                break
        else:
            links_hist[-1] += 1

    deg_buckets = ['0', '1', '2-3', '4-7', '8-15', '16-31', '32-63', '64+']
    db_edges = [0, 1, 2, 4, 8, 16, 32, 64]
    deg_hist = [0] * len(deg_buckets)
    for v in (degree.values() if degree else []):
        for i in range(len(db_edges) - 1):
            if db_edges[i] <= v < db_edges[i + 1]:
                deg_hist[i] += 1
                break
        else:
            deg_hist[-1] += 1

    def med(xs):
        xs = sorted(xs)
        m = len(xs)
        if not m:
            return 0
        return xs[m // 2] if m % 2 else (xs[m // 2 - 1] + xs[m // 2]) / 2

    top_files = sorted(per_file.items(), key=lambda kv: -kv[1]['w'])[:15]
    top_nodes = (degree.most_common(15) if degree else [])

    # scatter: cap sample for chart perf
    scatter = [{'x': v['w'], 'y': v['l'], 's': v['s']}
               for k, v in per_file.items()]
    if len(scatter) > 2000:
        step = len(scatter) / 2000.0
        scatter = [scatter[int(i * step)] for i in range(2000)]

    def series(counter, top=None):
        items = counter.most_common(top)
        return [{'label': k or '(none)', 'count': v} for k, v in items]

    months_sorted = sorted(set(months) | set(daily_months))
    cumulative = []
    _acc = 0
    for m in months_sorted:
        _acc += months[m]
        cumulative.append(_acc)

    ecdf = [round(100.0 - pct(sum(1 for w in words_all if w >= t), n), 1)
            for t in thresholds]
    avg_month = [round(month_words[m] / months[m], 1) if months[m] else 0
                 for m in months_sorted]

    ab_labels = ['<150', '150-299', '300-499', '500-999', '1000+']
    ab_edges = [0, 150, 300, 500, 1000]
    top_areas = [k for k, _ in areas.most_common(10) if k not in ('daily', '(root)')]

    def _bucket_of(w):
        for i in range(len(ab_edges) - 1):
            if ab_edges[i] <= w < ab_edges[i + 1]:
                return i
        return len(ab_edges) - 1

    area_buckets = {
        'areas': top_areas,
        'labels': ab_labels,
        'counts': [[sum(1 for r, pf in per_file.items()
                        if r.split('/')[0] == a and _bucket_of(pf['w']) == b)
                    for b in range(len(ab_labels))] for a in top_areas],
    }
    sm_labels = ['growing', 'stub', 'stable', 'other']
    status_by_month = {
        'labels': months_sorted,
        'datasets': [{'label': s, 'counts': [status_month[m].get(s, 0)
                                             for m in months_sorted]}
                     for s in sm_labels],
    }

    stats = {
        'generated': _dt.datetime.now(_dt.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
        'totals': {
            'files': n,
            'daily': sum(1 for f in files if f.startswith('daily/')),
            'words': total_words,
            'links': total_links,
            'median_words': med(words_all),
            'mean_words': round(total_words / n, 1) if n else 0,
            'median_words_no_daily': med(words_nd),
            'areas_count': len([k for k in areas if k not in ('daily', '(root)')]),
            'zero_link_files': zero_links,
            'zero_link_pct': pct(zero_links, n),
            'nodes': nodes,
            'edges': edges,
            'zero_degree_nodes': deg_hist[0] if deg_hist else 0,
        },
        'thresholds': {
            'labels': [str(t) for t in thresholds],
            'all': th_all,
            'no_daily': th_nd,
        },
        'histogram': {'labels': buckets, 'counts': hist},
        'status': series(statuses),
        'types': series(types_),
        'areas': series(areas, 15),
        'tags': series(tags, 20),
        'months': {
            'labels': months_sorted,
            'all': [months[m] for m in months_sorted],
            'daily': [daily_months[m] for m in months_sorted],
        },
        'last60': {
            'labels': sorted(days60)[-60:],
            'counts': [days60[d] for d in sorted(days60)[-60:]],
        },
        'links_hist': {'labels': link_buckets, 'counts': links_hist},
        'degree_hist': {'labels': deg_buckets, 'counts': deg_hist},
        'top_files': [{'path': k, 'title': v['w'], 'words': v['w']} for k, v in top_files],
        'top_nodes': [{'id': k, 'degree': v} for k, v in top_nodes],
        'words_by_area': [{'area': k, 'words': v, 'files': areas[k]}
                          for k, v in area_words.most_common(15)],
        'area_buckets': area_buckets,
        'status_by_month': status_by_month,
        'cumulative': {'labels': months_sorted, 'counts': cumulative},
        'ecdf': {'labels': [str(t) for t in thresholds], 'pct_le': ecdf},
        'avg_month': {'labels': months_sorted, 'words': avg_month},
        'links_in': ([{'id': k, 'links': v} for k, v in links_in.most_common(15)]
                     if links_in else []),
        'scatter': scatter,
    }

    html = TEMPLATE.replace('__STATS_JSON__', json.dumps(stats).replace('</', '<\\/'))
    out = os.path.join(ROOT, 'stats.html')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(html)

    print(f'stats.html written: {len(files)} files, {total_words} words, '
          f'{nodes}/{edges} graph nodes/edges, {total_links} links')
    print(f'  thresholds 300+/400+/500+: {th_all[4]}/{th_all[5]}/{th_all[6]} (all), '
          f'{th_nd[4]}/{th_nd[5]}/{th_nd[6]} (no daily)')


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MyKB Wiki Stats</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;font:14px/1.5 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#0b1120;color:#cbd5e1}
a{color:#a78bfa;text-decoration:none}
a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:20;background:#0d1424f2;backdrop-filter:blur(6px);border-bottom:1px solid #1e293b;padding:14px 20px}
header h1{margin:0;font-size:20px;color:#f1f5f9}
header .sub{color:#94a3b8;font-size:12px;margin-top:2px}
nav{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
nav a{font-size:12px;padding:4px 10px;border:1px solid #334155;border-radius:999px;color:#cbd5e1}
nav a:hover{background:#1e293b;text-decoration:none}
.offline{display:none;background:#3b2f00;color:#fde68a;border:1px solid #854d0e;padding:8px 14px;font-size:13px}
.wrap{max-width:1400px;margin:0 auto;padding:20px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:24px}
.card{background:#111a30;border:1px solid #1e293b;border-radius:12px;padding:14px 16px}
.card .n{font-size:26px;font-weight:700;color:#f1f5f9;font-variant-numeric:tabular-nums}
.card .l{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:#94a3b8;margin-top:4px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:16px}
.panel{background:#111a30;border:1px solid #1e293b;border-radius:14px;padding:16px}
.panel.wide{grid-column:1/-1}
.panel h2{margin:0 0 2px;font-size:15px;color:#f1f5f9}
.panel .why{color:#94a3b8;font-size:12px;margin:0 0 10px}
.panel .caveat{color:#64748b;font-size:11px;margin-top:8px}
.chart{position:relative;height:280px}
details{margin-top:8px}
summary{cursor:pointer;font-size:11px;color:#94a3b8}
table{width:100%;border-collapse:collapse;font-size:11px;margin-top:6px}
th,td{text-align:left;padding:3px 6px;border-bottom:1px solid #1e293b;color:#cbd5e1}
th{color:#94a3b8;font-weight:600}
footer{color:#64748b;font-size:11px;padding:24px 20px;border-top:1px solid #1e293b;margin-top:24px}
code{background:#0d1424;border:1px solid #1e293b;border-radius:4px;padding:1px 5px;font-size:11px}
</style>
</head>
<body>
<header>
  <h1>📊 MyKB Wiki Stats Hub</h1>
  <div class="sub">Knowledge graph + content metrics for <code>components/mykb</code> · generated <span id="gen"></span></div>
  <div class="offline" id="offline">⚠ Chart.js could not load from CDN — showing data tables only.</div>
  <nav>
    <a href="#totals">Overview</a>
    <a href="#length">Length</a>
    <a href="#content">Content</a>
    <a href="#time">Time</a>
    <a href="#graph">Graph</a>
    <a href="#quality">Quality</a>
  </nav>
</header>
<div class="wrap">
  <section id="totals" class="cards"></section>
  <section class="grid">
    <div class="panel wide" id="length">
      <h2>Files above word-count threshold</h2>
      <p class="why">Articles with at least N words of body text — all wiki files vs. knowledge files (daily notes excluded).</p>
      <div class="chart"><canvas id="th"></canvas></div>
      <details><summary>Exact counts</summary><table id="th-t"></table></details>
    </div>
    <div class="panel" id="hist">
      <h2>Word-count histogram</h2>
      <p class="why">Distribution of body length across all wiki markdown files.</p>
      <div class="chart"><canvas id="hist-c"></canvas></div>
      <details><summary>Buckets</summary><table id="hist-t"></table></details>
    </div>
    <div class="panel" id="ecdf">
      <h2>Share of files under N words</h2>
      <p class="why">Cumulative share (ECDF) of articles with body length below each threshold.</p>
      <div class="chart"><canvas id="ecdf-c"></canvas></div>
      <details><summary>Thresholds</summary><table id="ecdf-t"></table></details>
    </div>
    <div class="panel" id="topfiles">
      <h2>Longest files</h2>
      <p class="why">Top 15 by body word count.</p>
      <div class="chart"><canvas id="top-c"></canvas></div>
      <details><summary>Top files</summary><table id="top-t"></table></details>
    </div>
    <div class="panel" id="content">
      <h2>Status composition</h2>
      <p class="why">Lifecycle status from frontmatter (growing = full articles, stub = expansion targets).</p>
      <div class="chart"><canvas id="status-c"></canvas></div>
      <details><summary>Counts</summary><table id="status-t"></table></details>
    </div>
    <div class="panel" id="types">
      <h2>Notes by type</h2>
      <p class="why">OKF frontmatter <code>type</code> field.</p>
      <div class="chart"><canvas id="types-c"></canvas></div>
      <details><summary>Types</summary><table id="types-t"></table></details>
    </div>
    <div class="panel" id="areas">
      <h2>Notes by area</h2>
      <p class="why">Top 15 wiki subfolders by file count.</p>
      <div class="chart"><canvas id="areas-c"></canvas></div>
      <details><summary>Areas</summary><table id="areas-t"></table></details>
    </div>
    <div class="panel" id="area-words">
      <h2>Words by area</h2>
      <p class="why">Total body words per area (top 15) — where the knowledge weight lives.</p>
      <div class="chart"><canvas id="aw-c"></canvas></div>
      <details><summary>Areas</summary><table id="aw-t"></table></details>
    </div>
    <div class="panel" id="area-buckets">
      <h2>Word buckets by area</h2>
      <p class="why">Length composition per area (stacked): most full articles sit in the 150–300 word band.</p>
      <div class="chart"><canvas id="ab-c"></canvas></div>
      <details><summary>Areas</summary><table id="ab-t"></table></details>
    </div>
    <div class="panel" id="tags">
      <h2>Top tags</h2>
      <p class="why">Most-used frontmatter tags (top 20).</p>
      <div class="chart"><canvas id="tags-c"></canvas></div>
      <details><summary>Tags</summary><table id="tags-t"></table></details>
    </div>
    <div class="panel wide" id="time">
      <h2>Files by month</h2>
      <p class="why">Frontmatter timestamps — all files vs. daily notes per calendar month.</p>
      <div class="chart"><canvas id="months-c"></canvas></div>
      <details><summary>Months</summary><table id="months-t"></table></details>
    </div>
    <div class="panel" id="status-month">
      <h2>Status by month</h2>
      <p class="why">Lifecycle status of articles added per calendar month (stacked).</p>
      <div class="chart"><canvas id="sm-c"></canvas></div>
      <details><summary>Months</summary><table id="sm-t"></table></details>
    </div>
    <div class="panel" id="cumulative">
      <h2>Cumulative growth</h2>
      <p class="why">Total wiki content files over time.</p>
      <div class="chart"><canvas id="cum-c"></canvas></div>
      <details><summary>Months</summary><table id="cum-t"></table></details>
    </div>
    <div class="panel" id="avg-month">
      <h2>Average words per month</h2>
      <p class="why">Mean body length of articles added each month — acquisition volume vs. depth.</p>
      <div class="chart"><canvas id="avg-c"></canvas></div>
      <details><summary>Months</summary><table id="avg-t"></table></details>
    </div>
    <div class="panel" id="last60">
      <h2>Files per day (last 60 days)</h2>
      <p class="why">Recent acquisition activity from frontmatter timestamps.</p>
      <div class="chart"><canvas id="last60-c"></canvas></div>
      <details><summary>Days</summary><table id="last60-t"></table></details>
    </div>
    <div class="panel" id="graph">
      <h2>Node degree distribution</h2>
      <p class="why">How many links each graph node has (degree buckets over all nodes).</p>
      <div class="chart"><canvas id="deg-c"></canvas></div>
      <details><summary>Buckets</summary><table id="deg-t"></table></details>
    </div>
    <div class="panel" id="topnodes">
      <h2>Most connected nodes</h2>
      <p class="why">Top 15 graph nodes by degree (in + out links).</p>
      <div class="chart"><canvas id="topn-c"></canvas></div>
      <details><summary>Nodes</summary><table id="topn-t"></table></details>
    </div>
    <div class="panel" id="links-in">
      <h2>Most linked-to articles</h2>
      <p class="why">Top 15 by inbound graph links — the hub pages of the wiki.</p>
      <div class="chart"><canvas id="li-c"></canvas></div>
      <details><summary>Nodes</summary><table id="li-t"></table></details>
    </div>
    <div class="panel" id="linkshist">
      <h2>Wikilinks per file</h2>
      <p class="why">Number of <code>[[wikilinks]]</code> per file, bucketed.</p>
      <div class="chart"><canvas id="links-c"></canvas></div>
      <details><summary>Buckets</summary><table id="links-t"></table></details>
    </div>
    <div class="panel wide" id="quality">
      <h2>Length vs. linking (scatter)</h2>
      <p class="why">Each dot is a file: body words (x) vs. wikilinks (y). Color = status. Dense linking at top-right is the goal.</p>
      <div class="chart" style="height:360px"><canvas id="scatter-c"></canvas></div>
      <details><summary>Raw sample</summary><table id="scatter-t"></table></details>
    </div>
  </section>
</div>
<footer>
  <p>Word counts = whitespace tokens in body text with YAML frontmatter stripped. Index pages (<code>index.md</code>) and the bundle log (<code>log.md</code>) are excluded from all article-level stats; graph node/edge totals still include them. Link counts include frontmatter wikilinks. Timestamps read from frontmatter; files without one are omitted from time charts.</p>
  <p>Regenerate: <code>python3 components/mykb/.wiki-daemon/build_stats.py</code> · Snapshots: <code>python3 gen-static-data.py --check</code></p>
</footer>
<script>
const STATS = __STATS_JSON__;
const PALETTE = ['#a78bfa','#2dd4bf','#fbbf24','#f472b6','#60a5fa','#34d399','#fb923c','#a3e635','#38bdf8','#e879f9'];
const COLORS = {growing:'#a78bfa', stub:'#64748b', stable:'#2dd4bf', none:'#475569'};

function fmt(n){ return Number(n).toLocaleString('en-US'); }
function short(s){ return s.length > 28 ? '…' + s.slice(-27) : s; }
function tbl(el, headers, rows){
  const t = document.getElementById(el); if(!t) return;
  t.innerHTML = '<thead><tr>' + headers.map(h=>'<th>'+h+'</th>').join('') + '</tr></thead><tbody>' +
    rows.map(r=>'<tr>'+r.map(c=>'<td>'+c+'</td>').join('')).join('</tr>') + '</tbody>';
}

function base(){
  document.getElementById('gen').textContent = STATS.generated;
  const T = STATS.totals;
  const th = STATS.thresholds;
  const i300 = th.labels.indexOf('300'), i400 = th.labels.indexOf('400'), i500 = th.labels.indexOf('500');
  const cards = [
    ['wiki files', fmt(T.files), 'excl. log.md / index.md'],
    ['total words', fmt(T.words), ''],
    ['median words', fmt(T.median_words), 'all / ' + fmt(T.median_words_no_daily) + ' no-daily'],
    ['content areas', fmt(T.areas_count), ''],
    ['full articles (300+)', fmt(th.all[i300]), '400+ → ' + fmt(th.all[i400]) + ' · 500+ → ' + fmt(th.all[i500])],
    ['graph nodes', fmt(T.nodes), fmt(T.edges) + ' edges'],
    ['wikilinks', fmt(T.links), ''],
    ['zero-link files', fmt(T.zero_link_files), T.zero_link_pct + '% of wiki'],
    ['zero-degree nodes', fmt(T.zero_degree_nodes), ''],
  ];
  document.getElementById('totals').innerHTML = cards.map(c=>
    '<div class="card"><div class="n">'+c[1]+'</div><div class="l">'+c[0]+'</div>'+(c[2]?'<div class="l" style="text-transform:none;letter-spacing:0">'+c[2]+'</div>':'')+'</div>'
  ).join('');

  tbl('th-t', ['min words','all','no daily'], th.labels.map((l,i)=>[l, fmt(th.all[i]), fmt(th.no_daily[i])]));
  const h = STATS.histogram;
  tbl('hist-t', ['bucket','files'], h.labels.map((l,i)=>[l, fmt(h.counts[i])]));
  const ec = STATS.ecdf;
  tbl('ecdf-t', ['max words','share of files'], ec.labels.map((l,i)=>[l, ec.pct_le[i] + '%']));
  const tf = STATS.top_files;
  tbl('top-t', ['file','words'], tf.map(f=>[f.path, fmt(f.words)]));
  const st = STATS.status;
  tbl('status-t', ['status','files'], st.map(s=>[s.label, fmt(s.count)]));
  const ty = STATS.types;
  tbl('types-t', ['type','notes'], ty.map(t=>[t.label, fmt(t.count)]));
  const ar = STATS.areas;
  tbl('areas-t', ['area','files'], ar.map(a=>[a.label, fmt(a.count)]));
  const aw = STATS.words_by_area;
  tbl('aw-t', ['area','files','words'], aw.map(a=>[a.area, fmt(a.files), fmt(a.words)]));
  const ab = STATS.area_buckets;
  tbl('ab-t', ['area'].concat(ab.labels), ab.areas.map((a,i)=>[a].concat(ab.counts[i].map(fmt))));
  const tg = STATS.tags;
  tbl('tags-t', ['tag','files'], tg.map(t=>[t.label, fmt(t.count)]));
  const mo = STATS.months;
  tbl('months-t', ['month','all','daily'], mo.labels.map((l,i)=>[l, fmt(mo.all[i]), fmt(mo.daily[i])]));
  const sm = STATS.status_by_month;
  tbl('sm-t', ['month'].concat(sm.datasets.map(d=>d.label)), sm.labels.map((m,i)=>[m].concat(sm.datasets.map(d=>fmt(d.counts[i])))));
  const cum = STATS.cumulative;
  tbl('cum-t', ['month','total files'], cum.labels.map((l,i)=>[l, fmt(cum.counts[i])]));
  const av = STATS.avg_month;
  tbl('avg-t', ['month','avg words'], av.labels.map((l,i)=>[l, fmt(av.words[i])]));
  const l60 = STATS.last60;
  tbl('last60-t', ['day','files'], l60.labels.map((l,i)=>[l, fmt(l60.counts[i])]));
  const dg = STATS.degree_hist;
  tbl('deg-t', ['degree','nodes'], dg.labels.map((l,i)=>[l, fmt(dg.counts[i])]));
  const tn = STATS.top_nodes;
  tbl('topn-t', ['node','degree'], tn.map(n=>[n.id, fmt(n.degree)]));
  const li = STATS.links_in;
  tbl('li-t', ['node','inbound links'], li.map(x=>[x.id, fmt(x.links)]));
  const lh = STATS.links_hist;
  tbl('links-t', ['links','files'], lh.labels.map((l,i)=>[l, fmt(lh.counts[i])]));
  const sc = STATS.scatter;
  tbl('scatter-t', ['file words','links','status'], sc.slice(0,50).map(p=>[fmt(p.x), fmt(p.y), p.s]));
}

function charts(){
  if (!window.Chart) return;
  Chart.defaults.color = '#94a3b8';
  Chart.defaults.borderColor = '#1e293b';
  Chart.defaults.font.family = 'ui-sans-serif, system-ui, sans-serif';

  const th = STATS.thresholds;
  new Chart(document.getElementById('th'), {type:'bar', data:{labels:th.labels, datasets:[
    {label:'All wiki files', data:th.all, backgroundColor:'#a78bfa'},
    {label:'Excluding daily', data:th.no_daily, backgroundColor:'#2dd4bf'},
  ]}, options:{plugins:{legend:{display:false}}, scales:{x:{title:{display:true,text:'minimum words'}},y:{beginAtZero:true,title:{display:true,text:'files'}}}}});

  const h = STATS.histogram;
  new Chart(document.getElementById('hist-c'), {type:'bar', data:{labels:h.labels, datasets:[{label:'files', data:h.counts, backgroundColor:'#a78bfa'}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true}}}});

  const ec = STATS.ecdf;
  new Chart(document.getElementById('ecdf-c'), {type:'line', data:{labels:ec.labels, datasets:[{label:'share ≤ N words', data:ec.pct_le, borderColor:'#2dd4bf', backgroundColor:'rgba(45,212,191,.15)', fill:true, tension:.3}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true,max:100,title:{display:true,text:'% of files'}},x:{title:{display:true,text:'max words'}}}}});

  const tf = STATS.top_files;
  new Chart(document.getElementById('top-c'), {type:'bar', data:{labels:tf.map(f=>f.path.replace(/^.*\//,'')), datasets:[{label:'words', data:tf.map(f=>f.words), backgroundColor:'#fbbf24'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true}}}});

  const st = STATS.status;
  new Chart(document.getElementById('status-c'), {type:'doughnut', data:{labels:st.map(s=>s.label), datasets:[{data:st.map(s=>s.count), backgroundColor:st.map(s=>COLORS[s.label]||'#475569')}]},
    options:{plugins:{legend:{position:'right'}}}});

  const ty = STATS.types;
  new Chart(document.getElementById('types-c'), {type:'bar', data:{labels:ty.map(t=>t.label), datasets:[{label:'notes', data:ty.map(t=>t.count), backgroundColor:'#60a5fa'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true}}}});

  const ar = STATS.areas;
  new Chart(document.getElementById('areas-c'), {type:'bar', data:{labels:ar.map(a=>a.label), datasets:[{label:'files', data:ar.map(a=>a.count), backgroundColor:'#2dd4bf'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true}}}});

  const aw = STATS.words_by_area;
  new Chart(document.getElementById('aw-c'), {type:'bar', data:{labels:aw.map(a=>a.area), datasets:[{label:'words', data:aw.map(a=>a.words), backgroundColor:'#f472b6'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true,title:{display:true,text:'words'}}}}});

  const ab = STATS.area_buckets;
  const abPalette = ['#a78bfa','#2dd4bf','#fbbf24','#f472b6','#60a5fa'];
  new Chart(document.getElementById('ab-c'), {type:'bar', data:{labels:ab.areas, datasets:ab.labels.map((l,i)=>({label:l, data:ab.counts.map(r=>r[i]), backgroundColor:abPalette[i]}))},
    options:{indexAxis:'y', scales:{x:{stacked:true,beginAtZero:true}, y:{stacked:true}}}});

  const tg = STATS.tags;
  new Chart(document.getElementById('tags-c'), {type:'bar', data:{labels:tg.map(t=>t.label), datasets:[{label:'files', data:tg.map(t=>t.count), backgroundColor:tg.map((_,i)=>PALETTE[i%PALETTE.length])}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true}}}});

  const mo = STATS.months;
  new Chart(document.getElementById('months-c'), {type:'bar', data:{labels:mo.labels, datasets:[
    {label:'all files', data:mo.all, backgroundColor:'#a78bfa'},
    {label:'daily notes', data:mo.daily, backgroundColor:'#f472b6'},
  ]}, options:{scales:{y:{beginAtZero:true}}}});

  const sm = STATS.status_by_month;
  const smColors = {growing:'#a78bfa', stub:'#64748b', stable:'#2dd4bf', other:'#475569'};
  new Chart(document.getElementById('sm-c'), {type:'bar', data:{labels:sm.labels, datasets:sm.datasets.map(d=>({label:d.label, data:d.counts, backgroundColor:smColors[d.label]||'#475569'}))},
    options:{scales:{x:{stacked:true}, y:{stacked:true,beginAtZero:true}}}});

  const cum = STATS.cumulative;
  new Chart(document.getElementById('cum-c'), {type:'line', data:{labels:cum.labels, datasets:[{label:'total files', data:cum.counts, borderColor:'#a78bfa', backgroundColor:'rgba(167,139,250,.15)', fill:true, tension:.25}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true}}}});

  const av = STATS.avg_month;
  new Chart(document.getElementById('avg-c'), {type:'line', data:{labels:av.labels, datasets:[{label:'avg words', data:av.words, borderColor:'#fb923c', tension:.25}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true,title:{display:true,text:'words'}}}}});

  const l60 = STATS.last60;
  new Chart(document.getElementById('last60-c'), {type:'bar', data:{labels:l60.labels, datasets:[{label:'files', data:l60.counts, backgroundColor:'#38bdf8'}]},
    options:{plugins:{legend:{display:false}}, scales:{x:{ticks:{maxTicksLimit:12}},y:{beginAtZero:true}}}});

  const dg = STATS.degree_hist;
  new Chart(document.getElementById('deg-c'), {type:'bar', data:{labels:dg.labels, datasets:[{label:'nodes', data:dg.counts, backgroundColor:'#a78bfa'}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true}}}});

  const tn = STATS.top_nodes;
  new Chart(document.getElementById('topn-c'), {type:'bar', data:{labels:tn.map(n=>n.id.replace(/^.*\//,'')), datasets:[{label:'links', data:tn.map(n=>n.degree), backgroundColor:'#34d399'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true}}}});

  const li = STATS.links_in;
  new Chart(document.getElementById('li-c'), {type:'bar', data:{labels:li.map(x=>short(x.id.replace(/^wiki\//,''))), datasets:[{label:'inbound', data:li.map(x=>x.links), backgroundColor:'#fbbf24'}]},
    options:{indexAxis:'y', plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true,title:{display:true,text:'inbound links'}}}}});

  const lh = STATS.links_hist;
  new Chart(document.getElementById('links-c'), {type:'bar', data:{labels:lh.labels, datasets:[{label:'files', data:lh.counts, backgroundColor:'#fb923c'}]},
    options:{plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true}}}});

  const sc = STATS.scatter;
  new Chart(document.getElementById('scatter-c'), {type:'scatter', data:{datasets:[
    {label:'growing', data:sc.filter(p=>p.s==='growing').map(p=>({x:p.x,y:p.y})), backgroundColor:'#a78bfa', pointRadius:2.5},
    {label:'stub', data:sc.filter(p=>p.s==='stub').map(p=>({x:p.x,y:p.y})), backgroundColor:'#64748b', pointRadius:2.5},
    {label:'other', data:sc.filter(p=>p.s!=='growing'&&p.s!=='stub').map(p=>({x:p.x,y:p.y})), backgroundColor:'#2dd4bf', pointRadius:2.5},
  ]}, options:{scales:{x:{title:{display:true,text:'body words'}}, y:{title:{display:true,text:'wikilinks'}}}}});
}

base();
if (window.Chart) { charts(); } else { document.getElementById('offline').style.display='block'; }

</script>
</body>
</html>
"""

if __name__ == '__main__':
    main()
