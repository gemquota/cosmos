---
type: "concept"
title: "Semantic Networks"
description: "Graphs of concepts connected by labeled relations, used in cognition and computing"
tags: ["semantic-networks", "graphs", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Semantic_network", "https://dictionary.apa.org/semantic-network"]
---

# Semantic Networks

## Summary

Semantic Networks — Graphs of concepts connected by labeled relations, used in cognition and computing.

## Details

- Semantic networks represent knowledge as nodes (concepts) and labeled edges (relations such as is-a, part-of, causes). Collins and Quillian's cognitive model proposed hierarchical storage with cognitive economy — properties stored at the highest applicable node — later revised as spreading-activation theory.
- Empirical support: semantic priming (doctor primes nurse), category-size effects, and the fan effect (more links slow verification) shaped both psychology and AI knowledge representation. Modern knowledge graphs operationalize the same idea at web scale.
- Worked example: 'sparrow is-a bird; bird has-a wings; bird can fly' — a query engine inherits fly from bird to sparrow unless a specific edge blocks it (penguin).
- Computational forms range from RDF triples and OWL ontologies to graph databases and embedding-based graph neural networks. Spreading activation is also the conceptual ancestor of retrieval in vector databases.
- mykb relevance: wikilinks plus frontmatter create a semantic network; community detection and backlinks are spreading-activation-style traversal.

## Related

- [[wiki/memory/knowledge-representation|Knowledge Representation]] — formal context
- [[wiki/memory/ontology-design-principles|Ontology Design Principles]] — schema layer
- [[wiki/memory/semantic-prospection|Semantic Prospection]] — semantic memory use
- [[wiki/memory/concept-mapping|Concept Mapping]] — human-facing graphs
- [[wiki/memory/backlinks-research|Backlinks Research]] — graph navigation
- [[wiki/concepts/bayesian-networks|Bayesian Networks]] — existing wiki article
