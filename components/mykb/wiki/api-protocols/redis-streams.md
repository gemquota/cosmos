---
type: "concept"
title: "Redis Streams"
description: "Append-only log data structure in Redis for streaming, queues, and consumer groups"
tags: ["redis", "streams", "messaging", "pubsub", "data-structures"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://redis.io/docs/latest/develop/data-types/streams/", "https://redis.io/docs/latest/commands/xadd/"]
---

# Redis Streams

## Summary
Redis Streams is an append-only log data structure with consumer groups, pending-entry lists, and blocking reads. It brings Kafka-style semantics to a single-node, low-latency store.

## Details
- `XADD`, `XREAD`, `XREADGROUP`, and `XACK` manage entries and acknowledgments; entries keep IDs with timestamps.
- Consumer groups split work and track pending entries for recovery after crashes.
- Fits chat fan-out, WebSocket broadcast, and small job queues where a full broker is overkill.
- Redis Streams is an append-only log data type inside Redis, with entries, consumer groups, and per-consumer pending-entry lists.
- Streams combine the replayability of a log with Redis simplicity: XADD appends, XREAD reads, XREADGROUP reads with consumer-group semantics.
- Consumer groups track delivery and support acknowledgment, so failed processing can be retried from the pending list.
- It is lighter than Kafka — single-node by default, bounded by memory — and suits moderate-throughput event pipelines.
- **Worked example / comparison** — Worked example — a job queue uses XADD to enqueue, XREADGROUP so workers claim entries, XACK on success, and XPENDING to find and retry abandoned work.
- For mykb, Redis Streams is the light log alternative to Kafka, documented alongside it in api-protocols.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/api-protocols/kafka|Apache Kafka]]
- [[wiki/api-protocols/websockets|WebSockets]]
- [[wiki/api-protocols/event-sourcing|Event Sourcing]]
- [[wiki/devops-infra/replication|Replication]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/comparison-articles|Comparison Articles]]
