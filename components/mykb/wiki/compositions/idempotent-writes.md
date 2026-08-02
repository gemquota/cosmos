---
type: "concept"
title: "Idempotent Writes"
description: "Writes that produce the same result no matter how many times they run"
tags: ["idempotency", "writes", "reliability", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Idempotent Writes

## Summary
Idempotent writes can be applied repeatedly with the same effect — PUT by key, INSERT with a unique key, increments by idempotency key. They make retries safe, which is why they underpin reliable distributed systems.

## Details
- Design writes to be naturally idempotent: natural keys, upserts, content-hash dedup.
- For non-idempotent operations, attach idempotency keys stored with the result.
- Retries plus idempotency beats exactly-once machinery in practice.
- mykb relevance: wiki article saves are idempotent by slug with a content hash.

## Related
- [[wiki/tooling/idempotency-design|Idempotency Design]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/software-engineering/at-least-once|At-Least-Once]]
- [[wiki/compositions/compare-and-swap|Compare-and-Swap]]
- [[wiki/software-engineering/deduplication-queues|Deduplication Queues]]
