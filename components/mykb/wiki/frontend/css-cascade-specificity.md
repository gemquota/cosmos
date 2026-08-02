---
type: "concept"
title: "CSS Cascade and Specificity"
description: "How conflicting rules resolve by origin, specificity, and order"
tags: [css", "cascade", "specificity", "styling", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity", "https://www.w3.org/TR/css-cascade-5/"]
---

# CSS Cascade and Specificity

## Summary
The cascade decides which CSS rule wins when several target the same property. Resolution order runs through origin and importance, context, element-attached styles, specificity, and finally source order. Specificity scores selectors by id, class, and type counts, which is why deeply nested selectors fight overrides.

## Details
- Origin order: user-agent, user, author, then author !important, user !important, and UA !important — later origins win without !important.
- Specificity weights: inline styles beat ids, ids beat classes/attributes/pseudo-classes, which beat type/pseudo-element selectors.
- Tie-break: equal specificity falls to source order, so the last stylesheet rule wins.
- @layer: cascade layers let teams order entire groups of rules, taming specificity wars without !important.
- Custom properties bypass: custom property values are inherited, not subject to specificity conflicts at use sites.
- Practice: keep specificity flat with single-class selectors so overrides stay predictable across components.

## Related
- [[wiki/frontend/bem|BEM]] — naming methodology that keeps specificity flat
- [[wiki/frontend/utility-css|Utility-First CSS]] — sidesteps specificity via class-only rules
- [[wiki/frontend/css-modules|CSS Modules]] — scoped selectors remove cross-component conflicts
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — inheritance-driven theming
- [[wiki/frontend/css-in-js|CSS-in-JS]] — generating selectors to avoid collisions
- [[wiki/web-platforms/css-layout|CSS Layout]] — platform context for cascade behavior
