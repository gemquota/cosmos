---
type: "concept"
title: "Webhook Delivery"
description: "HTTP callbacks from servers to subscribers carrying event notifications"
tags: ["webhooks", "events", "http", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Webhook Delivery

## Summary
HTTP callbacks from servers to subscribers carrying event notifications. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Webhooks are HTTP POSTs from server to subscriber on events
- Delivery is at-least-once, so receivers must dedupe
- Open question — how do webhook systems expose delivery logs?

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-retries|Webhook Retries]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-events|Webhook Events]] — related coverage in the same cluster
- [[wiki/api-protocols/webhooks|Webhooks]] — related coverage in the same cluster
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
