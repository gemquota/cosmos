---
type: "concept"
title: "Kotlin Flows"
description: "Cold and hot asynchronous streams with backpressure support"
tags: ["kotlin", "flows", "reactive", "streams"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kotlinlang.org/docs/flow.html", "https://kotlinlang.org/docs/async-programming.html"]
---

# Kotlin Flows

## Summary


## Details
- Flows are cold asynchronous streams: values are produced lazily when a collector starts, and the pipeline suspends between emissions.
- Operators (map, filter, flatMapLatest, combine) transform the stream, and flowOn moves work between dispatchers.
- StateFlow and SharedFlow provide hot, shared state streams suitable for UI state and event buses, with lifecycle-aware collection via repeatOnLifecycle.
- Flows compose with coroutines, so backpressure, cancellation, and structured concurrency all come for free.
- **Worked example / comparison** — Worked example — a search screen uses a debounced flow of query text, flatMapLatest to cancel stale searches, and stateIn to expose the latest result as StateFlow.
- For mykb, Flows are documented as the modern reactive layer on top of coroutines for Android state management.

## Related
- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]]
- [[wiki/android-core/livedata|LiveData]]
- [[wiki/android-core/room-database|Room Database]]
- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]]
- [[wiki/android-core/kotlin-language|Kotlin Language]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
