---
type: "concept"
title: "App Threading"
description: "Main-thread rules and background threading models for Android"
tags: ["android", "threading", "performance", "main-thread"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# App Threading

Android UI runs on a single main thread; network and disk work must move to background threads or the app stutters and ANRs. Coroutines, executors, and HandlerThreads are the standard tools.
- The main thread handles input and drawing; keep it under 16ms per frame.
- Never block with network or disk IO; use coroutines with IO dispatcher.
- Thread-safety: shared state needs synchronization or confinement.
- StrictMode flags accidental main-thread IO during development.

## Related

- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]] — structured concurrency replaces raw threads
- [[wiki/android-core/anr-diagnostics|ANR Diagnostics]] — blocking the main thread is the ANR cause
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — threads leak when not shut down
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — threads must respect component lifetimes
