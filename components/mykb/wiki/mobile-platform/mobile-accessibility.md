---
type: "concept"
title: "Mobile Accessibility"
description: "Screen readers, semantics, and touch-target design for mobile"
tags: ["mobile", "accessibility", "a11y", "screen-reader"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Mobile Accessibility

Mobile accessibility means the app works with TalkBack and VoiceOver, dynamic type, switch access, and reduced motion. Semantics on views and composables plus 48dp touch targets are the baseline.
- Provide content descriptions and live regions for dynamic content.
- Compose semantics and iOS accessibility modifiers expose the tree.
- Support font scaling (sp) without layout breakage.
- Test with screen readers, not just contrast checkers.

## Related

- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — dynamic type is part of responsiveness
- [[wiki/mobile-platform/localization|Localization]] — locale and accessibility interact
- [[wiki/frontend-frameworks/material-design|Material Design]] — touch targets come from the spec
- [[wiki/android-core/android-architecture|Android Architecture]] — TalkBack rides the accessibility framework
