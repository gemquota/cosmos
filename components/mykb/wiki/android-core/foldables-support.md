---
type: "concept"
title: "Foldables Support"
description: "Layouts and postures for foldable and large-screen devices"
tags: ["android", "foldables", "large-screen", "layout"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Foldables Support

Foldable support means handling hinged postures, display cutouts, and continuity when a device folds or unfolds. Apps should respond to configuration changes and window size classes rather than assume one shape.
- Track posture (book, tabletop, tent) via WindowLayoutInfo.
- Avoid content in the hinge cutout; use safe drawing areas.
- Continuity: state must survive fold/unfold like rotation.
- Test with the foldable emulator and resizable windows.

## Related

- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — window size classes drive foldable layouts
- [[wiki/mobile-platform/tablet-support|Tablet Support]] — foldables open into tablet layouts
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — the umbrella discipline
- [[wiki/android-core/multi-window|Multi-Window]] — foldables enable split-screen usage
