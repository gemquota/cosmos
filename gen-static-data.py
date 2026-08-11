#!/usr/bin/env python3
"""Regenerate static data snapshots for the COSMOS GitHub Pages site.

Uses git-tracked files only so every entry in files.json / ecosystem.json
exists on the deployed site. Run from the repo root, then commit.

    python3 gen-static-data.py
"""
import json, os, re, subprocess, sys, datetime
from pathlib import Path

# Shared OKF frontmatter parser (enriched files.json entries).
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'components/mykb/.wiki-daemon'))
from frontmatter import entry_for  # noqa: E402

RSIS3 = 'components/rsis3'

def tracked(prefix=None):
    args = ['git', 'ls-files']
    if prefix:
        args.append(prefix)
    return subprocess.run(args, capture_output=True, text=True).stdout.splitlines()

def visible(path):
    return not any(seg.startswith('.') for seg in path.split('/'))

def build_dashboard_payload(rsis3):
    """Rebuild rack/pulses/dashboard-data.json from live loop telemetry.

    The RRP v2 pulse pipeline (``rack/pulses/pulse-*.json``) is no longer
    the source of truth — the nine loops write ``.rsis/telemetry/*.jsonl``
    instead. This derives the legacy dashboard schema (pulses / goals /
    score_history / summary) from that telemetry:

    - one *pulse* per telemetry session file,
    - *goals* from l2_start/l2_complete pairs (goal text + PASS/FAIL),
    - *score_history* = per-UTC-day L1–L9 activity (0–100, normalized),
    - *summary* = pass/fail/hold counts + implementations (l5 PASS).
    """
    tel_dir = Path(rsis3) / '.rsis' / 'telemetry'
    goals, pulses, day_counts, pd = [], [], {}, {}
    idx = 0
    for f in sorted(tel_dir.glob('*.jsonl')):
        evs = []
        try:
            evs = [json.loads(l) for l in f.read_text().splitlines()
                   if l.strip()]
        except (OSError, json.JSONDecodeError):
            continue
        if not evs:
            continue
        idx += 1
        pid = '%03d' % idx
        first_ts = last_ts = None
        open_goal = None
        g_n = approved = impl = 0
        confs = []
        for ev in evs:
            et = ev.get('type', '')
            ts = ev.get('timestamp')
            if ts:
                first_ts = ts if first_ts is None else min(first_ts, ts)
                last_ts = ts if last_ts is None else max(last_ts, ts)
            m = re.match(r'l([1-9])_complete$', et)
            if m and ts:
                lk = 'L' + m.group(1)
                day_counts.setdefault(ts[:10], {}).setdefault(lk, 0)
                day_counts[ts[:10]][lk] += 1
            if et == 'l2_start':
                open_goal = {'p': pid,
                             'd': ev.get('goal') or '(l2 goal)',
                             'dec': 'HOLD', 'type': 'improvement',
                             'constraints': {}, 'conversation': [],
                             'conf': '', 'file': '', 'func': ''}
            elif et == 'l2_complete':
                if open_goal:
                    ok = bool(ev.get('success'))
                    open_goal['dec'] = 'PASS' if ok else 'FAIL'
                    goals.append(open_goal)
                    g_n += 1
                    if ok:
                        approved += 1
                    open_goal = None
            elif et == 'l5_evaluation':
                if ev.get('decision') == 'PASS':
                    impl += 1
                sa = ev.get('score_avg')
                if sa is not None:
                    try:
                        confs.append(float(sa))
                    except (TypeError, ValueError):
                        pass
        if open_goal:  # started but never completed -> HOLD
            goals.append(open_goal)
            g_n += 1
        duration = 0.0
        if first_ts and last_ts:
            try:
                fdt = datetime.datetime.fromisoformat(
                    str(first_ts).replace('Z', '+00:00'))
                ldt = datetime.datetime.fromisoformat(
                    str(last_ts).replace('Z', '+00:00'))
                duration = (ldt - fdt).total_seconds()
            except ValueError:
                duration = 0.0
        pulses.append({
            'id': idx, 'type': 'telemetry-run',
            'ts_start': str(first_ts or '')[:19].replace('T', ' '),
            'duration': round(duration, 1),
            'goals_count': g_n, 'approved': approved,
            'implementation_count': impl,
            'avg_confidence': (round(sum(confs) / len(confs), 3)
                               if confs else 0.0),
        })
        pd[pid] = {'pre_state': {'telemetry_events': len(evs),
                                 'goals': g_n, 'loops': 9}}
    score_history = {}
    for day, counts in sorted(day_counts.items()):
        mx = max(counts.values()) or 1
        score_history[day] = {
            'L%d' % i: round(counts.get('L%d' % i, 0) / mx * 100, 1)
            for i in range(1, 10)}
    tot = len(goals)
    pass_n = sum(1 for gx in goals if gx['dec'] == 'PASS')
    fail_n = sum(1 for gx in goals if gx['dec'] == 'FAIL')
    hold_n = sum(1 for gx in goals if gx['dec'] == 'HOLD')
    return {
        'pulses': pulses, 'goals': goals, 'pulse_data': pd,
        'score_history': score_history, 'telemetry_aggregates': {},
        'generated': datetime.datetime.now(
            datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'summary': {
            'tot': tot, 'pass': pass_n, 'hold': hold_n, 'fail': fail_n,
            'impl_count': sum(p['implementation_count'] for p in pulses),
            'pulse_count': len(pulses),
            'ca': round(pass_n / tot, 3) if tot else 0.0,
            'cd': {},
        },
    }


prefix = 'components/mykb/'
md = sorted((p[len(prefix):] if p.startswith(prefix) else p)
            for p in tracked('components/mykb')
            if p.endswith('.md') and visible(p) and os.path.exists(p))
# --check validates the committed snapshots without rewriting them.
write = '--check' not in sys.argv
if write:
    entries = []
    for rel in md:
        try:
            text = open('components/mykb/' + rel, encoding='utf-8',
                        errors='ignore').read()
        except OSError:
            text = ''
        entries.append(entry_for(rel, text))
    json.dump(entries, open('components/mykb/files.json', 'w'), indent=1)

allf = [p for p in tracked() if visible(p) and os.path.exists(p)]
def count(prefix):
    return len([p for p in allf if p.startswith(prefix + '/')])

def md_count(prefix):
    return len([p for p in allf if p.startswith(prefix + '/') and p.endswith('.md')])

# ── Lite knowledge graph (fast default render for the KG viewport) ──────
# graph.json (4+ MB, ~5.5k nodes / ~37k edges) is too heavy for a snappy
# first paint on mobile. Derive a hub-focused lite graph: keep the top-N
# concepts by degree plus every edge between kept nodes, plus a per-area
# cluster rollup. okf-graph.html renders the lite payload by default and
# keeps the full graph one click away. Compact separators keep the file
# small enough to parse instantly.
LITE_HUBS = 420

def build_lite_graph(graph):
    nodes = graph.get('nodes', []) or []
    edges = graph.get('edges', []) or []
    deg = {}
    for e in edges:
        deg[e.get('source', '')] = deg.get(e.get('source', ''), 0) + 1
        deg[e.get('target', '')] = deg.get(e.get('target', ''), 0) + 1
    by_deg = sorted(nodes, key=lambda n: -deg.get(n.get('id', ''), 0))
    keep = {n['id'] for n in by_deg[:LITE_HUBS]}
    kept_edges = [e for e in edges
                  if e.get('source') in keep and e.get('target') in keep]
    areas = {}
    for n in nodes:
        a = n['id'].split('/')[0] if '/' in n.get('id', '') else '(root)'
        areas[a] = areas.get(a, 0) + 1
    return {
        'meta': {
            'total_nodes': len(nodes),
            'total_edges': len(edges),
            'lite_nodes': len(keep),
            'lite_edges': len(kept_edges),
            'areas': areas,
        },
        'nodes': [n for n in nodes if n['id'] in keep],
        'edges': kept_edges,
    }

def build_lite_catalog(catalog, lite_ids):
    out = []
    for c in catalog or []:
        if c and c.get('id') in lite_ids:
            out.append(c)
    return out

graph_path = Path('components/mykb/graph.json')
catalog_path = Path('components/mykb/catalog.json')
if write and graph_path.exists():
    try:
        g = json.load(open(graph_path))
        lite = build_lite_graph(g)
        json.dump(lite, open('components/mykb/graph.lite.json', 'w'),
                  separators=(',', ':'))
        if catalog_path.exists():
            catalog = json.load(open(catalog_path))
            lite_ids = {n['id'] for n in lite['nodes']}
            json.dump(build_lite_catalog(catalog, lite_ids),
                      open('components/mykb/catalog.lite.json', 'w'),
                      separators=(',', ':'))
        print(f'graph.lite.json: {lite["meta"]["lite_nodes"]} of '
              f'{lite["meta"]["total_nodes"]} nodes, '
              f'{lite["meta"]["lite_edges"]} of {lite["meta"]["total_edges"]} edges')
    except (OSError, ValueError) as e:
        print(f'graph.lite.json: skipped ({e})')

# Dashboard payload (Overview/Pulses/KG/Graphs/Constraints) — rebuilt
# from live loop telemetry when writing; validated as-committed in --check.
dash_path = Path(RSIS3) / 'rack' / 'pulses' / 'dashboard-data.json'
telemetry = {}
try:
    if write:
        payload = build_dashboard_payload(RSIS3)
        dash_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump(payload, open(dash_path, 'w'), indent=1)
    else:
        payload = json.load(open(dash_path))
    sm = payload.get('summary', {})
    telemetry = {
        'pulses': len(payload.get('pulses', [])),
        'goals': len(payload.get('goals', [])),
        'passed': sm.get('pass', 0), 'failed': sm.get('fail', 0),
        'held': sm.get('hold', 0), 'total': sm.get('tot', 0),
        'improvements': sm.get('impl_count', 0),
    }
except Exception:
    pass

# ── Loop stack snapshot (drives the dashboard "Loops" tab) ───────────────
# One row per loop of the nine-level hierarchy (L0 = substrate, not a loop).
# Defaults mirror rsis/config.py; live values come from committed/workspace
# `.rsis/<state>` files and telemetry when present (graceful never-run).
LOOPS = [
    {"id": "L0", "name": "Substrate", "status": "n/a",
     "target": "Workspace/artifact layer loops mutate — not a loop", "state_file": None,
     "default_params": []},
    {"id": "L1", "name": "Execution", "status": "implemented",
     "target": "Pure consumer of tuned params (L4→L1)", "state_file": None,
     "default_params": []},
    {"id": "L2", "name": "Improvement", "status": "implemented",
     "target": "Pure consumer of tuned params (L5→L2)", "state_file": None,
     "default_params": []},
    {"id": "L3", "name": "Evolution", "status": "implemented",
     "target": "Core stack — consolidates memory, derives strategies", "state_file": None,
     "default_params": []},
    {"id": "L4", "name": "Optimizer", "status": "implemented",
     "target": "Tunes L1 execution params", "state_file": ".rsis/optimizer_state.json",
     "default_params": [("l1.max_retries", 3), ("l1.max_tool_calls", 10)]},
    {"id": "L5", "name": "Evolution", "status": "implemented",
     "target": "Tunes L2 improvement params (population, mutation)", "state_file": ".rsis/strategies.json",
     "default_params": [("l2.max_attempts", 5)]},
    {"id": "L6", "name": "Identity", "status": "implemented",
     "target": "Tunes L3 evolution params (plateau timeout)", "state_file": ".rsis/identity_state.json",
     "default_params": [("l3.plateau_timeout_s", 86400)]},
    {"id": "L7", "name": "Meta-Cog", "status": "implemented",
     "target": "Tunes L4 optimizer params (window / thresholds)", "state_file": ".rsis/metacog_state.json",
     "default_params": [("l4.target_success_low", 0.5), ("l4.target_success_high", 0.85)]},
    {"id": "L8", "name": "Meta-Meta", "status": "implemented",
     "target": "Tunes L5 strategy params (population / mutation)", "state_file": ".rsis/metameta_state.json",
     "default_params": [("l5.mutation_rate", 0.2), ("l5.population_size", 8)]},
    {"id": "L9", "name": "MMM", "status": "implemented",
     "target": "Tunes L6 identity params (the recursion guard)", "state_file": ".rsis/mmm_state.json",
     "default_params": [("l6.shrink_below", 0.5), ("l6.grow_above", 0.8)]},
]

# Per-loop telemetry: runs (l{n}_start) and last l{n}_complete/error timestamp.
loop_events = {f"L{i}": {"runs": 0, "last_run": None} for i in range(10)}
tel_dir = Path(RSIS3) / '.rsis' / 'telemetry'
if tel_dir.exists():
    for f in tel_dir.glob('*.jsonl'):
        try:
            for line in f.read_text().splitlines():
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                et = ev.get('type', '')
                for i in range(1, 10):
                    if et == f'l{i}_start':
                        loop_events[f'L{i}']['runs'] += 1
                    elif et in (f'l{i}_complete', f'l{i}_error'):
                        ts = ev.get('timestamp')
                        if ts:
                            cur = loop_events[f'L{i}']['last_run']
                            if not cur or ts > cur:
                                loop_events[f'L{i}']['last_run'] = ts
        except OSError:
            continue

def load_state(rel_path):
    """Read a loop state file; None if absent (never-run default)."""
    if not rel_path:
        return None
    p = Path(RSIS3) / rel_path
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def state_params(meta, state):
    """Per-loop tuned params; L5's live tuning lives in its best strategy."""
    sp = (state or {}).get('params') or {}
    if not sp and meta['id'] == 'L5' and (state or {}).get('population'):
        best = max(state['population'], key=lambda s: s.get('fitness', 0.0))
        bp = best.get('params') or {}
        sp = {
            'l2.max_attempts': bp.get('l2_attempts', 5),
            'budget_factor': bp.get('budget_factor', 1.0),
            'focus': bp.get('focus', 'general'),
        }
    return [{"key": k, "value": v} for k, v in sp.items()]

loops_out = []
for meta in LOOPS:
    state = load_state(meta['state_file'])
    params = state_params(meta, state)
    if not params:
        params = [{"key": k, "value": v} for k, v in meta['default_params']]
    history = (state or {}).get('history') or []
    last_signal = None
    if history:
        last_signal = history[-1].get('signal')
    # Runtime state: "implemented" is a code-readiness label, not liveness.
    # RSIS3 loops run on demand (CLI per session/cadence) — nothing is
    # continuously active — so the snapshot is honest: RECENT when the loop
    # ran within the last 24h, IDLE when it ran before that, NEVER if it has
    # never run, n/a for the substrate row.
    runtime = 'n/a'
    if meta['id'] != 'L0':
        runs = loop_events[meta['id']]['runs']
        if runs == 0:
            runtime = 'never'
        else:
            runtime = 'idle'
            last = loop_events[meta['id']]['last_run']
            try:
                last_dt = datetime.datetime.fromisoformat(last)
                age_s = (datetime.datetime.now(datetime.timezone.utc) - last_dt).total_seconds()
                if 0 <= age_s <= 24 * 3600:
                    runtime = 'recent'
            except (TypeError, ValueError):
                pass
    entry = {
        "id": meta['id'],
        "name": meta['name'],
        "status": meta['status'],
        "target": meta['target'],
        "state_file": meta['state_file'],
        "runs": loop_events[meta['id']]['runs'],
        "last_run": loop_events[meta['id']]['last_run'],
        "cycle": (state or {}).get('cycle', 0),
        "history_len": len(history),
        "last_signal": last_signal,
        "runtime": runtime,
        "params": params,
    }
    loops_out.append(entry)

loops = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
    'note': 'Loop k+3 tunes loop k (L4→L1 … L9→L6); L7–L9 are untuned fixed points. '
            'Live state is injected at startup by load_config(); this is a static snapshot.',
    'loops': loops_out,
}
if write:
    json.dump(loops, open(f'{RSIS3}/dashboard/loops.json', 'w'), indent=1)

