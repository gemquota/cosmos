#!/usr/bin/env python3
"""Drain the Stub Auditor queue into an inference pass.

Reads `.wiki-daemon/buffers/stub-audit-queue.json` — written by the Stub
Auditor SPA via `POST /api/v2/stubs/queue` (or downloaded and placed there) —
and either plans or applies the human decisions:

  --plan   (default) print what would happen per decision, no changes
  --apply  execute the mechanical decisions (categorize/archive/delete via
           git mv / git rm, with plain-filesystem fallback) and emit an
           inference manifest for `enrich` items at
           `.wiki-daemon/buffers/stub-audit-inference.json`

The inference manifest is the handoff for the LLM expansion pass: each task
carries the stub path plus its metadata and opening snippet, so workers can
expand it past the 320-word floor without re-scanning the wiki. When a
guidance queue exists (`.wiki-daemon/buffers/guidance-queue.json` — wanted
pages, research directions, open questions, page-level feedback), it is
merged into the manifest as `guidance` so the same pass also seeds new pages
and honours human direction.

Usage: python3 .wiki-daemon/drain_stub_queue.py [--plan|--apply]
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # components/mykb
QUEUE = os.path.join(HERE, 'buffers', 'stub-audit-queue.json')
GUIDANCE = os.path.join(HERE, 'buffers', 'guidance-queue.json')
MANIFEST = os.path.join(HERE, 'buffers', 'stub-audit-inference.json')
GOAL_WORDS = 320
RESEARCH_KINDS = ('wanted', 'direction', 'question')


def run_git(args):
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT)


def queue_path(item):
    p = item.get('path', '').replace('\\', '/').lstrip('/')
    # Full bundle-relative paths (raw/archive junk items) pass through;
    # bare or wiki-relative stubs are rooted under wiki/.
    if p.startswith('wiki/') or p.startswith('raw/'):
        return p
    return 'wiki/' + p


def safe_move(src, dst):
    """git mv with plain-filesystem fallback for untracked files."""
    r = run_git(['git', 'mv', src, dst])
    if r.returncode != 0:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        os.rename(src, dst)


def safe_remove(src):
    r = run_git(['git', 'rm', '-q', src])
    if r.returncode != 0:
        os.remove(src)


def load_json(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def guidance_tasks():
    """Split the guidance queue into research tasks + page feedback."""
    g = load_json(GUIDANCE)
    if not g or not g.get('items'):
        return None, None
    research, feedback = [], []
    for it in g['items']:
        kind = it.get('kind', 'note')
        if kind in RESEARCH_KINDS:
            research.append({
                'kind': kind,
                'title': it.get('title', '') or it.get('note', '')[:120],
                'path': it.get('path', ''),
                'area': it.get('area', ''),
                'priority': it.get('priority', 2),
                'note': it.get('note', ''),
                'added': it.get('added', ''),
            })
        else:
            feedback.append({
                'kind': kind,
                'path': it.get('path', ''),
                'note': it.get('note', ''),
                'priority': it.get('priority', 2),
                'added': it.get('added', ''),
            })
    return research, feedback


def plan_or_apply(apply):
    if not os.path.isfile(QUEUE):
        print(f'No queue file: {QUEUE}')
        print('Open the Stub Auditor and press "Save queue" first.')
        return 1
    with open(QUEUE, encoding='utf-8') as fh:
        q = json.load(fh)
    items = q.get('items', [])
    if not items:
        print('Queue is empty.')
        return 0

    counts = {}
    for it in items:
        counts[it.get('decision')] = counts.get(it.get('decision'), 0) + 1
    summary = ' '.join(f'{k}={v}' for k, v in sorted(counts.items()))
    print(f'Queue {q.get("queued_at", "?")} — {len(items)} items ({summary})')
    print('')

    idx = {}
    idx_path = os.path.join(ROOT, 'stub-index.json')
    if os.path.isfile(idx_path):
        for s in json.load(open(idx_path, encoding='utf-8')).get('stubs', []):
            idx[s['path']] = s

    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    enrich, mech, missing = [], [], []
    for it in items:
        rel = queue_path(it)
        src = os.path.join(ROOT, rel)
        dec = it.get('decision')
        if not os.path.isfile(src):
            missing.append((rel, dec))
            continue
        if dec == 'e':
            meta = idx.get(rel, {})
            enrich.append({
                'path': rel,
                'title': it.get('title', ''),
                'words': it.get('words', 0),
                'links': it.get('links', 0),
                'status': it.get('status', ''),
                'type': it.get('type') or meta.get('type', 'concept'),
                'tags': it.get('tags') or meta.get('tags', []),
                'area': it.get('area') or meta.get('area', rel.split('/')[1] if rel.startswith('wiki/') else ''),
                'description': it.get('description', ''),
                'snippet': it.get('snippet', ''),
            })
        elif dec in ('c', 'a', 'd'):
            mech.append((it, src, rel))

    for it, src, rel in mech:
        dec = it.get('decision')
        if dec == 'c':
            target = (it.get('target') or '').replace('\\', '/').lstrip('/')
            if not target.endswith('.md'):
                target = target.rstrip('/') + '/' + rel.rsplit('/', 1)[-1]
            dst = os.path.join(ROOT, target)
            if src == dst:
                print(f'  = (no-op) {rel} → {target}')
                continue
            action = 'git mv %s %s' % (src, dst)
            if apply:
                safe_move(src, dst)
                print('  ✓ ' + action)
            else:
                print('  → ' + action)
        elif dec == 'a':
            arch = os.path.join(ROOT, 'raw', 'archive', 'stub-audit-' + today, rel)
            action = 'git mv %s %s' % (src, arch)
            if apply:
                safe_move(src, arch)
                print('  ✓ ' + action)
            else:
                print('  → ' + action)
        elif dec == 'd':
            action = 'git rm %s' % src
            if apply:
                safe_remove(src)
                print('  ✓ ' + action)
            else:
                print('  → ' + action)

    if missing:
        print('')
        for rel, dec in missing:
            print(f'  ! missing file, skipped: {rel} ({dec})')

    research, feedback = guidance_tasks()
    if research or feedback:
        print('')
        if research:
            print(f'Guidance research tasks: {len(research)} ({", ".join(sorted({t["kind"] for t in research}))})')
            for t in research[:5]:
                print(f'  - [{t["kind"]}] {t["title"]} (P{t["priority"]})')
            if len(research) > 5:
                print(f'  … and {len(research) - 5} more')
        if feedback:
            kinds = sorted({f["kind"] for f in feedback})
            print(f'Guidance page feedback: {len(feedback)} items ({", ".join(kinds)})')

    write_manifest = apply and (enrich or research or feedback)
    if enrich:
        print('')
        print(f'Enrich tasks for inference pass: {len(enrich)}')
        for t in enrich[:3]:
            print(f'  - {t["path"]} ({t["words"]} words)')
        if len(enrich) > 3:
            print(f'  … and {len(enrich) - 3} more')

    if write_manifest:
        manifest = {
            'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'source': QUEUE,
            'goal_words': GOAL_WORDS,
            'instructions': (
                'Expand each stub into a full article. Keep the existing frontmatter and title; '
                'grow the body past %d words; add concrete, accurate detail and 2-5 topical '
                '[[wikilinks]]; do not invent system claims about the wiki/RSIS3.' % GOAL_WORDS
            ),
            'tasks': enrich,
        }
        if research or feedback:
            manifest['guidance'] = {
                'source': GUIDANCE,
                'research': research,
                'feedback': feedback,
            }
        os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
        with open(MANIFEST, 'w', encoding='utf-8') as fh:
            json.dump(manifest, fh, indent=1, ensure_ascii=False)
        print(f'  manifest written: {MANIFEST}')
    elif not apply and (enrich or research or feedback):
        print('')
        print('  (--apply writes the inference manifest incl. guidance)')

    print('')
    return 0


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    sys.exit(plan_or_apply(apply))
