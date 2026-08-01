---
type: "concept"
title: "Shared Preferences"
description: "Legacy key-value store for simple app preferences"
tags: ["android", "storage", "preferences", "legacy"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Shared Preferences

SharedPreferences stores small key-value pairs in an XML file, synchronous and process-safe, but it is now legacy: Jetpack DataStore is the recommended successor. It still appears throughout existing codebases.
- Simple put/get API with commit (sync) and apply (async) writes.
- No type safety, no schema versioning, and no coroutine support.
- DataStore Preferences replaces it with Flow-based reads.
- Keep it for tiny flags during migrations only.

## Related

- [[wiki/android-core/datastore|DataStore]] — the recommended replacement
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — preferences participate in local state
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — persist small state at lifecycle points
- [[wiki/android-core/room-database|Room Database]] — structured data belongs in Room instead
