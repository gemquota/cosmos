---
type: "concept"
title: "Ontology Design"
description: "Modeling a domain's concepts, types, and relations into a formal, shareable schema"
tags: ["ontology", "schema", "knowledge-representation", "semantics", "design"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Ontology_(information_science)"]
---

# Ontology Design

## Summary
Ontology design defines the vocabulary of a domain: its classes, properties, and constraints. A well-designed ontology lets different systems share meaning, while an over-engineered one collapses under its own weight. Knowledge graphs need some ontology to be queryable, and mykb's typed wiki (concepts, sources, syntheses) is a lightweight ontology in practice.

## Details
- **Components** — classes (types), properties (relations and attributes), individuals (instances), and axioms (constraints such as disjointness).
- **Design trade-off** — top-down ontologies (formal, reusable, slow to build) vs bottom-up folksonomies (cheap, messy); most practical systems sit between, refining schema from observed usage.
- **Patterns** — naming conventions, `is-a` vs `part-of` distinctions, and avoiding deep inheritance hierarchies keep ontologies usable.
- **Worked example** — mykb uses `type: concept|synthesis|source|decision|pulse`; adding a `relation` type would let edges carry semantics ('cites', 'contradicts').
- **Formats** — RDF/OWL for formal ontologies; YAML frontmatter plus conventions for pragmatic ones like mykb.

## Related
- [[wiki/memory/taxonomy|Taxonomy]] — a single-hierarchy scheme ontologies generalize
- [[wiki/memory/folksonomy|Folksonomy]] — the bottom-up alternative to formal ontology
- [[wiki/data-storage/rdf|RDF]] — the data model formal ontologies are written in
- [[wiki/data-storage/json-ld|JSON-LD]] — JSON serialization for ontology-linked data
- [[wiki/data-storage/sparql|SPARQL]] — querying data structured by an ontology
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph an ontology schematizes
- [[wiki/data-storage/00-index|Data Storage]] — the storage-tech namespace for ontologies
- [[wiki/concepts/triad-architecture|Triad Architecture]] — mykb's typing scheme in the triad context
