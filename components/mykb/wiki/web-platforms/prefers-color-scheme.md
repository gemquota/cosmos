---
type: "concept"
title: "prefers-color-scheme"
description: "Media query detecting light or dark system preference"
tags: ["css", "dark-mode", "media-queries", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# prefers-color-scheme

## Summary

prefers-color-scheme matches the OS-level light/dark preference, letting sites ship a native-feeling theme without user tracking. Combined with token-based theming and a manual override, it is the backbone of dark mode.

## Details
- Mechanism: @media (prefers-color-scheme: dark) { ... } applies when the OS/browser reports dark; the feature can also be read from JS via matchMedia('(prefers-color-scheme: dark)'). The browser's own UI (scrollbars, form controls) respects the same preference when the color-scheme property is set.
- Concrete example: defining --surface/--text tokens per scheme and switching only tokens keeps every component themed; <meta name="color-scheme" content="light dark"> plus CSS color-scheme: light dark makes native controls match the page instead of staying white in dark mode.
- Failure modes: inverting colors instead of re-theming (images, brand hues, shadows break); components with hard-coded colors overriding tokens; scrollbars and native controls ignoring the theme; and the common bug of applying dark styles but keeping light favicon/theme-color, flashing white in browser chrome.
- Operational tradeoffs: a manual override (light/dark/system) must persist and win over the media query; syncing multiple tabs via storage events is a small but real feature. Token sets double the contrast-audit surface — test both schemes against WCAG.
- RSIS3/mykb relevance: the dashboard themes via tokens with a persisted override; telemetry records scheme adoption so design-notes stay informed by real usage.
- Meta theme-color: update the theme-color meta tag per scheme so the browser chrome (mobile URL bar) matches the page instead of flashing light in dark mode.
- Transition hygiene: theme switches that animate colors must respect prefers-reduced-motion, or the flash is both ugly and disruptive for motion-sensitive users.
- FOUC prevention: inline the initial theme decision (or set color-scheme early) so dark-mode users do not see a light flash before the token swap; the flash is the most common dark-mode complaint.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/dark-mode-practice|Dark Mode Practice]]
- [[wiki/web-platforms/prefers-contrast|prefers-contrast]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/frontend-frameworks/material-design|Material Design]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
