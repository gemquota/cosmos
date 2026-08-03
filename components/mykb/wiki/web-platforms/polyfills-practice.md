---
type: "concept"
title: "Polyfills in Practice"
description: "Emulating missing browser APIs for older engines"
tags: ["polyfills", "compatibility", "javascript", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Polyfills in Practice

## Summary

Polyfills emulate missing platform APIs so older engines run modern code. Good polyfill practice limits their number, loads them conditionally, and plans their removal — every polyfill is a maintenance and security liability.

## Details
- Mechanism: a polyfill detects a missing API and installs a JS implementation (e.g. Array.prototype.at, ResizeObserver, Intl locale data); loading strategies include bundling unconditionally, feature-detecting at runtime with a dynamic import, or using polyfill services that serve only what the requesting UA lacks.
- Concrete example: a dashboard supporting an old in-app WebView loads ResizeObserver and CSS.escape polyfills only when feature detection fails, so modern browsers download nothing extra; the polyfill bundle is version-pinned and reviewed, since polyfills reimplement security-sensitive APIs.
- Failure modes: shipping polyfills nobody needs (bundle bloat and startup cost); polyfills that change behavior subtly (native is faster and more correct); loading polyfills that themselves rely on the missing API (ordering bugs); and forgetting to remove them when the support baseline moves — a stale polyfill can mask native bugs or conflict.
- Operational tradeoffs: every polyfill buys support at the cost of complexity; prefer transpilation (browserslist-driven syntax) plus a short, audited polyfill list. Track usage per API and delete polyfills on the schedule your evergreen baseline allows.
- RSIS3/mykb relevance: the wiki browser's polyfill list is an audited, small set recorded here, so the loop removes entries as the documented browser baseline advances.
- Ordering: feature-detect once at bootstrap, load polyfills before app code, and assert the API exists afterward so a failed load fails loudly instead of misbehaving subtly.
- Licensing and supply chain: polyfills are third-party code with security impact; pin versions, run them through the same dependency audit as everything else, and prefer platform-native APIs as soon as the baseline allows.

## Related
- [[wiki/web-platforms/browser-rendering-pipeline|Browser Rendering Pipeline]]
- [[wiki/web-platforms/graceful-enhancement|Graceful Enhancement]]
- [[wiki/web-platforms/evergreen-browsers|Evergreen Browsers]]
- [[wiki/web-platforms/caniuse-practice|Can I Use in Practice]]
- [[wiki/web-platforms/web-standards|Web Standards]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
