---
type: "concept"
title: "Webhooks in Practice"
description: "Server-to-server HTTP callbacks that push event notifications to subscriber endpoints"
tags: ["webhooks", "events", "http", "api", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/webhooks", "https://docs.stripe.com/webhooks"]
---
# Webhooks in Practice

## Summary
Webhooks invert the API relationship: instead of clients polling, the server POSTs event notifications to a registered URL. They power payment confirmations, CI results, and repository events. Delivery is at-least-once, so receivers must be idempotent, and authenticity is proven with signatures.

## Details
- **Subscription model** — clients register endpoints, choose event topics, and exchange a shared secret; some providers verify endpoint ownership.
- **Delivery semantics** — at-least-once delivery means duplicates are normal; event IDs let receivers dedupe, and delivery logs expose retries.
- **Signatures** — HMAC-SHA256 over the raw body, compared in constant time, proves the payload came from the provider.
- **Retries** — failed deliveries retry with exponential backoff, then go to dead-letter or failure dashboards.
- **Worked example** — the mykb daemon could expose a webhook endpoint that a CI pipeline hits on build completion, updating the wiki log automatically.
- **Relevance** — for RSIS3, webhooks are how external systems signal the agent loop without busy-waiting.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-retries|Webhook Retries]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhooks|Webhooks]] — existing coverage
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — existing coverage
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — existing coverage
