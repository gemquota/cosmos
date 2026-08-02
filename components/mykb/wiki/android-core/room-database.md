---
type: "concept"
title: "Room Database"
description: "SQLite object mapper with compile-time query validation and Flow support"
tags: ["android", "room", "sqlite", "database"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/training/data-storage/room", "https://developer.android.com/reference/androidx/room/package-summary"]
---

# Room Database

## Summary


## Details
- Room is the SQLite object-mapping layer in Jetpack: entities map tables, DAOs map queries, and the schema is validated at compile time.
- Relations, migrations, and type converters are first-class, and Room works with Flow and coroutines for reactive queries.
- Schema versioning and migration tests keep app updates safe; a wrong migration loses user data permanently.
- Room removes raw Cursor and SQL boilerplate while keeping full SQL power for complex queries.
- **Worked example / comparison** — Worked example — a @Dao interface declares a Flow<List<Article>> query; the UI collects it and updates automatically when the underlying table changes.
- For mykb, Room is the on-device persistence layer that stores the mobile wiki cache and query history.

## Related
- [[wiki/android-core/android-content-providers|Android Content Providers]]
- [[wiki/android-core/kotlin-flows|Kotlin Flows]]
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]]
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]]
- [[wiki/devops-infra/sqlite|SQLite]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/data-storage/code-in-wiki|Code in the Wiki]]
