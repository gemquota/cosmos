---
type: "concept"
title: "Event Loops"
description: "A single-threaded dispatch model for handling many concurrent I/O operations"
tags: ["event-loops", "concurrency", "async", "io"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event Loops

## Summary
An event loop runs one thread that multiplexes thousands of I/O operations, dispatching callbacks when events fire. Node.js, libuv, Redis, and most UI frameworks use it — concurrency without threads, at the price of never blocking the loop.

## Details
- Never block the loop: a slow synchronous call stalls every other operation sharing the loop.
- Offload CPU-heavy work to worker threads or processes to keep the loop responsive.
- Backpressure discipline (bounded queues, slow-consumer signals) prevents event pileup.
- mykb relevance: the wiki watcher loop can watch thousands of files with one thread.

## Related
- [[wiki/software-engineering/async-await-patterns|Async/Await Patterns]]
- [[wiki/software-engineering/asynchronous-patterns|Asynchronous Patterns]]
- [[wiki/software-engineering/async-await-patterns|Event Loops]]
- [[wiki/software-engineering/promises-vs-callbacks|Promises vs Callbacks]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
