---
type: "concept"
title: "Rollup in Practice"
description: "Tree-shaking-first bundler for libraries and apps"
tags: ["rollup", "bundlers", "javascript", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Rollup in Practice

## Summary
Rollup is a tree-shaking-first bundler for libraries and applications: ESM input, precise dead-code elimination, and first-class output formats (ESM, CJS, IIFE) make it the default choice for publishing libraries. It powers the build core of Vite.

## Details
- Mechanism: Rollup parses ESM, builds a module graph, and tree-shakes unused exports via static analysis; plugins transform, resolve, and emit; outputs configure formats, code splitting, and external dependencies; watch mode and incremental builds support iteration.
- Concrete example: a library publishes ESM and CJS builds from the same source — package.json exports map each entry; Rollup drops unused exports, keeping bundle size minimal; a Vite app build delegates to Rollup for production output; external: marks peer dependencies so they are not bundled.
- Failure modes: tree shaking defeated by side-effectful code or dynamic access patterns; circular dependencies causing build or runtime issues; output format interop bugs (CJS named exports); plugins with ordering surprises; code splitting producing unexpected chunks in library output.
- Tradeoffs: Rollup's output precision and tree shaking suit published libraries; esbuild bundles faster but with less aggressive dead-code elimination; webpack carries ecosystem depth; the mature pattern is Rollup for libraries, Vite/Rollup for apps, and esbuild where raw speed wins.
- Operational notes: verify tree shaking with bundle analysis, test all output formats, and pin peer dependencies as external.
- RSIS3 relevance: if cosmos publishes the dashboard as a reusable component or library, Rollup's ESM/CJS outputs and tree shaking keep the artifact lean.
- Output control: preserveModules keeps the source file structure for library consumers, and explicit chunkFileNames and assetFileNames stabilize long-term caching; publish sourcemaps with the library so downstream debugging works, set external and peerDependencies explicitly so the consumer's copy is used instead of a bundled duplicate, since two copies of a package break instanceof checks and stateful singletons.

## Related
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]]
- [[wiki/js-ts-ecosystem/vite-practice|Vite in Practice]]
- [[wiki/js-ts-ecosystem/webpack-practice|Webpack in Practice]]
- [[wiki/js-ts-ecosystem/parcel-practice|Parcel in Practice]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
