---
type: "concept"
title: "Event Streaming Platforms"
description: "Kafka-style append-only logs with partitions and offsets"
tags: ["kafka", "event-streaming", "log", "partitions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://pulsar.apache.org/docs/3.3.x/concepts-overview/"]
---

# Event Streaming Platforms

## Summary
Event streaming platforms are distributed, append-only log systems — Apache Kafka, Apache Pulsar, Amazon MSK, Redpanda — that ingest high-throughput event streams and let many consumers read them independently. They combine durable storage with publish/subscribe delivery, acting as the backbone of modern event-driven architectures.

## Details
- **Topics and partitions** — events are written to topics, each split into ordered partitions; the partition is the unit of parallelism and ordering, so a keyed producer guarantees per-key order and consumers can scale one per partition.
- **Offsets and consumption** — consumers track offsets, the position in a partition's log; since data is retained, consumers can replay, rewind, or start at the beginning, which is what enables reprocessing and stream joins.
- **Durability and replication** — the log is persisted and replicated across brokers; Kafka uses ISR (in-sync replicas) and acks to trade durability against latency, and retention policies bound the log by time or size.
- **Beyond messaging** — unlike traditional queues, the log is a durable source of truth: consumers are not competing workers but independent readers, so the same stream feeds analytics, search indexes, and microservices.
- **Ecosystem** — Kafka Connect moves data in/out of databases and lakes; Kafka Streams and ksqlDB do stateful processing; Schema Registry (Confluent) governs message formats; Pulsar adds separate storage and compute tiers with per-subscription consumption modes.
- **Operations** — consumer lag, partition skew, and broker health dominate monitoring; rebalancing storms and retention misconfiguration are the classic failure modes.

## Related
- [[wiki/data-storage/message-queues|Message Queues]] — competing-consumer semantics vs logs
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — delivery guarantees in the log
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — consumers of the log
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — databases publishing into the log
- [[wiki/data-storage/backpressure|Backpressure]] — consumer lag and flow control
- [[wiki/data-storage/stream-windowing|Stream Windowing]] — time-based aggregation on streams
