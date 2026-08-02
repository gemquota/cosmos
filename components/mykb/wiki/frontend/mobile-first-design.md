---
type: "concept"
title: "Mobile-First Design"
description: "Designing from small screens up with enhancement"
tags: [css", "mobile-first", "responsive", "progressive-enhancement", "design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/responsive-web-design-basics", "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Responsive/Mobile_first"]
---

# Mobile-First Design

## Summary
Mobile-first design starts with the small-screen experience and enhances upward with min-width media queries. Because the base styles serve phones, performance budgets are set by the weakest device. Features are added as space and capability grow, which keeps complexity proportional to screen real estate.

## Details
- Ordering: base CSS targets narrow viewports; each min-width query layers in sidebars, multi-column grids, and richer chrome.
- Enhancement mindset: touch targets, readable type, and essential content ship first; hover-dependent interactions come later.
- Performance: designing for phones first exposes payload and layout costs early, aligning with Core Web Vitals.
- Content priority: small screens force deciding what matters, improving information architecture for all sizes.
- Testing: verify base styles without CSS or at 320px, then confirm enhancements across breakpoints.
- Caveats: mobile-first is an authoring strategy, not a guarantee — test on large screens and mid-size tablets too.

## Related
- [[wiki/frontend/responsive-design|Responsive Design]] — the umbrella discipline
- [[wiki/frontend/media-queries|Media Queries]] — min-width enhancement queries
- [[wiki/frontend/progressive-enhancement|Progressive Enhancement]] — capability layering applied to layout
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — mobile-first performance goals
- [[wiki/frontend/fluid-typography|Fluid Typography]] — type that scales from small bases
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — native platform counterpart
