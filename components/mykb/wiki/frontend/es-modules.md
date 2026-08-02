---
type: "concept"
title: "ES Modules"
description: "import/export semantics and static module graphs"
tags: [javascript", "es-modules", "modules", "web-platform", "standard"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules", "https://nodejs.org/api/esm.html"]
---

# ES Modules

## Summary
ES modules are the standardized JavaScript module system, built on import and export declarations. Their static structure — imports are known before execution — enables tree shaking, dead-code elimination, and parallel loading. Browsers run them natively with defer semantics, and Node.js supports them alongside CommonJS.

## Details
- Syntax: export names or defaults; import binds live references, so exported values update as the module state changes.
- Static graph: import paths are resolved at load time, letting tools analyze the full dependency graph without executing code.
- Browser behavior: module scripts defer by default and execute once per URL; import maps rewrite bare specifiers.
- Dynamic import: import() returns a promise, enabling code splitting and lazy loading at runtime.
- Node interop: .mjs or type: module enables ESM in Node; CommonJS require interop is handled by bundlers and Node's loader.
- Strict mode: modules always run strict, share module scope, and support top-level await in modern engines.

## Related
- [[wiki/frontend/tree-shaking|Tree Shaking]] — depends on static module structure
- [[wiki/frontend/module-bundlers|Module Bundlers]] — consume the module graph
- [[wiki/frontend/polyfills|Polyfills]] — legacy-browser shims for modules
- [[wiki/frontend/transpilation|Transpilation]] — converting module syntax for old targets
- [[wiki/frontend/code-splitting|Code Splitting]] — dynamic import in practice
- [[wiki/web-platforms/web-standards|Web Standards]] — the standard's home in the platform
