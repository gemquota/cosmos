---
type: "concept"
title: "Service Workers"
description: "Network interception, lifecycle, and offline caching"
tags: [service-workers", "offline", "pwa", "caching", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API", "https://web.dev/articles/offline-cookbook"]
---

# Service Workers

## Summary
Service workers are scriptable network proxies that sit between the page and the network. They intercept fetch events, serve cached responses, enable offline experiences, and handle push notifications. Their lifecycle — install, activate, fetch — and update rules make them the backbone of progressive web apps.

## Details
- Lifecycle: install pre-caches assets; activate cleans old caches; fetch serves requests with the chosen strategy.
- Caching strategies: cache-first for immutable assets, network-first for navigations, stale-while-revalidate for speed.
- HTTPS requirement: service workers only register on secure origins (localhost is exempt) because they control traffic.
- Update flow: byte-different script triggers a new worker; clients switch over on next load unless skipWaiting is used.
- Scope: a worker controls pages under its registration path; clients.claim extends control to open pages.
- APIs: push events, background sync, and periodic sync build notification and data-sync features on top.

## Related
- [[wiki/frontend/progressive-web-apps|Progressive Web Apps]] — the app model service workers enable
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — platform notes on the same model
- [[wiki/frontend/browser-caching|Browser Caching]] — HTTP caching combined with workers
- [[wiki/api-protocols/http-caching|HTTP Caching]] — the protocol semantics behind strategies
- [[wiki/frontend/fetch-api|Fetch API]] — the request model workers intercept
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — the native counterpart
