---
type: "concept"
title: "CSS Logical Properties"
description: "Flow-relative inset, margin, and padding properties for LTR and RTL"
tags: ["css", "rtl", "layout", "i18n"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Logical Properties

## Summary

Logical properties (margin-inline-start, padding-block, inset-inline) map layout directions to the text flow instead of physical axes, so the same stylesheet works in LTR and RTL without duplication. They are the modern default for internationalized UI.

## Details
- Mechanism: block/inline axes derive from writing-mode and direction: inline is the text flow direction (left-to-right in LTR, right-to-left in RTL), block is the stacking direction (top-to-bottom normally, vertical in vertical writing modes). Physical longhands (margin-left) ignore the flow; logical ones (margin-inline-start) follow it.
- Concrete example: padding-inline: 1rem on a button pads the text sides in both directions; border-inline-end puts the border on the right in LTR and on the left in RTL automatically. A sidebar using margin-inline-end places its gap correctly when the layout mirrors.
- Failure modes: mixing physical and logical values in one component (margin-left plus margin-inline) breaks mirroring unpredictably; absolute positioning with left/right instead of inset-inline; text-align: left not mirroring (use start/end); and older browser gaps for logical shorthands like inset-block.
- Operational tradeoffs: logical properties are the correct default for i18n-ready UIs; the cost is a mental shift and occasional ambiguity (which axis did I mean?). Use physical properties only for genuinely physical layouts (rotated elements, coordinate charts) and test RTL mirroring explicitly.
- RSIS3/mykb relevance: the wiki browser and dashboard use logical properties throughout, so enabling Arabic/Hebrew locales mirrors the chrome without a separate RTL stylesheet.
- Chart caveat: coordinate-based visuals (SVG plots, canvas) are physical by nature; keep physical properties there and switch to logical only in document flow.
- Fallbacks: where logical properties are unsupported, declare physical fallbacks first, then logical overrides; browsers that know logical values ignore the earlier physical ones.
- Legacy fallback: declare physical properties before logical ones so older engines get a working layout; logical values override where supported, making the fallback both safe and progressive.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/rtl-support|RTL Support]]
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]]
- [[wiki/web-platforms/clamp-practice|clamp() in Practice]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
