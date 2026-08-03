---
type: "concept"
title: "Event-Carried State"
description: "Events that include the data consumers need instead of just an ID"
tags: ["event-carried-state", "events", "architecture", "data-sharing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Event-Carried State

## Summary

Event-carried state sends the data needed to act alongside the event, so consumers do not have to call back to the source to understand it. It trades read-simplicity and decoupling against data duplication and staleness — a core decision in event-driven architectures.

## Details
- Mechanism: instead of OrderUpdated(userId), publish OrderUpdated(orderId, amount, status, itemsSummary) — the consumer has everything to update its projection or enforce policy; events become the source of truth for downstream state (CQRS projections, read models); schema evolution (adding fields, versioning) is the central governance problem.
- Concrete example: a billing service consumes OrderPlaced with the total and currency, computes taxes locally, and never queries the order service; an analytics projection rebuilds from the event stream without coupling to the source's current APIs. The failure pattern: an event with an ID only, forcing every consumer into synchronous back-calls that recreate the coupling events were meant to remove.
- Failure modes: duplicated state diverging (the event's snapshot goes stale while the source changes); large payloads bloating the stream and log storage; schema drift — consumers reading fields the producer renamed; and events carrying too much business logic, making the stream a hidden API.
- Operational tradeoffs: carry enough state to make consumers independent, but treat the event contract as versioned API; the discipline is event schema registry, versioning with compatibility checks, and projections rebuilt from the stream (replay) as the correctness backstop.
- RSIS3/mykb relevance: the wiki's cross-loop event stream carries state (metrics, conclusions) so downstream loops act without back-calls, and replays rebuild state after schema changes.
- Consistency expectations: consumers eventually converge, not instantly; design the read model to tolerate lag, and expose staleness explicitly where correctness demands it.
- Migration practice: add fields with defaults first, let consumers migrate, then remove the old shape — compatibility-checked schema evolution keeps the stream usable during rolling deploys.

## Related
- [[wiki/software-engineering/event-notification|Event Notification]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/event-sourcing-practice|Event Sourcing Practice]]
- [[wiki/software-engineering/denormalization-practice|Denormalization Practice]]
