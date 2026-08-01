---
type: "concept"
title: "Background Fetch"
description: "Periodic background refresh on iOS and Android"
tags: ["mobile", "background", "fetch", "sync"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Background Fetch

Background fetch refreshes app data periodically without user action: BGAppRefreshTask on iOS and WorkManager periodic work on Android. It is the polite way to keep caches fresh and sync queues drained.
- iOS schedules by system discretion; no guaranteed interval.
- Android: PeriodicWorkRequest with flexible intervals and constraints.
- Fetch small deltas, not full payloads, to respect quota.
- Pair with push for urgent invalidation.

## Related

- [[wiki/mobile-platform/background-execution|Background Execution]] — the platform rules that shape fetch
- [[wiki/android-core/workmanager|WorkManager]] — Android scheduling mechanism
- [[wiki/mobile-platform/mobile-data-sync|Mobile Data Sync]] — what background fetch triggers
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — fetch keeps local caches fresh
