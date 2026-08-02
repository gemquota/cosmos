---
type: "concept"
title: "WorkManager"
description: "Guaranteed, constraint-aware scheduler for deferrable background work"
tags: ["android", "background", "workmanager", "jobs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/libraries/architecture/workmanager", "https://developer.android.com/reference/androidx/work/WorkManager"]
---

# WorkManager

## Summary


## Details
- WorkManager schedules deferrable background work that is guaranteed to run even if the app or device restarts, using the OS's best available mechanism.
- Work is defined as a Worker class with constraints (network, charging, idle), and enqueued as unique or periodic work with retry and backoff policies.
- It is the recommended replacement for most background jobs: coroutine-friendly, chainable, and observable via LiveData or Flow.
- WorkManager is not for precise timing — alarm-clock scheduling belongs to AlarmManager instead.
- **Worked example / comparison** — Worked example — a weekly wiki-sync job is enqueued with a network constraint and periodic policy; if it fails, the backoff criteria decide when it retries.
- For mykb, WorkManager is documented as the durable background scheduler and is contrasted with AlarmManager for exact-time tasks.

## Related
- [[wiki/mobile-platform/background-execution|Background Execution]]
- [[wiki/android-core/android-services|Android Services]]
- [[wiki/android-core/alarmscheduler|AlarmScheduler]]
- [[wiki/mobile-platform/push-notifications|Push Notifications]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
