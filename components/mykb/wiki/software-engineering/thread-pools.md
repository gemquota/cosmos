---
type: "concept"
title: "Thread Pools"
description: "Reusing a fixed set of worker threads instead of spawning one per task"
tags: ["threads", "concurrency", "pools", "resource-management"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Thread Pools

## Summary

Thread pools bound the number of concurrent threads executing queued tasks, reusing threads instead of creating them per task. They are the default concurrency structure for I/O-bound and bounded-CPU workloads — and the source of deadlock and saturation bugs when sized or used wrongly.

## Details
- Mechanism: a pool has a fixed/maximum thread count, a work queue, and a policy for saturation (block, discard, caller-runs); tasks are submitted and run on pooled threads; sizing rules of thumb: I/O-bound pools can exceed cores (threads wait), CPU-bound pools ≈ cores + a margin; executors (Java, Python ThreadPoolExecutor, .NET) implement the pattern.
- Concrete example: a web server's request handler submits blocking DB calls to an I/O pool so CPU threads stay free; a batch processor uses a fixed pool of 8 for 10,000 files with a bounded queue; the failure pattern: a pool of 4 where every task waits on a pool of 4 (nested pools) → deadlock; unbounded queues hiding memory growth.
- Failure modes: thread pool starvation (all threads blocked on a dependency that also needs the pool); queue explosion from producers outpacing workers; thread-local state leaking across tasks (reuse — clear it); and shutdown handling that drops queued work.
- Operational tradeoffs: pools trade thread overhead for bounded resource use and queue management; the discipline is sizing by measurement (queue depth, wait times), separate pools for independent dependencies, and explicit rejection/shutdown policies.
- RSIS3/mykb relevance: the wiki's worker processes use sized pools with bounded queues; this note records the sizing data the loop uses when scaling worker counts.
- Naming and metrics: name pool threads and export queue depth, active count, and rejection rates; an unnamed pool is undebuggable under load.
- Avoid nested waits: if pooled tasks wait on other pooled tasks, the pool must be sized for the total dependency chain or the design must avoid nested submission.

## Related
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/dev-tools/bulkhead-isolation|Bulkhead Isolation]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
