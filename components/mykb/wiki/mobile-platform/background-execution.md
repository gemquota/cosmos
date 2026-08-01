---
type: "concept"
title: "Background Execution"
description: "Platform rules and APIs for work that runs when the app is not in the foreground"
tags: ["mobile", "background", "doze", "workmanager", "constraints"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started"]
---

# Background Execution

## Summary

Background execution is any work that runs when the app is not foregrounded, and mobile platforms constrain it heavily to protect battery and privacy. Android enforces Doze, App Standby, and foreground-service limits; iOS offers BGTaskScheduler and push-driven refresh. WorkManager is the recommended API for deferrable, guaranteed Android work.

## Details

- Doze defers network, jobs, and alarms when the device is stationary with the screen off; App Standby buckets apps by usage frequency.
- Foreground services need a visible notification and a declared type, and some types have time limits.
- WorkManager adds constraints (network, charging, storage quota), retries with backoff, unique work, and chains.
- AlarmManager handles exact alarms that users expect (alarms, calendar), while inexact alarms batch for battery.
- iOS uses BGAppRefreshTask and BGProcessingTask scheduled by the OS, plus silent push to trigger refresh.
- The pattern to remember: defer what can wait, batch what must run, and make everything resumable.
- RSIS3 relevance: always-on agent loops on Android must live in a foreground service or schedule via WorkManager to survive.

## Related

- [[wiki/android-core/workmanager|WorkManager]] — the default scheduler for deferrable background work
- [[wiki/android-core/alarmscheduler|AlarmScheduler]] — exact alarms for user-visible timing
- [[wiki/mobile-platform/background-fetch|Background Fetch]] — periodic refresh on iOS and Android
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]] — constraints exist to protect battery
- [[wiki/api-protocols/message-queues|Message Queues]] — queued background processing pattern
- [[wiki/devops-infra/observability|Observability]] — knowing what ran and when
