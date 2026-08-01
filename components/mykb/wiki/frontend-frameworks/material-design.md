---
type: "concept"
title: "Material Design"
description: "Google open design system for adaptive, expressive interfaces across Android, web, and Flutter"
tags: ["design", "material", "ui", "design-system", "theming"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://m3.material.io/"]
---

# Material Design

## Summary

Material Design is Google open design system for building consistent, adaptive interfaces, currently at Material 3 (M3). It defines color, typography, shape, elevation, and motion tokens that implementations like Compose Material3, Material Web, and Flutter Material widgets share. M3 emphasizes expressive color, tonal surfaces, and components that adapt to any screen size.

## Details

- Foundations: color, typography, shape, and elevation are expressed as design tokens that scale across platforms.
- M3 color system adds dynamic color (extracting palettes from wallpaper), tonal roles, and built-in dark theme support.
- Components adapt: navigation rail versus bottom bar, cards and lists, buttons and chips, all with recommended sizes and touch targets.
- Motion and state layers give feedback without inventing custom patterns, keeping apps learnable.
- Accessibility is built into the spec: contrast ratios, focus states, and 48dp minimum touch targets.
- Implementations stay consistent: the same token set drives Compose on Android, Material Web, and Flutter.
- RSIS3 relevance: a mykb dashboard and companion app can share one design language, reducing UI decision fatigue across the triad.

## Related

- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]] — M3 dynamic color and dark tokens implement it
- [[wiki/android-core/density-buckets|Density Buckets]] — density-aware spacing comes from the spec
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — M3 components switch form at window size classes
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Compose Material3 is the Android implementation
- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — Flutter ships Material widgets using the same system
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — Material Web brings the system to browsers
- [[wiki/compositions/dev-workflow|Development Workflow Pattern]] — design tokens integrate into the dev workflow
