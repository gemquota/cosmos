---
type: "concept"
title: "SQS and SNS Fanout"
description: "AWS queue and pub/sub pair for decoupling producers from consumers"
tags: ["sqs", "sns", "aws", "messaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SQS and SNS Fanout

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- SQS delivers messages with at-least-once semantics, visibility timeouts, and DLQs.
- SNS publishes to topics with fan-out to SQS queues, Lambda, and HTTP endpoints.
- The classic pattern: SNS topic fans events out to per-consumer SQS queues.
- Ordering is best-effort unless FIFO queues/topics are used (with throughput limits).

## Related

- [[wiki/data-storage/message-queues|Message Queues]] — queue fundamentals
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — SQS DLQ usage
- [[wiki/infrastructure/eventbridge-and-routing|Eventbridge And Routing]] — richer AWS routing
- [[wiki/api-services/webhooks-and-event-apis|Webhooks And Event Apis]] — HTTP delivery of events
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
