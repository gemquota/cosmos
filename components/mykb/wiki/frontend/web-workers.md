---
type: "concept"
title: "Web Workers"
description: "Background threads for CPU-heavy work"
tags: [web-workers", "concurrency", "javascript", "performance", "browser"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API", "https://html.spec.whatwg.org/multipage/workers.html"]
---

# Web Workers

## Summary
Web Workers run JavaScript on background threads, keeping CPU-heavy work off the main thread where rendering and input live. Workers communicate with the main thread through postMessage and structured-clone messages; module workers can import ES modules. They are the standard answer to long tasks caused by computation.

## Details
- Isolation: workers have no DOM access; they can fetch, use IndexedDB, and compute freely.
- Messaging: postMessage transfers data by structured clone; Transferable objects (ArrayBuffer) move without copying.
- Module workers: type: "module" enables import statements and dynamic import inside the worker.
- Dedicated vs shared: dedicated workers serve one page; SharedWorker serves multiple contexts where supported.
- Patterns: worker pools parallelize jobs; Comlink wraps postMessage into promises for ergonomic RPC.
- Limits: workers add memory overhead and message cost, so split work only when it clears the 50ms task threshold.

## Related
- [[wiki/frontend/long-tasks|Long Tasks]] — the problem workers solve
- [[wiki/frontend/service-workers|Service Workers]] — the network-focused worker cousin
- [[wiki/frontend/fetch-api|Fetch API]] — available inside workers
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — execution contexts in browsers
- [[wiki/web-platforms/browser-engines|Browser Engines]] — thread models
- [[wiki/devops-infra/worker-pools|Worker Pools]] — pooling patterns beyond the browser
