---
type: "concept"
title: "JavaScript Runtimes"
description: "The environments that execute JavaScript: V8, SpiderMonkey, JavaScriptCore, and Node/Deno/Bun"
tags: ["javascript", "runtimes", "engines", "node"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# JavaScript Runtimes

## Summary

JavaScript runs on engine + runtime pairs — V8/Node, SpiderMonkey/Firefox, JavaScriptCore/Safari, plus WebAssembly and embedded runtimes. The choice of runtime decides available APIs, startup cost, and performance characteristics, not just syntax.

## Details
- Mechanism: an engine compiles and executes JS (V8's TurboFan/Maglev, JSC's B3/DFG); the runtime supplies the host APIs — Node's fs/net, Deno's web-standard surface, the browser's DOM. Same language, different platform contracts, so code that assumes Node globals breaks in the browser and vice versa.
- Concrete example: a build script using process.env and fs works in Node only; porting it to Deno or Bun needs import.meta.env or the web-standard fs; in the browser the same logic needs a worker or server call. WebAssembly adds a second execution tier for compute-heavy kernels compiled from Rust/C.
- Failure modes: assuming V8 semantics everywhere (stack traces, GC timing differ); relying on Node-specific modules in edge runtimes that only ship web APIs; version drift between local runtime and production (Node 18 vs 22 behaviors); and startup cost differences — serverless cold starts punish runtimes that defer initialization.
- Operational tradeoffs: Node's ecosystem and stability vs Deno/Bun's modern defaults and speed; browsers constrain to web APIs by design, which is safer for portable code. Pin runtime versions in tooling and test in the actual deployment runtime, not just the dev machine.
- RSIS3/mykb relevance: the SPACE web UI and wiki browser target browser runtimes only, and build scripts run under the pinned Node version recorded in this note to keep loop tooling reproducible.
- Portability lint: configure tooling to flag Node- or browser-only globals when the target runtime is the other; this catches most portability breaks before deployment.
- Cold starts: for serverless, prefer lightweight entrypoints and lazy requires so the runtime initializes only what the first request needs.

## Related
- [[wiki/web-platforms/browser-engines|Browser Engines]] — JS engines are half of every browser engine
- [[wiki/web-platforms/web-apis|Web APIs]] — host APIs define what the runtime offers
- [[wiki/software-engineering/type-systems|Type Systems]] — TypeScript compiles down to these runtimes
- [[wiki/dev-tools/package-managers|Package Managers]] — npm ecosystem runs on Node
- [[wiki/testing/golden-tests|Golden Tests]] — runtime behavior is locked by goldens
