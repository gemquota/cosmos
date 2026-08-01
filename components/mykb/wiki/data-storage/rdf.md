---
type: "concept"
title: "RDF"
description: "W3C data model representing facts as subject-predicate-object triples"
tags: ["rdf", "linked-data", "triples", "semantic-web"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# RDF

## Summary
RDF (Resource Description Framework) models every fact as a triple: subject, predicate, object, each identified by an IRI. It is the foundation of the semantic web and of interoperable knowledge graphs.

## Details
- **Triples** — `(Alice, wrote, paperX)`; many triples form a graph of IRIs with literals as leaves.
- **Standards** — RDF 1.1, serialized as Turtle, JSON-LD, or RDF/XML; queried with SPARQL.
- **Agent relevance** — a formal export of mykb's links as triples would let RSIS3 run standard graph queries over its memory.

## Related
- [[wiki/data-storage/triplestore|Triplestore]] — the database built for RDF triples
- [[wiki/data-storage/sparql|SPARQL]] — the query language for RDF graphs
- [[wiki/data-storage/json-ld|JSON-LD]] — JSON serialization of RDF
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — RDF is a common KG data model
- [[wiki/memory/ontology-design|Ontology Design]] — ontologies constrain RDF vocabularies
- [[wiki/data-storage/index|Data Storage]] — linked-data storage family
