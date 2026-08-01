---
type: "concept"
title: "ViewModel Pattern"
description: "Configuration-stable holder for UI state that survives activity recreation"
tags: ["android", "viewmodel", "state", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# ViewModel Pattern

A ViewModel holds UI state and survives configuration changes such as rotation, so data survives recreation without leaking the old screen. It exposes state to the UI and offloads business logic from components.
- Created via viewModels() and scoped to an activity or fragment; cleared on finish.
- Never hold references to views or contexts that can leak; expose state instead.
- Compose reads ViewModel state with collectAsStateWithLifecycle.
- It is the state-holder half of modern Android architecture.

## Related

- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — ViewModel survives the lifecycle transitions
- [[wiki/android-core/livedata|LiveData]] — classic observable paired with ViewModels
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Compose consumes ViewModel state reactively
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — the pattern generalizes across toolkits
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — state survival parallels agent checkpoints
