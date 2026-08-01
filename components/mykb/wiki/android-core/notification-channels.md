---
type: "concept"
title: "Notification Channels"
description: "User-controllable categories for Android notifications"
tags: ["android", "notifications", "channels", "ux"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Notification Channels

Notification channels group an app notifications into user-controllable categories with importance levels, sounds, and visibility. Users can mute or downgrade channels without disabling the app.
- Create channels with NotificationChannel and an importance (IMPORTANCE_HIGH, etc.).
- Android 8.0+ requires a channel for every notification.
- Notification permission (Android 13+) gates all notification delivery.
- Fewer, well-named channels respect user attention.

## Related

- [[wiki/mobile-platform/push-notifications|Push Notifications]] — FCM messages target channels
- [[wiki/android-core/android-services|Android Services]] — foreground services must post to a channel
- [[wiki/android-core/android-broadcast-receivers|Broadcast Receivers]] — receivers post notifications
- [[wiki/mobile-platform/consent-management|Consent Management]] — channels are part of notification consent UX
