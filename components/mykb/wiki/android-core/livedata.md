---
type: "concept"
title: "LiveData"
description: "Lifecycle-aware observable data holder"
tags: ["android", "livedata", "observable", "lifecycle"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# LiveData

LiveData is an observable data holder that respects component lifecycles: observers only receive updates while active, avoiding leaks and crashes from dead screens. It was the standard reactive primitive before Kotlin Flow took over.
- MediatorLiveData merges streams; Transformations.map and switchMap compose values.
- Lifecycle awareness means no manual unregistering in most cases.
- StateFlow is now preferred for its coroutine integration and richer operators.
- Still common in legacy codebases and Room query return types.

## Related

- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]] — the canonical partner for LiveData
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — modern coroutine-based successor
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — lifecycle awareness is the core feature
- [[wiki/android-core/room-database|Room Database]] — Room can emit LiveData from queries
