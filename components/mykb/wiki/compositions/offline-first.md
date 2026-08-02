---
type: "concept"
title: "Offline-First"
description: "Designing apps so local data works without connectivity and syncs later"
tags: ["offline-first", "sync", "mobile", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Offline-First

## Summary
Offline-first means the app reads and writes local data as the primary path, syncing with servers when connectivity returns. Users get instant responses anywhere; the hard part is conflict resolution and sync semantics.

## Details
- Local store (SQLite, IndexedDB) is authoritative for the user; the server is the shared truth.
- Sync engines push and pull changes with versioning; conflicts need explicit resolution.
- Offline-first changes the whole error model: network is one more input, not a precondition.
- mykb relevance: the Termux wiki editor works offline and syncs the bundle on schedule.

## Related
- [[wiki/compositions/sync-engines|Sync Engines]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/mobile-platform/offline-first-apps|Offline Support]]
- [[wiki/compositions/setup-installation|Setup and Installation]]
