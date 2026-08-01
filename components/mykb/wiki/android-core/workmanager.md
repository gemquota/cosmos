---
type: "concept"
title: "WorkManager"
description: "Guaranteed, constraint-aware scheduler for deferrable background work"
tags: ["android", "background", "workmanager", "jobs"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# WorkManager

WorkManager schedules deferrable, guaranteed background work with constraints like network type, charging state, and storage space. It survives app restarts, retries with backoff, and supports unique work and chains.
- One-off (OneTimeWorkRequest) or periodic (PeriodicWorkRequest) execution.
- Enqueue constraints and observe results with WorkInfo.
- Preferred over services and alarms for sync and maintenance jobs.
- Long-running workers can report progress and mark success or failure.

## Related

- [[wiki/mobile-platform/background-execution|Background Execution]] — WorkManager is the platform-recommended path
- [[wiki/android-core/android-services|Android Services]] — services are the manual alternative
- [[wiki/android-core/alarmscheduler|AlarmScheduler]] — exact timing needs alarms instead
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — work is often triggered by pushes
