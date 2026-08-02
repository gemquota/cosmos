---
type: "concept"
title: "Ontology Design Principles"
description: "Guidelines for building clean, usable concept and relation vocabularies"
tags: ["ontology", "design", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Ontology_(information_science)", "https://www.w3.org/OWL/"]
---

# Ontology Design Principles

## Summary

Ontology Design Principles — Guidelines for building clean, usable concept and relation vocabularies.

## Details

- An ontology is an explicit specification of a conceptualization: classes, properties, relations, and constraints. Design principles cluster around clarity (unambiguous names and definitions), coherence (logical consistency), extensibility (new concepts fit without rework), and minimal encoding bias (form follows content, not the tool).
- Practical guidance from ontology engineering: reuse existing vocabularies, prefer composition over subclass explosion, keep is-a hierarchies strict, document every class, and test with competency questions the ontology must answer.
- Worked example: a wiki ontology might define type: concept | synthesis | question | episode; a competency question — 'list all syntheses citing spaced repetition' — forces the needed relation and property design.
- Anti-patterns: synonym sprawl, deep brittle hierarchies, and mixing taxonomies with instance data. Ontologies are living artifacts: they should change with the knowledge they organize.
- mykb relevance: mykb's frontmatter types, tags, and link conventions are a deliberately small ontology — this page applies the same discipline.

## Related

- [[wiki/memory/semantic-networks|Semantic Networks]] — the graph ontologies govern
- [[wiki/memory/taxonomy|Taxonomy]] — hierarchical subset
- [[wiki/memory/knowledge-representation|Knowledge Representation]] — formal basis
- [[wiki/memory/ontology-design|Ontology Design]] — existing mykb article
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — living maintenance
- [[wiki/meta-learning/friction-design|Friction Design]] — adjacent stub in this cluster
- [[wiki/concepts/arousal-and-performance|Arousal and Performance]] — adjacent stub in this cluster
