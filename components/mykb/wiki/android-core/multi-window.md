---
type: "concept"
title: "Multi-Window"
description: "Split-screen, freeform, and resizable activity windows"
tags: ["android", "multi-window", "layout", "activity"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Multi-Window

Multi-window lets apps share the screen: split-screen on phones, freeform on desktops, and resizable windows generally. Activities must handle resize, small sizes, and configuration changes.
- resizableActivity declares multi-window participation; API 24+ defaults apply.
- Picture-in-picture is a special resizable mode for continuous content.
- Layouts reflow via window size classes instead of assuming fullscreen.
- App compat concerns: min sizes, orientation locks, and insets.

## Related

- [[wiki/android-core/android-activities|Android Activities]] — activities are the resizable unit
- [[wiki/android-core/picture-in-picture|Picture-in-Picture]] — the floating-window mode
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — reflow rules for smaller windows
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — resize triggers lifecycle events
