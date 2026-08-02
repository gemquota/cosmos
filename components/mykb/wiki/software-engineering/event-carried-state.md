---
type: "concept"
title: "Event-Carried State"
description: "Events that include the data consumers need instead of just an ID"
tags: ["event-carried-state", "events", "architecture", "data-sharing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event-Carried State

## Summary
Event-carried state sends the full relevant data inside an event — customer name, order total — so consumers do not have to query the producer for it. It decouples services and improves availability at the cost of duplication.

## Details
- Consumers get fresher-than-query availability: no synchronous call means no dependency on the producer.
- Duplication means drift: data in events can go stale; version events and document the source of truth.
- Event size and PII blow up fast — carry what consumers need, not the whole record.
- mykb relevance: wiki events carry article summaries so the index rebuilds without reading files.

## Related
- [[wiki/software-engineering/event-notification|Event Notification]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/event-sourcing-practice|Event Sourcing Practice]]
- [[wiki/software-engineering/denormalization-practice|Denormalization Practice]]
