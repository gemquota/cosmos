---
type: "concept"
title: "prefers-contrast"
description: "Media query adapting UI to high-contrast preferences"
tags: ["css", "accessibility", "media-queries", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# prefers-contrast

## Summary

prefers-contrast signals the user's OS-level contrast preference — more, less, or no-preference — letting sites boost readability or offer low-contrast variants. It complements WCAG by reacting to user intent, not just computed ratios.

## Details
- Mechanism: @media (prefers-contrast: more) matches when the OS requests higher contrast; less requests reduced; no-preference is the default; browsers expose it to JS via matchMedia. It is distinct from prefers-color-scheme and from the forced-colors (Windows High Contrast) mode.
- Concrete example: a dashboard enables stronger borders and darker text tokens under prefers-contrast: more, and offers a soft "less" theme for users who find default contrast harsh; forced-colors mode separately strips custom backgrounds so system contrast takes over.
- Failure modes: assuming more means pure black/white (it often means stronger edges and separation); writing overrides that fight forced-colors; applying contrast styles to images or brand surfaces where they distort meaning; and testing only simulated settings rather than real OS configurations.
- Operational tradeoffs: contrast preferences are a small-audience but high-need accessibility surface; the cheap win is ensuring forced-colors support and never hard-coding colors that break under it. Treat prefers-contrast: more as a token-swap layer like dark mode.
- RSIS3/mykb relevance: the wiki UI defines a high-contrast token overlay, and the accessibility check in the loop verifies it against the WCAG contrast audit.
- Forced-colors: ensure forced-colors: active does not break layout by relying on custom colors — use system colors and avoid hiding outlines that carry meaning.
- Simulation: DevTools can emulate contrast and forced-colors settings; test both more and less on every major surface, not just text pages.
- Token mapping: define contrast variants as token overrides (--border-strong, --text-strong) rather than scattered rules; a token layer keeps the high-contrast theme maintainable across components.
- Audit both directions: test more and less variants against the real OS settings, not just the emulator defaults.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/prefers-color-scheme|prefers-color-scheme]]
- [[wiki/web-platforms/dark-mode-practice|Dark Mode Practice]]
- [[wiki/web-platforms/prefers-contrast|prefers-contrast]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/frontend-frameworks/material-design|Material Design]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