# ── Epoch-1 telemetry snapshot (Roadmap tab "Epoch 1" strip) ───────────────
# Parses .rsis/telemetry/epoch1.jsonl (the shared append-only channel used by
# all phases 16–50) so the dashboard can show per-sequel event counts without
# each phase shipping its own pipeline. Event type prefixes map to sequels.
EPOCH1_SEQUEL_PREFIX = {
    'IV': ('attestation', 'portable', 'redteam', 'apps'),
    'V': ('identity', 'exchange', 'swarm', 'popgov', 'resilience'),
    'VI': ('metagov', 'capacity', 'goals', 'steward', 'endurance'),
    'VII': ('inheritance', 'archive', 'succession', 'mission', 'generation'),
    'VIII': ('decision', 'policy', 'delegation', 'trust', 'codesign'),
    'IX': ('standard', 'commons', 'treaty', 'crisis'),
    'X': ('study', 'experiment', 'failure', 'nearmiss', 'meta-invariant', 'epoch'),
}
EPOCH1_SEQUELS = ['IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']


def epoch1_telemetry(rsis3_dir):
    """Count epoch-1 telemetry events from the workspace log."""
    path = Path(rsis3_dir) / '.rsis' / 'telemetry' / 'epoch1.jsonl'
    by_type = {}
    if path.is_file():
        for line in path.read_text(encoding='utf-8', errors='ignore').splitlines():
            if not line.strip():
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            t = ev.get('type') or ''
            if t:
                by_type[t] = by_type.get(t, 0) + 1
    sequels = {r: 0 for r in EPOCH1_SEQUELS}
    other = 0
    for t, n in by_type.items():
        prefix = t.split('.', 1)[0]
        placed = False
        for rom, prefixes in EPOCH1_SEQUEL_PREFIX.items():
            if prefix in prefixes:
                sequels[rom] += n
                placed = True
                break
        if not placed:
            other += n
    return {
        'events': sum(by_type.values()),
        'sequels': sequels,
        'other': other,
        'by_type': dict(sorted(by_type.items(), key=lambda kv: -kv[1])[:12]),
    }


