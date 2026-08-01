---
type: "concept"
title: "Android Lifecycle"
description: "System-driven state transitions of activities and fragments plus lifecycle-aware state holders"
tags: ["android", "lifecycle", "state", "viewmodel", "process"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/components/activities/activity-lifecycle"]
---

# Android Lifecycle

## Summary

Android components move through system-driven lifecycle states: created, started, resumed, paused, stopped, and destroyed, with configuration changes such as rotation causing teardown and recreation. Lifecycle-aware components observe these transitions so UI and data stay consistent. Getting the lifecycle right prevents crashes, leaks, and lost user state.

## Details

- Key callback pairs are onCreate/onDestroy, onStart/onStop, and onResume/onPause; the resumed state is where the activity interacts with the user.
- Configuration changes (rotation, dark mode, resizing) destroy and recreate the activity by default, unless configChanges opts out.
- ViewModels survive recreation, while onSaveInstanceState preserves transient UI state; durable data belongs in repositories or a persistence layer.
- LifecycleOwner and LifecycleObserver let UI and services react to state without manual plumbing; Compose exposes collectAsStateWithLifecycle for the same job.
- Process death can happen while stopped: never assume instance state persists; write critical data early.
- Leaks and ANRs are lifecycle bugs: unregistering listeners and releasing references on stop is mandatory.
- RSIS3 relevance: long-running agent sessions on Android should checkpoint state at lifecycle boundaries, like agents checkpointing at turn boundaries.

## Related

- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]] — configuration-stable state built on lifecycle semantics
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — lifecycle mistakes are the most common leak source
- [[wiki/android-core/anr-diagnostics|ANR Diagnostics]] — main-thread work in callbacks triggers ANRs
- [[wiki/android-core/app-threading|App Threading]] — threads and lifecycle callbacks must be coordinated
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — agent sessions reuse the same state-transition idea
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — checkpointing maps to lifecycle pause boundaries
