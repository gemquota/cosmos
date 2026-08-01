---
type: "concept"
title: "RabbitMQ"
description: "Mature AMQP message broker with routing, exchanges, and delivery guarantees"
tags: ["rabbitmq", "amqp", "messaging", "queues", "broker"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# RabbitMQ

## Summary
RabbitMQ is a battle-tested message broker implementing AMQP 0-9-1. Exchanges route messages to queues via bindings, supporting pub/sub, work queues, and RPC patterns.

## Details
- Routing models: direct, topic, fanout, and headers exchanges give flexible delivery semantics.
- Features: publisher confirms, consumer acknowledgments, dead-letter queues, and quorum queues for durability.
- Simpler to operate than Kafka for moderate throughput; a good default for web-app job queues.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]] — the general pattern
- [[wiki/api-protocols/kafka|Apache Kafka]] — log-based alternative
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — consumer retry policies
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] — drain queues on stop
- [[wiki/devops-infra/docker-compose|Docker Compose]] — local broker setup
- [[wiki/api-protocols/webhooks|Webhooks]] — queue buffers incoming webhook floods
