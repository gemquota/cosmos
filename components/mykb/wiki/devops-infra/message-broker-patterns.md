---
type: "concept"
title: "Message Broker Patterns"
description: "Using brokers to decouple producers and consumers: queues, topics, and delivery semantics"
tags: ["message-broker", "queues", "patterns", "async"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Message Broker Patterns

## Summary
Message brokers sit between producers and consumers, decoupling them in time and scale — producers publish, consumers pull, and the broker holds the messages. Queues give point-to-point delivery with competing consumers; topics fan out to many subscribers; delivery semantics and ordering shape how consumers must be written.

## Details
- Queue pattern: one message consumed by exactly one of N workers (competing consumers); ideal for jobs and tasks; the broker tracks acks and redelivers on failure; scale-out adds workers without touching producers.
- Topic pattern: each message is delivered to every subscriber group; the basis of event-driven fan-out (order.created to billing, analytics, notification consumers); subscription groups let independent consumers track their own positions.
- Delivery semantics: at-least-once (default for most brokers) requires idempotent consumers — process by message ID or dedupe keys; exactly-once is achievable via transactional outboxes or broker features but costs throughput; ordering is guaranteed per partition or per queue, not globally, so design keys around the ordering you need.
- Concrete example: an order service writes to an outbox table and a publisher forwards to a topic; the billing consumer and analytics consumer each track offsets; a job queue holds image-resize tasks consumed by a worker pool with ack-on-success and retry with backoff.
- Failure modes: consumer lag growing unboundedly when processing slows (alert on lag); poison messages that a consumer can never process, blocking the queue head (dead-letter queues); redelivery storms after a partial ack; brokers that add more operational weight than they remove — replication, retention, and rebalancing are real costs.
- Tradeoffs: Kafka wins on throughput, replay, and retention but is operationally heavy; RabbitMQ is simpler with rich routing; Redis Streams are lightest but weakest on durability; pick by scale and durability needs, not by fashion.
- RSIS3 relevance: RSIS3's loop events (pulses, completed experiments) fit a topic pattern — an append-only event log other loops subscribe to, replayable for audit and learning.

## Related
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — functions consuming broker events
- [[wiki/devops-infra/pub-sub-messaging|Pub/Sub Messaging]] — the fan-out variant
- [[wiki/api-protocols/message-queues|Message Queues]] — queue mechanics reference
- [[wiki/api-protocols/kafka|Apache Kafka]] — high-throughput broker
