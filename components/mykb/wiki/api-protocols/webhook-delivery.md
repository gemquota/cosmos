---
type: "concept"
title: "Webhook Delivery"
description: "HTTP callbacks from servers to subscribers carrying event notifications"
tags: ["webhooks", "events", "http", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Delivery

## Summary
Webhook delivery is the mechanism by which a server pushes an HTTP request to a subscriber's endpoint when an event occurs, reversing the usual pull model: instead of the client polling for changes, the server calls the client. Because delivery is inherently asynchronous and failure-prone, the design of delivery semantics — ordering, retries, idempotency, visibility — is where webhook systems live or die.

## Details
- Mechanism: on an event, the producer constructs a delivery (a POST to the subscriber's registered URL, typically with a JSON body, signature headers, and a unique delivery ID) and hands it to a delivery pipeline that manages concurrency, backoff, and retries. Delivery is at-least-once by nature: a network timeout, a 5xx, or a crash after send but before acknowledgment can duplicate a delivery, so receivers must dedupe on an event or delivery ID rather than assuming exactly-once semantics.
- Concrete examples: GitHub sends `push`, `issues`, and `workflow_run` events to configured endpoints; Stripe delivers payment and dispute events with signatures and idempotency keys; a warehouse-sync pipeline delivers `order.updated` events to a data lake ingester. Each of these exposes delivery metadata — headers like `X-Webhook-Id`, `X-Webhook-Delivery`, and `X-GitHub-Event` — that lets receivers correlate, dedupe, and audit what happened.
- Failure modes: the dominant failure is the unacknowledged delivery: the subscriber's endpoint is down, returns 500, or takes so long that the producer times out, and the event is retried until the retry budget is exhausted and the event lands in a dead-letter queue or is dropped. Silent failures are worse: a subscriber that returns 200 without actually processing (a crashed worker after the HTTP layer succeeds) makes the event appear delivered while data is lost. Ordering is another trap: parallel retries can reorder events, so subscribers should not assume `event.updated` arrives after `event.created` unless the producer guarantees ordering.
- Operational tradeoffs: producers must choose between strict ordering (serialize per subscriber or per subject, at the cost of throughput and head-of-line blocking) and parallel delivery (fast, but out of order). Delivery logs and webhook dashboards are the visibility layer: they should expose attempts, latencies, status codes, and retry counts per subscriber so a failing endpoint is detected before the retry budget drains. Consumers should return fast and process asynchronously, respond 2xx only after persisting, and keep processing idempotent.
- RSIS3/mykb relevance: RSIS3's loop events (pulse generation, checkpoint writes) are natural webhook subjects; modeling them as at-least-once deliveries with dedupe keys gives the system the same auditability and replay guarantees MyKB expects from its own event capture hooks.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]]
- [[wiki/api-protocols/webhook-retries|Webhook Retries]]
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]]
- [[wiki/api-protocols/webhook-events|Webhook Events]]
- [[wiki/api-protocols/webhooks|Webhooks]]
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
