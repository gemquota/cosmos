---
type: "concept"
title: "Dead Letter Queues"
description: "Parking undeliverable messages for inspection"
tags: ["dead-letter-queue", "messaging", "error-handling", "dlq"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html", "https://www.rabbitmq.com/docs/dlx"]
---

# Dead Letter Queues

## Summary
A dead letter queue (DLQ) is a secondary queue that receives messages a consumer could not process successfully, so they are parked instead of retried forever or silently dropped. DLQs decouple poison-message handling from the main pipeline and give operators a place to inspect, repair, and replay failures.

## Details
- **How messages land in a DLQ** — brokers move messages after a defined failure signal: SQS uses a configurable `maxReceiveCount` (a message is dead-lettered after N receives without a delete), while RabbitMQ dead-letters messages whose TTL expires, are negatively acknowledged (`basic.nack` with `requeue=false`), or exceed a queue-length limit via `x-dead-letter-exchange`.
- **Routing** — RabbitMQ routes dead letters to a configured dead-letter exchange with the original routing key or `x-dead-letter-routing-key`; SQS delivers to a distinct queue that can be in another account, with the original queue's metadata preserved.
- **Why not retry forever** — repeated failures amplify load, delay healthy messages behind poison messages, and can exhaust consumer memory; DLQs bound retries and isolate the failure for diagnosis.
- **Operations** — DLQs need monitoring and an owner: alert when depth grows, inspect message bodies and headers for the failure reason, fix the root cause, then replay (SQS DLQ redrive, RabbitMQ shovel or manual republish). An unmonitored DLQ is just a slow-motion data loss.
- **Design guidance** — set a real `maxReceiveCount`, include error metadata in message attributes, redrive only after the producer/consumer fix is deployed, and never use a DLQ as the primary error store.

## Related
- [[wiki/data-storage/message-queues|Message Queues]] — the parent abstraction
- [[wiki/data-storage/backpressure|Backpressure]] — flow control when consumers fail
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — DLQ-style topics for bad records
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — delivery guarantees and failures
- [[wiki/data-storage/data-observability|Data Observability]] — alerting on DLQ depth
