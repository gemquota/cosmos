---
type: "concept"
title: "ANR Diagnostics"
description: "Application Not Responding causes and trace-based diagnosis"
tags: ["android", "anr", "diagnostics", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# ANR Diagnostics

ANR (Application Not Responding) happens when the main thread is blocked too long - input dispatch, broadcast, or service timeouts. Diagnosis starts with /data/anr traces and the ANR dialog details.
- Causes: main-thread IO, locks, binder contention, or runaway work.
- Read trace.txt CPU and thread state to find the blocker.
- Fix by moving work off the main thread and fixing lock ordering.
- Watchdog-style telemetry on the main thread catches jank early.

## Details

- **Timeout types** — input dispatch ANRs fire when a key or touch event is not handled within about 5 seconds; broadcast ANRs fire when a receiver does not finish onReceive within 10 seconds (foreground) or 60 seconds (background); service ANRs fire when a service does not finish onCreate/onStart/onBind within 20 seconds (foreground) or 200 seconds (background); knowing which timeout fired narrows the search immediately.
- **Root causes** — the main thread is blocked by synchronous disk IO (SQLite queries, file reads, SharedPreferences apply-on-main), by lock contention (waiting on a background thread holding a lock, often via a callback that runs on the wrong thread), by binder calls that block (querying a ContentProvider or system service that is itself slow), or by runaway work (infinite loops, overly large layout passes, or a single frame taking seconds).
- **Reading the trace** — the /data/anr/trace.txt dump shows every thread's stack at the moment of the ANR; look at the main thread first, find the blocking call (e.g., `android.database.sqlite.SQLiteDatabase.lock` or `BinderProxy.transact`), then check which other threads hold the contended lock; the `CPU usage` header and `total time spent` lines reveal whether the device was overloaded (CPU starvation) or the thread was genuinely stuck.
- **Fix patterns** — move IO off the main thread (coroutines on Dispatchers.IO, WorkManager for deferrable work), fix lock ordering so the main thread never waits on a lock a worker holds, convert synchronous binder calls to async or cache their results, and chunk layout work; StrictMode flags the offending calls during development so the bugs never ship.
- **Failure modes** — the ANR dialog's 'wait' option can mask the problem in testing (production users see 'close'), traces can be empty on some devices (enable dumpsys activity and consider ANR-rate capture), and diagnosing by guesswork fails when the real cause is a slow background thread holding a lock, so always pull the trace before changing code.
- **Operational practice** — treat ANR rate as a release-blocking metric: aggregate ANR counts per screen and per OS version in crash-reporting tooling, set alerts on rate increases after releases, and use watchdog-style telemetry on the main thread (post a runnable every few seconds; if it stops executing, capture a stack dump) to catch near-ANR jank before the system timeout fires.
- **RSIS3 relevance** — if RSIS3 runs any Android-side tooling or mykb capture hooks, ANR diagnostics follow the same pattern as loop health checks: instrument the event loop, capture the stack when it stalls, and fix the blocking dependency rather than just restarting the loop.

## Related

- [[wiki/android-core/app-threading|App Threading]] — ANRs are main-thread violations
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — leaks and ANRs share root causes
- [[wiki/android-core/crash-reporting|Crash Reporting]] — ANRs and crashes share tooling
- [[wiki/devops-infra/observability|Observability]] — track ANR rates like any metric
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — ANRs are lifecycle violations
