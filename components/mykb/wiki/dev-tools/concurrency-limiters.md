---
type: "concept"
title: "Concurrency Limiters"
description: "Bounding how many requests are in flight simultaneously"
tags: ["concurrency", "limits", "resilience", "capacity"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Concurrency Limiters

## Summary
Concurrency limiters cap the number of in-flight operations — requests, calls, jobs — at a fixed or adaptive value. They protect dependencies from overload better than rate limits alone, because they bound simultaneous load, not just arrival rate.

## Details
- In-flight counting with a semaphore is the core; queue or reject when the limit is reached.
- Per-dependency limits (per backend pool) beat a single global limit.
- Pair with timeouts so in-flight slots are never held forever by hung calls.
- mykb relevance: a concurrency limiter keeps the agent from opening 50 model calls at once.

## Related
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]]
- [[wiki/dev-tools/adaptive-limits|Adaptive Limits]]
- [[wiki/dev-tools/bulkhead-isolation|Bulkhead Isolation]]
- [[wiki/software-engineering/thread-pools|Thread Pools]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
