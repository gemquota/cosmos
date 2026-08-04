---
type: "entity"
title: "LiveData"
description: "Lifecycle-aware observable data holder"
tags: ["android", "livedata", "observable", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/libraries/architecture/livedata", "https://developer.android.com/reference/androidx/lifecycle/LiveData"]
---

# LiveData

## Summary


## Details
- LiveData is an observable data holder that respects the Android lifecycle: observers only receive updates while their lifecycle is at least STARTED.
- Because it is lifecycle-aware, LiveData eliminates many manual subscription/unsubscription bugs and is safe to expose from a ViewModel.
- Transformations (map, switchMap) and MediatorLiveData compose streams; updates delivered on the main thread by default.
- Kotlin developers increasingly choose StateFlow for the same job, but LiveData remains the classic lifecycle-aware answer.
- **Worked example / comparison** — Worked example — a ViewModel exposes a LiveData<List<Article>>; the fragment observes it in onCreate and receives automatic updates only while it is started.
- For mykb, LiveData is documented as the lifecycle-aware observer pattern and as a stepping stone to Flow-based state.

## Related
- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]]
- [[wiki/android-core/kotlin-flows|Kotlin Flows]]
- [[wiki/android-core/android-lifecycle|Android Lifecycle]]
- [[wiki/android-core/room-database|Room Database]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
