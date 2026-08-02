---
type: "concept"
title: "HTML5 APIs"
description: "The platform APIs that moved the web beyond pages: storage, media, geolocation, sensors, and more"
tags: ["html5", "web-apis", "browsers", "platform", "javascript"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API", "https://html.spec.whatwg.org/multipage/"]
---
# HTML5 APIs

## Summary
The HTML5-era platform added capabilities that made the browser an application runtime: localStorage/IndexedDB, audio/video, canvas, geolocation, drag and drop, web workers, and more. Today the platform continues expanding with WebGPU, WebAuthn, and the File System Access API. Feature detection, not assumption, is the operating rule.

## Details
- **Storage family** — localStorage (sync, small), sessionStorage, IndexedDB (transactional, large), and Cache Storage (requests/responses).
- **Media** — video/audio elements with Media Source Extensions; WebRTC for capture and streaming; Web Audio for synthesis.
- **Concurrency** — Web Workers, SharedArrayBuffer (with cross-origin isolation), and OffscreenCanvas.
- **Permissions** — each capability asks via Permissions API; prompts must be justified.
- **Worked example** — the mykb offline reader uses Cache Storage for the shell, IndexedDB for articles, and a service worker for routing.
- **Relevance** — RSIS3's web tooling should catalog platform capabilities as first-class wiki concepts.
- **Progressive capability** — each API is feature-detected, never assumed; secure contexts gate sensitive APIs, and permissions must be requested in response to user intent.

## Related
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/macrotasks|Macrotasks]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/task-queues|Task Queues]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
