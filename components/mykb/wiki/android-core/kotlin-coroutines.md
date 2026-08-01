---
type: "concept"
title: "Kotlin Coroutines"
description: "Structured concurrency with suspend functions for Android"
tags: ["kotlin", "coroutines", "concurrency", "android"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Kotlin Coroutines

Coroutines bring structured concurrency to Kotlin: suspend functions pause without blocking threads, and coroutine scopes tie work to component lifecycles. They are the standard way Android code does IO, networking, and parallel work.
- Dispatchers (Main, IO, Default) route work to the right thread pools.
- Cancellation is cooperative and propagates through child coroutines.
- Retrofit, Room, and DataStore all expose suspend APIs.
- SupervisorJob and coroutineScope isolate failure domains.

## Related

- [[wiki/android-core/kotlin-language|Kotlin Language]] — coroutines are core Kotlin
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — reactive streams built on coroutines
- [[wiki/android-core/app-threading|App Threading]] — coroutines formalize threading rules
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — scopes must follow component lifetimes
