---
type: "concept"
title: "Apache Kafka"
description: "Distributed, durable, log-based event streaming platform for high-throughput pipelines"
tags: ["kafka", "streaming", "events", "distributed-systems", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/intro", "https://kafka.apache.org/documentation/"]
---

# Apache Kafka

## Summary
Apache Kafka is a distributed event streaming platform organized as append-only, partitioned logs. Topics store events durably; consumers track offsets and replay history.

## Details
- Partitions give parallelism and ordering guarantees per key; replication provides durability across brokers.
- Consumer groups divide partitions among workers; offsets track progress for exactly-once-ish processing with idempotent consumers.
- Suits telemetry pipelines, change-data-capture, and event sourcing at scale — heavier than RabbitMQ or Redis Streams.
- Kafka is a distributed event streaming platform organized as append-only, partitioned logs; producers append events and consumers track offsets.
- Partitions provide parallelism and per-key ordering; replication across brokers gives durability and availability.
- Consumer groups divide partitions among members, and committed offsets enable replay, exactly-once processing, and recovery.
- It suits high-throughput pipelines, change-data-capture, and event sourcing, but is heavier than a message broker for simple queuing.
- **Worked example / comparison** — Comparison — Kafka stores and replays history like a log, RabbitMQ routes and removes messages like a queue, and Redis Streams is a lighter in-memory log.
- For mykb, Kafka is documented as the heavyweight event backbone; the wiki's own telemetry pipelines use the same log model.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/api-protocols/event-sourcing|Event Sourcing]]
- [[wiki/api-protocols/redis-streams|Redis Streams]]
- [[wiki/api-protocols/rabbitmq|RabbitMQ]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/api-protocols/websockets|WebSockets]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/comparison-articles|Comparison Articles]]
