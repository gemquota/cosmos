#!/usr/bin/env python3
"""MemoryClient — RSIS3's unified interface to mykb.

This is the class RSIS3 imports. It exposes every memory operation
through one clean facade so RSIS3's subsystems never touch mykb directly.

Usage::

    from memory_bridge import MemoryClient

    kb = MemoryClient()                     # auto-discovers mykb/wiki path
    # or
    kb = MemoryClient(wiki_root="/path/to/mykb/wiki")

    # Write
    kb.identity.write_identity_snapshot(1, {...})
    kb.wiki.write_rrp_summary(...)
    kb.wiki.write_daily_note(pulse_data)

    # Search
    results = kb.search("crisis recovery patterns")
    similar = kb.find_similar("entities/fastapi-10")

    # Graph
    nbrs = kb.graph.neighborhood("entities/docker", hops=2)
    path = kb.graph.shortest_path("entities/a", "entities/b")

    # Temporal
    rising = kb.temporal.rising_entities()
    activity = kb.temporal.monthly_activity()

    # Gaps → Goals
    goals = kb.gaps.to_goals()
"""

import sys
import warnings
from pathlib import Path
from typing import Optional

from memory_bridge.wiki_writer import WikiWriter
from memory_bridge.knowledge_graph import KnowledgeGraph
from memory_bridge.vector_search import SemanticMemory
from memory_bridge.temporal_memory import TemporalMemory
from memory_bridge.gap_detector import GapDetector
# Lazy instance cache — keyed by wiki path to support multiple wikis
_instances = {}

def _get_instance(wiki, cls_name, mod_name):
    key = (cls_name, str(wiki))
    if key not in _instances:
        import importlib
        mod = importlib.import_module(f'memory_bridge.{mod_name}')
        cls = getattr(mod, cls_name)
        _instances[key] = cls(wiki)
    return _instances[key]

def _get_experience_memory(wiki):
    return _get_instance(wiki, 'ExperienceMemory', 'experience_memory')

def _get_reflection(wiki):
    return _get_instance(wiki, 'ReflectionEngine', 'reflection')

def _get_experiment(wiki):
    return _get_instance(wiki, 'ExperimentManager', 'experiment')

def _get_meta_learning(wiki):
    return _get_instance(wiki, 'MetaLearningEngine', 'meta_learning')

def _get_planner(wiki):
    return _get_instance(wiki, 'ExecutivePlanner', 'planner')
from memory_bridge.config import resolve_wiki_path, resolve_mykb_daemon


#  ── MemoryClient ──────────────────────────────────────────────

