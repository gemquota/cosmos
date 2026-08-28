"""KG robustness — edge-case loading, rel vocabulary, atomic saves, batching."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import CONFIG
from rsis.memory import MemoryManager


def make_memory(tmp_path, monkeypatch):
    monkeypatch.setattr(CONFIG.memory, "knowledge_graph_path",
                        str(tmp_path / "kg.json"))
    monkeypatch.setattr(CONFIG.memory, "vector_store_path",
                        str(tmp_path / "vectors"))
    return MemoryManager(str(tmp_path))


def test_load_skips_malformed_edges_and_nodes(tmp_path, monkeypatch):
    kg_path = tmp_path / "kg.json"
    kg_path.write_text(json.dumps({
        "nodes": [
            {"id": "ok", "attrs": {"type": "insight"}},
            {"attrs": {"type": "insight"}},          # no id
            "garbage",
        ],
        "edges": [
            {"source": "ok", "target": "ok", "rel": "led_to"},
            {"source": "ok", "rel": "led_to"},        # no target
            {"source": "ok", "target": "ok"},         # no rel
            "garbage",
        ],
    }))
    mem = make_memory(tmp_path, monkeypatch)
    assert mem.kg.node_count == 1
    assert mem.kg.edge_count == 1


def test_unknown_rel_warns(tmp_path, monkeypatch, caplog):
    import logging
    from rsis.memory import KnowledgeGraph
    monkeypatch.setattr(CONFIG.memory, "knowledge_graph_path",
                        str(tmp_path / "kg.json"))
    kg = KnowledgeGraph(str(tmp_path / "kg.json"))
    with caplog.at_level(logging.WARNING, logger="rsis.memory"):
        kg.add_edge("a", "b", rel="totally_unknown")
    assert any("Unknown relationship type" in r.message for r in caplog.records)


def test_save_is_atomic(tmp_path, monkeypatch):
    mem = make_memory(tmp_path, monkeypatch)
    mem.kg.add_node("a", "insight", description="x")
    mem.kg.add_node("b", "improvement", description="y")
    mem.kg.add_edge("a", "b", rel="led_to")
    # Mutation methods now batch (O1) — save() is explicit
    mem.kg.save()
    assert not (tmp_path / "kg.json.tmp").exists()
    data = json.loads((tmp_path / "kg.json").read_text())
    assert len(data["edges"]) == 1


def test_add_edges_batches(tmp_path, monkeypatch):
    mem = make_memory(tmp_path, monkeypatch)
    mem.kg.add_node("src", "insight", description="s", improvement_ids=["t1", "t2"])
    mem.kg.add_node("t1", "improvement", description="t1")
    mem.kg.add_node("t2", "improvement", description="t2")
    mem.kg.add_edges("src", "flags_as_redundant", ["t1", "t2"])
    assert mem.kg.edge_count == 2
    edges = mem.kg.get_edges("src")
    assert {e["target"] for e in edges} == {"t1", "t2"}
