---
type: "concept"
title: "Message Brokers"
description: "The middleware that moves messages between producers and consumers"
tags: ["message-brokers", "messaging", "queues", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Message_broker", "https://en.wikipedia.org/wiki/Message_queue"]
---

# Message Brokers

## Summary
Message brokers (RabbitMQ, Kafka, SQS, NATS) decouple producers from consumers: producers publish, brokers store and route, consumers subscribe. They bring durability, buffering, fan-out, and replay to system integration — along with new operational complexity.

## Details
- Queue brokers (RabbitMQ, SQS) deliver each message to one consumer and delete it; log brokers (Kafka) retain and replay events.
- Brokers provide buffering (decoupling load), fan-out (one event, many consumers), and delivery guarantees.
- Operational concerns dominate: availability of the broker, consumer lag, poison messages, and ordering semantics.
- Choose by semantics: point-to-point jobs want queues; event streams and replay want logs.
- The transactional outbox pattern keeps broker publication consistent with database changes.
- For the mykb bundle, a broker carries curation events: captures ingested, links verified, articles published.
- Worked example — the wiki ingestion publishes CaptureReceived; three consumers verify links, extract tags, and notify, each with its own group and lag dashboard.

Worked example — the wiki ingestion publishes CaptureReceived; three consumers verify links, extract tags, and notify, each with its own group and lag dashboard.

## Related
- [[wiki/software-engineering/consumer-groups|Consumer Groups]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/poison-messages|Poison Messages]]
- [[wiki/api-protocols/kafka|Kafka]]
- [[wiki/software-engineering/delivery-guarantees|Delivery Guarantees]]
