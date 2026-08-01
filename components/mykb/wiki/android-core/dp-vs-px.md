---
type: "concept"
title: "DP vs PX"
description: "Density-independent pixels and scale-independent pixels for text"
tags: ["android", "density", "units", "layout"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# DP vs PX

dp (density-independent pixels) normalizes sizes across screen densities: 1dp is 1px on mdpi and 3px on xxxhdpi. sp scales text with the user font-size setting, so text uses sp and geometry uses dp.
- Converting: px = dp * density, where density is the bucket factor.
- Use sp for text so accessibility font scaling works.
- Never mix: fixed px layouts break on high-density screens.
- Compose uses dp by default; sp maps to text units.

## Related

- [[wiki/android-core/density-buckets|Density Buckets]] — dp values select bucket resources
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — density independence is foundational
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — sp text honors user font settings
- [[wiki/frontend-frameworks/material-design|Material Design]] — the spec is written in dp and sp
