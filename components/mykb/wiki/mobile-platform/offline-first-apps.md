---
type: "concept"
title: "Offline-First Apps"
description: "Design where the local device store is the source of truth and the network is an optimization"
tags: ["mobile", "offline", "sync", "local-first", "reliability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/architecture/data-layer/offline-first"]
---

# Offline-First Apps

## Summary

Offline-first means the device store is the source of truth and the network is an optimization: apps read and write locally, then sync in the background. This improves speed, reliability, and battery life on flaky mobile networks, and it is the architecture behind local-first note tools. It requires a write queue, idempotent APIs, and a conflict-resolution policy.

## Details

- Local stack: Room for relational data, DataStore for preferences, and file or image caches for media.
- Writes go to a local queue and replay to the server when connectivity returns; server APIs must be idempotent to survive retries.
- Sync triggers: app start, connectivity change, WorkManager constraints, and manual pull-to-refresh.
- Conflicts are inevitable: pick last-write-wins, field-level merges, or a manual resolution UI, and record the policy.
- Caching with stale-while-revalidate gives instant reads; background fetch keeps caches fresh without blocking the UI.
- RSIS3 relevance: mykb notes and agent transcripts survive offline on a phone and reconcile later, exactly the local-first model.

## Related

- [[wiki/android-core/room-database|Room Database]] — local relational store at the heart of offline-first
- [[wiki/android-core/datastore|DataStore]] — preferences and small state stored locally
- [[wiki/android-core/shared-preferences|Shared Preferences]] — legacy local key-value store
- [[wiki/mobile-platform/mobile-data-sync|Mobile Data Sync]] — the synchronization layer that reconciles state
- [[wiki/api-protocols/http-caching|HTTP Caching]] — cache headers drive offline reads
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — local full-text search over offline notes
