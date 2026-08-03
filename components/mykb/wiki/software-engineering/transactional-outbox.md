---
type: "concept"
title: "Transactional Outbox"
description: "Pattern for publishing events reliably by writing them to a database table in the same transaction as the business change"
tags: ["events", "reliability", "messaging", "pattern"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Transactional Outbox

## Summary

The transactional outbox writes events to a database table in the same local transaction as the state change, then a relay publishes them to the message broker. It guarantees the event and the state change are atomic — the missing piece in most event-driven systems.

## Details
- Mechanism: business transaction updates state AND inserts an outbox row atomically (same DB, same ACID transaction); a separate relay process polls the outbox and publishes each row to the broker, marking it sent (or the broker pulls via CDC — Debezium-style); consumers get events at-least-once, so they must be idempotent. This solves the dual-write problem (DB + broker can't be atomic).
- Concrete example: an order service inserts the order and OrderCreated outbox row in one transaction; the relay publishes it; if the broker is down, the row stays and retries — no lost event, no inconsistency between the DB state and the event stream. Without an outbox, services publish-then-commit or commit-then-publish, losing events on failure.
- Failure modes: publishing before commit (event for a rollback) or after commit without the row (lost event); relay lag causing stale projections; outbox rows growing unbounded (retention/cleanup policy); and non-idempotent consumers double-processing on at-least-once delivery.
- Operational tradeoffs: the outbox adds a table, a relay, and delivery semantics to manage; it is the standard answer to dual-write consistency, replacing best-effort publish patterns. The discipline is idempotent consumers, outbox retention, and monitoring relay lag.
- RSIS3/mykb relevance: the wiki's event producers use the outbox so loop state changes and their events never diverge, even during broker outages.
- Relay design: make the relay idempotent (mark-sent on successful publish only) and monitor its lag; lag is the operational signal that the event stream is falling behind.
- Retention: archive or delete processed outbox rows on a schedule so the table does not grow without bound and slow the transaction.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — outbox is how reliable event publishing begins
- [[wiki/devops-infra/transactions|Database Transactions]] — the atomicity the pattern leans on
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — outbox rows resemble an event log
- [[wiki/devops-infra/backups|Backups]] — outbox tables need the same protection as state
