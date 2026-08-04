---
type: "entity"
title: "Vite"
description: "Dev server and build architecture on esbuild and Rollup"
tags: [vite", "build-tools", "bundlers", "javascript", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://vitejs.dev/guide/", "https://vitejs.dev/guide/why.html"]
---

# Vite

## Summary
Vite is a build tool that serves source files as native ES modules in development and produces optimized production bundles with Rollup. Development needs no bundling: the browser loads modules directly while Vite transforms on demand, and esbuild pre-bundles dependencies for speed. The result is instant startup and fast HMR.

## Details
- Native ESM dev server: browsers import source modules directly; Vite transforms TS, JSX, and CSS per request.
- Dependency pre-bundling: esbuild converts node_modules to ESM and caches them, avoiding hundreds of module requests.
- HMR: hot updates apply through the module graph with framework-specific boundaries, preserving state.
- Production build: Rollup emits tree-shaken, minified chunks with asset handling and hashed filenames.
- Plugins: a Rollup-compatible plugin API covers framework integrations, from React to Svelte to SSR.
- Ecosystem: scaffolding via create-vite; framework templates include SSR, library mode, and environment variables.

## Related
- [[wiki/frontend/module-bundlers|Module Bundlers]] — the architecture Vite combines
- [[wiki/frontend/es-modules|ES Modules]] — the native module model the dev server uses
- [[wiki/frontend/hot-module-replacement|Hot Module Replacement]] — Vite's fast HMR
- [[wiki/frontend/dev-server|Dev Server]] — the local serving layer
- [[wiki/frontend/rollup|Rollup]] — the production bundler inside Vite
- [[wiki/frontend/transpilation|Transpilation]] — esbuild transforms in the pipeline
