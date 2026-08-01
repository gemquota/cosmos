---
type: "concept"
title: "Triplestore"
description: "Database optimized for storing and querying RDF triples"
tags: ["triplestore", "rdf", "database", "semantic-web"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Triplestore

## Summary
A triplestore is a database whose storage and indexes are designed around RDF triples, with SPARQL as its query interface. It is the standard engine behind large public knowledge graphs.

## Details
- **Indexing** — six permutations of (subject, predicate, object) or compressed alternatives support fast pattern joins.
- **Products** — Virtuoso, Jena TDB, Blazegraph, GraphDB; embedded options exist for small graphs.
- **Agent relevance** — mykb's NetworkX graph is an in-memory triplestore of co-occurrence edges; a formal store would add persistence and SPARQL.

## Related
- [[wiki/data-storage/rdf|RDF]] — the triple model the store persists
- [[wiki/data-storage/sparql|SPARQL]] — the query language of triplestores
- [[wiki/data-storage/property-graph|Property Graph]] — the alternative labelled-graph model
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — triplestores host knowledge graphs
- [[wiki/data-storage/index|Data Storage]] — database technologies
