---
type: "concept"
title: "Idempotency Keys in APIs"
description: "Client-supplied keys that make retries safe"
tags: ["idempotency", "api-design", "retries", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Idempotency Keys in APIs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A client sends an idempotency key; the server stores the first result and replays it on retry.
- Stripe-style: key per request, stored with the response until expiration.
- Keys need an index, TTL, and careful handling of concurrent duplicates.
- They convert at-least-once delivery into effectively-once side effects.

## Related

- [[wiki/api-services/api-design-for-data|Api Design For Data]] — API design
- [[wiki/api-services/retry-strategies-and-backoff-jitter|Retry Strategies And Backoff Jitter]] — retry policy
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — data-side idempotency
- [[wiki/api-services/exactly-once-webhook-delivery|Exactly-Once Webhook Delivery]] — delivery semantics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
