---
type: "concept"
title: "Push Notifications"
description: "Platform-mediated delivery of timely messages to users, via FCM and APNs"
tags: ["mobile", "push", "notifications", "fcm", "apns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://firebase.google.com/docs/cloud-messaging"]
---

# Push Notifications

## Summary

Push notifications deliver time-sensitive messages to users even when the app is closed, mediated by platform services: Firebase Cloud Messaging (FCM) on Android and iOS, with APNs underneath on iOS. Apps register for a per-install token and route delivery through their backend. Push is best-effort transport: handlers must be idempotent and graceful.

## Details

- Each install gets an FCM token that the app sends to its backend; tokens rotate, so stale tokens must be pruned.
- Notification messages render via the OS (with channels on Android); data messages wake the app for custom handling.
- Android 13+ requires the POST_NOTIFICATIONS runtime permission; iOS prompts on first request, so design opt-in UX.
- Delivery is not guaranteed: no connectivity, throttling, and user settings all drop messages, so always pair with in-app refresh.
- Notification taps should deep-link into the relevant content, and analytics should track engagement.
- RSIS3 relevance: a companion app could push task completions and heartbeat alerts from agent loops to the phone lock screen.

## Related

- [[wiki/android-core/notification-channels|Notification Channels]] — Android user controls for notification categories
- [[wiki/mobile-platform/background-fetch|Background Fetch]] — background refresh complements push delivery
- [[wiki/android-core/workmanager|WorkManager]] — deferring processing of received payloads
- [[wiki/api-protocols/websockets|WebSockets]] — realtime alternative when push is insufficient
- [[wiki/api-protocols/idempotency|Idempotency]] — redelivered push payloads must not double-process
- [[wiki/ml-frameworks/server-sent-events|Server-Sent Events]] — browser-side push analog
