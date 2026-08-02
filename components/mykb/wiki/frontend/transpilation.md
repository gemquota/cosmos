---
type: "concept"
title: "Transpilation"
description: "Converting modern syntax to target-compatible JavaScript"
tags: [javascript", "transpilation", "babel", "typescript", "build-tools"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://babeljs.io/docs/", "https://developer.mozilla.org/en-US/docs/Glossary/Transpiler"]
---

# Transpilation

## Summary
Transpilation converts source code from one language or syntax version into another — typically modern JavaScript (or TypeScript, JSX) into the ES version supported by target browsers. Babel pioneered the workflow with plugins and presets; esbuild, SWC, and TypeScript's compiler offer faster alternatives. Targets are declared via browserslist.

## Details
- Syntax transforms: arrow functions, optional chaining, class fields, and async/await lower to compatible ES5/ES2015 equivalents.
- TypeScript and JSX: the compiler strips types and transforms JSX into framework runtime calls before bundling.
- Presets: @babel/preset-env applies transforms and polyfills based on browserslist targets; preset-react handles JSX.
- Helpers and runtime: transformed code imports shared helpers (asyncToGenerator), which bundlers can deduplicate.
- Speed: esbuild and SWC compile in native code, orders of magnitude faster than Babel's JavaScript implementation.
- Trade-offs: transpiled output is larger than source; modern engines often make transpilation unnecessary for evergreen targets.

## Related
- [[wiki/frontend/es-modules|ES Modules]] — module syntax transpilation must handle
- [[wiki/frontend/polyfills|Polyfills]] — the runtime complement to syntax transforms
- [[wiki/frontend/minification|Minification]] — the next pipeline stage
- [[wiki/frontend/vite|Vite]] — esbuild-based transpilation
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Patterns]] — TS as a transpiler
- [[wiki/web-platforms/web-standards|Web Standards]] — the target language versions
