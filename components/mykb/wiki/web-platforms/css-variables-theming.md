---
type: "concept"
title: "CSS Variables and Theming"
description: "Custom properties, inheritance, and token-driven light/dark theming"
tags: ["css", "variables", "theming", "design-tokens", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties", "https://www.w3.org/TR/css-variables-1/"]
---
# CSS Variables and Theming

## Summary
CSS custom properties (`--token: value`) hold values that cascade and can change at runtime. They power design-token systems: define tokens once, override them in themes or scopes, and components consume tokens instead of literals. Theming swaps token values rather than stylesheets.

## Details
- **Cascade and inheritance** — custom properties inherit; overriding on `:root` or a container changes the subtree; `var()` resolves at computed-value time.
- **Theming** — `[data-theme="dark"]` or `prefers-color-scheme` overrides tokens; `color-scheme` aligns native controls.
- **Runtime switching** — JS can set property values on the root, enabling live theme toggles without reloads.
- **Limitations** — custom properties are not animatable directly in all engines; media queries cannot read them (container queries can via query units).
- **Worked example** — the mykb UI defines `--surface`, `--text`, and `--accent` tokens; dark mode overrides them once at the root.
- **Relevance** — token-based theming keeps RSIS3's generated screens consistent with the host app.

## Related
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]] — adjacent concept in this wiki
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]] — adjacent concept in this wiki
- [[wiki/web-platforms/color-mix|color-mix() CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/contrast-ratios|Contrast Ratios]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
