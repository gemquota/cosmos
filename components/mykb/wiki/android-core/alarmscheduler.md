---
type: "concept"
title: "AlarmScheduler"
description: "AlarmManager scheduling for exact and inexact alarms"
tags: ["android", "alarms", "scheduling", "background"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# AlarmScheduler

AlarmManager fires intents or PendingIntents at a time, exact when the user expects it (alarms, calendar) and inexact for everything else. Inexact alarms batch for battery; Doze can defer even exact ones.
- setExactAndAllowWhileIdle for user-visible events; setAndAllowWhileIdle for urgent-ish.
- SCHEDULE_EXACT_ALARM permission and USE_EXACT_ALARM for alarm-clock apps.
- Most deferred work belongs in WorkManager, not alarms.
- Prefer setInexactRepeating or WorkManager for periodic tasks.

## Related

- [[wiki/mobile-platform/background-execution|Background Execution]] — alarms are one tool in the background toolbox
- [[wiki/android-core/workmanager|WorkManager]] — the default for deferrable periodic work
- [[wiki/android-core/android-services|Android Services]] — alarms often start services
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]] — alarms are a battery trade-off
