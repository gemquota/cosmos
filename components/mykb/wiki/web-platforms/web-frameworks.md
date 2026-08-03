---
type: "concept"
title: "Web Frameworks"
description: "Libraries and platforms that structure web development: React, Vue, Svelte, Next.js, and their kin"
tags: ["frameworks", "react", "frontend", "spa"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Web Frameworks

## Summary

Web frameworks structure how UI is built — from vanilla DOM discipline to React/Vue/Svelte component models to meta-frameworks like Next/Astro. Choosing one is a commitment to its rendering model, update cadence, and escape hatches.

## Details
- Mechanism: component frameworks diff declarative trees against the DOM (React's virtual DOM, Vue's reactive system, Svelte's compile-time reactivity); meta-frameworks add routing, SSR/SSG, and data loading on top; the rendering strategy (CSR vs SSR vs SSG vs islands) decides where HTML is produced and how interactive it is.
- Concrete example: a content wiki can be static-first (SSG + minimal JS) while its dashboard needs client rendering and real-time data; an island architecture ships JS only around interactive widgets, keeping most pages light; a large SPA bundles everything once and pays a startup tax for instant navigation.
- Failure modes: framework lock-in when a team needs a rendering model the framework fights (heavy real-time UI in a static-first setup); bundle bloat from default imports and unconfigured code-splitting; hydration mismatches between server and client HTML; and upgrade risk when the ecosystem moves faster than the product.
- Operational tradeoffs: frameworks trade dependency risk and abstraction for development speed and consistency; vanilla DOM stays relevant for small, performance-critical surfaces. The durable pattern is framework-agnostic foundations (tokens, safe rendering, measurement) with the view layer swappable.
- RSIS3/mykb relevance: the wiki browser and SPACE UI document their framework choices and rendering models here, so the loop's generated interfaces follow the same architecture.
- Cost accounting: include framework updates, bundle weight, and build complexity in the decision; a framework's DX advantage is real but must be re-earned at every upgrade.
- Migration path: keep rendering-safe boundaries (sanitized markup, tokens, measurement hooks) framework-agnostic so a future view-layer change does not rewrite security-critical code.

## Related
- [[wiki/web-platforms/component-architecture|Component Architecture]] — frameworks implement the component model
- [[wiki/web-platforms/state-management|State Management]] — frameworks provide state primitives
- [[wiki/web-platforms/web-components|Web Components]] — the standard-based alternative
- [[wiki/frontend/static-site-generation|Static Site Generation]] — meta-frameworks pre-render pages
- [[wiki/testing/golden-tests|Golden Tests]] — framework rendering is golden-tested
