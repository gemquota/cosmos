---
type: "concept"
title: "Exactly-Once Webhook Delivery"
description: "Making webhook calls safe to retry"
tags: ["webhooks", "exactly-once", "delivery", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exactly-Once Webhook Delivery

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- True exactly-once is impossible over flaky networks; effectively-once via idempotency is the goal.
- Webhook payloads carry event IDs so receivers can deduplicate.
- Receivers should return stable ACKs and store processed event IDs.
- Delivery order and retry windows matter for stateful receivers.

## Related

- [[wiki/api-services/webhooks-and-event-apis|Webhooks And Event Apis]] — webhook design
- [[wiki/api-services/idempotency-keys-in-apis|Idempotency Keys In Apis]] — idempotency keys
- [[wiki/api-services/retry-strategies-and-backoff-jitter|Retry Strategies And Backoff Jitter]] — retries
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — DLQ fallback
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
