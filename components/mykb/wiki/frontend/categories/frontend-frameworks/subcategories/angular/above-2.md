---
type: "entity"
title: "ABOVE"
description: "ABOVE: z-order stacking and above-the-fold visibility in interfaces"
tags: ["acronym", "ajax", "android", "angular", "api", "ast", "auth", "entity", "stacking"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# ABOVE

## Summary

ABOVE is the angular-cluster entity for stacking and layering in interfaces: which elements render above others and what sits above the fold. Z-order and visibility order shape interaction and perception. It matters because stacking mistakes silently swallow clicks and content. Predictable stacking rules are what keep overlay-heavy interfaces maintainable.

## Details

- **Definition** — Above-ness in interfaces has two senses: paint order (which element is visually on top) and fold order (what is visible without scrolling).
- **Z-index** — Positioned elements stack by z-index; equal values fall back to document order, a common source of surprises.
- **Stacking contexts** — Transforms, opacity, and position create stacking contexts that isolate z-index values inside them.
- **Above the fold** — Content visible without scrolling drives first impressions; below-the-fold content needs explicit discoverability.
- **Overlay layers** — Modals, dropdowns, and tooltips must stack above the page without leaking click-through.
- **Failure modes** — Runaway z-index arms races, modal traps, and content hidden by sticky headers are classic failures. A documented z-index scale, reviewed with every new overlay, prevents the arms race before it starts.
- **Worked example** — A dropdown menu sets its own stacking context so it renders above cards without fighting the page's z-index scale.
- **Practical relevance** — Predictable stacking rules make overlay-heavy UIs maintainable.
- **Z-scale** — A small, documented z-index scale with named layers prevents arbitrary arms races.
- **Isolation** — Creating stacking contexts on widgets contains their internal z-order.
- **Testing** — Click and screenshot tests verify that overlays render above content and intercept input.
- **Overlay management** — A dedicated overlay system that owns modals and menus prevents ad-hoc z-index values scattered through components.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/area|AREA]] — regions being stacked
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/aabb-2|AABB]] — bounds of stacked elements
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/alert|ALERT]] — overlays that must stay on top
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — cluster sibling page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/global-config|Global Config]] — overlay configuration
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/adhd|ADHD]] — attention to overlays
