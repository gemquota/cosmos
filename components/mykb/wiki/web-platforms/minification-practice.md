---
type: "concept"
title: "Minification Practice"
description: "Shrinking HTML, CSS, and JavaScript payloads through whitespace removal, mangling, and tree shaking"
tags: ["minification", "performance", "javascript", "css", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Minification", "https://developer.mozilla.org/en-US/docs/Web/Performance"]
---
# Minification Practice

## Summary
Minification removes characters unnecessary for execution: whitespace, comments, long names, and dead code. Combined with compression (gzip/Brotli), it is the cheapest and most reliable way to cut transfer size. Modern bundlers minify by default with source maps for debugging.

## Details
- **What minifiers do** — strip whitespace and comments, shorten local names, rewrite constant expressions, and drop unused code (tree shaking).
- **Trade-offs** — readability and stack traces suffer; source maps restore them in devtools.
- **Compression synergy** — Brotli/gzip after minification yields the biggest wins; precompressed assets avoid server cost.
- **Budgets** — JS budgets per route; minified size is the metric that matters, plus parse/execute time.
- **Worked example** — the mykb bundle ships minified with Brotli and source maps; CI fails if the JS budget is exceeded.
- **Relevance** — RSIS3's generated HTML/JS artifacts should be minified the same way before serving.

## Related
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/module-preload|modulepreload]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/import-maps|Import Maps]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
- [[wiki/api-protocols/http-compression|HTTP Compression]] — existing coverage
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
