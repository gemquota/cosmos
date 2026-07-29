#!/usr/bin/env python3
"""KnowledgeGraph bridge — replaces RSIS3's KG with mykb's graph engine.

RSIS3's original ``src/tools/knowledge_graph.py`` stored nodes/edges as
flat JSON. This module wraps mykb's networkx-based co-occurrence graph
(``.wiki-daemon/graph_engine.py``) so RSIS3 gains community detection,
neighbourhood traversal, centrality analysis, and bridge detection.
"""

import json
import time
from pathlib import Path
from typing import Optional
from memory_bridge.mykb_loader import load_mykb_module


#  ── KnowledgeGraph (bridge) ────────────────────────────────────

class KnowledgeGraph:
    """RSIS3 Knowledge Graph backed by mykb's networkx co-occurrence graph.

    Maintains backward-compatible API with RSIS3's original KG while
    delegating to mykb's richer engine.

    Usage::

        kg = KnowledgeGraph()
        kg.create_node("imp-001", "improvement", "Improve crisis thresholds")
        kg.create_edge("goal-001", "imp-001", "produced")
        kg.record_improvement("imp-002", "goal-002", "…", "success")
    """

    def __init__(self, mykb_wiki: Optional[str | Path] = None):
        self._wiki_path = Path(mykb_wiki) if mykb_wiki else self._default_wiki()
        self._ge = None  # lazy import
        self._G = None   # networkx Graph cache
        self._titles = {}
        self._nodes: list[dict] = []
        self._edges: list[dict] = []

    # ── lazy init ─────────────────────────────────────────────

    @property
    def ge(self):
        if self._ge is None:
            self._ge = load_mykb_module('graph_engine')
        return self._ge

    # ── public API (matches RSIS3's original KG interface) ────

    def create_node(self, node_id: str, node_type: str, label: str,
                    metadata: Optional[dict] = None) -> dict:
        """Create a node in the graph (backed by mykb entity page)."""
        metadata = metadata or {}
        node = {
            'id': node_id,
            'type': node_type,
            'label': label,
            'metadata': metadata,
            'created_at': time.time(),
        }
        self._nodes.append(node)

        # Also write as a mykb entity
        from memory_bridge.wiki_writer import WikiWriter
        writer = WikiWriter(self._wiki_path)
        writer.write_entity(
            entity_id=node_id,
            title=label,
            description=metadata.get('description', ''),
            tags=[node_type] + metadata.get('tags', []),
            body=metadata.get('body', ''),
        )
        return node

    def create_edge(self, source_id: str, target_id: str,
                    rel: str, metadata: Optional[dict] = None) -> dict:
        """Create a typed relationship between two nodes.

        Also writes a concept link in the source entity's wiki page.
        """
        metadata = metadata or {}
        source_exists = any(n.get('id') == source_id for n in self._nodes)
        target_exists = any(n.get('id') == target_id for n in self._nodes)
        if not source_exists or not target_exists:
            raise ValueError(f"Node '{source_id}' or '{target_id}' not found")

        edge = {
            'source': source_id,
            'target': target_id,
            'rel': rel,
            'metadata': metadata,
            'created_at': time.time(),
        }
        self._edges.append(edge)

        from memory_bridge.wiki_writer import WikiWriter
        writer = WikiWriter(self._wiki_path)
        writer.write_concept_link(source_id, target_id, rel, metadata)
        return edge

    def record_improvement(self, improvement_id: str, goal_id: str,
                           description: str, outcome: str,
                           scores: Optional[dict] = None) -> tuple:
        """Record an improvement with its source goal."""
        goal_node = self.get_node(goal_id)
        if not goal_node:
            goal_node = self.create_node(goal_id, 'goal', description[:80], {
                'description': description, 'status': 'completed',
            })
        imp_node = self.create_node(improvement_id, 'improvement', description[:80], {
            'description': description, 'outcome': outcome, 'scores': scores or {},
        })
        edge = self.create_edge(goal_id, improvement_id, 'produced', {'outcome': outcome})
        return (imp_node, edge)

    # ── graph queries (delegated to mykb's graph engine) ──────

    def _ensure_graph(self):
        """Ensure mykb's co-occurrence graph is loaded."""
        if self._G is None:
            graph_path = self._wiki_path.parent / '.wiki-daemon' / 'graph.json'
            if graph_path.exists():
                G, titles = self.ge.load_graph(str(graph_path))
                self._G = G
                self._titles = titles

    def neighborhood(self, entity_id: str, hops: int = 2) -> list[dict]:
        """Get k-hop neighbourhood of an entity (uses mykb graph engine)."""
        self._ensure_graph()
        if self._G is None:
            return []
        return self.ge.neighborhood(self._G, entity_id, hops=hops)

    def shortest_path(self, entity_a: str, entity_b: str):
        """Shortest path between two entities (uses mykb graph engine)."""
        self._ensure_graph()
        if self._G is None:
            return None
        return self.ge.shortest_path(self._G, entity_a, entity_b)

    def central_entities(self, top_n: int = 20) -> list[dict]:
        """Most central entities by degree centrality."""
        self._ensure_graph()
        if self._G is None:
            return []
        return self.ge.central_entities(self._G, top_n=top_n)

    def bridge_entities(self, community_a: set, community_b: set) -> list[dict]:
        """Find bridge entities connecting two communities."""
        self._ensure_graph()
        if self._G is None:
            return []
        return self.ge.bridge_entities(self._G, community_a, community_b)

    def communities(self):
        """Detect communities using greedy modularity."""
        self._ensure_graph()
        if self._G is None:
            return []
        comms, _ = self.ge.detect_communities(self._G)
        return comms

    # ── standard RSIS3 KG queries ────────────────────────────

    def get_node(self, node_id: str) -> Optional[dict]:
        for n in self._nodes:
            if n.get('id') == node_id:
                return n
        return None

    def get_edges_for_node(self, node_id: str) -> list[dict]:
        return [
            e for e in self._edges
            if e.get('source') == node_id or e.get('target') == node_id
        ]

    def get_nodes_by_type(self, node_type: str) -> list[dict]:
        return [n for n in self._nodes if n.get('type') == node_type]

    def delete_node(self, node_id: str) -> bool:
        """Delete a node and all edges connected to it."""
        before = len(self._nodes)
        self._nodes = [n for n in self._nodes if n.get('id') != node_id]
        self._edges = [e for e in self._edges 
                       if e.get('source') != node_id and e.get('target') != node_id]
        return len(self._nodes) < before

    def delete_edge(self, edge_id: int) -> bool:
        """Delete an edge by index. The KnowledgeGraph bridge stores edges as a list,
        so ``edge_id`` is treated as the list index. For the mykb-backed bridge,
        this removes the edge from the in-memory list."""
        if 0 <= edge_id < len(self._edges):
            self._edges.pop(edge_id)
            return True
        return False

    def count_nodes(self) -> int:
        return len(self._nodes)

    def count_edges(self) -> int:
        return len(self._edges)

    def to_dict(self) -> dict:
        return {
            'version': '2.0-mykb',
            'nodes': self._nodes,
            'relationships': self._edges,
            'total_nodes_raw': len(self._nodes),
            'total_nodes_consolidated': len({n.get('id') for n in self._nodes}),
            'utility_density': round(
                len({n.get('id') for n in self._nodes}) / max(len(self._nodes), 1), 4
            ),
            'last_synced': time.time(),
        }

    @staticmethod
    def _default_wiki() -> Path:
        """Resolve the default mykb wiki path relative to this file."""
        return resolve_wiki_path()
