---
type: "concept"
title: "Message Broker Patterns"
description: "Using brokers to decouple producers and consumers: queues, topics, and delivery semantics"
tags: ["message-broker", "queues", "patterns", "async"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Message Broker Patterns

## Summary
Message brokers sit between producers and consumers, decoupling them in time and scale — producers publish, consumers pull, and the broker holds the messages. They enable resilient, elastic async systems.

## Details
- Queues give point-to-point delivery with competing consumers; topics fan out to many subscribers.
- Delivery semantics (at-least-once, exactly-once, ordering) shape consumer design — idempotency is the usual requirement.
- Broker choice trades throughput, ordering, and replay (Kafka) against simplicity (Redis Streams, RabbitMQ).
- Open question: when a broker adds more operational weight than it removes.

## Related
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — functions consuming broker events
- [[wiki/devops-infra/pub-sub-messaging|Pub/Sub Messaging]] — the fan-out variant
- [[wiki/api-protocols/message-queues|Message Queues]] — queue mechanics reference
- [[wiki/api-protocols/kafka|Apache Kafka]] — high-throughput broker
