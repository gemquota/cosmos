---
type: "concept"
title: "Exactly-Once Claims"
description: "The expensive and often illusory guarantee that a message is processed precisely once"
tags: ["exactly-once", "delivery", "messaging", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Exactly-Once Claims

## Summary
Exactly-once processing is usually a combination of at-least-once delivery plus idempotent consumers, not a property of the transport alone. Systems advertise it (Kafka transactions, SQS FIFO) but the real burden is end-to-end idempotency.

## Details
- End-to-end exactly-once requires idempotent effects and exactly-once state changes — hard.
- Kafka transactions give exactly-once semantics within the log; external side effects still need idempotency.
- Most teams should target at-least-once plus idempotency and skip the complexity.
- mykb relevance: article writes are idempotent by slug, making exactly-once claims unnecessary.

## Related
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/software-engineering/at-most-once|At-Most-Once]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/software-engineering/deduplication-queues|Deduplication Queues]]
- [[wiki/api-protocols/kafka|Kafka]]
