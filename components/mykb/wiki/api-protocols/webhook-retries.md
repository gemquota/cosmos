---
type: "concept"
title: "Webhook Retries"
description: "Redelivery policies for failed webhook HTTP calls"
tags: ["webhooks", "retry", "reliability", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Retries

## Summary
Webhook retries are the redelivery policy that governs what happens when a webhook HTTP call fails. Because delivery is at-least-once, a failed attempt is not the end: producers retry with exponential backoff, honor the subscriber's feedback, and eventually park hopeless deliveries in a dead-letter queue so operators can inspect and replay them.

## Details
- Mechanism: on a failure — non-2xx response, network error, or timeout — the producer schedules a retry after a delay that typically grows exponentially (1s, 2s, 4s, ... up to a cap), often with jitter so many subscribers recovering at once do not synchronize into a thundering herd. Retry budgets are expressed as a maximum attempt count or a delivery window (for example, retry for 24 hours, roughly 40 attempts). Some producers honor `Retry-After` headers or pause permanently after a 410 Gone so they do not hammer a deliberately removed endpoint.
- Concrete examples: GitHub retries with an escalating schedule and disables a webhook after repeated failures, surfacing the problem in the repository settings; Stripe retries deliveries with backoff and stops after a bounded period, marking events as failed in the dashboard; a queue-based producer persists each delivery to a durable queue, so a crash mid-retry resumes from the stored attempt state rather than losing the event.
- Failure modes: the worst failure is retrying everything indiscriminately: transient 5xx and permanent 4xx (a malformed payload, an authorization failure) both get retried, wasting attempts on errors retries can never fix, so policies should classify statuses (retry 5xx and timeouts, dead-letter 4xx). Equally bad is over-aggressive retrying, which converts a subscriber outage into a load spike; and retries without idempotency, which multiply side effects when a delivery that actually succeeded is retried because the acknowledgment was lost.
- Operational tradeoffs: the producer's lever is the retry budget — too small and transient outages lose events; too large and failed endpoints consume resources for days. The subscriber's side matters just as much: return 2xx only after persisting, return 4xx for permanent problems, and make processing idempotent by event ID so duplicates are cheap. Dead-letter queues (with delivery logs, payload inspection, and manual or automated replay) turn exhausted budgets from silent data loss into an auditable backlog.
- RSIS3/mykb relevance: RSIS3 loop notifications and MyKB session-capture callbacks should adopt the same policy: classify errors, back off with jitter, dedupe by event ID, and dead-letter what cannot be delivered, so a failing sink never stalls the memory layer or silently drops knowledge.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]]
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]]
- [[wiki/api-protocols/webhook-events|Webhook Events]]
- [[wiki/api-protocols/webhook-topics|Webhook Topics]]
- [[wiki/api-protocols/webhooks|Webhooks]]
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
