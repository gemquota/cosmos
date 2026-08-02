---
type: "concept"
title: "Projections"
description: "Read-optimized views derived from an event log or source of truth"
tags: ["projections", "event-sourcing", "read-models", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Projections

## Summary
Projections are derived views — a current-state table, a search index, a summary feed — built by folding events or source changes. They enable many read shapes from one write model and must be rebuildable.

## Details
- Each projection subscribes to events and updates incrementally; rebuild from the log on schema change.
- Projections are eventually consistent with the log — define and accept the lag.
- Idempotent projection logic is what makes replays safe.
- mykb relevance: the link-index and tag-cloud are projections over the article corpus.

## Related
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/event-sourcing-practice|Event Sourcing Practice]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/denormalization-practice|Denormalization Practice]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
