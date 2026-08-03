---
type: "concept"
title: "Kotlin Coroutines"
description: "Structured concurrency with suspend functions for Android"
tags: ["kotlin", "coroutines", "concurrency", "android"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kotlinlang.org/docs/coroutines-guide.html", "https://kotlinlang.org/docs/coroutines-basics.html"]
---

# Kotlin Coroutines

## Summary


## Details
- Coroutines suspend execution without blocking threads: suspend functions pause at suspension points and resume later, letting one thread serve many concurrent tasks.
- Structured concurrency scopes work (launch, async) to a lifecycle, so cancellation propagates and leaks are prevented.
- Dispatchers control which thread pool runs what: Main for UI, IO for blocking work, Default for CPU-bound computation.
- The mental model is sequential-looking code that is actually concurrent, which removes callback nesting and thread-switch bugs.
- **Worked example / comparison** — Worked example — fetching two sources concurrently is two async calls inside a coroutineScope; if one fails, the scope cancels the other and rethrows.
- Cancellation is cooperative: suspend functions check for cancellation at suspension points and throw CancellationException, so cleanup via try/finally or NonCancellable keeps resources released.
- Flows are the streaming counterpart: cold flows emit on collection, operators transform lazily, and state flows expose the latest value to the UI with lifecycle-aware collection.
- Exception handling differs from threads: a coroutine that throws without a handler crashes the scope, so SupervisorJob and try/catch around async are deliberate choices.
- Structured concurrency is what prevents leaks: every coroutine is scoped to a lifecycle, cancellation propagates from parent to children, and scopes are cancelled in onDestroy or onCleared.
- Dispatchers can be switched mid-flow with withContext, letting IO-bound suspend calls run off the main thread while the caller's structure stays unchanged.
- Suspension is not blocking: a suspended coroutine releases its thread, so a dispatcher with a handful of threads can serve thousands of concurrent tasks, which is why suspend functions are the backbone of Android networking and IO layers.
- For mykb, coroutines are the concurrency backbone of Android tooling; the wiki's own daemons would use the same suspend-and-resume model.

## Related
- [[wiki/android-core/kotlin-language|Kotlin Language]]
- [[wiki/android-core/kotlin-flows|Kotlin Flows]]
- [[wiki/android-core/app-threading|App Threading]]
- [[wiki/android-core/android-lifecycle|Android Lifecycle]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
