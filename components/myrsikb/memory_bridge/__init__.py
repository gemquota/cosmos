"""memory_bridge — RSIS3 ↔ mykb integration layer.

RSIS3's cognitive architecture delegates all long-term knowledge
storage, retrieval, and graph operations to mykb through this package.

Usage::

    from memory_bridge import MemoryClient

    kb = MemoryClient()
    kb.store_identity_snapshot(1, {...})
    results = kb.search("crisis recovery")
    goals = kb.gap_driven_goals()
"""

from memory_bridge.client import MemoryClient
from memory_bridge.wiki_writer import WikiWriter
from memory_bridge.knowledge_graph import KnowledgeGraph
from memory_bridge.vector_search import SemanticMemory
from memory_bridge.temporal_memory import TemporalMemory
from memory_bridge.gap_detector import GapDetector



# Re-export all subsystems — new subsystems are accessible directly or via MemoryClient
from memory_bridge.experience_memory import ExperienceMemory
from memory_bridge.reflection import ReflectionEngine
from memory_bridge.experiment import ExperimentManager
from memory_bridge.meta_learning import MetaLearningEngine
from memory_bridge.planner import ExecutivePlanner
from memory_bridge.telemetry_writer import TelemetryWriter

__all__ = [
    'MemoryClient',
    'WikiWriter',
    'KnowledgeGraph',
    'SemanticMemory',
    'TemporalMemory',
    'GapDetector',
    'ExperienceMemory',
    'ReflectionEngine',
    'ExperimentManager',
    'MetaLearningEngine',
    'ExecutivePlanner',
    'TelemetryWriter',
]
