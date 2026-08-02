---
type: "concept"
title: "At-Least-Once Delivery"
description: "A delivery guarantee where messages may be delivered more than once, but never lost"
tags: ["delivery", "guarantees", "messaging", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# At-Least-Once Delivery

## Summary
At-least-once delivery means the broker retries until the consumer acknowledges, so every message is delivered at least once — duplicates are possible, loss is not. It is the default guarantee of most queues and the baseline for distributed systems.

## Details
- Consumers must be idempotent: processing the same message twice must not double the effect.
- Ack-based redelivery (SQS, Kafka consumer groups) trades duplicates for no-loss.
- At-least-once plus idempotent consumers is the standard reliability recipe.
- mykb relevance: wiki ingestion uses at-least-once and dedup, never exactly-once magic.

## Related
- [[wiki/software-engineering/exactly-once-claims|Exactly-Once Claims]]
- [[wiki/software-engineering/at-most-once|At-Most-Once]]
- [[wiki/software-engineering/delivery-guarantees|Delivery Guarantees]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]]
