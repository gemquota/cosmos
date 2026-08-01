---
type: "concept"
title: "Home Screen Widgets"
description: "Glanceable home-screen surfaces on Android and iOS"
tags: ["android", "widgets", "homescreen", "ux"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Home Screen Widgets

Home-screen widgets are glanceable app surfaces on the launcher: Android AppWidgets with RemoteViews and iOS Home Screen widgets with SwiftUI timelines. They are a retention surface that shows data without opening the app.
- Android: AppWidgetProvider + RemoteViews, updated via WorkManager.
- iOS: WidgetKit timelines rendered with SwiftUI.
- Widgets should be lightweight, glanceable, and battery-friendly.
- Tap actions deep-link into the app.

## Related

- [[wiki/android-core/widget-providers|Widget Providers]] — Android implementation
- [[wiki/mobile-platform/ios-platform|iOS Platform]] — iOS Home Screen widgets via WidgetKit
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — widgets and notifications share update triggers
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Glance builds widgets with Compose
