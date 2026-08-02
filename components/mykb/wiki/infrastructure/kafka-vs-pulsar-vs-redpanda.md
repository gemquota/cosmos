---
type: "concept"
title: "Kafka vs Pulsar vs Redpanda"
description: "Choosing among the leading event-streaming platforms"
tags: ["kafka", "pulsar", "redpanda", "event-streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Kafka vs Pulsar vs Redpanda

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Kafka: log-based, broker-local storage, huge ecosystem, ZooKeeper/KRaft metadata.
- Pulsar: separates serving from storage (BookKeeper), multi-tenancy, and tiered storage by design.
- Redpanda: Kafka API-compatible C++ broker, no JVM/ZooKeeper, lower latency per node.
- Decision factors: ecosystem maturity, storage cost, multi-tenancy, and operational model.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event streaming concepts
- [[wiki/data-storage/message-queues|Message Queues]] — queue vs log distinction
- [[wiki/data-storage/kafka-architecture-and-partitioning|Kafka Architecture And Partitioning]] — Kafka internals
- [[wiki/infrastructure/pulsar-architecture-and-tiers|Pulsar Architecture And Tiers]] — Pulsar internals
- [[wiki/infrastructure/rabbitmq-vs-kafka-vs-sqs|Rabbitmq Vs Kafka Vs Sqs]] — broker-family comparison
