---
type: "concept"
title: "scroll-behavior CSS"
description: "Controlling smooth versus instant scroll navigation"
tags: ["css", "scroll", "ux", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# scroll-behavior CSS

## Summary

Scroll behavior controls how scrolling happens — instant jumps vs smooth animation — via CSS scroll-behavior and the JS scrollTo options. It shapes perceived navigation quality and must respect reduced-motion preferences.

## Details
- Mechanism: scroll-behavior: smooth on a scroll container makes programmatic scrolls (anchor links, scrollIntoView, scrollTo) animate; auto keeps instant jumps. JS can pass behavior: 'smooth'|'auto'|'instant' per call, overriding CSS. Scroll snap (scroll-snap-type/align) separately governs where scrolling rests.
- Concrete example: a docs sidebar's anchor links glide to sections with CSS scroll-behavior: smooth; a "back to top" button uses instant to avoid a long animation; a carousel uses scroll-snap so gestures settle on whole slides instead of half-scrolled states.
- Failure modes: smooth scroll on long pages causing disorientation when the user just wants to jump; programmatic smooth scrolling fighting user wheel/gesture input; accessibility — smooth scrolling can trigger vestibular discomfort, so gate on prefers-reduced-motion; and scrollIntoView defaults varying by browser, making cross-browser behavior inconsistent.
- Operational tradeoffs: smooth scrolling is polish, not correctness — keep durations short, respect reduced-motion, and ensure keyboard and anchor navigation work with behavior: 'auto'. Measure whether smooth scroll interferes with scroll-linked effects (parallax, sticky headers).
- RSIS3/mykb relevance: the wiki browser animates note navigation smoothly but respects prefers-reduced-motion, and the scroll-snap gallery in the OKF graph view is documented in this note.
- Focus and accessibility: after programmatic scrolling, move focus to the target (or manage aria) so keyboard and screen-reader users land where the viewport went.
- Performance: smooth scrolling across thousands of layout-affecting elements can jank; prefer scroll-margin-top on targets and transform-only scroll effects.
- Scroll margins: add scroll-margin-top to sticky-header targets so anchored sections do not hide under the header; the visual offset is part of the scroll UX, not an afterthought. Test scroll snap with keyboard focus, since snap containers can trap focus in unexpected places.

## Related
- [[wiki/web-platforms/virtual-scrolling|Virtual Scrolling]]
- [[wiki/web-platforms/scroll-snap|Scroll Snap]]
- [[wiki/web-platforms/sticky-position|position: sticky]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
