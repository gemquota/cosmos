---
type: "concept"
title: "Battery-Aware Development"
description: "Treating battery as a first-class resource through batching, constraints, and measurement"
tags: ["mobile", "battery", "performance", "doze", "power"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/performance/power"]
---

# Battery-Aware Development

## Summary

Battery is a first-class mobile resource: Doze, App Standby, and foreground-service limits penalize apps that work aggressively in the background. Battery-aware development batches work, avoids wake locks, uses constraint-based scheduling, and measures power with profilers. Users uninstall battery hogs, so this is also a retention strategy.

## Details

- Doze and App Standby defer network, jobs, and alarms when the device idles; design work to tolerate deferral.
- Avoid partial wake locks; prefer foreground services only when the user sees value, and let WorkManager handle the rest.
- Location requests should match real needs: low accuracy, long intervals, geofencing, or passive updates instead of continuous GPS.
- Batch network sync and defer uploads to charging and unmetered connections; adapt media quality to network conditions.
- Measure with the battery profiler and Battery Historian; watch wake-ups, sensor usage, and per-feature drain.
- RSIS3 relevance: always-on device agents must batch and defer to stay invisible in battery stats, or users will kill them.

## Related

- [[wiki/mobile-platform/background-execution|Background Execution]] — the platform rules battery-aware code follows
- [[wiki/android-core/workmanager|WorkManager]] — constraints encode charging and network preferences
- [[wiki/android-core/alarmscheduler|AlarmScheduler]] — exact alarms are the exception to batching
- [[wiki/android-core/sensors-api|Sensors API]] — sensor batching reduces power draw
- [[wiki/mobile-platform/mobile-network-optimization|Mobile Network Optimization]] — less network means less battery
- [[wiki/devops-infra/observability|Observability]] — power telemetry belongs in observability
- [[wiki/api-protocols/websockets|WebSockets]] — persistent connections trade radio power for latency
