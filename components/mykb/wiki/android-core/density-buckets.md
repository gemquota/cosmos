---
type: "concept"
title: "Density Buckets"
description: "Asset buckets for mdpi through xxxhdpi screen densities"
tags: ["android", "density", "assets", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Density Buckets

Density buckets map screen pixel density to resource qualifiers (mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi) so Android picks the right images. Vector drawables remove most bucket work today.
- Buckets correspond to density factors: mdpi=1.0, xxhdpi=3.0, etc.
- Density-specific drawable and layout resources live in matching folders.
- Prefer vector drawables and adaptive icons over raster sets.
- Wrong buckets cause blurry icons or wasted download size.

## Related

- [[wiki/android-core/dp-vs-px|DP vs PX]] — density units underpin buckets
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — density handling is part of responsiveness
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — screens vary in size and density
- [[wiki/frontend-frameworks/material-design|Material Design]] — icons and spacing follow density rules
