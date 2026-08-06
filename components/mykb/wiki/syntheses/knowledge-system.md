---
type: synthesis
title: "Knowledge System Overview"
status: growing
created: 2026-07-20
updated: 2026-07-20
tags: [meta, workflow, curation]
---
## Knowledge System
# Knowledge System Overview
## Core Loop
```text
raw/inbox → wiki/sources → wiki/concepts → wiki/syntheses → wiki/index + log
```
## The Four Operations
| Phase | Action | Output |
|---|---|---|
| **Capture** | Drop raw material into `raw/inbox/` | Unprocessed notes, links, clippings |
| **Process** | Create source pages in `wiki/sources/` | Structured notes with provenance |
| **Connect** | Extract concepts, questions, projects | Linked knowledge nodes |
| **Synthesize** | Cross-source synthesis | Conclusions, frameworks, insights |
## Agent Integration
The LLM wiki daemon auto-extracts sessions into entities, decisions, and concepts. Manual curation enriches the auto-extracted content with proper definitions, context, and cross-links.
## Health Checks
- `okf validate .` — OKF conformance
- `okf lint .` — curation quality report
- Review isolated pages (`wiki/` files with no backlinks)
- Review stale questions in `wiki/questions/open-questions.md`
**Domain:** Syntheses
## Related
- [[wiki/syntheses/README|Readme]]
- [[wiki/syntheses/weekly-review|Weekly Review]]
## 2026-07 Acquisition Round
The [knowledge acquisition](../../ops/knowledge-acquisition.md) round of 2026-07 added
400 articles (100 full + 300 stubs) across four clusters: agent architectures,
knowledge & memory systems, LLM engineering, and semantic infrastructure.
Key conclusions:
- **Memory is retrieval-shaped** — the design of a knowledge base follows the
  [[wiki/data-storage/retrieval-augmented-generation|RAG]] lifecycle: capture,
  chunk, embed, index, retrieve, synthesize (see
  [[wiki/data-storage/semantic-search|semantic search]] and
  [[wiki/data-storage/hybrid-search|hybrid search]]).
- **Linking is modelling** — the [[wiki/data-storage/knowledge-graph|knowledge]]
  graph]] is emergent from markdown links; curation is mostly link repair
  ([[wiki/memory/knowledge-curation|knowledge curation]]).
- **Stubs are a queue** — 300 stubs (`status: stub`) are the expansion
  backlog, prioritized by retrieval value rather than novelty.
