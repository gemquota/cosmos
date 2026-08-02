---
type: "concept"
title: "Outbox Pattern"
description: "Persisting events with state changes so messaging never loses them"
tags: ["outbox", "events", "transactions", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://microservices.io/patterns/data/transactional-outbox.html", "https://en.wikipedia.org/wiki/Message_queue"]
---

# Outbox Pattern

## Summary
The outbox pattern writes a business change and its outgoing events into the same database transaction, then a relay publishes the events to the broker. It eliminates the dual-write problem — database updated but event lost — and gives at-least-once delivery by construction.

## Details
- The outbox table records events alongside the state change; a poller or CDC publisher ships them.
- Publication is retried until acked, so consumers must be idempotent — duplicates are possible.
- Outbox rows need cleanup and monitoring; growth or stuck rows are operational alarms.
- It is the standard answer to dual writes between a database and a broker.
- For the mykb bundle, article saves and their LinkChanged events commit atomically; the relay feeds the index and sync.
- Worked example — a wiki save inserts the article and an ArticlePublished row in one transaction; the relay publishes it to the broker; a crash before publication means the row is simply published later.

Worked example — a wiki save inserts the article and an ArticlePublished row in one transaction; the relay publishes it to the broker; a crash before publication means the row is simply published later.

## Related
- [[wiki/software-engineering/outbox-table|Outbox Table]]
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]]
- [[wiki/compositions/dual-writes|Dual Writes]]
- [[wiki/software-engineering/inbox-pattern|Inbox Pattern]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
