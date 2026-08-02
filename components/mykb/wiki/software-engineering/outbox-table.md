---
type: "concept"
title: "Outbox Table"
description: "Persisting events in the same transaction as the state change they describe"
tags: ["outbox", "events", "transactions", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Outbox Table

## Summary
The outbox pattern writes business changes and the events they must emit into one database table in a single transaction, then a relay publishes the events. It guarantees events are never lost between the DB and the message bus.

## Details
- Transactional outbox: insert order + outbox row atomically; a poller publishes and marks sent.
- At-least-once delivery emerges naturally: the relay retries until the row is acked.
- Watch for outbox growth and duplicate publication — make consumers idempotent.
- mykb relevance: article saves and their LinkChanged events commit atomically in the outbox.

## Related
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]]
- [[wiki/software-engineering/transactional-outbox|Outbox Table]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/api-protocols/message-queues|Message Queues]]
