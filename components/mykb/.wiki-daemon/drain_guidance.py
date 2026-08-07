#!/usr/bin/env python3
"""Drain the guidance queue into scaffolded pages + a research manifest.

Reads `.wiki-daemon/buffers/guidance-queue.json` — wanted pages, research
directions, open questions, and page-level feedback written by the Guide tab
via `POST /api/v2/guidance/queue` — and turns it into executable research
direction:

  --plan   (default) print what would be scaffolded / exported, no changes
  --apply  scaffold `wanted` items as frontmatter stub pages and `question`
           items under wiki/questions/, then write a research manifest at
           `.wiki-daemon/buffers/guidance-inference.json` with the remaining
           directions and page feedback for the next acquisition/enrichment
           session.

Existing files are never overwritten; scaffolds carry `status: stub` and
`source: ["guidance-queue"]` so they flow into the normal stub triage and
enrichment pipeline.

Usage: python3 .wiki-daemon/drain_guidance.py [--plan|--apply]
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # components/mykb
QUEUE = os.path.join(HERE, 'buffers', 'guidance-queue.json')
MANIFEST = os.path.join(HERE, 'buffers', 'guidance-inference.json')
RESEARCH_KINDS = ('wanted', 'direction', 'question')
FEEDBACK_KINDS = ('suggestion', 'correction', 'priority', 'note')
TODAY = datetime.now(timezone.utc).strftime('%Y-%m-%d')


def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', (s or '').lower().strip())
    return re.sub(r'-+', '-', s).strip('-') or 'wanted-page'


def load_json(path):
    if not os.path.isfile(path):
        return None
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def item_title(it):
    if it.get('title'):
        return it['title']
    p = (it.get('path') or '').replace('\\', '/').strip().lstrip('/')
    if p:
        base = p.rstrip('.md').split('/')[-1]
        return ' '.join(w.capitalize() for w in base.split('-')) or base
    return (it.get('note') or '').split('\n')[0].strip() or slugify(it.get('kind', ''))


def item_desc(it):
    n = (it.get('note') or '').strip().replace('\n', ' ')
    return n[:140]


def derive_path(it):
    """Canonical wiki-relative path for a wanted/question item."""
    p = (it.get('path') or '').replace('\\', '/').strip().lstrip('/')
    if p:
        if p.startswith('wiki/'):
            p = p[len('wiki/'):]
        if not p.endswith('.md'):
            p += '.md'
        return 'wiki/' + p
    area = (it.get('area') or '').strip().strip('/')
    if it.get('kind') == 'question':
        area = 'questions'
    if not area:
        area = 'concepts'
    return 'wiki/%s/%s.md' % (area, slugify(item_title(it)))


def scaffold(kind, path, title, desc):
    area = path.split('/')[1]
    desc = (desc or '').replace('[[', '').replace(']]', '').strip()
    if kind == 'question':
        ftype = 'question'
        body = (
            '# %s\n\n## Summary\n\n%s\n\n'
            '## Details\n\n- Open question queued from the mykb Guidance UI.\n\n'
            '## Related\n\n' % (title, desc or title)
        )
    else:
        ftype = 'concept'
        body = (
            '# %s\n\n## Summary\n\n%s\n\n'
            '## Details\n\n- Wanted page scaffolded from the mykb Guidance UI; '
            'expand past the 320-word floor and link to related concepts.\n\n'
            '## Related\n\n' % (title, desc or title)
        )
    fm = {
        'type': ftype,
        'title': title,
        'description': desc or title,
        'tags': [area, 'guidance'],
        'timestamp': TODAY + 'T00:00:00Z',
        'status': 'stub',
        'created': TODAY,
        'source': ['guidance-queue'],
    }
    lines = ['---']
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append('%s: [%s]' % (k, ', '.join('"%s"' % x for x in v)))
        else:
            lines.append('%s: "%s"' % (k, v))
    lines.append('---')
    return '\n'.join(lines) + '\n\n' + body


def plan_or_apply(apply):
    q = load_json(QUEUE)
    if not q or not q.get('items'):
        print('No guidance queue: %s' % QUEUE)
        print('Open the Guide tab, add wanted pages / directions / questions, then Save guidance.')
        return 1 if not q else 0
    items = q['items']
    by_kind = {}
    for it in items:
        by_kind.setdefault(it.get('kind', 'note'), []).append(it)
    summary = ' '.join('%s=%d' % (k, len(v)) for k, v in sorted(by_kind.items()))
    print('Guidance queue %s — %d items (%s)' % (q.get('queued_at', '?'), len(items), summary))
    print('')

    created, skipped, research, feedback = [], [], [], []
    for it in items:
        kind = it.get('kind', 'note')
        if kind not in RESEARCH_KINDS:
            feedback.append({
                'kind': kind, 'path': it.get('path', ''),
                'note': it.get('note', ''), 'priority': it.get('priority', 2),
                'added': it.get('added', ''),
            })
            continue
        title = item_title(it)
        desc = item_desc(it)
        if kind == 'direction':
            research.append({
                'kind': 'direction', 'title': title, 'note': it.get('note', ''),
                'area': it.get('area', ''), 'priority': it.get('priority', 2),
                'added': it.get('added', ''),
            })
            continue
        path = derive_path(it)
        full = os.path.join(ROOT, path)
        if os.path.isfile(full):
            skipped.append({'path': path, 'title': title})
            print('  = exists, skip: %s' % path)
            continue
        text = scaffold(kind, path, title, desc)
        if apply:
            os.makedirs(os.path.dirname(full), exist_ok=True)
            with open(full, 'w', encoding='utf-8') as fh:
                fh.write(text)
            print('  ✓ scaffold %s (%s)' % (path, kind))
        else:
            print('  → scaffold %s (%s)' % (path, kind))
        created.append({
            'path': path, 'title': title, 'kind': kind,
            'description': desc, 'priority': it.get('priority', 2),
            'note': it.get('note', ''),
        })

    if research:
        print('')
        print('Research directions for the inference pass: %d' % len(research))
        for r in research[:5]:
            print('  - [%s] %s (P%s)' % (r['kind'], r['title'], r['priority']))
        if len(research) > 5:
            print('  … and %d more' % (len(research) - 5))
    if feedback:
        print('')
        kinds = sorted({f['kind'] for f in feedback})
        print('Page feedback carried to the manifest: %d (%s)' % (len(feedback), ', '.join(kinds)))

    if apply:
        manifest = {
            'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
            'source': QUEUE,
            'created': created,
            'skipped': skipped,
            'research': research,
            'feedback': feedback,
        }
        os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
        with open(MANIFEST, 'w', encoding='utf-8') as fh:
            json.dump(manifest, fh, indent=1, ensure_ascii=False)
        print('')
        print('manifest written: %s (%d created, %d skipped)' % (
            MANIFEST, len(created), len(skipped)))
    elif created or research or feedback:
        print('')
        print('  (--apply writes the scaffolds + research manifest)')
    print('')
    return 0


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    sys.exit(plan_or_apply(apply))
