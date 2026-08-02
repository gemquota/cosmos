---
type: "concept"
title: "Rollup"
description: "ES-module-first bundling with strong tree shaking"
tags: [rollup", "bundlers", "es-modules", "build-tools", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://rollupjs.org/introduction/", "https://web.dev/articles/reduce-javascript-payloads-with-tree-shaking"]
---

# Rollup

## Summary
Rollup is a bundler designed around ES modules, famous for aggressive tree shaking and clean output. It is the production engine inside Vite and the default choice for publishing JavaScript libraries. Its plugin ecosystem and output formats make it flexible for both applications and distributable packages.

## Details
- ESM-first: Rollup analyzes the static module graph, eliminating unused exports with precision that predates webpack's support.
- Output formats: esm, cjs, iife, umd, and system target every consumption environment, including browsers and Node.
- Code splitting: dynamic import produces shared chunks; manualChunks lets library authors shape the output.
- Plugins: resolve, commonjs, typescript, and terser plugins cover the gaps between ES modules and real-world dependencies.
- Rollup in Vite: Vite uses Rollup for production builds, so plugin skills transfer between the two.
- Library fit: libraries benefit from preserving ESM output and shipping types; applications often prefer Vite or webpack.

## Related
- [[wiki/frontend/es-modules|ES Modules]] — the module system Rollup optimizes
- [[wiki/frontend/tree-shaking|Tree Shaking]] — Rollup's headline feature
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the ecosystem context
- [[wiki/frontend/vite|Vite]] — Rollup as its production bundler
- [[wiki/frontend/minification|Minification]] — terser plugin integration
- [[wiki/frontend/source-maps|Source Maps]] — debugging Rollup output
