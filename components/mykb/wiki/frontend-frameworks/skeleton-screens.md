---
type: "concept"
title: "Skeleton Screens"
description: "Placeholder shapes that preview content layout while data loads"
tags: ["skeleton", "loading", "ux", "performance", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.smashingmagazine.com/2020/04/skeleton-screens-react/", "https://web.dev/learn/design"]
---
# Skeleton Screens

## Summary
Skeleton screens show gray placeholder shapes matching the final layout while content loads, reducing perceived latency and preventing layout shift. They work best when the structure is known but data is not. Skeletons must reserve real space and should be replaced promptly.

## Details
- **Placement** — mimic final geometry: text lines, image boxes, and avatar circles sized to the real layout.
- **Reserved space** — skeletons double as layout reservations, so the swap to real content causes no shift.
- **Motion** — subtle shimmer or pulse indicates loading; respect `prefers-reduced-motion`.
- **Anti-patterns** — skeleton on first load of an unknown structure, or skeletons that outlast the data by seconds.
- **Worked example** — the mykb article view shows a headline-line skeleton and two content blocks while the markdown fetches.
- **Relevance** — skeleton + reserved space is the standard pair for CLS-safe loading in RSIS3's UIs.

## Related
- [[wiki/web-platforms/reserved-space|Reserving Layout Space]] — adjacent concept in this wiki
- [[wiki/web-platforms/aspect-ratio-images|Aspect Ratio for Images]] — adjacent concept in this wiki
- [[wiki/web-platforms/font-shift|FOIT and Font Shift]] — adjacent concept in this wiki
- [[wiki/web-platforms/content-visibility|content-visibility CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
