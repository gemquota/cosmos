---
type: "entity"
title: "DataStore"
description: "Jetpack DataStore: coroutine-based preferences and proto storage"
tags: ["android", "datastore", "storage", "kotlin"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# DataStore

DataStore is the Jetpack replacement for SharedPreferences: Preferences DataStore for key-value pairs and Proto DataStore for typed objects, both exposing Flow APIs with coroutine safety.
- Asynchronous, transactional, and consistent with Room-style discipline.
- Preferences DataStore maps to a typed key-value API.
- Proto DataStore defines a schema and generates accessors.
- Migrate from SharedPreferences with built-in migration helpers.

## Design and Usage

DataStore is built on Kotlin coroutines and Flow, which makes reads reactive and writes explicit. Reads are exposed as a `Flow` so the UI can observe the latest persisted value without manual refresh logic. Writes are suspend functions that complete only after the change is durably committed, and transactional updates are performed through an edit or updateData lambda that receives the current value and returns the new one.

Each DataStore instance is scoped to a single file. Keeping one instance per file, typically obtained through a property delegate at the application level, avoids the overhead and inconsistency of creating multiple instances. Because DataStore serializes operations on the underlying file, heavy or frequent writes should be batched inside a single transaction rather than issued as many small updates.

Preferences DataStore is a good fit for small, simple key-value settings such as feature flags, onboarding state, and user preferences. Proto DataStore suits structured data where type safety matters: the schema is declared in a Protocol Buffers definition, and generated accessors replace stringly-typed keys. Proto also makes evolving the schema explicit through field numbering and default values.

## Migration and Trade-offs

DataStore ships with a SharedPreferences migration helper, but the migration must be registered before the first read or write and can be used only once per file. A common pitfall is reading the legacy store lazily inside the app after DataStore has already created its own file, which silently skips migration. Apps that need querying, indexes, or partial updates should prefer Room or another SQL database; DataStore is not a query layer.

## Related

- [[wiki/android-core/shared-preferences|Shared Preferences]] — the legacy store DataStore replaces
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — DataStore exposes Flow reads
- [[wiki/android-core/room-database|Room Database]] — sibling Jetpack persistence layer
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — preferences survive offline on device
- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]] — the concurrency model DataStore uses
- [[wiki/android-core/hilt-di|Hilt DI]] — recommended way to scope DataStore instances
