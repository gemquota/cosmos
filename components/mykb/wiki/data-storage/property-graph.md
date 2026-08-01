---
type: "concept"
title: "Property Graph"
description: "Graph data model with typed nodes, edges, and properties on both"
tags: ["property-graph", "graph-database", "neo4j", "model"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Property Graph

## Summary
A property graph stores nodes and edges that both carry key-value properties, with optional types and labels. It favors traversal and operational workloads over formal semantics, and is the model behind Neo4j and most product graphs.

## Details
- **Features** — labels on nodes, relationship types and direction, arbitrary properties, and index-backed lookups.
- **Query** — Cypher-style pattern traversal; paths are first-class results.
- **Contrast** — property graphs are flexible but schema-less; RDF is strict and standards-based; both can represent the same facts.

## Related
- [[wiki/data-storage/triplestore|Triplestore]] — the RDF alternative to property graphs
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — property graphs are a KG storage option
- [[wiki/memory/graph-notes|Graph Notes]] — note graphs are informal property graphs
- [[wiki/meta-learning/node2vec|Node2Vec]] — learns embeddings from property-graph structure
- [[wiki/data-storage/index|Data Storage]] — graph storage family
