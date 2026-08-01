---
type: "concept"
title: "Redis Streams"
description: "Append-only log data structure in Redis for streaming, queues, and consumer groups"
tags: ["redis", "streams", "messaging", "pubsub", "data-structures"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Redis Streams

## Summary
Redis Streams is an append-only log data structure with consumer groups, pending-entry lists, and blocking reads. It brings Kafka-style semantics to a single-node, low-latency store.

## Details
- `XADD`, `XREAD`, `XREADGROUP`, and `XACK` manage entries and acknowledgments; entries keep IDs with timestamps.
- Consumer groups split work and track pending entries for recovery after crashes.
- Fits chat fan-out, WebSocket broadcast, and small job queues where a full broker is overkill.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]] — stream/queue hybrid semantics
- [[wiki/api-protocols/kafka|Apache Kafka]] — the scale-up alternative
- [[wiki/api-protocols/websockets|WebSockets]] — fan-out messages to live clients
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — simple event log
- [[wiki/devops-infra/replication|Replication]] — Redis durability model
