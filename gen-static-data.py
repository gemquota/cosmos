#!/usr/bin/env python3
"""Regenerate static data snapshots for the COSMOS GitHub Pages site.

Uses git-tracked files only so every entry in files.json / ecosystem.json
exists on the deployed site. Run from the repo root, then commit.

    python3 gen-static-data.py
"""
import json, os, subprocess, sys, datetime
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

telemetry = {}
try:
    d = json.load(open('components/rsis3/rack/pulses/dashboard-data.json'))
    sm = d.get('summary', {})
    telemetry = {
        'pulses': len(d.get('pulses', [])), 'goals': len(d.get('goals', [])),
        'passed': sm.get('pass', 0), 'failed': sm.get('fail', 0), 'held': sm.get('hold', 0),
        'total': sm.get('tot', 0), 'improvements': sm.get('impl_count', 0),
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

eco = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
    'components': {
        'mykb': {'files': count('components/mykb'), 'md': md_count('components/mykb')},
        'space': {'files': count('components/space')},
        'rsis3': {'files': count('components/rsis3')},
    },
    'telemetry': telemetry,
}
if write:
    json.dump(eco, open(f'{RSIS3}/dashboard/ecosystem.json', 'w'), indent=1)

print(f'files.json: {len(md)} md files')
print(f'ecosystem.json: {json.dumps(eco["components"])}')
print(f'loops.json: {len(loops_out)} loops (runs: '
      + ', '.join(f"{e['id']}={e['runs']}" for e in loops_out if e['runs']) + ')')

# Validation mode for CI/deploy: exit non-zero if the snapshot is inconsistent.
if '--check' in sys.argv:
    on_disk = json.load(open('components/mykb/files.json'))
    on_disk_paths = ([e.get('path', '') for e in on_disk]
                     if on_disk and isinstance(on_disk[0], dict) else on_disk)
    bad = [p for p in on_disk_paths
           if p.startswith('components/') or not os.path.exists('components/mykb/' + p)]
    ok = on_disk_paths == md and not bad
    eco2 = json.load(open(f'{RSIS3}/dashboard/ecosystem.json'))
    ok = ok and eco2['components']['mykb']['md'] == len(md) and eco2['components']['mykb']['files'] == count('components/mykb')
    # loops.json: all ten ids present with required keys and consistent statuses
    try:
        loops2 = json.load(open(f'{RSIS3}/dashboard/loops.json'))
        ids = {e['id'] for e in loops2['loops']}
        required = {'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'}
        ok = ok and ids == required and all(
            all(k in e for k in ('name', 'status', 'target', 'runs', 'params'))
            for e in loops2['loops']
        )
    except Exception:
        ok = False
    print('check:', 'OK' if ok else 'FAIL', f'({len(md)} entries, {len(bad)} bad)')
    sys.exit(0 if ok else 1)
