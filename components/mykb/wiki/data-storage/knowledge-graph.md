---
type: "concept"
title: "Knowledge Graph"
description: "Graph-structured store of entities and relationships that supports semantic query and retrieval"
tags: ["knowledge-graph", "semantic", "retrieval", "ontology", "graph"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Knowledge_graph"]
---

# Knowledge Graph

## Summary
A knowledge graph (KG) stores entities and their relationships as typed nodes and edges, giving machines a structured model of a domain. It matters because it enables fact-grounded queries, entity linking, and explainable retrieval that flat text cannot provide. In the mykb ecosystem the co-occurrence graph and entity extraction feed RSIS3's planning loop.

## Details
- **Shape** — nodes are entities (people, concepts, files) and edges are typed relations such as `is-a`, `part-of`, or `cites`; each triple is a fact (subject-predicate-object).
- **Schema** — ontologies or lightweight taxonomies define allowed types and relations, while schema-lite KGs (like mykb's NetworkX graph) infer structure from co-occurrence.
- **Storage** — RDF triplestores and property graphs are the two main engines; the choice trades standards (SPARQL, RDF) against traversal speed and flexibility.
- **Retrieval role** — KGs complement vector search: vectors find semantically similar text, KGs ground answers in explicit facts and support multi-hop reasoning such as 'who authored the papers citing this concept?'.
- **Worked example** — mykb extracts entities from notes into `wiki/entities/`; the graph engine detects communities (clusters) and the backlink engine follows incoming links to surface related memories for RSIS3.
- **Comparison** — vector store = fuzzy similarity over dense embeddings; KG = exact relational structure; hybrid systems (GraphRAG) use both.

## Related
- [[wiki/data-storage/rdf|RDF]] — the standard triple data model behind many knowledge graphs
- [[wiki/data-storage/triplestore|Triplestore]] — a storage engine purpose-built for RDF triples
- [[wiki/data-storage/property-graph|Property Graph]] — the labelled-graph alternative to triple storage
- [[wiki/memory/ontology-design|Ontology Design]] — defines the schema a knowledge graph instantiates
- [[wiki/data-storage/semantic-search|Semantic Search]] — retrieval that leverages graph structure and meaning
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the practice that keeps graph entities clean
- [[wiki/concepts/triad-architecture|Triad Architecture]] — mykb's graph engine serves RSIS3 within the triad
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the capture-process-connect-synthesize loop that feeds the graph
