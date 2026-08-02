---
type: "concept"
title: "RDF"
description: "W3C data model representing facts as subject-predicate-object triples"
tags: ["rdf", "linked-data", "triples", "semantic-web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/RDF/", "https://www.w3.org/TR/rdf11-primer/"]
---

# RDF

## Summary
RDF (Resource Description Framework) models every fact as a triple: subject, predicate, object, each identified by an IRI. It is the foundation of the semantic web and of interoperable knowledge graphs.

## Details
- **Triples** — `(Alice, wrote, paperX)`; many triples form a graph of IRIs with literals as leaves.
- **Standards** — RDF 1.1, serialized as Turtle, JSON-LD, or RDF/XML; queried with SPARQL.
- **Agent relevance** — a formal export of mykb's links as triples would let RSIS3 run standard graph queries over its memory.
- The Resource Description Framework (RDF) is the W3C standard for describing resources as subject-predicate-object triples.
- Triples form a directed labeled graph, and every node is identified by an IRI (or is a literal), which makes the graph globally addressable.
- RDF is schema-flexible by design: statements can be added without migrating a table, at the cost of validation discipline.
- It is the substrate under SPARQL querying, triplestores, and the linked-data web.
- **Worked example / comparison** — Worked example — the triple (mykb:circuit-breaker, rdfs:seeAlso, mykb:retry-backoff) records a relationship the graph can traverse and query.
- For mykb, RDF is documented as the abstract graph model that triplestores and SPARQL implement.

## Related
- [[wiki/data-storage/triplestore|Triplestore]]
- [[wiki/data-storage/sparql|SPARQL]]
- [[wiki/data-storage/json-ld|JSON-LD]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/memory/ontology-design|Ontology Design]]
- [[wiki/data-storage/index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
