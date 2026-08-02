---
type: "concept"
title: "Asynchronous Patterns"
description: "The recurring designs for non-blocking, event-driven execution"
tags: ["async", "patterns", "concurrency", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)", "https://en.wikipedia.org/wiki/Concurrency_(computer_science)"]
---

# Asynchronous Patterns

## Summary
Asynchronous patterns structure work that must not block: fire-and-forget, callbacks, promises, async/await, event emitters, and queues. Each pattern decides how completion is signaled, how errors surface, and how concurrency is bounded.

## Details
- Callbacks signal completion but nest and invert error handling; promises and async/await flatten both.
- Event emitters decouple producers from listeners; queues decouple in time and add durability.
- Concurrency control is the hidden layer: semaphores, limits, and backpressure bound in-flight async work.
- Cancellation and timeouts are async concerns: without them, abandoned work leaks resources.
- The debugging cost is real: async stacks are fragmented, so structured logs and trace IDs become essential.
- For the mykb bundle, the fetch and verification stages are async with bounded concurrency.
- Worked example — the wiki source fetcher uses async/await with a semaphore of 10 and per-fetch timeouts; results land in a bounded queue that applies backpressure.

Worked example — the wiki source fetcher uses async/await with a semaphore of 10 and per-fetch timeouts; results land in a bounded queue that applies backpressure.

## Related
- [[wiki/software-engineering/async-await-patterns|Async/Await Patterns]]
- [[wiki/software-engineering/promises-vs-callbacks|Promises vs Callbacks]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/dev-tools/cancellation-tokens|Cancellation Tokens]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/reactive-streams|Reactive Streams]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
- [[wiki/api-protocols/backpressure|Backpressure]]
