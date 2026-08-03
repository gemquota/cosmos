---
type: "concept"
title: "Webhook Events"
description: "The event objects and schemas webhook deliveries carry"
tags: ["webhooks", "events", "schemas", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Events

## Summary
Webhook events are the structured payloads a producer delivers to subscribers — the actual object of the notification. A well-designed event schema carries stable identifiers, a versioned type, a timestamp, and the affected subject, so a subscriber can dedupe, order, filter, and evolve independently of the producer's internal data model.

## Details
- Mechanism: an event envelope wraps the domain payload: `id` (a unique event ID for dedupe), `type` (like `order.created` or `issue.closed`), `timestamp` (when the event occurred), `data` (the subject, often with a `type` and `id` of its own), and optionally `schema_version` or `data_version`. Producers publish the envelope; subscribers dispatch on `type`, dedupe on `id`, and validate the payload against the declared version. Keeping the envelope stable while versioning only the `data` section lets old subscribers keep working when new fields are added.
- Concrete examples: Stripe's `checkout.session.completed` carries a `data.object` with the session; GitHub's `pull_request` event carries `action`, `number`, and `pull_request` plus `sender` and `repository`; a fintech ledger emits `transaction.created`, `transaction.updated`, and `transaction.voided` with a shared transaction schema. The common thread is that the event is a fact about the past (past tense verbs), immutable, and self-contained — subscribers should not need to call back into the producer to understand it.
- Failure modes: unversioned schemas are the classic failure: a producer renames a field or changes a type and every subscriber breaks at once, with no way to stage the migration. Events that embed mutable references instead of snapshots force subscribers to re-fetch and race with deletion; events that omit `id` or `timestamp` make dedupe and replay impossible. Type drift is subtler: `order.created` reused for both creation and updates (or `action` values that multiply) pushes business logic into the subscriber and breaks filter semantics.
- Operational tradeoffs: versioned, additive schemas (never remove or rename fields; add new optional fields with defaults) allow subscribers to upgrade independently, at the cost of permanent payload baggage and producer-side maintenance. Sharing schemas across organizations argues for a published schema registry (JSON Schema or protobuf) with validation in CI, so a breaking change fails at publish time rather than at delivery time. For internal systems, treat event schemas as API contracts with the same review and compatibility gates as request/response types.
- RSIS3/mykb relevance: MyKB's session capture and RSIS3's pulse records are event streams; giving them stable event envelopes (id, type, timestamp, versioned data) means the knowledge graph can replay, dedupe, and evolve schemas without corrupting historical state — the same discipline webhook consumers depend on.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]]
- [[wiki/api-protocols/webhook-topics|Webhook Topics]]
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]]
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]]
- [[wiki/api-protocols/webhooks|Webhooks]]
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
