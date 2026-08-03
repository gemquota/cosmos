---
type: "concept"
title: "WOFF2 Format"
description: "The compressed web font container format"
tags: ["fonts", "woff2", "formats", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# WOFF2 Format

## Summary

WOFF2 is the web font container: Brotli-compressed, with per-glyph hinting pruning and better table handling, it is ~30% smaller than WOFF and supported by every evergreen browser. It is the shipping format for web fonts.

## Details
- Mechanism: WOFF2 wraps the sfnt tables of TrueType/OpenType, applies Brotli compression plus transform-level optimizations (glyph outline delta-encoding, hinting pruning, table overlap removal), and adds per-table checksums; browsers decompress it to the native font format at load. Only woff2 as the sole format means no fallback needed for modern targets.
- Concrete example: Inter's 400 weight as TTF (~300KB) becomes ~100KB woff2 after subsetting to latin; @font-face src: url(font.woff2) format('woff2') with no ttf/eot fallback is fine for the evergreen baseline; old IE/Android 4.x fallbacks (woff/eot/ttf) are only needed when the support matrix demands them.
- Failure modes: shipping un-subsetted woff2 (the container saves less than subsetting does); serving woff2 with wrong Content-Type or cache headers, causing repeat downloads; and font-loading errors from missing crossorigin on preloaded fonts (CORS applies to fonts).
- Operational tradeoffs: woff2 is the right default; pair with subsetting, unicode-range slicing, and font-display control; the remaining variance is per-engine decompression and hinting quality, which is why variable fonts and woff2 still need visual testing per platform.
- RSIS3/mykb relevance: the wiki's font pipeline would emit subsetted woff2 with versioned URLs; this node records the build settings so font changes stay cache-stable.
- Encoding edge cases: some fonts (CFF-based, variable axes) compress differently; verify woff2 output size and rendering after conversion rather than trusting ratios.
- Cache strategy: versioned filenames plus immutable cache headers make font updates instant while keeping repeat visits cache-hit.
- Subsetting order: subset to the needed character set before converting to woff2; the container shrinks the tables, but subsetting is what removes the unused glyphs that dominate size.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/icon-fonts|Icon Fonts]]
- [[wiki/web-platforms/font-fallbacks|Font Fallbacks]]
- [[wiki/web-platforms/variable-fonts|Variable Fonts]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
