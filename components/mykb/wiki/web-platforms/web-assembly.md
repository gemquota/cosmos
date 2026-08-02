---
type: "concept"
title: "WebAssembly"
description: "Portable, low-level binary format that runs near-native code in the browser"
tags: ["wasm", "web", "performance", "compilers", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://webassembly.org/", "https://developer.mozilla.org/en-US/docs/WebAssembly"]
---
# WebAssembly

## Summary
WebAssembly (Wasm) is a binary instruction format executed at near-native speed in a sandbox. Languages like Rust, C/C++, Go, and Swift compile to Wasm for the browser, server runtimes, and edge functions. It complements JavaScript for CPU-heavy work: codecs, games, cryptography, and ML inference.

## Details
- **Execution model** — linear memory, typed instructions, and explicit imports/exports; no GC by default, with Wasm GC arriving for managed languages.
- **Toolchain** — Emscripten and wasm-bindgen target Wasm; the component model standardizes interfaces between modules.
- **Performance** — SIMD, threads, and bulk memory close the gap to native; instantiation and memory growth are the usual costs.
- **Security** — sandboxed memory and validated modules; supply-chain and host-API boundaries still need care.
- **Worked example** — a Rust parser tokenizes the mykb corpus as a Wasm module, offloading heavy text work from JS.
- **Relevance** — RSIS3's on-device inference and parsing can move hot loops into Wasm while keeping the orchestration in Python/JS.

## Related
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/commonjs-vs-esm|CommonJS vs ESM]] — adjacent concept in this wiki
- [[wiki/web-platforms/polyfills-practice|Polyfills in Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/evergreen-browsers|Evergreen Browsers]] — adjacent concept in this wiki
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