class MemoryClient:
    """RSIS3's memory interface — wraps all mykb subsystems.

    Args:
        wiki_root: Path to mykb's ``wiki/`` directory. If ``None``,
            resolves automatically relative to the memory_bridge package.
        auto_init: If True, ensures the wiki directory structure exists.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None,
                 auto_init: bool = True):
        self._wiki = Path(wiki_root) if wiki_root else self._default_wiki()
        if auto_init:
            self._wiki.mkdir(parents=True, exist_ok=True)

        # Ensure mykb daemon dir is on sys.path for sub-imports
        _daemon = resolve_mykb_daemon()
        _daemon_str = str(_daemon)
        if _daemon_str not in sys.path:
            sys.path.insert(0, _daemon_str)
        
        # Check version compatibility with rsis3 and mykb
        self._check_versions()

        # Sub-interfaces
        self.wiki = WikiWriter(self._wiki)
        self.graph = KnowledgeGraph(self._wiki)
        self.semantic = SemanticMemory(self._wiki)
        self.temporal = TemporalMemory(self._wiki)
        self.gaps = GapDetector(self._wiki)
        self.experiences = _get_experience_memory(self._wiki)
        self.reflection = _get_reflection(self._wiki)
        self.experiments = _get_experiment(self._wiki)
        self.meta_learning = _get_meta_learning(self._wiki)
        self.planner = _get_planner(self._wiki)

    # ── Version compatibility ───────────────────────────────

    def _check_versions(self):
        """Check version compatibility between rsis3, mykb, and myrsikb.
        
        Reads VERSION files from each project root and warns on mismatch.
        This is advisory only — no hard block.
        """
        myrsikb_root = Path(__file__).resolve().parent.parent
        myrsikb_ver = self._read_version(myrsikb_root / "VERSION")
        
        # rsis3 is typically at ../../rsis3 relative to myrsikb
        rsis3_root = myrsikb_root.parent / "rsis3"
        rsis3_ver = self._read_version(rsis3_root / "VERSION")
        
        # mykb wiki is at our wiki root's parent (wiki/ -> mykb root)
        mykb_root = self._wiki.parent
        mykb_ver = self._read_version(mykb_root / "VERSION")
        
        versions = {
            "myrsikb": myrsikb_ver,
            "rsis3": rsis3_ver,
            "mykb": mykb_ver,
        }
        
        # Check that all versions are present and equal
        present = {k: v for k, v in versions.items() if v}
        if len(set(present.values())) > 1:
            warnings.warn(
                f"[memory] Version mismatch: {present}. "
                f"Expected all triad components at the same version."
            )
        
        self._versions = versions

    @staticmethod
    def _read_version(path: Path) -> str:
        """Read a VERSION file, returning empty string if not found."""
        try:
            return path.read_text().strip()
        except (FileNotFoundError, OSError):
            return ""

    # ── Convenience wrappers ─────────────────────────────────

    def store_identity_snapshot(self, snapshot_id: int, data: dict) -> Path:
        """Convenience: write identity snapshot + trigger re-index (best-effort)."""
        path = self.wiki.write_identity_snapshot(snapshot_id, data)
        try:
            self.semantic.store(
                f'identity/snapshot-{snapshot_id:04d}',
                str(data),
                {'type': 'snapshot', 'title': f'Identity Snapshot {snapshot_id}'},
            )
        except Exception as exc:
            # Vector indexing is best-effort — wiki page is the primary artifact
            print(f"[memory] semantic index skipped for identity snapshot: {exc}")
        return path

    def store_rrp_session(self, session_id: str, use_case: str,
                          decisions: list, constraints: list,
                          ambiguity: dict, outcome: str) -> Path:
        """Convenience: write RRP summary + extract entities + index."""
        path = self.wiki.write_rrp_summary(
            session_id, use_case, decisions, constraints, ambiguity, outcome,
        )
        # Extract key entities from decisions
        for d in decisions:
            desc = d.get('description', '')
            if desc:
                self.wiki.write_entity(
                    entity_id=f'rrp-{_slugify(desc[:40])}',
                    title=desc[:80],
                    description=d.get('reasoning', desc)[:200],
                    tags=['rrp', 'decision', outcome],
                    body=f"From RRP session {session_id[:12]}: {desc}",
                )
        return path

    def store_pulse(self, pulse_data: dict) -> Path:
        """Convenience: write pulse as daily note + index (best-effort)."""
        path = self.wiki.write_daily_note(pulse_data)
        try:
            # Also store in semantic index for search — best-effort
            self.semantic.store(
                f'pulse-{pulse_data.get("pulse_id", "latest")}',
                str(pulse_data),
                {'type': 'pulse', 'title': f'Pulse #{pulse_data.get("pulse_id", 0)}'},
            )
        except Exception as exc:
            print(f"[memory] semantic index skipped for pulse: {exc}")
        return path

    def store_code_change(self, problem: str, patch: str,
                          reason: str, outcome: str,
                          benchmark: Optional[dict] = None) -> Path:
        path = self.wiki.write_codegen_event(problem, patch, reason, outcome, benchmark)
        self.semantic.store(
            f'codegen-{_slugify(problem[:40])}',
            f'{problem}\n{patch}\n{reason}',
            {'type': 'codegen', 'title': f'Code: {problem[:80]}',
             'tags': ['codegen', outcome]},
        )
        return path

    def store_goal(self, goal_id: str, description: str, priority: float,
                   source_signal: Optional[str] = None,
                   value_alignment: Optional[list[str]] = None,
                   suggested_tasks: Optional[list[str]] = None) -> Path:
        return self.wiki.write_goal(
            goal_id, description, priority, source_signal,
            value_alignment, suggested_tasks,
        )

    # ── Search ───────────────────────────────────────────────

    def search(self, query: str, top_k: int = 20,
               filters: Optional[dict] = None) -> list[dict]:
        """Hybrid search across all knowledge."""
        return self.semantic.search(query, top_k=top_k, filters=filters)

    def find_similar(self, entity_id: str, top_k: int = 10) -> list[dict]:
        """Find semantically similar entities."""
        return self.semantic.find_similar(entity_id, top_k=top_k)

    # ── Graph ────────────────────────────────────────────────

    def graph_neighborhood(self, entity_id: str, hops: int = 2) -> list[dict]:
        return self.graph.neighborhood(entity_id, hops=hops)

    def graph_shortest_path(self, a: str, b: str):
        return self.graph.shortest_path(a, b)

    def graph_central(self, top_n: int = 20) -> list[dict]:
        return self.graph.central_entities(top_n=top_n)

    def graph_communities(self):
        return self.graph.communities()

    # ── Temporal ─────────────────────────────────────────────

    def rising_topics(self, top_n: int = 10) -> list[dict]:
        return self.temporal.rising_entities(top_n=top_n)

    def monthly_focus(self, year_month: Optional[str] = None) -> dict:
        return self.temporal.monthly_activity(year_month=year_month)

    def trend_report(self) -> dict:
        return self.temporal.trend_summary()

    # ── Knowledge Gaps → Goals ───────────────────────────────

    def knowledge_gaps(self) -> dict:
        return self.gaps.analyze()

    def gap_driven_goals(self, max_goals: int = 10) -> list[dict]:
        """Generate RSIS3 goals from knowledge gaps."""
        return self.gaps.to_goals(max_goals=max_goals)

    # ── Health ───────────────────────────────────────────────

    def status(self) -> dict:
        """Check memory subsystem health."""
        return {
            'wiki_path': str(self._wiki),
            'vectors': self._safe_vector_count(),
            'entities': len(list(self._wiki.glob('entities/*.md'))),
            'sessions': len(list(self._wiki.glob('sessions/*.md'))),
            'decisions': len(list(self._wiki.glob('decisions/*.md'))),
            'daily_notes': len(list(self._wiki.glob('daily/*.md'))),
            'identity_snapshots': len(list(self._wiki.glob('identity/*.md'))),
            'pulse_memories': self.experiences.count(),
            'graph_nodes': self.graph.count_nodes(),
            'graph_edges': self.graph.count_edges(),
        }

    def _safe_vector_count(self) -> int:
        try:
            return self.semantic.count()
        except Exception:
            return 0

    @staticmethod
    def _default_wiki() -> Path:
        """Resolve mykb/wiki relative to the memory_bridge package."""
        return resolve_wiki_path()


    # Pulse Memory (Experience Memory)
    def store_pulse_memory(self, pulse_data: dict) -> str:
        return self.experiences.store_pulse(pulse_data)

    def retrieve_similar_pulses(self, query: str, top_k: int = 5) -> list[dict]:
        return self.experiences.retrieve_similar_pulses(query, top_k=top_k)

    def recent_pulses(self, limit: int = 5) -> list[dict]:
        return self.experiences.recent_pulses(limit=limit)

    # Reflection
    def reflect(self, context: Optional[dict] = None) -> dict:
        return self.reflection.reflect(context=context)

    def reflection_goals(self) -> list[dict]:
        return self.reflection.reflect().get('meta_goals', [])

    # Experiments
    def create_experiment(self, hypothesis: str, control_desc: str,
                           treatment_desc: str, metric: str = 'pass_rate',
                           min_samples: int = 5) -> str:
        return self.experiments.create_experiment(
            hypothesis, control_desc, treatment_desc, metric, min_samples)

    def record_experiment_result(self, experiment_id: str, variant: str,
                                  metrics: dict, sample_size: int = 1) -> dict:
        return self.experiments.record_result(experiment_id, variant, metrics, sample_size)

    def conclude_experiment(self, experiment_id: str) -> dict:
        return self.experiments.conclude_experiment(experiment_id)

    # Meta-Learning
    def analyze_meta_learning(self) -> dict:
        return self.meta_learning.analyze()

    def get_parameter_updates(self) -> list[dict]:
        return self.meta_learning.get_parameter_updates()

    # Executive Planner
    def create_plan(self, title: str, goal_id: str,
                     horizon: str = 'medium',
                     steps: Optional[list[dict]] = None):
        return self.planner.create_plan(title, goal_id, horizon, steps)

    def get_next_plan_step(self, plan_id: str):
        return self.planner.next_step(plan_id)

    def complete_plan_step(self, plan_id: str, step_id: str):
        return self.planner.complete_step(plan_id, step_id)

    def get_active_plans(self) -> list[dict]:
        return self.planner.list_active_plans()

def _slugify(text: str, max_len: int = 60) -> str:
    import re
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:max_len]
