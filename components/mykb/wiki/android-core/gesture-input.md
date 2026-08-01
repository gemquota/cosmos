---
type: "concept"
title: "Gesture Input"
description: "Touch gestures, system back gestures, and gesture navigation"
tags: ["android", "gestures", "input", "navigation"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Gesture Input

Gesture input covers touch handling (taps, swipes, long-presses), the predictive back gesture, and edge-to-edge gesture navigation. Android 10+ replaced the button bar with gestures that apps must respect.
- GestureDetector and GestureDetectorCompat parse raw touch events.
- Edge-to-edge apps draw behind system bars and handle insets.
- Predictive back lets the system preview where a back gesture lands.
- Compose pointer input APIs wrap the same gesture pipeline.

## Related

- [[wiki/android-core/android-activities|Android Activities]] — gestures drive activity navigation
- [[wiki/android-core/haptics|Haptics]] — gestures pair with haptic feedback
- [[wiki/android-core/edge-to-edge|Edge-to-Edge]] — gesture navigation needs inset handling
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — gestures must have accessible alternatives
