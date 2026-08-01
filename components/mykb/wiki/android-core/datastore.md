---
type: "concept"
title: "DataStore"
description: "Jetpack DataStore: coroutine-based preferences and proto storage"
tags: ["android", "datastore", "storage", "kotlin"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# DataStore

DataStore is the Jetpack replacement for SharedPreferences: Preferences DataStore for key-value pairs and Proto DataStore for typed objects, both exposing Flow APIs with coroutine safety.
- Asynchronous, transactional, and consistent with Room-style discipline.
- Preferences DataStore maps to a typed key-value API.
- Proto DataStore defines a schema and generates accessors.
- Migrate from SharedPreferences with built-in migration helpers.

## Related

- [[wiki/android-core/shared-preferences|Shared Preferences]] — the legacy store DataStore replaces
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — DataStore exposes Flow reads
- [[wiki/android-core/room-database|Room Database]] — sibling Jetpack persistence layer
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — preferences survive offline on device
