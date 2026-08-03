---
type: "concept"
title: "CommonJS vs ESM"
description: "Two JavaScript module systems and their resolution differences"
tags: ["modules", "esm", "commonjs", "javascript"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CommonJS vs ESM

## Summary
CommonJS and ESM are the two JavaScript module systems. CJS (require/module.exports) resolves synchronously and is the Node legacy standard; ESM (import/export) is the language standard, async, statically analyzable, and tree-shakeable. Interop rules govern named and default exports between them.

## Details
- Mechanism: CJS loads modules synchronously at runtime, executing the file and exposing module.exports; ESM parses and links statically — imports are hoisted, cycles are handled via live bindings, and top-level await is allowed; Node decides per file by extension (.mjs/.cjs) or package type; bundlers unify both into one graph.
- Interop: Node allows require of ESM (with caveats) and import of CJS (default is module.exports); named exports from CJS are detected heuristically, which can break; bundlers normalize the differences so application code rarely sees them.
- Concrete example: a library ships both builds (exports map with require/import conditions); a CJS app requires it synchronously; an ESM app imports named exports; a dual-package hazard appears when a package is loaded as both, creating two instances of shared state.
- Failure modes: dual-package hazard — two copies of a module with separate state; named-import breakage when relying on CJS interop heuristics; synchronous require inside ESM top-level failing; circular dependencies behaving differently across systems; __dirname and import.meta differences breaking shared code.
- Tradeoffs: ESM is the future — static analysis, tree shaking, and standards — but CJS remains pervasive in Node libraries; the mature pattern is ESM-first authoring with dual exports for compatibility, and tools that normalize the difference.
- Operational notes: test both entry points, avoid relying on named-export interop, and keep package exports explicit.
- RSIS3 relevance: the dashboard and tooling should target ESM where the runtime allows, with CJS interop only where dependencies demand it.

## Related
- [[wiki/js-ts-ecosystem/typescript-systems|TypeScript Systems]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/top-level-await|Top-Level Await]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/module-preload|modulepreload]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/web-platforms/web-standards|Web Standards]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
