---
type: "concept"
title: "JavaScript Runtimes"
description: "The environments that execute JavaScript: V8, SpiderMonkey, JavaScriptCore, and Node/Deno/Bun"
tags: ["javascript", "runtimes", "engines", "node"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# JavaScript Runtimes

## Summary
A JavaScript runtime is the environment that executes JS: an engine (V8, SpiderMonkey, JavaScriptCore) plus the host APIs. Browsers embed runtimes for web code; Node, Deno, and Bun are standalone runtimes for servers and tools.

## Details
- Engine plus host: browsers add DOM APIs; Node adds fs, http, and process APIs.
- Runtime differences (APIs, semantics, event loop behavior) are a top cross-platform bug source.
- RSIS3 relevance: any dashboard frontend and its build tooling run on these runtimes.

## Related
- [[wiki/web-platforms/browser-engines|Browser Engines]] — JS engines are half of every browser engine
- [[wiki/web-platforms/web-apis|Web APIs]] — host APIs define what the runtime offers
- [[wiki/software-engineering/type-systems|Type Systems]] — TypeScript compiles down to these runtimes
- [[wiki/dev-tools/package-managers|Package Managers]] — npm ecosystem runs on Node
- [[wiki/testing/golden-tests|Golden Tests]] — runtime behavior is locked by goldens
