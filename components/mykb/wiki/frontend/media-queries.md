---
type: "concept"
title: "Media Queries"
description: "Querying viewport and device features for conditional styles"
tags: [css", "media-queries", "responsive", "styling", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries", "https://www.w3.org/TR/mediaqueries-5/"]
---

# Media Queries

## Summary
Media queries apply styles conditionally based on viewport size, device capabilities, and user preferences. The classic use is responsive breakpoints, but media queries also handle orientation, hover support, color schemes, and motion preferences. Media Queries Level 5 adds a range syntax that reads like ordinary comparisons.

## Details
- Syntax: @media (min-width: 600px) gates rules on viewport width; and, or (or comma), and not compose conditions.
- Range syntax: (width > 600px) and (400px <= width <= 800px) replace min-/max- forms in modern engines.
- Features: orientation, aspect-ratio, hover and pointer distinguish touch from fine pointers, and display-mode targets PWAs.
- Preferences: prefers-color-scheme, prefers-reduced-motion, prefers-contrast, and forced-colors adapt to user settings.
- Stylesheet-level: media attributes on link elements let the browser download stylesheets lazily when the query matches.
- Practice: keep breakpoints content-driven, avoid device-specific widths, and remember emulation differs from real devices.

## Related
- [[wiki/frontend/responsive-design|Responsive Design]] — the discipline media queries enable
- [[wiki/frontend/container-queries|Container Queries]] — sizing styles by container instead
- [[wiki/frontend/prefers-reduced-motion|Reduced Motion]] — a user-preference query
- [[wiki/frontend/theming|Theming]] — prefers-color-scheme powers dark mode
- [[wiki/frontend/mobile-first-design|Mobile-First Design]] — the authoring order queries follow
- [[wiki/web-platforms/css-layout|CSS Layout]] — the styling platform media queries gate
