---
type: "concept"
title: "IndexedDB in Practice"
description: "The browser's transactional object store for structured data, offline-first apps, and caches"
tags: ["indexeddb", "storage", "offline", "browsers", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API", "https://web.dev/articles/indexeddb"]
---
# IndexedDB in Practice

## Summary
IndexedDB is the browser's built-in transactional database: object stores, indexes, cursors, and queries. It stores structured data (objects, blobs) far beyond cookies and localStorage, making it the backbone of offline-first apps and client caches. Promises via wrapper libraries tame its callback API.

## Details
- **Model** — databases contain object stores; stores index by keyPath or key generator; indexes enable lookups by other fields.
- **Transactions** — readwrite and readonly transactions with automatic commit; versions upgrade schemas.
- **Patterns** — cache data with an invalidation strategy, store blobs for offline media, and mirror server state for optimistic UI.
- **Quotas** — storage is shared and evictable; check `navigator.storage.estimate()` and persist where needed.
- **Worked example** — the mykb reader caches fetched article bodies in IndexedDB, serving them offline with a staleness flag.
- **Relevance** — RSIS3's local-first tooling should treat IndexedDB as the client-side durable layer.

## Related
- [[wiki/web-platforms/atomic-writes|Atomic Writes]] — adjacent concept in this wiki
- [[wiki/web-platforms/file-locks|File Locking]] — adjacent concept in this wiki
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]] — adjacent concept in this wiki
- [[wiki/web-platforms/toctou|TOCTOU Vulnerabilities]] — adjacent concept in this wiki
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
