---
type: "concept"
title: "Room Database"
description: "SQLite object mapper with compile-time query validation and Flow support"
tags: ["android", "room", "sqlite", "database"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Room Database

Room is the Jetpack SQLite layer: entities, DAOs, and a database class map to tables and queries checked at compile time. It returns LiveData or Flow for reactive UI and supports migrations between schema versions.
- DAO methods compile-check SQL; indexes speed lookups.
- DatabaseBuilder with fallbackToDestructiveMigration only as a last resort.
- Works with Kotlin coroutines and flows natively.
- Pairs with content providers for cross-app data sharing.

## Related

- [[wiki/android-core/android-content-providers|Android Content Providers]] — Room often backs a provider
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — Room emits reactive query results
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — Room is the local source of truth
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — full-text search over Room tables
- [[wiki/devops-infra/sqlite|SQLite]] — the underlying engine
