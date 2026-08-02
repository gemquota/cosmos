---
type: "concept"
title: "Stream Processing Engines"
description: "Flink/Spark-style continuous computation frameworks"
tags: ["stream-processing", "flink", "spark", "stateful-processing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/overview/", "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html"]
---

# Stream Processing Engines

## Summary
Stream processing engines run continuous computations over unbounded data: filtering, enriching, aggregating, joining, and windowing events as they arrive. Apache Flink, Kafka Streams, and Spark Structured Streaming dominate the space, differing mainly in state management, exactly-once guarantees, and event-time handling.

## Details
- **Unbounded streams** — unlike batch jobs that process finite inputs, stream engines ingest endless events and maintain state across them; the execution model is long-running operators wired into a topology or graph.
- **State and fault tolerance** — stateful operators (counters, windows, join buffers) must survive crashes: Flink checkpoints operator state and offsets atomically and restores from the last snapshot; Kafka Streams stores state in local RocksDB backed by changelog topics; Spark Structured Streaming uses WALs and state stores.
- **Exactly-once processing** — engines pair input offsets with output commits so replays do not double-count; Flink's checkpoint-based two-phase commit and Kafka's transactional output are the reference implementations.
- **Event time and watermarks** — out-of-order events are handled by event-time processing with watermarks: an engine waits until a watermark passes the end of a window before emitting it, trading latency for completeness; this is Flink's core differentiator and Kafka Streams' and Spark's key challenge.
- **Choosing an engine** — Flink suits complex event-time, state-heavy pipelines with strong exactly-once needs; Kafka Streams embeds in JVM services and reuses Kafka infrastructure; Spark Structured Streaming fits teams already on Spark and micro-batch semantics; all three run SQL-like APIs on top.
- **Operations** — checkpointing frequency, state size, backpressure, and rebalances dominate monitoring; state TTLs keep long-running jobs bounded.

## Related
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — the input log
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — time-based aggregation semantics
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — the guarantee engines implement
- [[wiki/data-storage/backpressure|Backpressure]] — operator-level flow control
- [[wiki/data-storage/batch-vs-stream-processing|Batch vs Stream Processing]] — the two paradigms
- [[wiki/data-storage/materialized-views|Materialized Views]] — stream-maintained output stores
