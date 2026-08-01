---
type: "concept"
title: "SPARQL"
description: "Query language for RDF graphs, the SQL of the semantic web"
tags: ["sparql", "query", "rdf", "linked-data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SPARQL

## Summary
SPARQL is the W3C query language for RDF data: pattern matching over triples with joins, filters, and optional clauses. It turns a triple store into an answerable knowledge graph.

## Details
- **Basics** — `SELECT ?s ?p ?o WHERE { ?s ?p ?o }` finds all triples; variables bind to nodes; `FILTER` and `OPTIONAL` refine patterns.
- **Power** — graph traversal (property paths), federated queries across endpoints, and inference over ontologies.
- **Agent relevance** — if mykb exported entities as RDF, SPARQL would answer relational questions ('which concepts cite this source?') directly.

## Related
- [[wiki/data-storage/rdf|RDF]] — the graph model SPARQL queries
- [[wiki/data-storage/triplestore|Triplestore]] — the engine SPARQL runs on
- [[wiki/data-storage/json-ld|JSON-LD]] — a serialization to load before querying
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the structure SPARQL explores
- [[wiki/memory/ontology-design|Ontology Design]] — ontology-driven query patterns
- [[wiki/data-storage/index|Data Storage]] — query technologies
