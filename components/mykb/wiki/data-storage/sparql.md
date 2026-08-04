---
type: "entity"
title: "SPARQL"
description: "Query language for RDF graphs, the SQL of the semantic web"
tags: ["sparql", "query", "rdf", "linked-data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/TR/sparql11-query/", "https://www.w3.org/TR/sparql11-overview/"]
---

# SPARQL

## Summary
SPARQL is the W3C query language for RDF data: pattern matching over triples with joins, filters, and optional clauses. It turns a triple store into an answerable knowledge graph.

## Details
- **Basics** — `SELECT ?s ?p ?o WHERE { ?s ?p ?o }` finds all triples; variables bind to nodes; `FILTER` and `OPTIONAL` refine patterns.
- **Power** — graph traversal (property paths), federated queries across endpoints, and inference over ontologies.
- **Agent relevance** — if mykb exported entities as RDF, SPARQL would answer relational questions ('which concepts cite this source?') directly.
- SPARQL is the W3C query language for RDF data, combining graph pattern matching with aggregation, filtering, and path traversal.
- A query is built from triple patterns with variables; the engine binds the variables to produce result sets or graphs.
- SPARQL supports inference-aware traversal, federated queries across endpoints, and update operations via SPARQL Update.
- Its power is querying relationships directly — following edges the way you think about knowledge — without joining tables.
- **Worked example / comparison** — Worked example — a SPARQL query asks for all concepts that link to both 'circuit-breaker' and 'retry-backoff' and returns the intersection in one pass.
- For mykb, SPARQL is documented as the query language for the RDF layer, the counterpart to graph traversals in property graphs.

## Related
- [[wiki/data-storage/rdf|RDF]]
- [[wiki/data-storage/triplestore|Triplestore]]
- [[wiki/data-storage/json-ld|JSON-LD]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/memory/ontology-design|Ontology Design]]
- [[wiki/data-storage/00-index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
