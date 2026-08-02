---
type: "concept"
title: "Thread Pools"
description: "Reusing a fixed set of worker threads instead of spawning one per task"
tags: ["threads", "concurrency", "pools", "resource-management"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Thread Pools

## Summary
A thread pool keeps a bounded set of worker threads that pull tasks from a queue, avoiding the cost of thread creation and unbounded contention. Pool size tuning is a classic tradeoff between latency, throughput, and oversubscription.

## Details
- Fixed pools bound resource use; cached pools scale but can oversubscribe; work-stealing pools balance load.
- Size pools around blocking versus CPU-bound work: blocking I/O wants more threads, CPU work wants cores.
- Reject or queue overflow explicitly — unbounded queues hide backpressure.
- mykb relevance: the agent executor should use a small pool per task, not a thread per tool call.

## Related
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/dev-tools/bulkhead-isolation|Bulkhead Isolation]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
