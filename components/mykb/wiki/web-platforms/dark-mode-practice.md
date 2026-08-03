---
type: "concept"
title: "Dark Mode Practice"
description: "Implementing themeable dark interfaces without jarring contrast"
tags: ["css", "dark-mode", "theming", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Dark Mode Practice

## Summary

Dark mode is a real theming requirement driven by prefers-color-scheme, user expectation, and OLED power savings. Good practice builds it from tokens and logical surfaces, not by inverting colors or bolting on a second stylesheet.

## Details
- Mechanism: media (prefers-color-scheme: dark) lets CSS switch token values; the robust pattern is CSS custom properties — --surface, --text, --border — defined once per scheme, with components referencing tokens only. The browser matches the OS setting, and users can override per site via UA or extension.
- Concrete example: a card uses background: var(--surface) and color: var(--text); the light theme defines --surface: #fff, dark theme --surface: #1a1a1a. Components never hard-code colors, so both themes are consistent by construction. Images and embeds may need filter tweaks (dimming white-background screenshots).
- Failure modes: naive inversion (filter: invert(1)) breaks images and hues; hard-coded grays in components create contrast failures only in dark mode; forgetting scrollbars, shadows (replace with borders/ambient), and focus rings; and forcing a theme without respecting the OS setting or providing a manual override.
- Operational tradeoffs: dual themes double the contrast and color-blind audit surface; tokenization makes it tractable. Also consider auto dark variants of brand colors via color-mix rather than hand-picking. Test both schemes against WCAG contrast and color-blind simulations.
- RSIS3/mykb relevance: the dashboard ships light/dark token sets and records which scheme users prefer in telemetry, feeding the design-notes wiki.
- Auto schemes: prefers-color-scheme can also match OS-level "auto" themes in recent browsers; token sets should define the default scheme explicitly rather than inheriting the UA default.
- Form controls and embeds: native inputs, scrollbars, and third-party iframes may ignore the theme, so style controls via accent-color and color-scheme properties to keep them coherent.
- Media sync: keep the manual override in sync with the OS setting via matchMedia listeners, and persist the user's choice so it survives navigation and reloads.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/prefers-contrast|prefers-contrast]]
- [[wiki/web-platforms/prefers-color-scheme|prefers-color-scheme]]
- [[wiki/web-platforms/dark-mode-practice|Dark Mode Practice]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/frontend-frameworks/material-design|Material Design]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
