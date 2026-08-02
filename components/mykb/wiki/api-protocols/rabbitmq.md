---
type: "concept"
title: "RabbitMQ"
description: "Mature AMQP message broker with routing, exchanges, and delivery guarantees"
tags: ["rabbitmq", "amqp", "messaging", "queues", "broker"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rabbitmq.com/getstarted.html", "https://www.rabbitmq.com/documentation.html"]
---

# RabbitMQ

## Summary
RabbitMQ is a battle-tested message broker implementing AMQP 0-9-1. Exchanges route messages to queues via bindings, supporting pub/sub, work queues, and RPC patterns.

## Details
- Routing models: direct, topic, fanout, and headers exchanges give flexible delivery semantics.
- Features: publisher confirms, consumer acknowledgments, dead-letter queues, and quorum queues for durability.
- Simpler to operate than Kafka for moderate throughput; a good default for web-app job queues.
- RabbitMQ is a message broker implementing AMQP 0-9-1: producers publish to exchanges, which route to queues via bindings, and consumers pull or receive pushes.
- Exchange types (direct, topic, fanout, headers) give flexible routing; queues offer durability, TTL, dead-lettering, and prefetch control.
- It optimizes for flexible routing and per-message acknowledgement rather than replayable history, which makes it a queue rather than a log.
- Clustering provides availability, and plugins add protocols like MQTT and STOMP.
- **Worked example / comparison** — Worked example — a topic exchange routes 'wiki.updated' events to a search-index queue and an email-notification queue based on binding keys.
- For mykb, RabbitMQ is the routing-heavy alternative to Kafka, documented in the same messaging cluster.

## Related
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/api-protocols/kafka|Apache Kafka]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]]
- [[wiki/devops-infra/docker-compose|Docker Compose]]
- [[wiki/api-protocols/webhooks|Webhooks]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/comparison-articles|Comparison Articles]]
