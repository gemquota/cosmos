---
type: "concept"
title: "Exactly-Once Semantics"
description: "Delivery and processing guarantees in streaming systems"
tags: ["exactly-once", "streaming", "idempotency", "delivery-guarantees"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/#semantics", "https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/"]
---

# Exactly-Once Semantics

## Summary
Exactly-once semantics (EOS) guarantee that each event affects downstream state exactly one time even when failures cause retries. Real systems implement it with a combination of atomic commits, idempotency, and transaction logs rather than by literally delivering a message once over a lossy network.

## Details
- **The three delivery levels** — at-most-once (messages may be lost), at-least-once (messages are redelivered on failure), and exactly-once (no loss, no duplication from the application's viewpoint). Most brokers default to at-least-once because it is cheap and safe.
- **The impossibility trap** — a network cannot guarantee single delivery; EOS is achieved end to end by making retries safe: consumers must produce the same result whether an event arrives once or repeatedly, or the system must make the commit atomic across input offset and output state.
- **Kafka's implementation** — transactional producers mark batches with transaction IDs; consumers read only committed data; a transaction coordinator brokers the commit of both the output and the consumed offsets, giving exactly-once across the read-process-write cycle.
- **Flink's approach** — checkpointing snapshots operator state and offsets; on failure, the whole pipeline rolls back to the last checkpoint and replays, making effects idempotent because state and offsets commit together.
- **Idempotency as the fallback** — deduplication keys, unique constraints, and write-once stores (idempotent sinks) convert at-least-once delivery into effectively-once behavior; this is the common practical route outside full transactional pipelines.
- **Costs** — EOS adds latency and coordination overhead; many workloads tolerate at-least-once plus idempotent sinks, so choose EOS where duplicates are genuinely unacceptable (payments, inventory, counts).

## Related
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — where delivery guarantees live
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — checkpointing as EOS machinery
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — making replays safe
- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — handling unprocessable events
- [[wiki/data-storage/backpressure|Backpressure]] — retry behavior under load
