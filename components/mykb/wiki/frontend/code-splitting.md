---
type: "concept"
title: "Code Splitting"
description: "Splitting bundles by route, component, or dynamic import"
tags: [performance", "code-splitting", "bundlers", "javascript", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/reduce-javascript-payloads-with-code-splitting", "https://react.dev/reference/react/lazy"]
---

# Code Splitting

## Summary
Code splitting divides one large JavaScript bundle into smaller chunks loaded on demand. Route-level splitting ships only the code for the current page; component-level splitting defers heavy widgets until they render; vendor splitting isolates third-party libraries for better caching. The result is a faster initial load and less parse time.

## Details
- Dynamic import: import("./module.js") creates an async chunk; bundlers emit separate files with hashed names.
- Route splitting: frameworks wire lazy loading to router navigation, so each route's code loads when visited.
- React pattern: React.lazy plus Suspense renders a fallback while the chunk downloads.
- Vendor splitting: bundler config splits node_modules into shared chunks, improving cache reuse across deploys.
- Costs: too many tiny chunks multiply requests; measure with bundle analysis and keep a sensible chunk budget.
- SSR caution: lazy boundaries must be deterministic during server rendering to avoid hydration mismatches.

## Related
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the tooling that emits chunks
- [[wiki/frontend/tree-shaking|Tree Shaking]] — dead-code removal alongside splitting
- [[wiki/frontend/lazy-loading|Lazy Loading]] — the deferral concept applied to code
- [[wiki/frontend/bundle-analysis|Bundle Analysis]] — seeing what each chunk contains
- [[wiki/frontend/vite|Vite]] — built-in code splitting via Rollup
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — chunks and splitChunks configuration
