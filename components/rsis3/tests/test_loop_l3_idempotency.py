"""L3 — redundancy flagging must be idempotent and bounded."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import CONFIG
from rsis.loop_l3 import L3EvolutionLoop
from rsis.memory import MemoryManager


class RecordTelemetry:
    def __init__(self):
        self.events = []

    def record(self, event):
        self.events.append(event)


def make_loop(tmp_path, monkeypatch):
    monkeypatch.setattr(CONFIG.memory, "knowledge_graph_path",
                        str(tmp_path / "kg.json"))
    monkeypatch.setattr(CONFIG.memory, "vector_store_path",
                        str(tmp_path / "vectors"))
    memory = MemoryManager(str(tmp_path))
    loop = L3EvolutionLoop(telemetry=RecordTelemetry(), memory=memory)
    return loop, memory


def seed_redundant_pair(memory: MemoryManager) -> None:
    # >3 improvements on the same file with >0.5 description overlap.
    for i in range(4):
        memory.kg.add_node(
            f"improvement-{i}", "improvement",
            description=f"Add retry with backoff to BatchRunner in "
                        f"rsis/batch.py (v{i})",
            target_files=["rsis/batch.py"],
        )


def test_flagging_is_idempotent(tmp_path, monkeypatch):
    loop, memory = make_loop(tmp_path, monkeypatch)
    seed_redundant_pair(memory)

    first = loop._refine_redundancies()
    assert first == 6  # all pairwise pairs flagged on the first pass
    edges_after_first = memory.kg.edge_count

    second = loop._refine_redundancies()
    assert second == 0
    assert memory.kg.edge_count == edges_after_first


def test_flagging_is_capped(tmp_path, monkeypatch):
    loop, memory = make_loop(tmp_path, monkeypatch)
    for i in range(5):
        memory.kg.add_node(
            f"improvement-{i}", "improvement",
            description=f"Add retry with backoff to rsis/batch.py {i}",
            target_files=["rsis/batch.py"],
        )
    monkeypatch.setattr(loop.config, "max_redundancy_flags_per_cycle", 2)
    assert loop._refine_redundancies() == 2


def test_save_collapses_identical_parallel_edges(tmp_path, monkeypatch):
    monkeypatch.setattr(CONFIG.memory, "knowledge_graph_path",
                        str(tmp_path / "kg.json"))
    monkeypatch.setattr(CONFIG.memory, "vector_store_path",
                        str(tmp_path / "vectors"))
    memory = MemoryManager(str(tmp_path))
    memory.kg.add_node("a", "insight", description="x")
    memory.kg.add_node("b", "improvement", description="y")
    memory.kg.graph.add_edge("a", "b", rel="flags_as_redundant")
    memory.kg.graph.add_edge("a", "b", rel="flags_as_redundant")
    memory.kg.save()

    reloaded = MemoryManager(str(tmp_path))
    assert reloaded.kg.edge_count == 1


def test_save_prunes_stale_redundancy_flag_edges(tmp_path, monkeypatch):
    monkeypatch.setattr(CONFIG.memory, "knowledge_graph_path",
                        str(tmp_path / "kg.json"))
    monkeypatch.setattr(CONFIG.memory, "vector_store_path",
                        str(tmp_path / "vectors"))
    memory = MemoryManager(str(tmp_path))
    for i in range(3):
        memory.kg.add_node(f"imp-{i}", "improvement", description=f"x {i}")
    memory.kg.add_node(
        "redundancy-1-0", "insight",
        description="dup", file="a.py", similarity=0.9,
        improvement_ids=["imp-0", "imp-1"],
    )
    memory.kg.add_edge("redundancy-1-0", "imp-0", rel="flags_as_redundant")
    memory.kg.add_edge("redundancy-1-0", "imp-1", rel="flags_as_redundant")
    memory.kg.add_edge("redundancy-1-0", "imp-2", rel="flags_as_redundant")  # stale
    memory.kg.save()
    reloaded = MemoryManager(str(tmp_path))
    flag_edges = [e for e in reloaded.kg.get_edges()
                  if e["rel"] == "flags_as_redundant"]
    assert len(flag_edges) == 2
    assert {e["target"] for e in flag_edges} == {"imp-0", "imp-1"}
