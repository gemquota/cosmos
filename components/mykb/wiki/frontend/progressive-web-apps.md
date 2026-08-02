---
type: "concept"
title: "Progressive Web Apps"
description: "Installability, app shell, and offline experiences"
tags: [pwa", "offline", "installable", "service-workers", "web-apps"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/learn/pwa/", "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps"]
---

# Progressive Web Apps

## Summary
Progressive web apps combine the reach of the web with app-like capabilities: they install to the home screen, launch full-screen, work offline, and receive push notifications. The core ingredients are HTTPS, a web app manifest, and a service worker. PWAs update through the web, sidestepping app-store distribution entirely.

## Details
- Manifest: name, icons, start_url, display mode, and theme color define installability and the installed experience.
- App shell: a cached HTML, CSS, and JS skeleton makes launches instant, with content filling from cache or network.
- Offline: service-worker caching strategies keep the shell and recent content available without connectivity.
- Install criteria: modern browsers relax requirements but typically expect HTTPS, a manifest, and a functional offline fallback.
- Platform quirks: iOS supports the core model with limitations; Android adds WebAPK packaging and richer integration.
- Fit: content, commerce, and tools benefit; complex native capabilities (background GPS, deep OS integration) still favor native.

## Related
- [[wiki/frontend/service-workers|Service Workers]] — the offline engine of PWAs
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — the platform-level article
- [[wiki/frontend/browser-caching|Browser Caching]] — HTTP caching inside the app shell
- [[wiki/frontend/indexeddb|IndexedDB]] — storing app data offline
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — design for connectivity loss
- [[wiki/frontend/fetch-api|Fetch API]] — requests the worker intercepts
