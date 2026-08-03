---
type: "concept"
title: "Concurrency Limiters"
description: "Bounding how many requests are in flight simultaneously"
tags: ["concurrency", "limits", "resilience", "capacity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Concurrency Limiters

## Summary
Concurrency limiters cap the number of in-flight operations — requests, calls, jobs — at a fixed or adaptive value. They protect dependencies from overload better than rate limits alone, because they bound simultaneous load (connections, memory, threads), not just arrival rate.

## Details
- Mechanism: a semaphore or counter tracks in-flight work; each operation acquires a slot, and when slots are exhausted new work either queues or is rejected; per-dependency limiters isolate each backend pool instead of sharing one global budget; timeouts pair with limiters so a hung call does not hold a slot forever.
- Concrete example: an API client allows 50 concurrent calls to the model provider; a burst of 200 requests queues 150 with a bounded wait; a per-pool limiter of 10 protects a slow analytics backend while the fast API keeps its own budget; adaptive variants raise and lower the cap from latency signals.
- Failure modes: a global limiter starving a critical dependency behind a noisy one; queueing without bounds — the queue itself becomes the memory bomb; slots held by hung calls (no timeout) permanently shrinking capacity; limiters set from average load, so they trip on normal peaks; rejections without clear errors, triggering confusing client retry behavior.
- Tradeoffs: limiters bound worst-case load at the cost of rejecting or queueing legitimate work; rate limits are easier to reason about per second but do not bound simultaneous resource use; the combination — rate limit at the edge, concurrency limit at the client — covers both arrival rate and in-flight load.
- Operational notes: monitor in-flight counts, queue depth, and rejection rates; alert when limits stay pinned; and size from peak concurrency.
- RSIS3 relevance: a concurrency limiter keeps the agent from opening 50 model calls at once — the same bound RSIS3 wants on parallel retrieval and generation.

## Related
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]]
- [[wiki/dev-tools/adaptive-limits|Adaptive Limits]]
- [[wiki/dev-tools/bulkhead-isolation|Bulkhead Isolation]]
- [[wiki/software-engineering/thread-pools|Thread Pools]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
