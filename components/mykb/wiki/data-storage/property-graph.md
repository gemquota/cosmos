---
type: "concept"
title: "Property Graph"
description: "Graph data model with typed nodes, edges, and properties on both"
tags: ["property-graph", "graph-database", "neo4j", "model"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Graph_database", "https://neo4j.com/docs/getting-started/", "https://neo4j.com/developer/graph-database/"]
---

# Property Graph

## Summary
A property graph stores nodes and edges that both carry key-value properties, with optional types and labels. It favors traversal and operational workloads over formal semantics, and is the model behind Neo4j and most product graphs.

## Details
- **Features** — labels on nodes, relationship types and direction, arbitrary properties, and index-backed lookups.
- **Query** — Cypher-style pattern traversal; paths are first-class results.
- **Contrast** — property graphs are flexible but schema-less; RDF is strict and standards-based; both can represent the same facts.
- A property graph stores entities (nodes) and relationships (edges), each able to carry arbitrary key-value properties.
- Unlike RDF, edges are first-class citizens with identity and properties, and the model is usually schema-optional with indexes.
- Query languages like Cypher and Gremlin traverse the graph directly, which makes path-based questions natural.
- Property graphs are the model behind most graph databases (Neo4j, Amazon Neptune) and fit domain models where relationships are the core value.
- **Worked example / comparison** — Worked example — the wiki's link graph is a property graph: articles are nodes with title and status properties, wikilinks are edges with a 'why' property from the Related annotation.
- For mykb, property-graph is documented as the model the wiki's own graph tooling would use, in contrast to the RDF/triplestore family.

- Fit for the wiki: articles, statuses, and 'why' annotations map naturally onto nodes, properties, and typed edges, which is why the model fits the corpus's retrieval needs.
- Model rationale: property graphs favor traversal and operational workloads, while RDF suits strict, standards-based semantics; the wiki's documented model is the property graph, in contrast to the triplestore family.
- Graph tooling intent: the wiki's own graph tooling would use the property-graph model, with each wikilink carrying a 'why' property from the Related annotation, so traversal-based queries stay natural.
- Limits: schema-optional models need index and validation discipline, so the graph should be checked for missing or malformed properties on the same cadence as other corpus invariants.
## Related
- [[wiki/data-storage/triplestore|Triplestore]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/memory/graph-notes|Graph Notes]]
- [[wiki/meta-learning/node2vec|Node2Vec]]
- [[wiki/data-storage/00-index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
