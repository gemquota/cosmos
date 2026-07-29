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