# ── Roadmap snapshot (drives the dashboard "Roadmap" tab) ───────────────
# Parses the status tables in the main roadmap + sequel docs so the program
# registry (100 phases / 2 epochs) stays in sync with the source documents.
ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII',
         9: 'IX', 10: 'X', 11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
         16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX'}
roadmap_phases, roadmap_arcs = [], []
for num in range(1, 21):
    rom = ROMAN[num]
    fname = 'multi-phase-development-roadmap.md' if num == 1 \
        else f'multi-phase-development-roadmap-sequel-{num}.md'
    path = os.path.join(RSIS3, 'docs', fname)
    if not os.path.exists(path):
        continue
    text = open(path, encoding='utf-8', errors='ignore').read()
    if num == 1:
        title, arc = 'Operational Autonomy', \
            'build → communicate → secure → persist → observe → operate → self-retune'
    else:
        m = re.search(r'Maturity arc: Phases [^—]+— \*\*(.+?)\*\*', text, re.S)
        title = m.group(1).strip() if m else f'Sequel {rom}'
        arc = ''
        m = re.search(r'Maturity arc: Phases [^—]+— \*\*(.+?)\*\*\s*\((.+?)\)', text, re.S)
        if m:
            arc = ' '.join(m.group(2).split())
    for row in text.split('## Status', 1)[-1].splitlines():
        m = re.match(r'\|\s*Phase (\d+)\s*—\s*(.+?)\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|', row)
        if not m:
            continue
        n = int(m.group(1))
        status_raw = m.group(4).strip()
        if '✅ delivered' in status_raw:
            status = 'validation' if '⏳' in status_raw else 'delivered'
        else:
            status = 'queued'
        roadmap_phases.append({
            'n': n, 'name': m.group(2).strip(), 'area': m.group(3).strip(),
            'status': status, 'status_raw': status_raw,
            'epoch': 1 if n <= 50 else 2, 'sequel': rom, 'doc': fname,
        })
    roadmap_arcs.append({
        'sequel': rom, 'phases': f'Phases {num * 5 - 4}–{num * 5}',
        'title': title, 'arc': arc, 'epoch': 1 if num <= 10 else 2, 'doc': fname,
    })
