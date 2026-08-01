---
type: "concept"
title: "Geofencing"
description: "Trigger app actions when the device enters or exits a geographic region"
tags: ["android", "geofencing", "location", "events"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Geofencing

Geofencing fires transitions when a device crosses a defined region, via GeofencingClient with a PendingIntent. It is a low-power way to make location-aware features reactive.
- Define Geofence objects with radius, expiration, and transitions (ENTER, EXIT, DWELL).
- Requires location permission and works best with coarse accuracy.
- The system batches checks to protect battery.
- Handlers should schedule work (WorkManager) rather than run long tasks.

## Related

- [[wiki/android-core/location-services|Location Services]] — geofences consume location updates
- [[wiki/android-core/android-services|Android Services]] — transitions often wake a service
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]] — geofencing is the battery-friendly trigger
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — region events can notify users
