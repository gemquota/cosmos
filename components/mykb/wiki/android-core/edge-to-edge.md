---
type: "concept"
title: "Edge-to-Edge"
description: "Drawing app content behind system bars with inset handling"
tags: ["android", "edge-to-edge", "insets", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Edge-to-Edge

Edge-to-edge apps draw behind the status and navigation bars, using WindowInsets to reserve space for gestures and bars. It is the default visual model on modern Android.
- EnableWindowEdgeToEdge or Compose edge-to-edge APIs apply the look.
- Insets: systemBars, displayCutout, and ime insets drive padding.
- Predictive back and gesture navigation assume edge-to-edge.
- Mis-handled insets cause content under the bars.

## Related

- [[wiki/android-core/gesture-input|Gesture Input]] — gesture navigation pairs with edge-to-edge
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Compose handles insets declaratively
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — insets vary by form factor
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — drawing full-bleed is responsive behavior
