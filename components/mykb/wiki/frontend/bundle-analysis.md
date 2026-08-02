---
type: "concept"
title: "Bundle Analysis"
description: "Measuring, visualizing, and auditing bundle composition"
tags: [performance", "bundlers", "analysis", "javascript", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/webpack-contrib/webpack-bundle-analyzer", "https://web.dev/articles/reduce-javascript-payloads-with-code-splitting"]
---

# Bundle Analysis

## Summary
Bundle analysis reveals what your JavaScript actually contains: which packages dominate, whether duplicates exist, and how much each route loads. Tools like webpack-bundle-analyzer render a treemap of modules, while Rollup and Vite expose similar visualizations. Auditing bundles regularly prevents dependency drift from silently inflating payloads.

## Details
- Treemaps: visual sizes show the biggest offenders instantly; hover for module identity and size in bytes.
- Duplicate detection: the same library resolved at multiple versions inflates bundles — dedupe with resolution aliases.
- Size reporting: compare raw, gzip, and brotli sizes; compression changes what weight actually matters on the wire.
- Chunk insight: see which chunks share code, where vendor code lands, and whether route splitting actually isolates pages.
- CI integration: compare bundle size against a budget or a baseline commit and fail the build on regressions.
- Frequency: run analysis on every significant dependency change, not just at release time.

## Related
- [[wiki/frontend/performance-budgets|Performance Budgets]] — the limits analysis is checked against
- [[wiki/frontend/code-splitting|Code Splitting]] — restructuring what analysis shows
- [[wiki/frontend/tree-shaking|Tree Shaking]] — removing what analysis exposes
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the output being analyzed
- [[wiki/frontend/source-maps|Source Maps]] — mapping bundle modules to source
- [[wiki/frontend/vite|Vite]] — built-in rollup-plugin-visualizer support
