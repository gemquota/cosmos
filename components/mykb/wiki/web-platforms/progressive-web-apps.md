---
type: "concept"
title: "Progressive Web Apps"
description: "Web applications that use platform capabilities — installability, offline, push — while remaining web-delivered"
tags: ["pwa", "offline", "service-workers", "web-apps"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/progressive-web-apps/"]
---

# Progressive Web Apps

## Summary
Progressive web apps (PWAs) are web applications that progressively gain native-app capabilities: installability, offline operation, and push notifications, all delivered over HTTPS from a normal URL. Web.dev documents the pattern as the web platform's answer to app stores.

## Details
- The technical core: a service worker for offline caching and background sync, a web app manifest for installability, and HTTPS as a hard requirement.
- Installability: the browser adds the app to the home screen or OS app menu; there is no store review or install wall.
- Offline-first strategies cache app shells and update in the background, making PWAs resilient on poor networks.
- Capabilities keep expanding: push, badges, file system access, and payment handlers bridge more of the native gap.
- Trade-offs: platform services (background, sensors, stores) still lag native in places; support varies across engines.
- RSIS3 relevance: a mykb dashboard as a PWA would let RSIS3's operator open it offline on the same device.
- Worked example: an app shell cached by a service worker, with runtime data refreshed when online.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — PWAs are built from standard web APIs
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — offline caching is a performance strategy
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — service workers run in a dedicated runtime
- [[wiki/web-platforms/web-apis|Web APIs]] — manifest, cache, and push are web APIs
- [[wiki/api-protocols/http-caching|HTTP Caching]] — network caching complements service workers
- [[wiki/devops-infra/observability|Observability]] — PWA installs and offline use deserve telemetry
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — the mobile device context PWAs target
