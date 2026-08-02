---
type: "concept"
title: "Event Notification"
description: "Events that say something happened, with consumers fetching details as needed"
tags: ["event-notification", "events", "architecture", "decoupling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event Notification

## Summary
Event notification sends a lightweight signal — OrderPlaced(id) — and consumers fetch any details they need. It decouples timing while keeping a single source of truth; the cost is a synchronous fetch per consumer.

## Details
- Notifications are the thinnest event flavor: ID plus a few routing fields.
- Consumers may query the producer, which can fail or load it — consider event-carried state instead.
- Good for fan-out of 'do something now' signals: reindex, notify, invalidate.
- mykb relevance: LinkBroken(id) notifies the indexer, which re-reads the article for details.

## Related
- [[wiki/software-engineering/event-carried-state|Event-Carried State]]
- [[wiki/software-engineering/observer-pattern|Observer Pattern]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/event-sourcing-practice|Event Sourcing Practice]]
- [[wiki/api-protocols/webhooks|Webhooks]]