roadmap_phases.sort(key=lambda p: p['n'])
roadmap_counts = {
    'total': len(roadmap_phases),
    'delivered': sum(1 for p in roadmap_phases if p['status'] == 'delivered'),
    'validation': sum(1 for p in roadmap_phases if p['status'] == 'validation'),
    'queued': sum(1 for p in roadmap_phases if p['status'] == 'queued'),
}
roadmap = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
    'note': 'Parsed from the main roadmap + sequel docs status tables; '
            'autonomy is cumulative but never unconditional.',
    'epochs': [
        {'id': 1, 'phases': '1–50', 'sequels': 'I–X', 'title': 'Epoch 1 — one lineage to decade-scale maturity'},
        {'id': 2, 'phases': '51–100', 'sequels': 'XI–XX', 'title': 'Epoch 2 — the Age of Living Systems'},
    ],
    'arcs': roadmap_arcs,
    'phases': roadmap_phases,
    'counts': roadmap_counts,
}
if write:
    json.dump(roadmap, open(f'{RSIS3}/dashboard/roadmap.json', 'w'), indent=1)

eco = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
    'components': {
        'mykb': {'files': count('components/mykb'), 'md': md_count('components/mykb')},
        'space': {'files': count('components/space')},
        'rsis3': {'files': count('components/rsis3')},
    },
    'telemetry': telemetry,
    'epoch1': epoch1_telemetry(RSIS3),
    'roadmaps': {
        'epochs': len(roadmap['epochs']),
        'sequels': len(roadmap_arcs),
        'phases': roadmap_counts['total'],
        'delivered': roadmap_counts['delivered'],
        'validation_pending': roadmap_counts['validation'],
        'queued': roadmap_counts['queued'],
    },
}
if write:
    json.dump(eco, open(f'{RSIS3}/dashboard/ecosystem.json', 'w'), indent=1)

