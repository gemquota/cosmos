---
type: "concept"
title: "Wear OS"
description: "Wearable platform for watch faces, tiles, and complications"
tags: ["android", "wear", "wearables", "watch"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Wear OS

Wear OS is Google wearable platform for smartwatches, with tiles for glanceable info, watch faces, and complications. Apps are built with a wearable UI toolkit and constrained hardware in mind.
- Tiles update without a full app; complications live on watch faces.
- Health and sensor APIs (HR, step count) drive fitness apps.
- Battery and connectivity (BLE, Wi-Fi) are the hard constraints.
- Companion phone apps share data through sync.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — Wear OS is a tuned Android profile
- [[wiki/android-core/android-services|Android Services]] — watch apps rely on background services
- [[wiki/android-core/sensors-api|Sensors API]] — wearables are sensor platforms
- [[wiki/android-core/bluetooth-le|Bluetooth LE]] — the primary watch connectivity
