---
type: "concept"
title: "CSS Architecture"
description: "Organizing stylesheets for maintainability: naming, specificity, layers, and design tokens"
tags: ["css", "architecture", "design-systems", "maintainability", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/How_CSS_is_structured", "https://css-tricks.com/css-modules-part-1-need/"]
---
# CSS Architecture

## Summary
CSS architecture is the discipline of keeping styles predictable as apps grow: bounded specificity, scoped selectors, consistent naming, and design tokens. Methodologies like BEM, CSS Modules, and utility classes coexist; Cascade Layers add explicit priority control.

## Details
- **Specificity and cascade** — ID vs class vs type selectors and `!important` create priority; layers (`@layer`) let teams order whole subsystems instead of fighting specificity.
- **Naming conventions** — BEM (block, element, modifier) keeps selectors flat and readable; utility classes (Tailwind-style) trade markup noise for consistency.
- **Encapsulation** — CSS Modules, Shadow DOM, and styled-components scope styles to components; global styles stay in tokens and reset layers.
- **Tokens** — colors, spacing, and type live in custom properties; theming swaps token values without selector surgery.
- **Worked example** — the mykb dashboard uses layered CSS with design tokens for light/dark theming, keeping new components on tokens instead of magic values.
- **Relevance** — RSIS3's generated UIs should follow the same token discipline so agent-rendered screens stay consistent.

## Related
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/z-index-management|Z-Index Management]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
