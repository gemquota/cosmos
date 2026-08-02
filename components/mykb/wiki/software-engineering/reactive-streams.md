---
type: "concept"
title: "Reactive Streams"
description: "A standard for asynchronous stream processing with backpressure"
tags: ["reactive", "streams", "backpressure", "async"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reactive Streams

## Summary
Reactive Streams (and the Reactive Streams spec adopted by RxJava, Project Reactor, Akka Streams) standardizes publisher-subscriber pipelines with demand-based backpressure. Subscribers request N elements and publishers produce at most N — memory stays bounded.

## Details
- The protocol is four interfaces: Publisher, Subscriber, Subscription, Processor; demand signals flow upstream.
- Operators (map, filter, buffer) compose without breaking backpressure — the spec's core promise.
- Implementations differ (Java spec, ReactiveX, RSocket) but share the demand-signal model.
- mykb relevance: streaming agent output with backpressure keeps token buffers bounded.

## Related
- [[wiki/software-engineering/backpressure-spec|Backpressure Spec]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
- [[wiki/software-engineering/event-loops|Event Loops]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
