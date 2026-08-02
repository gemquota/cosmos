---
type: "concept"
title: "CSS Custom Properties"
description: "Cascading variables for theming and runtime updates"
tags: [css", "custom-properties", "variables", "theming", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties", "https://www.w3.org/TR/css-variables-1/"]
---

# CSS Custom Properties

## Summary
CSS custom properties — variables written as --name and read with var() — hold values that cascade and inherit like ordinary properties. Because they are evaluated at use time, they can change at runtime without regenerating stylesheets. They are the backbone of modern theming, design tokens, and component libraries.

## Details
- Syntax: --accent: #0af; then color: var(--accent, #00f); the second argument is the fallback.
- Inheritance: custom properties flow from ancestors to descendants, so a theme class on html re-themes the whole page.
- Runtime updates: setting el.style.setProperty("--accent", value) restyles instantly, enabling live theme switching.
- Scoping: components can define private defaults while exposing overridable tokens, which works through Shadow DOM.
- Typed values: @property registers syntax, types, and initial values so properties can animate and validate.
- Pitfalls: var() does not work in media-query conditions, and every use re-resolves, so deep dependency chains cost style recalc.

## Related
- [[wiki/frontend/theming|Theming]] — dark mode and theme switching via variables
- [[wiki/frontend/design-tokens|Design Tokens]] — the value system custom properties carry
- [[wiki/frontend/css-cascade-specificity|CSS Cascade and Specificity]] — inheritance, not specificity
- [[wiki/frontend/container-queries|Container Queries]] — container-relative units pair with variables
- [[wiki/frontend/shadow-dom|Shadow DOM]] — variables pierce encapsulation
- [[wiki/web-platforms/css-layout|CSS Layout]] — where these values drive layout
