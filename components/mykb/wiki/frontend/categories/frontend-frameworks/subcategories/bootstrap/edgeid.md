---
type: "entity"
title: "EdgeId"
description: "EdgeId: stable identifiers for graph edges and connections"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "graph"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# EdgeId

## Summary

EdgeId is the bootstrap-cluster entity for stable edge identity in graph and node editors: the identifiers that let connections survive re-renders, saves, and edits. Stable IDs keep serialized graphs consistent and diffable. They matter because graph integrity depends on references that do not silently change. Edge identity is the same discipline as database primary keys: stable, unique, and never reused.

## Details

- **Definition** — An edge ID uniquely identifies a connection between two nodes across the editor's lifetime.
- **Stability** — IDs are assigned once and never reused, so references in saves, selections, and undo history stay valid.
- **Serialization** — Stable IDs make graphs serializable and diffable; regenerated IDs break diffs and external references.
- **Referential integrity** — Edges reference node IDs; orphaned edges point at deleted nodes and must be cleaned up.
- **Worked example** — A saved graph stores each edge with its ID and endpoints; re-importing preserves selections and history.
- **Failure modes** — Index-based identity breaks when nodes reorder; random IDs without collision handling corrupt saved graphs.
- **Practical relevance** — The same principle applies to wiki links: stable page names are edge IDs for the knowledge graph.
- **ID generation** — Monotonic or UUID identifiers avoid collisions when graphs merge from multiple sources.
- **Dangling edges** — Deleting a node must cascade to its edges, or validation must surface the orphans.
- **Import stability** — Re-importing a graph with stable IDs preserves references from external tools and annotations.
- **Diff tooling** — Stable IDs make graph diffs readable, so version control over graph documents becomes practical.
- **Cross-referencing** — External annotations and comments can point at edges by ID, surviving reorders and re-renders.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodeeditor|NodeEditor]] — the graph that edges connect
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodedefinitions|NodeDefinitions]] — node identity and types
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/noderenderer|NodeRenderer]] — rendering the connected graph
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/dimensions|Dimensions]] — geometry of edges
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/nodedefinitions|NodeDefinitions]] — node identity and types
