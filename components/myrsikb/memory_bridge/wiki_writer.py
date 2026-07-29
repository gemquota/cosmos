#!/usr/bin/env python3
"""WikiWriter — writes RSIS3 cognitive artifacts as mykb wiki pages.

Each RSIS3 subsystem (identity, RRP, pulse, codegen) produces structured
knowledge that becomes permanent wiki entries with YAML frontmatter (OKF format).
"""

import os
import re
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Optional


#  ── Helpers ─────────────────────────────────────────────────────

def _slugify(text: str, max_len: int = 60) -> str:
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:max_len]


def _frontmatter(**fields) -> str:
    """Build YAML frontmatter block. Tags are the only list field."""
    lines = ['---']
    for k, v in fields.items():
        if k == 'tags' and isinstance(v, (list, tuple)):
            quoted = ', '.join(f'"{t}"' for t in v)
            lines.append(f'tags: [{quoted}]')
        elif isinstance(v, str):
            escaped = v.replace('"', "'")
            lines.append(f'{k}: "{escaped}"')
        elif isinstance(v, bool):
            lines.append(f'{k}: {"true" if v else "false"}')
        elif isinstance(v, (int, float)):
            lines.append(f'{k}: {v}')
        else:
            lines.append(f'{k}: {json.dumps(v)}')
    lines.append('---')
    return '\n'.join(lines)


