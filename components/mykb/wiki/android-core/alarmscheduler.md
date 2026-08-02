---
type: "concept"
title: "AlarmScheduler"
description: "AlarmManager scheduling for exact and inexact alarms"
tags: ["android", "alarms", "scheduling", "background"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/develop/background-work/services/alarms/schedule", "https://developer.android.com/reference/android/app/AlarmManager"]
---

# AlarmScheduler

## Summary


## Details
- AlarmManager schedules exact or inexact alarms that fire at a time even when the app is not running, using the system alarm service.
- Exact alarms are restricted on modern Android because of battery abuse; apps must declare the SCHEDULE_EXACT_ALARM permission and may be denied.
- For work that only needs to happen around a time — not exactly at it — inexact alarms and WorkManager are the battery-friendly choices.
- Alarms do not survive reboots unless the app re-schedules them with BOOT_COMPLETED, which is a common bug.
- **Worked example / comparison** — Worked example — a medication reminder needs exact delivery, so it uses an exact alarm plus a broadcast receiver; a daily digest, in contrast, uses inexact scheduling or WorkManager.
- For mykb, AlarmManager is documented as the precise-timing tool, with freshness review important because Android's alarm policies change frequently.

## Related
- [[wiki/mobile-platform/background-execution|Background Execution]]
- [[wiki/android-core/workmanager|WorkManager]]
- [[wiki/android-core/android-services|Android Services]]
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/decision-guides|Decision Guides]]
