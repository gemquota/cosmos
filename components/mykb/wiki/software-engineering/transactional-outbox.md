---
type: "concept"
title: "Transactional Outbox"
description: "Pattern for publishing events reliably by writing them to a database table in the same transaction as the business change"
tags: ["events", "reliability", "messaging", "pattern"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Transactional Outbox

## Summary
The transactional outbox writes an event row into the same database transaction as the business mutation, then a relay publishes it to the message broker. This prevents the classic dual-write problem where the database commit and the event publish diverge.

## Details
- A poller or CDC feed (Debezium) reads the outbox table and publishes each row exactly-once-ish.
- Adds latency and a table, but guarantees that events and state cannot disagree.
- RSIS3 relevance: any agent that must emit knowledge-change events can adopt the outbox.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — outbox is how reliable event publishing begins
- [[wiki/devops-infra/transactions|Database Transactions]] — the atomicity the pattern leans on
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — outbox rows resemble an event log
- [[wiki/devops-infra/backups|Backups]] — outbox tables need the same protection as state