def _iso_now() -> str:
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def _write_md(path: Path, front: dict, body: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    content = _frontmatter(**front) + '\n\n' + body.strip() + '\n'
    path.write_text(content, encoding='utf-8')


#  ── WikiWriter ──────────────────────────────────────────────────

class WikiWriter:
    """Writes structured knowledge from RSIS3 into mykb's wiki bundle.

    Args:
        wiki_root: Path to mykb's ``wiki/`` directory.
    """

    def __init__(self, wiki_root: str | Path):
        self.root = Path(wiki_root)
        # Sub-directories mirror mykb's type_dirs
        self._dirs = {
            'session':   self.root / 'sessions',
            'entity':    self.root / 'entities',
            'decision':  self.root / 'decisions',
            'tool':      self.root / 'tools',
            'topic':     self.root / 'topics',
            'daily':     self.root / 'daily',
            'identity':  self.root / 'identity',
        }
        for d in self._dirs.values():
            d.mkdir(parents=True, exist_ok=True)

    # ── Identity ─────────────────────────────────────────────

    def write_identity_snapshot(self, snapshot_id: int, data: dict) -> Path:
        """Write an identity snapshot as a wiki page.

        ``data`` should contain layer_scores, value_axioms, self_concept,
        narrative, etc.
        """
        narrative = data.get('narrative', '') or data.get('self_concept', {}).get('current_narrative', '')
        scores = data.get('layer_scores', {})

        body_parts = [f'# Identity Snapshot {snapshot_id}\n']
        body_parts.append(f'**Narrative:** {narrative}\n')
        body_parts.append('## Layer Scores\n')
        for lid in sorted(scores):
            entry = scores[lid]
            if isinstance(entry, dict):
                score = entry.get('score', 0)
                body_parts.append(f'- **{lid}**: `{score}`')
            else:
                body_parts.append(f'- **{lid}**: `{entry}`')

        axioms = data.get('value_axioms', {})
        if axioms:
            body_parts.append('\n## Value Axioms\n')
            for name, state in axioms.items():
                if isinstance(state, dict):
                    count = state.get('reinforced_count', state.get('count', 0))
                else:
                    count = state
                body_parts.append(f'- **{name}** — reinforced {count}×')

        tags = ['identity', 'snapshot', f'snapshot-{snapshot_id}']
        front = {
            'type': 'snapshot',
            'title': f'Identity Snapshot {snapshot_id}',
            'description': narrative[:120] if narrative else self._score_summary(scores),
            'tags': tags + [f'layer-{lid.lower()}' for lid in scores],
            'timestamp': _iso_now(),
        }

        path = self._dirs['identity'] / f'snapshot-{snapshot_id:04d}.md'
        _write_md(path, front, '\n'.join(body_parts))
        return path

    def write_decision(self, decision_id: str, description: str,
                       reasoning: str, confidence: float,
                       tags: Optional[list[str]] = None) -> Path:
        """Write a decision (from RRP or identity) as a wiki decision page."""
        body = (
            f'# Decision: {description}\n\n'
            f'**Confidence:** {confidence}\n\n'
            f'## Reasoning\n\n{reasoning}\n'
        )
        front = {
            'type': 'decision',
            'title': description[:80],
            'description': reasoning[:200],
            'tags': (tags or []) + ['decision'],
            'timestamp': _iso_now(),
            'confidence': confidence,
        }
        path = self._dirs['decision'] / f'{_slugify(description)}.md'
        _write_md(path, front, body)
        return path

    def write_value_reinforcement(self, axiom_name: str, count: int,
                                  context: str = '') -> Path:
        """Log a value reinforcement event."""
        body = (
            f'# Value Reinforcement: {axiom_name}\n\n'
            f'**Count:** {count}\n\n'
            f'**Context:** {context}\n'
        )
        front = {
            'type': 'entity',
            'title': f'Value: {axiom_name}',
            'description': f'Reinforced {count}×. {context[:100]}',
            'tags': ['value-axiom', _slugify(axiom_name)],
            'timestamp': _iso_now(),
        }
        slug = _slugify(f'value-{axiom_name}')
        path = self._dirs['entity'] / f'{slug}.md'
        _write_md(path, front, body)
        return path

    # ── RRP (Reasoning & Resolution Protocol) ────────────────

    def write_rrp_summary(self, session_id: str, use_case: str,
                          decisions: list[dict], constraints: list[dict],
                          ambiguity: dict, outcome: str) -> Path:
        """Summarise an RRP session as a wiki session page."""
        body_parts = [f'# RRP Session: {session_id[:12]}\n']
        body_parts.append(f'**Use Case:** {use_case}')
        body_parts.append(f'**Outcome:** {outcome}\n')

        if decisions:
            body_parts.append('## Decisions\n')
            for d in decisions:
                dt = d.get('decision_type', d.get('type', 'decision'))
                desc = d.get('description', '')
                conf = d.get('confidence', d.get('rating', 0))
                body_parts.append(f'- [{dt}] {desc} (confidence: {conf})')

        if constraints:
            body_parts.append('\n## Constraints\n')
            for c in constraints:
                k = c.get('key', c.get('name', ''))
                v = c.get('value', c.get('description', ''))
                src = c.get('source', 'unknown')
                body_parts.append(f'- **{k}**: {v} _(source: {src})_')

        if ambiguity:
            body_parts.append('\n## Ambiguity Vector\n')
            for dim, val in ambiguity.items():
                if isinstance(val, (int, float)):
                    bar = '█' * int(val * 10) + '░' * (10 - int(val * 10))
                    body_parts.append(f'- **{dim}**: {bar} {val:.2f}')

        concept_tags = ['rrp', 'reasoning', outcome or 'unknown']
        front = {
            'type': 'session',
            'title': f'RRP Session: {use_case[:60]}',
            'description': f'{len(decisions)} decisions, {len(constraints)} constraints → {outcome}',
            'tags': concept_tags,
            'timestamp': _iso_now(),
        }
        path = self._dirs['session'] / f'session-{_slugify(session_id, 50)}.md'
        _write_md(path, front, '\n'.join(body_parts))
        return path

    # ── Pulse (telemetry / observations) ─────────────────────

    def write_daily_note(self, pulse_data: dict) -> Path:
        """Write a pulse observation as a daily wiki page."""
        date_str = datetime.utcnow().strftime('%Y-%m-%d')
        pulse_id = pulse_data.get('pulse_id', 0)
        narrative = pulse_data.get('narrative', pulse_data.get('description', ''))

        body_parts = [f'# Daily Note: {date_str}\n']
        body_parts.append(f'**Pulse:** #{pulse_id}\n')

        baseline = pulse_data.get('baseline', pulse_data.get('system_baseline', {}))
        if isinstance(baseline, dict):
            ls = baseline.get('layer_scores', {})
            if ls:
                body_parts.append('## Layer Scores\n')
                for lid in sorted(ls):
                    v = ls[lid]
                    if isinstance(v, dict):
                        v = v.get('score', v.get('value', 0))
                    body_parts.append(f'- **{lid}**: {v}')

        signals = pulse_data.get('signals', pulse_data.get('observations', []))
        if signals:
            body_parts.append('\n## Signals\n')
            for sig in signals[:10]:
                if isinstance(sig, dict):
                    body_parts.append(f'- {sig.get("type", sig.get("signal_type", "signal"))}: {sig.get("description", sig.get("source", ""))}')

        if narrative:
            body_parts.append(f'\n## Narrative\n\n{narrative}\n')

        tags = ['daily', 'pulse', date_str]
        front = {
            'type': 'concept',
            'title': f'Daily Note {date_str}',
            'description': narrative[:120] if narrative else f'Pulse #{pulse_id}',
            'tags': tags,
            'timestamp': _iso_now(),
        }
        path = self._dirs['daily'] / f'{date_str}.md'
        _write_md(path, front, '\n'.join(body_parts))
        return path

    # ── Codegen (self-modification) ──────────────────────────

    def write_codegen_event(self, problem: str, patch_summary: str,
                            reason: str, outcome: str,
                            benchmark: Optional[dict] = None) -> Path:
        """Write a code generation event as a wiki topic page.

        Every successful mutation becomes a searchable wiki article.
        """
        slug = _slugify(problem, 50)
        body_parts = [
            f'# Code Mutation: {problem}\n',
            f'**Outcome:** {outcome}\n',
            f'**Patch:** {patch_summary}\n',
            f'**Rationale:** {reason}\n',
        ]
        if benchmark:
            body_parts.append('\n## Benchmark\n')
            for k, v in benchmark.items():
                body_parts.append(f'- **{k}**: {v}')

        front = {
            'type': 'topic',
            'title': f'Code: {problem[:80]}',
            'description': f'{patch_summary[:150]} → {outcome}',
            'tags': ['codegen', 'mutation', outcome, slug],
            'timestamp': _iso_now(),
        }
        path = self._dirs['topic'] / f'codegen-{slug}.md'
        _write_md(path, front, '\n'.join(body_parts))
        return path

    def write_goal(self, goal_id: str, description: str, priority: float,
                   source_signal: Optional[str] = None,
                   value_alignment: Optional[list[str]] = None,
                   suggested_tasks: Optional[list[str]] = None) -> Path:
        """Write a generated goal as a wiki page."""
        body = (
            f'# Goal: {description}\n\n'
            f'**Priority:** {priority}\n'
            f'**Source:** {source_signal or "system"}\n\n'
        )
        if value_alignment:
            body += '**Value Alignment:** ' + ', '.join(f'`{v}`' for v in value_alignment) + '\n\n'
        if suggested_tasks:
            body += '## Suggested Tasks\n' + '\n'.join(f'- {t}' for t in suggested_tasks) + '\n'

        front = {
            'type': 'topic',
            'title': f'Goal: {description[:80]}',
            'description': f'Priority {priority} from {source_signal or "state analysis"}',
            'tags': ['goal'] + (value_alignment or []) + [f'prio-{priority:.1f}'],
            'timestamp': _iso_now(),
        }
        path = self._dirs['topic'] / f'goal-{_slugify(description, 50)}.md'
        _write_md(path, front, body)
        return path

    # ── Knowledge Graph ──────────────────────────────────────

    def write_entity(self, entity_id: str, title: str,
                     description: str, tags: Optional[list[str]] = None,
                     body: str = '') -> Path:
        """Write a named entity (concept, tool, etc.) into the wiki."""
        front = {
            'type': 'entity',
            'title': title,
            'description': description[:200],
            'tags': (tags or []) + ['entity'],
            'timestamp': _iso_now(),
        }
        body_text = body or f'# {title}\n\n{description}\n'
        path = self._dirs['entity'] / f'{_slugify(entity_id, 50)}.md'
        _write_md(path, front, body_text)
        return path

    def write_concept_link(self, source_id: str, target_id: str,
                           rel: str, metadata: Optional[dict] = None) -> None:
        """Record a relationship between two wiki entities."""
        target_title = target_id.replace('-', ' ').title()
        link_text = f'  - *{rel}* → [[{target_id}|{target_title}]]'
        if metadata:
            link_text += f'  _{json.dumps(metadata)}_'

        path = self._dirs['entity'] / f'{_slugify(source_id, 50)}.md'
        if path.exists():
            content = path.read_text(encoding='utf-8')
            if '---' in content:
                parts = content.split('---', 2)
                if len(parts) == 3:
                    parts[2] = parts[2].rstrip() + '\n' + link_text + '\n'
                    path.write_text('---'.join(parts), encoding='utf-8')

    # ── helpers ──────────────────────────────────────────────

    @staticmethod
    def _score_summary(scores: dict) -> str:
        parts = []
        for lid in sorted(scores):
            v = scores[lid]
            if isinstance(v, dict):
                v = v.get('score', 0)
            parts.append(f'{lid}={v}')
        return ' '.join(parts)
