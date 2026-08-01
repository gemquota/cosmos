---
type: "concept"
title: "Adaptive Layouts"
description: "Layouts driven by window size classes instead of device guesses"
tags: ["mobile", "layout", "adaptive", "large-screen"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Adaptive Layouts

Adaptive layouts respond to window size classes - compact, medium, expanded - so the same code serves phones, tablets, and foldables. Navigation and content change form at each class.
- Compact: bottom navigation; Expanded: navigation rail or drawer.
- List-detail panes emerge at medium and expanded widths.
- Compose adaptive components (Material3 adaptive) implement the patterns.
- Test across resizable windows, not just device names.

## Related

- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — the umbrella principle
- [[wiki/mobile-platform/tablet-support|Tablet Support]] — tablets are the canonical large screen
- [[wiki/android-core/foldables-support|Foldables Support]] — foldables cross size classes
- [[wiki/frontend-frameworks/material-design|Material Design]] — M3 defines adaptive components
