---
type: "concept"
title: "Webhooks"
description: "HTTP callbacks that push event notifications from a provider to a consumer's endpoint"
tags: ["webhooks", "api", "events", "integration", "http"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://docs.github.com/en/webhooks"]
---

# Webhooks

## Summary
Webhooks are user-defined HTTP callbacks: a provider sends a POST to your endpoint when an event occurs, instead of waiting for you to poll. They power integrations like GitHub notifying CI systems, Stripe notifying billing backends, and any event-driven glue between platforms. Because delivery is asynchronous and best-effort, consumers must verify, deduplicate, and retry.

## Details
- Flow: event occurs, provider signs a JSON payload and POSTs to the registered URL; consumer responds 2xx to acknowledge, 4xx/5xx triggers provider retries.
- Signature verification: providers sign payloads with HMAC or asymmetric keys (e.g. `X-Hub-Signature-256`); always verify before processing.
- Deduplication: at-least-once delivery means the same event can arrive twice; store `event_id` and skip duplicates.
- Retries and backoff: providers retry with exponential backoff for hours/days; consumers should be idempotent so replays are harmless.
- Security: validate the event source, use HTTPS endpoints, and never trust unauthenticated payloads.
- Worked example: the mykb daemon could register a webhook endpoint so RSIS3 receives "note indexed" events without polling, keeping the dashboard live.
- Tools: GitHub, Stripe, and Slack all ship webhook platforms; frameworks expose receiver helpers with signature middleware.

## Related
- [[wiki/api-protocols/idempotency|Idempotency]] — replays must not double-process events
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — provider-side delivery retries
- [[wiki/security/secrets-management|Secrets Management]] — webhook signing secrets need vaults
- [[wiki/api-protocols/message-queues|Message Queues]] — buffering webhook floods for workers
- [[wiki/devops-infra/github-actions|GitHub Actions]] — triggered by repository webhooks
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — capture hooks mirror webhook delivery
- [[wiki/concepts/triad-architecture|Triad Architecture]] — daemon webhook receiver in the triad
