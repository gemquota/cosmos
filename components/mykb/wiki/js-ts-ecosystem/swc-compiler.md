---
type: "concept"
title: "SWC Compiler"
description: "Rust-based TypeScript and JavaScript transpiler"
tags: ["swc", "compilers", "typescript", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SWC Compiler

## Summary
SWC is a Rust-based TypeScript and JavaScript transpiler that powers many bundlers' transform stages: it compiles TS, JSX, and modern syntax at Rust speed with correctness close to Babel. It is the transform engine inside Next.js, Parcel, and others.

## Details
- Mechanism: SWC parses source with its Rust parser, applies transforms (TypeScript stripping, JSX, preset-env-style syntax lowering, minification), and emits code with source maps; it is used as a library (next-swc, @swc/core) or CLI; correctness-focused modes and a plugin system (Rust or WASM) extend it.
- Concrete example: a Next.js app transpiles with SWC instead of Babel — faster builds and HMR; a CLI `swc src -d dist` transpiles TS in a fraction of tsc's time; a bundler integrates @swc/core as its transform stage; minification is built in.
- Failure modes: transform edge cases where SWC and Babel diverge (check with a conformance suite); plugin ecosystem younger than Babel's; TypeScript emit without type checking (pair with tsc --noEmit); configuration parity issues when migrating from Babel presets.
- Tradeoffs: SWC trades Babel's mature plugin ecosystem for order-of-magnitude speed — for most projects the transform set is equivalent; the alternative, Babel, is slower and more extensible; the mature pattern is SWC for build speed with type checking handled separately.
- Operational notes: run type checks separately, verify transforms on a representative codebase, and pin versions.
- RSIS3 relevance: the dashboard's TS build benefits from SWC-speed transforms — with tsc --noEmit as the type gate.

## Related
- [[wiki/js-ts-ecosystem/bundlers-and-build-tools|Bundlers and Build Tools]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/esbuild-practice|esbuild in Practice]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/rollup-practice|Rollup in Practice]] — related coverage in the same cluster
- [[wiki/js-ts-ecosystem/vite-practice|Vite in Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — related coverage in the same cluster
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — related coverage in the same cluster
