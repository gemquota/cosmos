---
type: "concept"
title: "Webhook Signatures"
description: "HMAC or asymmetric signatures proving webhook payload authenticity"
tags: ["webhooks", "security", "signatures", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Webhook Signatures

## Summary
HMAC or asymmetric signatures proving webhook payload authenticity. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- HMAC or asymmetric signatures authenticate webhook payloads
- Signature schemes must cover the raw body to resist tampering
- Open question — should webhook signatures adopt standardized envelopes?

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-events|Webhook Events]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-topics|Webhook Topics]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]] — related coverage in the same cluster
- [[wiki/api-protocols/webhooks|Webhooks]] — related coverage in the same cluster
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
