---
type: "concept"
title: "Font Loading Strategy"
description: "Serving web fonts fast and without layout shift: subsetting, preload, and font-display"
tags: ["fonts", "performance", "css", "loading", "typography"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/font-best-practices", "https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face"]
---
# Font Loading Strategy

## Summary
Fonts are render-blocking assets that also cause layout shift. A sound strategy self-hosts subsetted WOFF2 files, declares `font-display`, preloads critical families, and reserves space with `size-adjust` or `ascent-override`. The goal: text paints quickly and doesn't jump when the webfont lands.

## Details
- **Format and subsetting** — WOFF2 with unicode-range subsets shrinks downloads to needed glyphs; language subsets add requests but cut bytes.
- **font-display** — `swap` shows fallbacks immediately (FOUT); `optional` skips the font for fast connections; `block` hides text (FOIT) and risks blank text.
- **Preload and self-hosting** — preload the primary family; self-hosting avoids third-party DNS and cookie overhead.
- **Metric alignment** — `size-adjust`, `ascent-override`, and `descent-override` align fallback metrics with the webfont, reducing CLS.
- **Worked example** — the mykb reader serves two subsetted WOFF2 families with `font-display: swap` and size-adjusted fallbacks, cutting CLS to near zero.
- **Relevance** — font metrics are part of the CLS budget RSIS3's reports must respect.

## Related
- [[wiki/web-platforms/font-fallbacks|Font Fallbacks]] — adjacent concept in this wiki
- [[wiki/web-platforms/variable-fonts|Variable Fonts]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-fonts|Web Fonts]] — adjacent concept in this wiki
- [[wiki/web-platforms/font-display-swap|font-display: swap]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
