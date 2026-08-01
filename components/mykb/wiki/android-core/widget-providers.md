---
type: "concept"
title: "Widget Providers"
description: "AppWidgetProvider for home-screen app widgets"
tags: ["android", "widgets", "homescreen", "appwidget"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Widget Providers

AppWidgetProvider is a broadcast-receiver subclass that renders remote views on the home screen, updated via periodic WorkManager or configuration changes. Widgets are a retention surface users see constantly.
- Declared in the manifest with an AppWidgetProviderInfo XML resource.
- RemoteViews support only a limited view set; interactions use PendingIntents.
- Prefer WorkManager over frequent widget updates to save battery.
- Widget previews in the picker come from a layout resource.

## Related

- [[wiki/android-core/home-screen-widgets|Home Screen Widgets]] — the cross-platform widget concept
- [[wiki/android-core/android-broadcast-receivers|Broadcast Receivers]] — widgets are receiver-backed
- [[wiki/android-core/android-manifest|Android Manifest]] — widget provider declaration lives here
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Glance brings compose-style widgets
