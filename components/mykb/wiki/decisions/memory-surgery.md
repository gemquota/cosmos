---
type: "decision"
title: "Memory Surgery"
description: "Deliberately editing an AI system's stored knowledge or memories"
tags: ["memory", "editing", "safety", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Memory_consolidation", "https://en.wikipedia.org/wiki/Long-term_memory"]
---

# Memory Surgery

## Summary
Memory surgery is the deliberate, targeted editing of an AI system's stored knowledge — deleting harmful facts, correcting outdated beliefs, or removing traumatic episodes. Knowledge-editing research shows this is technically possible (and error-prone) in LLMs and agent memory stores.

## Details
- **Levels** — weight-level edits (knowledge editing), retrieval-level edits (vector store updates), and episodic-memory curation.
- **Safety uses** — removing hazardous knowledge, correcting misconceptions, and unlearning private data.
- **Risks** — collateral damage to nearby knowledge, memory inconsistency, and the edited system hiding its edits.
- **Evidence** — editing models on factual pairs often degrades unrelated facts; localization methods reduce but don't eliminate side effects.
- **RSIS3 parallel** — mykb curation (archiving junk entities, pruning dead links) is memory surgery on the knowledge graph.

## Related
- [[wiki/memory/memory-consolidation|Memory Consolidation]] — the memory substrate
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]] — graph-level surgery
- [[wiki/concepts/model-tampering|Model Tampering]] — the adversarial mirror
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — rollback for surgery
- [[wiki/concepts/training-data-memorization|training-data-memorization]] — removal technique
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — curation practice
