---
type: "concept"
title: "Triplestore"
description: "Database optimized for storing and querying RDF triples"
tags: ["triplestore", "rdf", "database", "semantic-web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Triplestore", "https://www.w3.org/TR/rdf11-primer/"]
---

# Triplestore

## Summary
A triplestore is a database whose storage and indexes are designed around RDF triples, with SPARQL as its query interface. It is the standard engine behind large public knowledge graphs.

## Details
- **Indexing** — six permutations of (subject, predicate, object) or compressed alternatives support fast pattern joins.
- **Products** — Virtuoso, Jena TDB, Blazegraph, GraphDB; embedded options exist for small graphs.
- **Agent relevance** — mykb's NetworkX graph is an in-memory triplestore of co-occurrence edges; a formal store would add persistence and SPARQL.
- A triplestore is a database purpose-built for storing and querying RDF triples, indexed for graph patterns rather than relational joins.
- It answers SPARQL queries efficiently and often adds inference (reasoning) over the stored triples.
- Triplestores trade relational rigidity for flexibility: any statement can be added at any time, but validation and aggregation require discipline.
- They are the storage engine of choice for knowledge graphs, catalogs, and linked-data applications.
- **Worked example / comparison** — Comparison — a triplestore queries relationships natively but struggles with the numeric and transactional workloads a relational database handles well; the choice follows the data's shape.
- For mykb, the triplestore is documented as the RDF-native storage option, contrasted with property-graph databases.

## Related
- [[wiki/data-storage/rdf|RDF]]
- [[wiki/data-storage/sparql|SPARQL]]
- [[wiki/data-storage/property-graph|Property Graph]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/data-storage/00-index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