print(f'files.json: {len(md)} md files')
print(f'ecosystem.json: {json.dumps(eco["components"])}')
print(f'loops.json: {len(loops_out)} loops (runs: '
      + ', '.join(f"{e['id']}={e['runs']}" for e in loops_out if e['runs']) + ')')
print(f'roadmap.json: {roadmap_counts["total"]} phases, '
      + f"{roadmap_counts['delivered']} delivered, {roadmap_counts['validation']} validation pending, "
      + f"{roadmap_counts['queued']} queued)")

# Validation mode for CI/deploy: exit non-zero if the snapshot is inconsistent.
if '--check' in sys.argv:
    # Ecosystem data contracts (contracts/README.md) — shape + field rules.
    from contracts import validate as contracts
    _, contract_fail, _ = contracts.run_checks()
    # Snapshot freshness: committed files.json matches the current git-tracked
    # markdown list, and ecosystem counts match what this script would emit.
    on_disk = json.load(open('components/mykb/files.json'))
    on_disk_paths = ([e.get('path', '') for e in on_disk]
                     if on_disk and isinstance(on_disk[0], dict) else on_disk)
    bad = [p for p in on_disk_paths
           if p.startswith('components/') or not os.path.exists('components/mykb/' + p)]
    fresh = on_disk_paths == md and not bad
    eco2 = json.load(open(f'{RSIS3}/dashboard/ecosystem.json'))
    fresh = fresh and eco2['components']['mykb']['md'] == len(md) \
        and eco2['components']['mykb']['files'] == count('components/mykb')
    rm2 = json.load(open(f'{RSIS3}/dashboard/roadmap.json'))
    fresh = fresh and rm2['counts']['total'] == len(roadmap_phases) \
        and [p['n'] for p in rm2['phases']] == [p['n'] for p in roadmap_phases] \
        and eco2.get('roadmaps', {}).get('phases') == roadmap_counts['total'] \
        and eco2.get('epoch1', {}).get('events') == epoch1_telemetry(RSIS3)['events']
    ok = fresh and contract_fail == 0
    print('check:', 'OK' if ok else 'FAIL',
          f'({len(md)} entries, {len(bad)} bad, {contract_fail} contract FAIL)')
    sys.exit(0 if ok else 1)
