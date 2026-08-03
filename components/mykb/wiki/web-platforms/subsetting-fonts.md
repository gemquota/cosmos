---
type: "concept"
title: "Font Subsetting"
description: "Trimming font files to only the glyphs a site actually uses"
tags: ["fonts", "performance", "typography", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Font Subsetting

## Summary

Subsetting trims a font to only the glyphs a site uses — the Latin set, a specific unicode range, or even per-page glyphs — cutting font payloads from hundreds of KB to tens. It is the highest-leverage web-font optimization.

## Details
- Mechanism: a font file contains thousands of glyphs; subsetting tools (pyftsubset, fonttools, woff2) drop unused ones and their hinting, then rebuild the tables; unicode-range in @font-face lets the browser download only the slices covering the text actually present, splitting one font into many small files.
- Concrete example: a Latin-only site subsets Inter to the Latin + Latin-ext ranges (~30-60KB woff2 instead of 300KB+); a page using a display font for three headline characters can ship a tiny custom subset; code pages subset to the specific codepoints in the monospace face.
- Failure modes: over-subsetting that omits glyphs appearing later (dynamic content, user input) — the browser silently falls back or renders tofu; subsets that break dynamic font features (ligatures, alternates) or OpenType features like kerning tables; missing unicode-range coverage for punctuation or currency symbols; and subset-per-page multiplying cache entries.
- Operational tradeoffs: subsetting adds a build step and cache complexity but directly shrinks LCP and CLS-relevant font bytes; keep a generous character set (latin-ext + common symbols) unless per-page subsetting is automated, and always verify with a glyph coverage test.
- RSIS3/mykb relevance: the wiki's fonts are subset to latin/latin-ext with coverage tests in CI; this node records the subset ranges so the loop does not reintroduce full-font files.
- Dynamic content risk: subsets must cover punctuation, digits, and currency used by user-generated content, not just static strings; a coverage test over the real corpus catches missing glyphs before they render as tofu.
- Format benefit: woff2 plus subsetting multiplies savings — subset first, then compress; the two optimizations are complementary, and skipping either one leaves significant bytes on the table.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/woff2|WOFF2 Format]]
- [[wiki/web-platforms/icon-fonts|Icon Fonts]]
- [[wiki/web-platforms/font-fallbacks|Font Fallbacks]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
