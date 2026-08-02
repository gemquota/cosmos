---
type: "concept"
title: "Design Tokens"
description: "Platform-agnostic style values and distribution"
tags: [design-tokens", "design-systems", "css", "theming", "style-values"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://tr.designtokens.org/format/", "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"]
---

# Design Tokens

## Summary
Design tokens are named, platform-agnostic values for style decisions — colors, spacing, typography, radii, and motion. A single token definition can be transformed into CSS custom properties, Sass variables, or native platform constants. Tokens create the single source of truth that design systems and theming are built on.

## Details
- Anatomy: a token has a name (color.surface.muted), a value, and metadata such as type and description.
- Primitives vs semantic: primitive tokens hold raw values (blue-500); semantic tokens reference intent (color.primary).
- Distribution: W3C Design Tokens Community Group format standardizes JSON; build tools emit CSS, SCSS, or Swift/Kotlin files.
- CSS mapping: tokens typically compile to custom properties, enabling runtime theming and inheritance.
- Aliasing: semantic tokens reference primitives so re-theming changes one layer instead of every value.
- Governance: versioned token releases let apps upgrade design values without code changes.

## Related
- [[wiki/frontend/design-systems|Design Systems]] — the system tokens serve
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — the runtime representation
- [[wiki/frontend/theming|Theming]] — switching token sets per theme
- [[wiki/frontend/utility-css|Utility-First CSS]] — utilities generated from tokens
- [[wiki/frontend/css-modules|CSS Modules]] — consuming tokens in scoped styles
- [[wiki/frontend/color-contrast|Color Contrast]] — token palettes with contrast safety
