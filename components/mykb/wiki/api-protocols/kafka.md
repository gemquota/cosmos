---
type: "concept"
title: "Apache Kafka"
description: "Distributed, durable, log-based event streaming platform for high-throughput pipelines"
tags: ["kafka", "streaming", "events", "distributed-systems", "messaging"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Apache Kafka

## Summary
Apache Kafka is a distributed event streaming platform organized as append-only, partitioned logs. Topics store events durably; consumers track offsets and replay history.

## Details
- Partitions give parallelism and ordering guarantees per key; replication provides durability across brokers.
- Consumer groups divide partitions among workers; offsets track progress for exactly-once-ish processing with idempotent consumers.
- Suits telemetry pipelines, change-data-capture, and event sourcing at scale — heavier than RabbitMQ or Redis Streams.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]] — family of async delivery systems
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — Kafka as the event store
- [[wiki/api-protocols/redis-streams|Redis Streams]] — lighter log alternative
- [[wiki/api-protocols/rabbitmq|RabbitMQ]] — broker-style alternative
- [[wiki/devops-infra/observability|Observability]] — telemetry transport
- [[wiki/api-protocols/websockets|WebSockets]] — fan-out to clients
