---
type: "concept"
title: "Concurrency Models"
description: "The ways systems structure simultaneous execution: threads, events, actors, async"
tags: ["concurrency", "models", "threads", "async"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Concurrency_(computer_science)", "https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)"]
---

# Concurrency Models

## Summary
Concurrency models are the different structures for simultaneous execution: threads with shared memory, event loops, actor models, async/await, and dataflow. Each model chooses what is shared, how work is scheduled, and how failures and backpressure behave.

## Details
- Threads + shared memory is expressive but races, locks, and deadlocks are the tax.
- Event loops multiplex I/O on one thread — concurrency without threads, but nothing may block.
- Actors isolate state behind mailboxes; message passing replaces shared memory.
- Async/await makes non-blocking code readable, with suspension points that are scheduling points.
- The model must fit the workload: I/O-bound wants async or actors; CPU-bound wants parallelism; both want clear boundaries.
- For the mykb bundle, the curation pipeline mixes models: async fetches, worker pools for verification, and queues between stages.
- Worked example — the wiki pipeline fetches 50 sources concurrently via async, verifies them on a bounded pool, and queues writes — each stage using the model that fits its I/O pattern.

Worked example — the wiki pipeline fetches 50 sources concurrently via async, verifies them on a bounded pool, and queues writes — each stage using the model that fits its I/O pattern.

## Related
- [[wiki/software-engineering/asynchronous-patterns|Asynchronous Patterns]]
- [[wiki/software-engineering/actor-model|Actor Model]]
- [[wiki/software-engineering/thread-pools|Thread Pools]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/message-passing|Message Passing]]
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
- [[wiki/dev-tools/benchmark-testing|Benchmark Testing]]
