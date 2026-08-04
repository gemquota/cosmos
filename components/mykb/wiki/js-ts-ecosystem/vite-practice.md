---
type: "entity"
title: "Vite in Practice"
description: "Dev-server-first build tool using native ES modules"
tags: ["vite", "bundlers", "dev-server", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Vite in Practice

## Summary
Vite is a dev-server-first build tool: it serves unbundled native ESM in development (fast startup, instant HMR) and bundles for production with Rollup. esbuild handles dependency pre-bundling and transforms; the result is a modern default for frontend apps.

## Details
- Mechanism: in dev, the server serves modules as native ESM over HTTP — no bundling of app code — with esbuild pre-bundling dependencies for caching; HMR pushes module updates to the browser; production builds delegate to Rollup for optimized, tree-shaken output; plugins unify the dev and build pipelines.
- Concrete example: a React app with Vite starts instantly and hot-reloads on save; dependency pre-bundling makes first load fast; a production build outputs hashed, minified chunks; a library mode builds ESM/CJS outputs; huge repos may need caching tuning as module counts grow.
- Failure modes: dev and prod behavior diverging (esbuild transforms vs Rollup output); slow cold starts on very large dependency graphs; ESM-only assumptions breaking on legacy browsers without the legacy plugin; plugin ecosystem gaps versus webpack; HMR edge cases with non-standard module patterns.
- Tradeoffs: Vite trades webpack's universality for a dramatically better dev experience and simpler config; the cost is production-build delegation and some ecosystem gaps; the mature pattern is Vite for new apps and webpack where legacy plugins bind.
- Operational notes: pin the version, test prod builds in CI, and keep the dev/prod parity checked.
- RSIS3 relevance: the dashboard's frontend is a natural Vite app — instant dev feedback and Rollup-optimized production output.
- Config surface: most projects only need server.proxy for dev, env-var handling, and build.rollupOptions for production; resist adding plugins the defaults cover, keep the config small so upgrades stay cheap, and verify dev/prod parity in CI because the esbuild dev transforms and Rollup production output can drift on exotic syntax.

## Related
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]]
- [[wiki/js-ts-ecosystem/webpack-practice|Webpack in Practice]]
- [[wiki/js-ts-ecosystem/parcel-practice|Parcel in Practice]]
- [[wiki/js-ts-ecosystem/turbopack-practice|Turbopack in Practice]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
