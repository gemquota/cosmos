---
type: "concept"
title: "Event Sourcing"
description: "Persisting state as an immutable sequence of events that can be replayed to reconstruct any state"
tags: ["event-sourcing", "events", "architecture", "cqrs", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Event Sourcing

## Summary
Event sourcing stores every state change as an immutable event in an append-only log; current state is a projection of replayed events. It gives full audit history and temporal querying.

## Details
- Events are facts (`NoteCreated`, `NoteLinked`); snapshots bound replay cost; projections build read models.
- Pairs naturally with CQRS and message queues; the log doubles as an integration bus.
- RSIS3's pulse/session history is conceptually event-sourced — each pulse is an append-only record.

## Related
- [[wiki/api-protocols/cqrs|CQRS]] — separates writes from read projections
- [[wiki/api-protocols/kafka|Apache Kafka]] — durable event log storage
- [[wiki/api-protocols/redis-streams|Redis Streams]] — lightweight event log
- [[wiki/devops-infra/transactions|Transactions]] — atomic event appends
- [[wiki/concepts/pulse-cycle|Pulse Cycle]] — append-only telemetry pattern
- [[wiki/devops-infra/observability|Observability]] — telemetry as an append-only event stream
