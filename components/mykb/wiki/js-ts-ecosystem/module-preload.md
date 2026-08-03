---
type: "concept"
title: "modulepreload"
description: "Preloading ES module graphs before execution"
tags: ["modules", "preload", "esm", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# modulepreload

## Summary
modulepreload fetches and parses ES module graphs before they are needed, parallelizing dependency loading instead of discovering imports one file at a time. It is the browser's hint that a module (and its dependencies) will be used soon.

## Details
- Mechanism: <link rel="modulepreload" href="..."> tells the browser to fetch, parse, and register the module and, in some implementations, its dependencies; combined with import maps, the preloaded module graph is ready before execution; bundlers emit modulepreload hints for entry chunks and their critical dependencies.
- Concrete example: an app preloads the entry module and its imports at page load; navigation to a route triggers dynamic import with the module already fetched — no waterfall; a Vite build emits modulepreload for the initial graph, warming the cache.
- Failure modes: preloading everything, wasting bandwidth on unused modules; preload lists drifting from the actual graph after builds; double-fetching when preload and import race without proper ordering; modulepreload on non-module resources doing nothing; large graphs preloaded greedily delaying first paint.
- Tradeoffs: modulepreload trades startup bandwidth for runtime latency — the module is fetched early so execution is fast; the alternative, on-demand loading, is leaner and slower; the mature pattern is preloading the initial graph and critical split points, not everything.
- Operational notes: audit the preload list per build, measure fetch timing, and verify preloads match imports.
- RSIS3 relevance: the dashboard can preload its entry module graph so first interaction after load is instant — the hint that removes the module waterfall.
- Resource-hint details: modulepreload differs from prefetch — prefetch is a low-priority hint for future navigation while modulepreload fetches at high priority now; add crossorigin when the module is loaded cross-origin so the preload uses the same credentials mode as the import, and prefer preloading over inlining for shared dependencies that multiple routes reuse.

## Related
- [[wiki/js-ts-ecosystem/typescript-systems|TypeScript Systems]]
- [[wiki/js-ts-ecosystem/import-maps|Import Maps]]
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]]
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
- [[wiki/web-platforms/web-standards|Web Standards]]
- [[wiki/web-platforms/web-frameworks|Web Frameworks]]
