#!/usr/bin/env python3
"""Regenerate static data snapshots for the COSMOS GitHub Pages site.

Uses git-tracked files only so every entry in files.json / ecosystem.json
exists on the deployed site. Run from the repo root, then commit.

    python3 gen-static-data.py
"""
import json, subprocess, datetime

def tracked(prefix=None):
    args = ['git', 'ls-files']
    if prefix:
        args.append(prefix)
    return subprocess.run(args, capture_output=True, text=True).stdout.splitlines()

def visible(path):
    return not any(seg.startswith('.') for seg in path.split('/'))

md = sorted(p for p in tracked('components/mykb') if p.endswith('.md') and visible(p))
json.dump(md, open('components/mykb/files.json', 'w'), indent=1)

allf = [p for p in tracked() if visible(p)]
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

eco = {
    'generated': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ'),
    'components': {
        'mykb': {'files': count('components/mykb'), 'md': md_count('components/mykb')},
        'space': {'files': count('components/space')},
        'rsis3': {'files': count('components/rsis3')},
    },
    'telemetry': telemetry,
}
json.dump(eco, open('components/rsis3/dashboard/ecosystem.json', 'w'), indent=1)

print(f'files.json: {len(md)} md files')
print(f'ecosystem.json: {json.dumps(eco["components"])}')
