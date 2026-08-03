---
type: "concept"
title: "Icon Fonts"
description: "Rendering icons as glyphs, with their trade-offs versus SVG"
tags: ["icons", "fonts", "svg", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Icon Fonts

## Summary

Icon fonts render glyphs from a font file, making icons scalable and colorable via CSS. They are convenient but carry real costs — font loading, missing-glyph boxes, inaccessible semantics — that inline SVG usually avoids.

## Details
- Mechanism: icons are encoded as glyphs in a font with ligature or codepoint mappings; <span class="icon">home</span> renders the glyph. Color comes from color/font-size, and the whole set ships as one font file with a subsetting step.
- Concrete example: a legacy dashboard using FontAwesome swaps colors and sizes purely in CSS; but a user whose font fails to load sees empty rectangles, screen readers hear nothing unless aria-labels are added, and the ligature class can collide with real text.
- Failure modes: FOUT/invisible icons while the font loads; glyphs looking different across platforms (hinting, fallback fonts); accessibility — icon fonts need aria-hidden plus a label, and are invisible to some assistive tech; CLS when the font swaps; and a bloated file if subsets are not trimmed.
- Operational tradeoffs: inline SVG gives per-icon caching, crisp scaling, fill/stroke control, and real a11y semantics at the cost of more markup; icon fonts win when you need a huge icon set swapped dynamically via CSS classes. Many teams now ship SVG sprites or component libraries and reserve icon fonts for legacy.
- RSIS3/mykb relevance: the dashboard migrated status icons to inline SVG, and this node records the tradeoff so loop-generated UI does not reintroduce icon fonts.
- Semantics: icon-font glyphs are invisible to screen readers and copy-paste; pair each icon with aria-label or visible text, and mark decorative icons aria-hidden so assistive tech does not read garbage.
- Cache economics: one icon font file caches well and swaps via CSS classes, which is its real advantage over per-icon requests; measure whether your icon set is big enough to justify the format over an SVG sprite.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/font-fallbacks|Font Fallbacks]]
- [[wiki/web-platforms/variable-fonts|Variable Fonts]]
- [[wiki/web-platforms/web-fonts|Web Fonts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
