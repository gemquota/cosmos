---
type: "concept"
title: "Event Streaming"
description: "Continuously publishing and consuming ordered event logs as the source of truth for state"
tags: ["event-streaming", "kafka", "events", "data-pipelines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Event Streaming

## Summary
Event streaming treats events as an append-only, replayable log: producers write facts, consumers read them at their own pace and position. The log is ordered, retained, and replayable, which makes it a durable source of truth that new consumers can join at any point in history.

## Details
- Mechanics: the log is partitioned for parallelism; ordering is guaranteed only within a partition, so the partitioning key (user id, order id, tenant) decides which events share an order; consumers track offsets — committing a position enables replay, reprocessing, and late-joining consumers; retention policy (time or size) bounds the log.
- Concrete example: an order service publishes `order.created`, `order.paid`, `order.shipped`; a billing consumer reads paid events, an analytics consumer reads all events, and a new consumer joins by reading from the oldest retained offset; the stream serves as the audit record of everything that happened.
- Failure modes: events published without idempotency keys cause duplicates on replay; schema evolution breaks consumers that cannot parse new fields (use schema registry and backward-compatible changes); partitions skew when one key dominates, creating a hot partition that limits throughput; retention too short for slow consumers or late joiners; poison messages that a consumer can never process, blocking its offset.
- Tradeoffs: the log-as-database idea is powerful for event sourcing and CQRS but complex state (joins, aggregations, deletions) needs materialized views or a real database — push the log far enough for audit and replay, not for every query; streaming adds operational weight (brokers, consumer groups, schemas) that batch processing avoids.
- Operational notes: monitor consumer lag, define retention by replay needs, and version schemas from day one.
- RSIS3 relevance: RSIS3's pulses and loop events are a natural event stream — an append-only, replayable log of loop activity would let later loops audit, replay, and learn from past behavior exactly as event streaming intends.

## Related
- [[wiki/devops-infra/pub-sub-messaging|Pub/Sub Messaging]] — delivery vs log model
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — consumers of event streams
- [[wiki/devops-infra/stream-processing|Stream Processing]] — consuming the log live
- [[wiki/api-protocols/kafka|Apache Kafka]] — the reference stream broker
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — state from the event log
