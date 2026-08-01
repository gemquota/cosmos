---
type: "concept"
title: "Android Services"
description: "Long-running or background components without a UI, constrained by Android background execution limits"
tags: ["android", "services", "background", "foreground", "workmanager"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/components/services"]
---

# Android Services

## Summary

A Service is a component that performs long-running operations without a user interface, either started by an intent or bound to a client. Android distinguishes started, bound, and foreground services, and newer versions strictly limit when background services may start. For deferrable work the platform recommends WorkManager instead of raw services.

## Details

- Started services run until stopSelf or stopService is called; bound services expose a client-server interface through onBind and die when no clients remain.
- Foreground services must call startForeground with a persistent notification and a declared foregroundServiceType; time limits apply for some types such as camera or microphone use.
- Background execution limits: starting a service while the app is in the background is restricted, with exemptions for events like user actions, high-priority FCM messages, or broadcasts such as BOOT_COMPLETED.
- Doze and App Standby defer background work when the device is idle, so services must tolerate delay (see battery-aware development).
- WorkManager offers guaranteed, constraint-aware execution for deferrable work and is the default recommendation for sync and maintenance tasks.
- RSIS3 relevance: a long-running mobile daemon that indexes notes or streams telemetry fits a foreground service with a visible notification, delegating periodic sync to WorkManager.

## Related

- [[wiki/android-core/workmanager|WorkManager]] — the recommended scheduler for deferrable service-like work
- [[wiki/mobile-platform/background-execution|Background Execution]] — the OS rules that constrain when services may start
- [[wiki/android-core/notification-channels|Notification Channels]] — foreground services must surface a persistent channel notification
- [[wiki/android-core/android-broadcast-receivers|Broadcast Receivers]] — receivers hand off heavy work to services
- [[wiki/api-protocols/websockets|WebSockets]] — persistent sockets that keepalive daemon services
- [[wiki/devops-infra/observability|Observability]] — service health and liveness for mobile daemons
