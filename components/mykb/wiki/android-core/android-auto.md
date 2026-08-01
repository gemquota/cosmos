---
type: "concept"
title: "Android Auto"
description: "Android for cars with safe, template-driven driving UIs"
tags: ["android", "auto", "automotive", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Android Auto

Android Auto projects an optimized app UI onto car screens, constrained to glanceable templates for safe driving. Media, messaging, navigation, and parking apps get templates; custom layouts are not allowed.
- Build with AndroidX car-app library templates (lists, grids, message screens).
- Audio apps must handle audio focus and playback resumption.
- Testing uses the desktop head unit emulator.
- Phone projection and built-in (AAOS) share the template model.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — Auto runs on the Android stack
- [[wiki/android-core/wear-os|Wear OS]] — the sibling constrained form factor
- [[wiki/android-core/android-tv|Android TV]] — another template-driven surface
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — glanceability is accessibility
