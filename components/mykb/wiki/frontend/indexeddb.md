---
type: "concept"
title: "IndexedDB"
description: "Client-side structured database for large data"
tags: [indexeddb", "storage", "database", "javascript", "offline"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API", "https://developer.chrome.com/docs/devtools/storage/indexeddb/"]
---

# IndexedDB

## Summary
IndexedDB is the browser's transactional database for large, structured data. It stores JavaScript objects in object stores, indexes them by keys, and supports transactions, cursors, and queries. Unlike Web Storage, it is asynchronous and can hold megabytes to gigabytes of data per origin.

## Details
- Object stores: like tables without schemas; records are structured-clone serialized values addressed by keys.
- Indexes: secondary keys over record properties enable lookups and ranged queries beyond the primary key.
- Transactions: reads and writes run in read-only or read-write transactions that commit atomically.
- Asynchronous API: promise wrappers (idb, Dexie) hide the callback-heavy native API.
- Cursor iteration: cursors walk records in key order for pagination and bulk processing.
- Use cases: offline-first apps, caches of fetched data, sync queues, and media libraries; service workers use it for offline assets.

## Related
- [[wiki/frontend/web-storage|Web Storage]] — the lighter-weight alternative
- [[wiki/frontend/service-workers|Service Workers]] — offline pipelines built on IndexedDB
- [[wiki/frontend/fetch-api|Fetch API]] — data indexed after fetching
- [[wiki/data-storage/00-index|Data Storage]] — broader storage architecture
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — offline experiences using it
- [[wiki/frontend/progressive-web-apps|Progressive Web Apps]] — the app layer over IndexedDB
