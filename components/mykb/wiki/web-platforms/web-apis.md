---
type: "concept"
title: "Web APIs"
description: "The browser-provided interfaces — DOM, fetch, storage, sensors — that web code calls"
tags: ["web-apis", "browser", "javascript", "platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Web APIs

## Summary
Web APIs are the interfaces browsers expose to JavaScript: DOM manipulation, fetch, localStorage, geolocation, canvas, and hundreds more. MDN documents them as the platform surface every web application builds on.

## Details
- Organized into families: DOM/HTML, data (fetch, Storage, IndexedDB), media, device, and performance APIs.
- Feature detection and progressive enhancement handle APIs that not all engines ship.
- RSIS3 relevance: agent browser tooling drives these APIs through automation.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — standards define the API surface
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — the foundational document API
- [[wiki/web-platforms/browser-engines|Browser Engines]] — engines implement the APIs
- [[wiki/api-protocols/rest-apis|REST APIs]] — fetch consumes REST from the browser
- [[wiki/testing/golden-tests|Golden Tests]] — API behavior is golden-testable
