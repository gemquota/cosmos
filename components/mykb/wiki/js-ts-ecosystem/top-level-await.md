---
type: "concept"
title: "Top-Level Await"
description: "Using await at module scope in ESM"
tags: ["esm", "async", "javascript", "modules"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Top-Level Await

## Summary
Top-level await lets ESM modules use await at module scope: the module's evaluation pauses until the awaited promise settles, and its importers wait for it. It makes async initialization idiomatic in modules — with the cost that one slow awaited dependency delays every importer.

## Details
- Mechanism: in ESM, top-level await is allowed by the language; the module's dependency graph resolves first, then modules evaluate, and a top-level await suspends evaluation of that module (and anything importing it) until it settles; dynamic import of a top-level-await module returns a promise that resolves after evaluation completes.
- Concrete example: a module loads configuration from an API at import time with top-level await; an i18n module initializes dictionaries before exporting; a data module fetches a manifest once, and all importers await the same settled promise; CJS cannot use it — a migration constraint.
- Failure modes: slow top-level awaits delaying the whole import graph (startup regression); await on non-promises creating unnecessary suspensions; bundlers targeting older formats having to transform or forbid it; error handling — a rejected top-level await rejects the module, and importers must handle it; circular imports with top-level await producing undefined exports.
- Tradeoffs: top-level await makes async module init clean — the alternative, async init functions or entry-point awaits, is boilerplate and easy to forget; the cost is that evaluation becomes order-dependent on network and timing; the mature pattern is top-level await for true one-time init, with caching so it settles once.
- Operational notes: audit which modules await at top level, monitor startup timing, and keep rejected awaits handled.
- RSIS3 relevance: the dashboard could initialize its data layer with top-level await — clean startup, provided the awaited dependencies are fast and reliable.

## Related
- [[wiki/js-ts-ecosystem/typescript-systems|TypeScript Systems]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-preload|modulepreload]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/import-maps|Import Maps]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/web-platforms/web-standards|Web Standards]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
