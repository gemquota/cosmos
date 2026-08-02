---
type: "concept"
title: "Backpressure Spec"
description: "The formal Reactive Streams contract for demand and cancellation"
tags: ["backpressure", "reactive", "spec", "streams"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backpressure Spec

## Summary
The Reactive Streams spec fixes the rules of the game: subscribers request elements, publishers honor requests, and cancellations propagate upstream. Its value is interoperability — any compliant publisher works with any compliant subscriber.

## Details
- Rule highlights: onSubscribe exactly once, request(n) can be called repeatedly, cancel stops the stream.
- Signals must be sequential and non-blocking; violations break backpressure guarantees.
- The JVM spec is the reference; the ideas map to Kotlin Flow, Swift Combine, and JavaScript streams.
- mykb relevance: an agent streaming long outputs uses these rules to stay within a token budget.

## Related
- [[wiki/software-engineering/reactive-streams|Reactive Streams]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
- [[wiki/dev-tools/cancellation-tokens|Cancellation Tokens]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
