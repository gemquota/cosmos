---
type: "concept"
title: "ViewModel Pattern"
description: "Configuration-stable holder for UI state that survives activity recreation"
tags: ["android", "viewmodel", "state", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/libraries/architecture/viewmodel", "https://developer.android.com/reference/androidx/lifecycle/ViewModel"]
---

# ViewModel Pattern

## Summary


## Details
- A ViewModel holds UI state and survives configuration changes, so rotation does not reset the data the screen is showing.
- It separates the screen's data from its view lifecycle: the ViewModel outlives the Activity or Fragment while the UI is alive.
- ViewModelStore ties ViewModels to a scope; clearing happens when the scope finishes, which is where cleanup of long-lived work belongs.
- It is the natural home for exposing state via LiveData or StateFlow to the UI layer, keeping business logic testable without a device.
- **Worked example / comparison** — Worked example — a detail screen fetches an article once in its ViewModel; rotating the device keeps the loaded article in memory instead of re-fetching.
- For mykb, the ViewModel pattern anchors the architecture cluster that also covers LiveData and Kotlin Flows.

## Related
- [[wiki/android-core/android-lifecycle|Android Lifecycle]]
- [[wiki/android-core/livedata|LiveData]]
- [[wiki/android-core/jetpack-compose|Jetpack Compose]]
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]]
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
