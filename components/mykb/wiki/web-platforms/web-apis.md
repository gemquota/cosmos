---
type: "concept"
title: "Web APIs"
description: "The browser-provided interfaces — DOM, fetch, storage, sensors — that web code calls"
tags: ["web-apis", "browser", "javascript", "platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Web APIs

## Summary

The web platform's API surface — fetch, DOM, storage, workers, sensors, media, and more — is the browser's standard library. Engineering with it well means feature-detecting capabilities, minding permission and lifecycle semantics, and knowing what needs polyfills.

## Details
- Mechanism: web APIs are exposed on window/navigator/document and inside workers; they range from stable (fetch, DOM) to experimental (battery, sensors) with support gated by feature detection, permissions, and secure-context requirements. Browser engines implement them against standards, with per-engine gaps and quirks.
- Concrete example: fetch replaces XHR with promise semantics and streaming (ReadableStream bodies); the Storage API and IndexedDB replace cookies/localStorage for scale; the Web Animations API unifies CSS animations and JS timelines; Web Workers and OffscreenCanvas move heavy work off the main thread.
- Failure modes: assuming API availability without detection (some APIs exist only in secure contexts); permission-required APIs (geolocation, clipboard, notifications) failing silently when denied; lifecycle surprises (IndexedDB transactions, worker termination); and memory/performance cliffs from APIs that look cheap (large IndexedDB blobs, many observers).
- Operational tradeoffs: platform APIs are dependency-free and battle-tested but vary across engines and versions; the decision is when to use them directly vs a library that normalizes (fetch → axios is usually unnecessary; IndexedDB → a wrapper is often wise). Feature-detect, fall back, and version your capability matrix.
- RSIS3/mykb relevance: the wiki browser's feature matrix (which APIs the dashboard can use) is maintained here, so the loop's generated code detects rather than assumes.
- Capability matrix: maintain a per-API matrix (supported engines, permissions, secure-context requirement) as a wiki note so new features are adopted by detection, not assumption.
- Deprecation watch: track API removals (e.g. appcache, unload events) and schedule migration as part of the loop's browser-baseline reviews.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — standards define the API surface
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — the foundational document API
- [[wiki/web-platforms/browser-engines|Browser Engines]] — engines implement the APIs
- [[wiki/api-protocols/rest-apis|REST APIs]] — fetch consumes REST from the browser
- [[wiki/testing/golden-tests|Golden Tests]] — API behavior is golden-testable
