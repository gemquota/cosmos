---
type: "concept"
title: "BEM"
description: "Block-Element-Modifier class naming methodology"
tags: [css", "bem", "naming", "architecture", "styling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.bem.info/methodology/", "https://getbem.com/introduction/"]
---

# BEM

## Summary
BEM — Block, Element, Modifier — is a CSS class naming methodology that gives every UI piece a predictable, single-purpose name. A block is a standalone component, an element is a part of that block, and a modifier expresses a variation. The naming convention keeps specificity flat and makes styles portable across projects.

## Details
- Syntax: block__element--modifier, for example .card__title--large; double underscores and hyphens encode the hierarchy.
- Rules: elements belong to their block, modifiers change appearance or state, and blocks never style each other.
- Specificity: every selector is one class deep, so overrides are easy and cascade conflicts are rare.
- Maintainability: reading the class name reveals the component structure, replacing tribal knowledge about markup.
- Downsides: names get long, and strict BEM can feel verbose without preprocessors or naming utilities.
- Ecosystem fit: BEM predates CSS Modules and utility CSS but remains a solid convention for plain, portable stylesheets.

## Related
- [[wiki/frontend/css-cascade-specificity|CSS Cascade and Specificity]] — why flat selectors matter
- [[wiki/frontend/utility-css|Utility-First CSS]] — the composition-based alternative
- [[wiki/frontend/css-modules|CSS Modules]] — tooling that makes scoping automatic
- [[wiki/frontend/component-composition|Component Composition]] — blocks map to components
- [[wiki/frontend/design-systems|Design Systems]] — naming conventions inside shared libraries
- [[wiki/web-platforms/css-layout|CSS Layout]] — styling foundations BEM organizes
