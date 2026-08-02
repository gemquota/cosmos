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
- For mykb, coroutines are the concurrency backbone of Android tooling; the wiki's own daemons use the same suspend-and-resume model.

## Related
- [[wiki/android-core/kotlin-language|Kotlin Language]]
- [[wiki/android-core/kotlin-flows|Kotlin Flows]]
- [[wiki/android-core/app-threading|App Threading]]
- [[wiki/android-core/android-lifecycle|Android Lifecycle]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
