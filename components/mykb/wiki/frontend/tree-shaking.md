---
type: "concept"
title: "Tree Shaking"
description: "Removing unused exports via static module analysis"
tags: [performance", "tree-shaking", "bundlers", "es-modules", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/reduce-javascript-payloads-with-tree-shaking", "https://rollupjs.org/introduction/"]
---

# Tree Shaking

## Summary
Tree shaking deletes unused exports from JavaScript bundles by analyzing the static structure of ES modules. Because import and export are compile-time declarations, bundlers can trace which exports are actually referenced and drop the rest. Done well, it trims libraries like lodash and date-fns to only the functions a page uses.

## Details
- Prerequisite: ES module syntax; CommonJS require is dynamic, so webpack and Rollup cannot reliably shake it.
- Side effects: files with side effects (polyfills, global styles) must be marked sideEffects: false in package.json or be kept.
- Barrel files: re-export indexes can defeat shaking when bundlers fail to trace through; import deep paths when needed.
- Toolchain: Rollup pioneered it; webpack (production mode), esbuild, and Vite all shake with varying aggressiveness.
- Limits: property access on objects (lodash.chain) and dynamic keys defeat static analysis.
- Measurement: compare bundle size with and without shaking; bundle analysis reveals what survived.

## Related
- [[wiki/frontend/es-modules|ES Modules]] — the syntax tree shaking depends on
- [[wiki/frontend/module-bundlers|Module Bundlers]] — where shaking executes
- [[wiki/frontend/rollup|Rollup]] — the strongest tree-shaking implementation
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — production-mode shaking
- [[wiki/frontend/minification|Minification]] — removing what shaking leaves behind
- [[wiki/frontend/bundle-analysis|Bundle Analysis]] — verifying shaken output
