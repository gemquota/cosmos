---
type: "concept"
title: "Islands Architecture"
description: "Static HTML shells with isolated interactive component islands"
tags: [rendering", "hydration", "ssg", "performance", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.astro.build/en/concepts/islands/", "https://web.dev/articles/rendering-on-the-web"]
---

# Islands Architecture

## Summary
The islands architecture serves static HTML by default and hydrates only the small, isolated regions of a page that are actually interactive — the search box, the cart, the video player. Everything else stays as plain markup. Frameworks like Astro, Fresh, and Marko popularized the model as a response to whole-page hydration.

## Details
- Each island owns its JavaScript: only interactive components ship code, and each island hydrates independently on its own schedule.
- Progressive enhancement fit: static content works without JavaScript; interactivity layers on top instead of being required.
- No global app root: there is no single framework mount point wrapping the document, which simplifies partial upgrades.
- Framework mixing: islands can use different frameworks side by side, so a React widget can live in an otherwise vanilla page.
- Performance: JavaScript payload and Time to Interactive drop dramatically because most of the page never hydrates.
- Trade-offs: shared state across islands needs explicit wiring, and anything needing global interactivity is harder to express.

## Related
- [[wiki/frontend/hydration|Hydration]] — the mechanism islands scope to components
- [[wiki/frontend/ssg|Static Site Generation]] — the static base islands build on
- [[wiki/frontend/progressive-enhancement|Progressive Enhancement]] — the principle islands formalize
- [[wiki/frontend/web-components|Web Components]] — a technology for building islands
- [[wiki/web-platforms/component-architecture|Component Architecture]] — how islands compose
- [[wiki/frontend/static-site-generation|Static Site Generation]] — deployment pattern for island sites
