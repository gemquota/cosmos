---
type: "concept"
title: "Event-Driven APIs"
description: "Event notification and pub/sub API patterns"
tags: ["event-driven", "pubsub", "events", "architecture", "messaging"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/201701-event-driven.html", "https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven"]
---

# Event-Driven APIs

## Summary
Event-driven APIs publish facts about state changes (order.created, user.updated) instead of exposing request-response endpoints for everything. Consumers subscribe and react asynchronously, which decouples producers from consumers — the pattern behind webhooks, Kafka topics, MQTT, and event streaming platforms.

## Details
- Core pattern: producers emit events to a broker or endpoint; consumers subscribe to topics/patterns and process independently — no direct calls between them.
- Event vs command: events state what happened (order.paid, past tense, immutable); commands request an action — mixing them muddies semantics.
- Delivery modes: push (webhooks, SSE), pull (queue polling), and broker fan-out (pub/sub topics with consumer groups).
- Guarantees: at-least-once is the norm; consumers dedupe with event ids and process idempotently; ordering needs per-key partitioning.
- Sagas and outbox: events drive distributed workflows (saga pattern) and reliable publication (transactional outbox), making events a consistency tool.
- Contracts: AsyncAPI documents channels and schemas; schema registries validate events at the edges.
- Trade-offs: async is harder to debug and trace; visibility (correlation ids, tracing) and failure handling must be designed in.

## Related
- [[wiki/api-protocols/webhooks|Webhooks]] — push-style event delivery over HTTP
- [[wiki/api-protocols/mqtt|MQTT]] — a broker-based pub/sub protocol
- [[wiki/api-protocols/asyncapi|AsyncAPI]] — the contract spec for event APIs
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — the architecture style behind it
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — the delivery guarantee to design for
