---
type: "concept"
title: "Theming"
description: "Theme switching and dark mode strategies"
tags: [theming", "dark-mode", "css", "custom-properties", "design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme", "https://web.dev/articles/prefers-color-scheme"]
---

# Theming

## Summary
Theming lets one UI render multiple visual variants — light, dark, brand, or high-contrast — by swapping values rather than stylesheets. CSS custom properties make themes data: a theme class or attribute redefines tokens and everything updates. prefers-color-scheme handles system-driven dark mode, and color-scheme aligns native controls.

## Details
- Token-driven: components consume var(--color-surface) so changing the theme changes every surface consistently.
- Theme scoping: html[data-theme="dark"] { ... } redefines tokens; inline style overrides allow per-component themes.
- System preference: @media (prefers-color-scheme: dark) sets the initial theme; a manual toggle overrides it.
- color-scheme: declares which palette native form controls, scrollbars, and canvas use, avoiding mismatched chrome.
- Flash prevention: inline theme bootstrap in the head applies before first paint; persist the choice in storage.
- Accessibility: contrast must hold in every theme, and forced-colors mode may bypass CSS entirely.

## Related
- [[wiki/frontend/design-tokens|Design Tokens]] — the values themes swap
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — the mechanism behind themes
- [[wiki/frontend/media-queries|Media Queries]] — prefers-color-scheme handling
- [[wiki/frontend/design-systems|Design Systems]] — theming across a system
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]] — the native counterpart
- [[wiki/frontend/color-contrast|Color Contrast]] — accessible theme palettes
