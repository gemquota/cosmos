---
type: "concept"
title: "Kotlin Flows"
description: "Cold and hot asynchronous streams with backpressure support"
tags: ["kotlin", "flows", "reactive", "streams"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Kotlin Flows

Flows are Kotlin cold streams for sequences of async values, with operators like map, filter, and flatMapLatest and structured cancellation. StateFlow and SharedFlow adapt flows to UI state and event buses.
- Cold by default: each collector triggers a fresh producer; shareIn/stateIn make them hot.
- StateFlow exposes current state plus updates, ideal for ViewModels.
- Room and DataStore emit flows natively.
- Flow operators run on the collecting context unless flowOn shifts it.

## Related

- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]] — flows run inside coroutines
- [[wiki/android-core/livedata|LiveData]] — flows are the modern replacement
- [[wiki/android-core/room-database|Room Database]] — Room queries return flows
- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]] — StateFlow feeds the ViewModel-to-UI path
- [[wiki/android-core/kotlin-language|Kotlin Language]] — flows are core Kotlin
