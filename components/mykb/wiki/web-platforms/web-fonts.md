---
type: "concept"
title: "Web Fonts"
description: "Serving and applying downloadable font files in the browser"
tags: ["fonts", "css", "typography", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Web Fonts

## Summary

Web fonts balance typography against performance: they add identity and readability but cost bytes, blocking, and layout shift. The discipline is self-host, subset, preload, and control the swap.

## Details
- Mechanism: @font-face declares families with src URLs, format hints (woff2), and descriptors (font-display, unicode-range); the browser fetches only faces whose unicode-range matches rendered text. Loading options: self-hosted (full control, cache-friendly) vs CDN (fast edge, but third-party dependency and no metric overrides).
- Concrete example: a site self-hosts Inter subsets (latin, latin-ext) as woff2, preloads the primary face with crossorigin, uses font-display: swap, and matches fallback metrics with size-adjust so the swap does not shift layout; the LCP text is visible in the fallback immediately.
- Failure modes: full-family loading (every weight/italic) multiplying bytes; external font hosts adding DNS/TLS latency and a privacy dependency; FOIT hiding text on slow connections (fixed by swap); missing unicode-range so unused scripts download anyway; and fonts blocking rendering when critical text uses them (mitigate with preload + swap).
- Operational tradeoffs: typography quality vs bytes is the core trade; variable fonts compress a family into one file, and per-language subsets shrink payloads further. A practical budget: 1-2 families, subset aggressively, preload one face, and keep the fallback metrics close to the real font.
- RSIS3/mykb relevance: the wiki's font strategy (families, subsets, loading hints) is a recorded policy here so the loop does not introduce font drift in generated UI.
- Performance budget: treat font bytes as part of the LCP budget — a 100KB font preloaded at high priority delays the hero image; prioritize assets by what the LCP element actually is.
- Accessibility: never rely on font loading for legibility — fallback stacks must be readable; and honor font-size preferences by keeping sizes in rem so user text settings scale the page.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/font-display-swap|font-display: swap]]
- [[wiki/web-platforms/subsetting-fonts|Font Subsetting]]
- [[wiki/web-platforms/woff2|WOFF2 Format]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
