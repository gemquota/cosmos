---
type: "concept"
title: "Dynamic Import"
description: "Loading modules on demand with import()"
tags: ["modules", "esm", "javascript", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Dynamic Import

## Summary
Dynamic import — import() — loads modules on demand at runtime instead of at parse time. It enables code splitting and lazy routes: a bundler sees the import, extracts it into its own chunk, and the browser fetches it only when the code path runs.

## Details
- Mechanism: import(path) returns a promise resolving to the module namespace; bundlers statically analyze the string argument (and common template patterns) to create split points; each dynamic import becomes a separate chunk fetched on demand; it composes with top-level await and works in both browsers and Node.
- Concrete example: a router that lazy-loads each page — const page = await import(`./pages/${name}.js`) — with bundlers generating per-page chunks; a heavy library (charting, PDF) imported only when a user opens the relevant view; preload hints and modulepreload warm the split chunks.
- Failure modes: dynamic expressions the bundler cannot analyze (fully dynamic strings) defeating code splitting, producing one giant chunk or runtime misses; dynamic imports of non-existent paths failing at runtime instead of build time; chunk waterfall — many sequential small fetches slowing first render; circular dynamic imports; forgetting prefetching for likely-next routes, so the lazy path is slow.
- Tradeoffs: dynamic import trades initial bundle size for runtime fetch latency — the split point decision controls the balance; the alternative, static imports everywhere, is simpler and faster on warm caches; the mature pattern is route- and feature-level splitting with prefetching for the likely next step.
- Operational notes: inspect the chunk graph, set prefetch strategies, and test the lazy paths for errors.
- RSIS3 relevance: the dashboard can lazy-load heavy views (graphs, meta-viewers) with dynamic imports — initial load stays light while features remain available.

## Related
- [[wiki/js-ts-ecosystem/typescript-systems|TypeScript Systems]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/top-level-await|Top-Level Await]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-preload|modulepreload]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/import-maps|Import Maps]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/web-platforms/web-standards|Web Standards]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
