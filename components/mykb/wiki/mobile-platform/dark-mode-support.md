---
type: "concept"
title: "Dark Mode Support"
description: "Dark theme support with dynamic color and system preference detection"
tags: ["mobile", "dark-mode", "theming", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Dark Mode Support

Dark mode adapts UI to low-light and user preference, driven by the system setting and in-app toggles. Material 3 dynamic color and Compose theming make dark themes a token switch rather than a redesign.
- Detect isSystemInDarkTheme and theme composables accordingly.
- Design tokens (M3 dynamic color) generate dark palettes.
- Test contrast: dark mode breaks hardcoded colors.
- Photos and media need dark-aware treatment.

## Related

- [[wiki/frontend-frameworks/material-design|Material Design]] — M3 tokens implement dark themes
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — theming APIs handle dark mode
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — theme and size are independent axes
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — contrast rules apply in both themes
