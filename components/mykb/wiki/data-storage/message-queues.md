---
type: "concept"
title: "Message Queues"
description: "Point-to-point work distribution with acknowledgments"
tags: ["message-queue", "messaging", "rabbitmq", "work-queues"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rabbitmq.com/docs/queues", "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"]
---

# Message Queues

## Summary
Message queues implement point-to-point messaging: producers enqueue messages and consumers dequeue them, with the broker ensuring each message is delivered to exactly one consumer. Queues decouple producers from consumers, smooth load spikes, and provide retry and acknowledgment semantics for reliable work distribution.

## Details
- **Point-to-point semantics** — unlike publish/subscribe (where every subscriber gets a copy), a queue delivers each message to one competing consumer; this makes queues the standard tool for dispatching jobs, notifications, and background tasks.
- **Acknowledgment** — consumers signal success with an ack; RabbitMQ requires explicit acks unless `autoAck` is enabled, SQS deletes a message only when the consumer calls `DeleteMessage`, and unacked messages are redelivered after visibility timeouts — the mechanism behind at-least-once delivery.
- **Broker behavior** — messages are held in memory or on disk until consumed; queues can be durable (survive broker restart), have TTLs for expiry, and support priorities; SQS's standard queues trade strict ordering for throughput while FIFO queues preserve order.
- **Retries and failures** — consumer crashes trigger redelivery, which makes consumers idempotent a requirement; poison messages move to dead letter queues; backpressure appears as queue depth.
- **Scaling** — adding consumers parallelizes processing, but per-queue ordering constrains parallelism: RabbitMQ quorum queues and SQS FIFO guarantee order per message group, and partition counts bound consumer scale.
- **Choosing** — brokers like RabbitMQ and ActiveMQ give rich routing and protocol flexibility; managed SQS is serverless and elastic; for replayable multi-consumer streams, an event streaming platform is the better fit.

## Related
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — logs vs competing consumers
- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — where failed messages park
- [[wiki/data-storage/backpressure|Backpressure]] — queue depth as the pressure gauge
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — redelivery and deduplication
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — safe redelivery handling
- [[wiki/data-storage/data-observability|Data Observability]] — monitoring queue depth and age
