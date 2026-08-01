---
type: "concept"
title: "Message Queues"
description: "Asynchronous buffers decoupling producers from consumers for reliable work distribution"
tags: ["queues", "messaging", "async", "reliability", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Message Queues

## Summary
Message queues decouple producers from consumers: producers enqueue work, consumers pull and acknowledge it. They absorb bursts, retry failures, and let components scale independently.

## Details
- Core semantics: at-least-once vs exactly-once delivery, dead-letter queues, and consumer acknowledgments.
- Common implementations: RabbitMQ (broker), Kafka/Redis Streams (log-based), SQS (managed).
- Use for indexing jobs, webhook ingestion, and telemetry fan-out in systems like mykb.

## Related
- [[wiki/api-protocols/kafka|Apache Kafka]] — log-based distributed queue
- [[wiki/api-protocols/rabbitmq|RabbitMQ]] — classic AMQP broker
- [[wiki/api-protocols/redis-streams|Redis Streams]] — lightweight stream primitives
- [[wiki/api-protocols/webhooks|Webhooks]] — queue buffers incoming event floods
- [[wiki/frontend/serverless|Serverless]] — queue-triggered functions
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — indexing pipeline reliability
