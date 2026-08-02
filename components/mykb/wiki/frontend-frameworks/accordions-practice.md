---
type: "concept"
title: "Accordions in Practice"
description: "Collapsible sections: disclosure semantics, animation, and when accordions help"
tags: ["accordions", "disclosure", "ux", "accessibility", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details", "https://www.w3.org/WAI/ARIA/apg/patterns/accordion/"]
---
# Accordions in Practice

## Summary
Accordions collapse content into expandable sections, decluttering dense pages. The native `<details>`/`<summary>` gives semantics for free; ARIA's accordion pattern formalizes multi-section behavior. Accordions hide content, so they fit reference material, not primary tasks.

## Details
- **Native details** — `<details>`/`<summary>` is keyboard- and AT-accessible with zero JS; styling via `::details-content` where supported.
- **State** — one-open-at-a-time (classic) vs independent sections; both have established patterns.
- **Animation** — animating height is tricky; use grid-template-rows or the new `interpolate-size` for smooth disclosure.
- **When to use** — FAQs, settings groups, and long reference pages; avoid for critical content users must scan.
- **Worked example** — the mykb wiki's metadata block uses independent `<details>` sections per field group.
- **Relevance** — disclosure widgets are a recurring component in RSIS3's generated documentation pages.
- **State preservation** — collapsing sections must not destroy their content; keep components mounted or preserve scroll and input state so users do not lose work.

## Related
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/content-visibility|content-visibility CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/contain-property|CSS Containment]] — adjacent concept in this wiki
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
