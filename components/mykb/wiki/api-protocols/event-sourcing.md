---
type: "concept"
title: "Event Sourcing"
description: "Persisting state as an immutable sequence of events that can be replayed to reconstruct any state"
tags: ["event-sourcing", "events", "architecture", "cqrs", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://microservices.io/patterns/data/event-sourcing.html", "https://martinfowler.com/eaaDev/EventSourcing.html"]
---

# Event Sourcing

## Summary
Event sourcing stores every state change as an immutable event in an append-only log; current state is a projection of replayed events. It gives full audit history and temporal querying.

## Details
- Events are facts (`NoteCreated`, `NoteLinked`); snapshots bound replay cost; projections build read models.
- Pairs naturally with CQRS and message queues; the log doubles as an integration bus.
- RSIS3's pulse/session history is conceptually event-sourced — each pulse is an append-only record.
- Event sourcing persists every state change as an immutable event; the current state is derived by replaying events, never stored as the source of truth.
- The event log is both audit trail and truth: you can rebuild any past state, debug by replay, and feed other systems from the same stream.
- The costs are replay performance (solved with snapshots), event-schema evolution, and the discipline that events are facts that can never be edited.
- It pairs with CQRS, which separates the write model (append events) from read models (projections).
- **Worked example / comparison** — Worked example — a wiki page is a series of 'created', 'edited', 'promoted' events; the current article is a projection, and a bug can be traced by replaying the exact event sequence.
- For mykb, event sourcing models how the wiki's own change log works: every promotion and edit is an event that the graph rebuilds from.

## Related
- [[wiki/api-protocols/cqrs|CQRS]]
- [[wiki/api-protocols/kafka|Apache Kafka]]
- [[wiki/api-protocols/redis-streams|Redis Streams]]
- [[wiki/devops-infra/transactions|Transactions]]
- [[wiki/concepts/pulse-cycle|Pulse Cycle]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/deep-dives|Deep Dives]]
