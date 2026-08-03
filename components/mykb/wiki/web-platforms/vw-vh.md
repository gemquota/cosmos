---
type: "concept"
title: "vw and vh Units"
description: "Viewport-relative length units and their pitfalls"
tags: ["css", "units", "viewport", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# vw and vh Units

## Summary

vw/vh units size relative to the viewport — 100vw is the viewport width, 100vh the height. They enable full-bleed sections and fluid sizing, but raw 100vh/vw have mobile-chrome and scrollbar pitfalls that dvh/svw/dvw units address.

## Details
- Mechanism: vw/vh resolve against the viewport size (the small/large viewport split on mobile: vh historically equals the largest, so it can overshoot the visible area); percentages resolve against the parent instead. 100vw includes the scrollbar width in some engines, causing horizontal overflow.
- Concrete example: a hero with height: 100vh hides its bottom behind the mobile URL bar; height: 100dvh tracks the visible area; a full-width strip with width: 100vw overflows by the scrollbar width while width: 100% does not. Fluid type often mixes vw inside clamp for viewport-proportional scaling.
- Failure modes: 100vh on mobile landing above/below the visible region; dvh changing when browser chrome collapses, re-flowing layouts mid-scroll; vw-based type on ultrawide monitors growing unbounded (clamp bounds fix this); and nested contexts where vw should really be container-relative.
- Operational tradeoffs: prefer % and container units for layout structure, reserving viewport units for genuinely viewport-bound effects (full-bleed media, fluid type); provide vh fallbacks before dvh/svh since unknown units are dropped by older engines.
- RSIS3/mykb relevance: the wiki mobile layout uses dvh for the app-shell height with vh fallback; this note records the unit ordering the loop must preserve.
- Landscape and rotation: mobile orientation changes alter vh/dvh mid-session; re-evaluate shell heights on resize rather than caching a computed value.
- Print and embed: viewport units resolve against the iframe or print viewport; a component using 100vh inside an embedded panel sizes to the panel, not the page — decide intent explicitly.
- Safe-area interplay: combine vh-based shells with env(safe-area-inset-*) so notches and home indicators do not overlap interactive chrome on modern phones.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/dvh-svh|Dynamic and Small Viewport Units]]
- [[wiki/web-platforms/em-vs-rem|em vs rem]]
- [[wiki/web-platforms/px-vs-rem|px vs rem]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
