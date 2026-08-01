---
type: "concept"
title: "ANR Diagnostics"
description: "Application Not Responding causes and trace-based diagnosis"
tags: ["android", "anr", "diagnostics", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# ANR Diagnostics

ANR (Application Not Responding) happens when the main thread is blocked too long - input dispatch, broadcast, or service timeouts. Diagnosis starts with /data/anr traces and the ANR dialog details.
- Causes: main-thread IO, locks, binder contention, or runaway work.
- Read trace.txt CPU and thread state to find the blocker.
- Fix by moving work off the main thread and fixing lock ordering.
- Watchdog-style telemetry on the main thread catches jank early.

## Related

- [[wiki/android-core/app-threading|App Threading]] — ANRs are main-thread violations
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — leaks and ANRs share root causes
- [[wiki/android-core/crash-reporting|Crash Reporting]] — ANRs and crashes share tooling
- [[wiki/devops-infra/observability|Observability]] — track ANR rates like any metric
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — ANRs are lifecycle violations
