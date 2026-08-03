---
type: "concept"
title: "App Threading"
description: "Main-thread rules and background threading models for Android"
tags: ["android", "threading", "performance", "main-thread"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# App Threading

Android UI runs on a single main thread; network and disk work must move to background threads or the app stutters and ANRs. Coroutines, executors, and HandlerThreads are the standard tools.
- The main thread handles input and drawing; keep it under 16ms per frame.
- Never block with network or disk IO; use coroutines with IO dispatcher.
- Thread-safety: shared state needs synchronization or confinement.
- StrictMode flags accidental main-thread IO during development.

## Details

- **The 16ms budget** — the main thread must handle input, layout, and drawing within the frame budget (16.6ms at 60Hz, ~8ms at 120Hz); anything that pushes past the budget drops frames, and sustained drops show up as jank; the budget includes everything the app does between frames, so main-thread work must be measured as a whole, not per-task.
- **What must leave the main thread** — network IO (sockets, HTTP), disk IO (file reads, database queries, SharedPreferences writes), image decoding, JSON parsing of large payloads, and any long computation; coroutines with Dispatchers.IO or Dispatchers.Default are the modern tool, executors and HandlerThreads still appear in legacy code, and WorkManager handles deferrable background work with system-managed scheduling.
- **Thread-safety** — shared state needs synchronization or confinement: confine mutable UI state to the main thread, use atomic types or locks for cross-thread counters, and prefer single-writer patterns so background workers publish results via a single channel; races in Android show up as occasional crashes or corrupted state that are nearly impossible to reproduce, so correctness here is preventive.
- **Lifecycle coupling** — background work must respect component lifetimes: launching a coroutine without scope awareness leaks the thread (or the Activity), and callbacks that touch a destroyed Activity crash; scope work to the ViewModel or lifecycle owner, cancel on clear, and never assume a background task will finish before the UI is gone.
- **Failure modes** — the classic bugs are blocking the main thread with a query that was fine in tests but slow in production data, lock contention between a worker and the main thread, thread pools exhausted by unbounded parallel work, and callbacks posted to the wrong looper; each is a different fix, so diagnosis starts with where the block is, not what the symptom is.
- **Tooling** — StrictMode flags accidental main-thread IO during development (disk read/write and network violations log as soon as they happen); systrace and Perfetto show where frames actually go; and a main-thread watchdog (periodic runnable with a stack dump on stall) catches near-ANR stalls in production before the system's own timeout fires.
- **RSIS3 relevance** — any Android capture or telemetry hook RSIS3 runs inherits these rules: keep the capture path non-blocking (async uploads, batched writes), scope work to the app's lifecycle, and treat main-thread stalls as loop health events rather than silent failures.


## Related
- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]] — structured concurrency replaces raw threads
- [[wiki/android-core/anr-diagnostics|ANR Diagnostics]] — blocking the main thread is the ANR cause
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — threads leak when not shut down
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — threads must respect component lifetimes
