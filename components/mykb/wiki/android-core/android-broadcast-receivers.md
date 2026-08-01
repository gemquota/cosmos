---
type: "concept"
title: "Android Broadcast Receivers"
description: "Lightweight components that react to system-wide or app-wide announcements"
tags: ["android", "broadcast", "receivers", "events", "system"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/components/broadcasts"]
---

# Android Broadcast Receivers

## Summary

Broadcast receivers react to system-wide announcements such as boot completion, connectivity changes, and battery state, or to app-defined events. They are meant to be lightweight: any heavy work must be handed off to a service or WorkManager. Android 8.0 restricted most implicit manifest broadcasts, pushing apps to register receivers explicitly while active.

## Details

- Two registration modes exist: manifest-declared receivers (persistent, for system broadcasts like BOOT_COMPLETED) and context-registered receivers (live only while the registering component is active).
- Implicit broadcast restrictions: most manifest receivers for implicit broadcasts are no longer delivered on Android 8.0+, with a small allowlist of system broadcasts remaining.
- Useful system broadcasts include ACTION_BOOT_COMPLETED, CONNECTIVITY_CHANGE, TIMEZONE_CHANGED, and BATTERY_LOW.
- Receivers run on the main thread and get a short execution window; blocking work causes ANRs, so delegate to WorkManager or a foreground service.
- LocalBroadcastManager is deprecated; prefer in-process observers or PendingIntent delivery.
- RSIS3 relevance: a mobile agent can register for connectivity and boot events to trigger a mykb resync exactly when the network returns.

## Related

- [[wiki/android-core/workmanager|WorkManager]] — the safe place to move work triggered by a receiver
- [[wiki/android-core/notification-channels|Notification Channels]] — receivers often surface results as channel notifications
- [[wiki/android-core/alarmscheduler|AlarmScheduler]] — scheduled alternatives to event-driven wakeups
- [[wiki/api-protocols/webhooks|Webhooks]] — event delivery pattern echoed by broadcast semantics
- [[wiki/devops-infra/observability|Observability]] — event streams for mobile daemon health
- [[wiki/api-protocols/message-queues|Message Queues]] — queued delivery fits deferred broadcast handling
