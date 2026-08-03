---
type: "concept"
title: "Webhook Topics"
description: "Categorizing subscribable event types in a webhook system"
tags: ["webhooks", "events", "api", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Webhook Topics

## Summary
Webhook topics are the named categories of events a producer offers for subscription — `order.created`, `user.deleted`, `repo.push`. They are the vocabulary of the webhook system: the granularity and naming of topics determine how much irrelevant traffic subscribers receive, how easily they can express what they care about, and how hard the system is to evolve.

## Details
- Mechanism: topics are usually hierarchical strings with a noun and past-tense action (`invoice.paid`, `issue.closed`), which groups naturally by resource and state transition. A subscription selects a set of topics, and the producer routes each event to every subscription whose topic set matches. Granular topics reduce irrelevant deliveries: a subscriber that only cares about successful payments subscribes to `payment.succeeded` instead of receiving every `payment.*` event and filtering locally. Wildcards (`payment.*`, `*.created`) offer convenience but shift filtering responsibility and complicate delivery accounting.
- Concrete examples: Stripe exposes topics like `checkout.session.completed` and `charge.refunded`; GitHub uses `push`, `pull_request`, and `workflow_run` with a single subscription receiving all of them; a commerce platform offers `order.created`, `order.updated`, `order.cancelled` plus `inventory.low`, letting a warehouse system subscribe to the inventory topic only. The naming convention itself is part of the contract: consistent `<resource>.<action>` names make discovery predictable, while ad-hoc names grow an unmanageable vocabulary.
- Failure modes: topic sprawl is the first failure mode — dozens of near-duplicate topics (`order.shipped`, `order.shipped.fedex`, `order.shipped.domestic`) make subscriptions unmanageable and force consumers to interpret micro-semantics. Topic under-granularity is the opposite failure: one `order` topic delivers everything, and consumers pay the cost of filtering and processing events they do not need. Renaming or merging topics breaks existing subscriptions silently unless the system keeps aliases or a migration path, and wildcard subscriptions that over-match can flood a subscriber with events at retry-scaled volumes.
- Operational tradeoffs: more topics mean clearer contracts but more documentation, schema maintenance, and routing rules; fewer topics mean simpler plumbing but fatter deliveries. A pragmatic design publishes a small set of stable, coarse topics for compatibility plus finer-grained ones for new subscribers, versions topic names when semantics change (never silently repurpose `order.updated` to mean something new), and exposes a topic catalog in the dashboard so consumers can see what exists and what is deprecated.
- RSIS3/mykb relevance: RSIS3's pulse and checkpoint events are natural topics; defining a stable topic vocabulary for knowledge events (article.created, synthesis.promoted) gives MyKB consumers the same opt-in granularity and keeps the graph update fan-out predictable as the wiki grows.

## Related
- [[wiki/api-protocols/webhooks-practice|Webhooks in Practice]]
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]]
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]]
- [[wiki/api-protocols/webhook-retries|Webhook Retries]]
- [[wiki/api-protocols/webhooks|Webhooks]]
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]]
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
