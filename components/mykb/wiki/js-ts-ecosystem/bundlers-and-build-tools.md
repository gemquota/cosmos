---
type: "concept"
title: "Bundlers and Build Tools"
description: "The modern build pipeline: transpilation, bundling, code splitting, and dev servers"
tags: ["bundlers", "build-tools", "vite", "webpack", "javascript"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://vitejs.dev/guide/", "https://webpack.js.org/concepts/"]
---
# Bundlers and Build Tools

## Summary
Build tools convert source (TSX, CSS, assets) into optimized deployables: transpile, resolve modules, bundle, split code, and minify. Modern tools like Vite (esbuild + Rollup), esbuild, and Turbopack prioritize speed; webpack remains the configurable workhorse. Dev servers add HMR for iteration.

## Details
- **Pipeline stages** — parse/transform (Babel, SWC, esbuild), module resolution, bundling with tree shaking, splitting, and minification.
- **Dev experience** — native ESM serving and HMR make iteration instant; production builds optimize differently.
- **Code splitting** — entry points, dynamic imports, and shared chunks balance payload size and caching.
- **Trade-offs** — speed vs ecosystem: esbuild is fastest, webpack most extensible, Vite the DX middle ground.
- **Worked example** — the mykb web app builds with Vite: esbuild for transforms, Rollup for the production bundle, and route-level splitting.
- **Relevance** — RSIS3's artifacts should pick build tools by the same speed/extensibility criteria.

## Related
- [[wiki/js-ts-ecosystem/babel-practice|Babel in Practice]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/swc-compiler|SWC Compiler]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/esbuild-practice|esbuild in Practice]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/rollup-practice|Rollup in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — existing coverage
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — existing coverage
