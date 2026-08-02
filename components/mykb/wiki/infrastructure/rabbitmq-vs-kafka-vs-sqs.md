---
type: "concept"
title: "RabbitMQ vs Kafka vs SQS"
description: "When to pick a queue, a log, or a managed queue service"
tags: ["rabbitmq", "kafka", "sqs", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# RabbitMQ vs Kafka vs SQS

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- RabbitMQ: flexible routing (exchanges, bindings), ideal for task queues and request/reply.
- Kafka: replayable log for event streaming, fan-out, and integration at scale.
- SQS: fully managed queue with at-least-once delivery and visibility timeouts.
- The question is delivery semantics, replayability, and routing flexibility.

## Related

- [[wiki/data-storage/message-queues|Message Queues]] — queue semantics
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — log semantics
- [[wiki/infrastructure/kafka-vs-pulsar-vs-redpanda|Kafka Vs Pulsar Vs Redpanda]] — log-family comparison
- [[wiki/infrastructure/sqs-and-sns-fanout|Sqs And Sns Fanout]] — AWS queue + fanout
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
