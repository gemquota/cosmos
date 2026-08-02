---
type: "concept"
title: "Module Bundlers"
description: "How bundlers resolve, transform, and emit dependency graphs"
tags: [build-tools", "bundlers", "javascript", "modules", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://webpack.js.org/concepts/", "https://vitejs.dev/guide/why.html"]
---

# Module Bundlers

## Summary
Module bundlers take a graph of JavaScript modules — plus CSS, assets, and other imports — and emit optimized browser-ready files. They resolve import paths, apply transformations, and produce bundles with code splitting, tree shaking, and hashed filenames. webpack, Rollup, esbuild, and Vite represent the current landscape.

## Details
- Resolution: bundlers walk import and require statements, honoring node_modules, aliases, and extension order.
- Transformation: loaders or plugins compile TypeScript, JSX, SCSS, and assets into plain modules the browser understands.
- Emission: output can be one bundle, many chunks, or library formats; filenames hash for cache busting.
- Optimization: tree shaking, minification, scope hoisting, and asset inlining happen during the production build.
- Dev mode: bundlers power dev servers with hot module replacement, source maps, and fast rebuilds.
- Trade-offs: configuration-heavy bundlers give control; simpler tools trade features for speed and predictability.

## Related
- [[wiki/frontend/es-modules|ES Modules]] — the module semantics bundlers consume
- [[wiki/frontend/webpack-concepts|Webpack Concepts]] — the dominant configurable bundler
- [[wiki/frontend/vite|Vite]] — dev-first bundling on esbuild and Rollup
- [[wiki/frontend/rollup|Rollup]] — the ES-module-first alternative
- [[wiki/frontend/code-splitting|Code Splitting]] — an output strategy bundlers implement
- [[wiki/frontend/tree-shaking|Tree Shaking]] — an optimization bundlers perform
