---
type: "concept"
title: "Reactive Programming"
description: "Programming with asynchronous data streams and declarative transformations"
tags: ["programming", "async", "streams", "observables"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Reactive Programming

## Summary
Reactive programming models data as streams of events and expresses transformations declaratively, letting changes propagate automatically. Libraries like RxJS and frameworks like React (via hooks) popularized it.

## Details
- Observables emit values over time; operators filter, map, and combine them without manual state wiring.
- Backpressure and error propagation are first-class concerns in stream libraries.
- RSIS3 relevance: agent telemetry is a stream that reactive pipelines can filter and aggregate.

## Related
- [[wiki/software-engineering/functional-programming|Functional Programming]] — stream operators are functional composition
- [[wiki/web-platforms/state-management|State Management]] — reactive stores drive modern UI state
- [[wiki/api-protocols/websockets|WebSockets]] — a transport that feeds live streams
- [[wiki/concepts/perception-loop|Perception Loop]] — agents consume environment streams reactively
