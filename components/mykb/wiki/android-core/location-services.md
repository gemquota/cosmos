---
type: "concept"
title: "Location Services"
description: "Fused location provider with permissions and power-aware updates"
tags: ["android", "location", "gps", "permissions"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Location Services

Location services on Android center on the FusedLocationProviderClient, which blends GPS, Wi-Fi, and cell signals. Updates require runtime location permission and should match accuracy to need.
- Request ACCESS_FINE_LOCATION or COARSE depending on accuracy needs.
- setInterval and setSmallestDisplacement trade battery for freshness.
- Background location needs extra permission and scrutiny.
- Geofencing and passive updates cut power further.

## Related

- [[wiki/android-core/android-permissions|Android Permissions]] — location permission is the gate
- [[wiki/android-core/geofencing|Geofencing]] — region-based location triggers
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]] — location polling is a top battery cost
- [[wiki/mobile-platform/mobile-network-optimization|Mobile Network Optimization]] — network location is cheaper than GPS
