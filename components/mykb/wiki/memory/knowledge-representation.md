---
type: "concept"
title: "Knowledge Representation"
description: "Formal schemes — logic, graphs, frames, vectors — for encoding knowledge in systems"
tags: ["representation", "knowledge", "AI"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning", "https://en.wikipedia.org/wiki/Knowledge_representation"]
---

# Knowledge Representation

## Summary

Knowledge Representation — Formal schemes — logic, graphs, frames, vectors — for encoding knowledge in systems.

## Details

- Knowledge representation (KR) is the field of encoding knowledge so a system can reason with it. Major schemes include logical formulas, semantic networks and graphs, frames and slots, production rules, and distributed vector embeddings; each trades expressiveness against computational cost and learnability.
- Key desiderata (Davis, Shrobe & Szolovits): a representation must stand for the world, support inference, be efficient, and be acquirable. Ontologies supply the vocabulary; knowledge graphs supply the instances.
- Worked example: representing 'Anki uses SM-2' as a triple (anki, uses, SM-2) in a semantic network lets a query engine traverse to related algorithms, while a frame adds slots like 'scheduler family' and 'default intervals'.
- Neural embeddings complement symbolic KR: they capture similarity without explicit structure but resist explanation and precise inference. Hybrid systems increasingly combine both.
- mykb relevance: the wiki is a lightweight KR system — typed frontmatter plus wikilinks form the ontology and the graph.

## Related

- [[wiki/memory/semantic-networks|Semantic Networks]] — graph-based scheme
- [[wiki/memory/ontology-design-principles|Ontology Design Principles]] — vocabulary discipline
- [[wiki/concepts/frames-and-slots|Frames and Slots]] — structured scheme
- [[wiki/memory/knowledge-integration|Knowledge Integration]] — combining representations
- [[wiki/memory/knowledge-articulation|Knowledge Articulation]] — adjacent stub in this cluster
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — existing wiki article
- [[wiki/memory/knowledge-capture|Knowledge Capture]] — existing wiki article
