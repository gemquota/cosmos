---
type: "concept"
title: "Web Frameworks"
description: "Libraries and platforms that structure web development: React, Vue, Svelte, Next.js, and their kin"
tags: ["frameworks", "react", "frontend", "spa"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Web Frameworks

## Summary
Web frameworks provide the structure for building interfaces: component models, routing, state, and build tooling. React, Vue, and Svelte dominate the component layer; Next.js, Astro, and Remix add full-stack structure.

## Details
- Choose by model: component-based (React/Vue), compiler-based (Svelte), or meta-frameworks that add SSR and file routing.
- Framework lock-in trades against standardization: Web Components remain the escape hatch.
- RSIS3 relevance: the mykb dashboard stack (if any) should be chosen for maintainability, not novelty.

## Related
- [[wiki/web-platforms/component-architecture|Component Architecture]] — frameworks implement the component model
- [[wiki/web-platforms/state-management|State Management]] — frameworks provide state primitives
- [[wiki/web-platforms/web-components|Web Components]] — the standard-based alternative
- [[wiki/frontend/static-site-generation|Static Site Generation]] — meta-frameworks pre-render pages
- [[wiki/testing/golden-tests|Golden Tests]] — framework rendering is golden-tested
