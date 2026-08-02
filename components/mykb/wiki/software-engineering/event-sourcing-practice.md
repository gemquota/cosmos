---
type: "concept"
title: "Event Sourcing Practice"
description: "Storing state as an append-only log of events instead of current rows"
tags: ["event-sourcing", "events", "architecture", "audit"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event Sourcing Practice

## Summary
Event sourcing persists every state change as an immutable event and derives current state by replay. The event log is the source of truth — giving perfect audit, temporal queries, and rebuildable projections, at the cost of complexity.

## Details
- Append-only store: events are facts; state is a projection you can rebuild from zero.
- Snapshots bound replay cost; projection idempotency makes rebuilds safe.
- Schema evolution of events is harder than table migrations — version every event.
- mykb relevance: the wiki link-graph could replay ArticleCreated events to rebuild indexes.

## Related
- [[wiki/software-engineering/projections|Event Sourcing Practice]]
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/api-protocols/event-sourcing|Event Sourcing]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
