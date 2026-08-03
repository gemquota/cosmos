---
type: "concept"
title: "RTL Support"
description: "Building interfaces that mirror correctly for right-to-left languages"
tags: ["rtl", "i18n", "css", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# RTL Support

## Summary

Right-to-left (RTL) support means the UI mirrors correctly for Hebrew, Arabic, Persian, and Urdu. Modern practice relies on direction-aware CSS — logical properties, start/end alignment — rather than duplicated mirror stylesheets.

## Details
- Mechanism: dir="rtl" (or lang + UA heuristics) flips the inline flow: text, flex order, grid columns, and block alignment start from the right; logical properties (margin-inline-start, inset-inline-end) automatically track the direction; text-align: start follows it too. The DOM order stays the same — only the visual axis mirrors.
- Concrete example: a sidebar using margin-inline-end instead of margin-right places its gap correctly in both directions; a breadcrumb with padding-inline-start reads correctly in Arabic; icons that imply direction (arrows, chevrons) should flip or be mirrored so "next" still points right-to-left.
- Failure modes: physical properties (left/right) that hard-code the LTR layout; numbers and dates embedded in RTL text needing bidi isolation (use dir="ltr" spans or bdi for mixed content); inputs and placeholders inheriting wrong alignment; and CSS transforms or absolutely-positioned overlays that do not mirror automatically.
- Operational tradeoffs: logical properties are the durable fix — write them from the start and RTL is nearly free; testing still needs real content in RTL scripts (not just dir flipping) since long strings and numerals reflow differently. Add RTL to the QA matrix and pseudo-localize.
- RSIS3/mykb relevance: the wiki UI is built with logical properties and tested with an Arabic fixture corpus, documented here so new dashboard surfaces inherit the same guarantee.
- Bidi isolation: wrap mixed-direction content (numbers, product codes, usernames) in dir="ltr" spans or <bdi> so the surrounding RTL flow does not scramble it; direction is a per-node property, not just a page setting.
- Icon mirroring: direction-implying icons (arrows, chevrons, back buttons) must flip in RTL; handle this with CSS logical transforms or mirrored assets rather than shipping two sets.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]]
- [[wiki/web-platforms/clamp-practice|clamp() in Practice]]
- [[wiki/web-platforms/aspect-ratio-css|aspect-ratio in CSS]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
