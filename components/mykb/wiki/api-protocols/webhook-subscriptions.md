---
type: "concept"
title: "Webhook Subscriptions"
description: "Managing endpoint registrations, filters, and lifecycle for webhooks"
tags: ["webhooks", "events", "api", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Subscriptions

## Summary
A webhook subscription is the registered contract between a producer and a consumer: which endpoint receives deliveries, for which event types, with what secret and filter. Managing subscriptions well — creation, verification, updates, suspension, and deletion — is what keeps a webhook system trustworthy at scale, because every registration is also a permission for the producer to send traffic to a URL.

## Details
- Mechanism: a subscription record stores the endpoint URL, the subscribed topics or event filters, a per-subscription signing secret, and lifecycle state (active, disabled, pending verification). The producer reads this registry when routing events, applies the filters, signs the delivery with the subscription's secret, and records per-subscription delivery metrics. Because registering a URL is a standing authorization to POST to it, most systems add a verification challenge: on creation the producer sends a GET or POST with a random code (or requires echoing a header value), and the subscription only becomes active when the owner of the endpoint proves control.
- Concrete examples: GitHub requires a secret and lets you enable/disable webhooks without deleting them; Stripe's dashboard lists endpoints with their signing secrets and delivery health; an internal platform lets teams register a URL, select topics, and set a filter like `only events with severity=critical`, with the registry backed by a database and an audit log of every change.
- Failure modes: the big ones are unverified endpoints (the producer hammers a URL nobody controls, or worse, the URL points at an internal service — an SSRF vector through the subscription registry), zombie subscriptions (a deleted endpoint still registered, consuming retry budget and confusing delivery dashboards), and secret mismanagement (secrets shown in plaintext, never rotated, or shared across subscriptions so one leak exposes all deliveries). Filter misconfiguration is quieter: a filter that is too broad floods subscribers, one that is too narrow silently drops events they expected.
- Operational tradeoffs: the producer's tradeoff is between per-subscription flexibility (filters, secrets, custom signing) and registry complexity — every dimension must be stored, versioned, and audited, and each new filter capability is new code and new failure modes. The consumer's tradeoff is that sophisticated filtering pushes logic into the producer, so simple systems often expose only topic selection and let consumers filter locally. Health is the missing piece at scale: track per-subscription success rates and automatically disable or alert on endpoints that consistently fail, so churn and rot are visible before they become silent data loss.
- RSIS3/mykb relevance: the subscription registry mirrors RSIS3's configuration discipline: every registered consumer is a declared integration with a contract (endpoint, topics, secret, filters), versioned and audited like the loop registry, so the memory layer knows exactly which sinks receive which knowledge events.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-retries|Webhook Retries]] — related coverage in the same cluster
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]] — related coverage in the same cluster
- [[wiki/api-protocols/webhooks|Webhooks]] — related coverage in the same cluster
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — related coverage in the same cluster
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — related coverage in the same cluster
