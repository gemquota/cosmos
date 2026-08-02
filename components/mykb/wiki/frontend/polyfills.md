---
type: "concept"
title: "Polyfills"
description: "Feature detection and shims for legacy browsers"
tags: [javascript", "polyfills", "browsers", "compatibility", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Polyfill", "https://github.com/zloirock/core-js"]
---

# Polyfills

## Summary
A polyfill is code that implements a missing browser API so older engines gain modern behavior. Polyfills pair with feature detection — check before shimming — and with transpilation, which handles syntax while polyfills handle runtime APIs. They extend reach at the cost of bundle size and sometimes fidelity.

## Details
- Mechanism: if (!window.fetch) { ... } installs an implementation; the global is then available everywhere.
- Syntax vs runtime: Babel and esbuild convert syntax; polyfills such as core-js provide missing Promise, Array, and Intl features.
- Targets: browserslist drives which polyfills ship, so a modern-only audience may need none at all.
- Cost: polyfills add bytes and can be slower than native implementations; load them conditionally by feature.
- Pitfalls: partial implementations diverge subtly from specs; test on real legacy browsers, not just emulators.
- Modern practice: bundle-splitting polyfills into a separate legacy chunk, or serving an ES5 build only to legacy browsers.

## Related
- [[wiki/frontend/transpilation|Transpilation]] — the syntax half of legacy support
- [[wiki/frontend/es-modules|ES Modules]] — an API polyfilled via bundlers
- [[wiki/web-platforms/browser-engines|Browser Engines]] — the engines being targeted
- [[wiki/frontend/minification|Minification]] — keeping polyfill payloads small
- [[wiki/web-platforms/web-standards|Web Standards]] — what polyfills approximate
- [[wiki/frontend/performance-budgets|Performance Budgets]] — accounting for polyfill weight
