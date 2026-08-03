---
type: "concept"
title: "Import Maps"
description: "Mapping bare module specifiers to URLs in the browser"
tags: ["modules", "esm", "import-maps", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Import Maps

## Summary
Import maps map bare module specifiers (react, lodash) to URLs in the browser, letting native ESM resolve dependencies without a bundler. They remove the bundler from some setups — the browser resolves the same way Node does with package maps.

## Details
- Mechanism: a <script type="importmap"> declares mappings from specifier to URL; module scripts import bare names and the browser resolves them; scopes allow per-prefix overrides; fallbacks and integrity can be layered on; the map is fetched before module execution.
- Concrete example: an app imports react and the import map points it at a CDN URL; a dev setup maps specifiers to local dev servers and production to hashed URLs; scopes map a test override for one module; multiple apps on a page share one map, deduplicating dependencies.
- Failure modes: the map not loaded before modules execute (a classic ordering bug); CDN outages with no fallback; integrity and caching interactions — hashed URLs need map updates on every release; bare specifiers resolving differently in Node and browser; large maps becoming a maintenance surface.
- Tradeoffs: import maps eliminate bundler-generated dependency graphs for simple setups — faster, more cacheable, closer to the platform — at the cost of losing tree shaking, minification, and build-time optimization; the mature pattern is import maps for dependency resolution plus a bundler for application code.
- Operational notes: keep the map versioned, add SRI where feasible, and test module loading order.
- RSIS3 relevance: the dashboard could use an import map for its few external dependencies — native ESM resolution with cacheable URLs, no bundler step for vendors.

## Related
- [[wiki/js-ts-ecosystem/typescript-systems|TypeScript Systems]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/top-level-await|Top-Level Await]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/web-platforms/web-standards|Web Standards]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
