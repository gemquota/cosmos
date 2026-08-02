---
type: "concept"
title: "Idempotency Design"
description: "Making operations safe to repeat without changing the outcome"
tags: ["idempotency", "design", "reliability", "apis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://stripe.com/blog/idempotency", "https://en.wikipedia.org/wiki/Idempotence"]
---

# Idempotency Design

## Summary
Idempotency design ensures an operation produces the same result whether it runs once or many times. In distributed systems, where retries are inevitable, idempotency is the property that makes exactly-once semantics achievable.

## Details
- Naturally idempotent operations: PUT by key, DELETE, and upserts with natural keys.
- For non-idempotent operations, clients send an idempotency key; the server stores the result and replays it on repeat.
- The stored result approach also prevents duplicate side effects like double charges or double notifications.
- Idempotency keys need storage, TTL, and clear response semantics for replays.
- Design for it at the API contract: document which operations are idempotent and how.
- For the mykb bundle, article writes are idempotent by slug; sync replays are safe by design.
- Worked example — the wiki publish API takes an Idempotency-Key header; a retried publish returns the original result instead of creating a duplicate article.

Worked example — the wiki publish API takes an Idempotency-Key header; a retried publish returns the original result instead of creating a duplicate article.

## Related
- [[wiki/compositions/idempotent-writes|Idempotent Writes]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/software-engineering/deduplication-queues|Deduplication Queues]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/software-engineering/inbox-pattern|Inbox Pattern]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/api-protocols/idempotency-keys|Idempotency Keys]]
