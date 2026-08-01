---
type: "concept"
title: "Mobile Data Sync"
description: "Reconciling local and server data with change tracking, deltas, and conflict resolution"
tags: ["mobile", "sync", "data", "conflicts", "replication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://firebase.google.com/docs/firestore/manage-data/enable-offline"]
---

# Mobile Data Sync

## Summary

Data sync reconciles copies of the same data on device and server across sessions and devices. Reliable sync needs change tracking, delta transfer, idempotent writes, retries, and an explicit conflict-resolution policy. Firestore offline persistence is the reference implementation most Android teams study first.

## Details

- Change tracking: updated_at timestamps, monotonic versions, or change logs identify what changed since the last sync.
- Delta sync transfers only changed records; pagination and cursors keep large datasets manageable over REST or gRPC.
- Push-pull model: client pushes local changes with idempotency keys, pulls server changes since its last cursor, and merges.
- Conflict strategies: last-write-wins by timestamp, field-level merging, server or device precedence, or manual resolution UI.
- Retries use exponential backoff with jitter; duplicate delivery is handled by deduplication and idempotent APIs.
- Backups and data versioning protect against sync bugs that corrupt both copies.
- RSIS3 relevance: notes and session logs syncing between phone and server benefit from versioned, delta-based sync.

## Related

- [[wiki/android-core/datastore|DataStore]] — local state that participates in sync
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — sync is the online half of offline-first
- [[wiki/mobile-platform/background-fetch|Background Fetch]] — periodic refresh keeps sync fresh
- [[wiki/api-protocols/idempotency|Idempotency]] — retries must not duplicate writes
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — failure handling for sync jobs
- [[wiki/data-storage/data-versioning|Data Versioning]] — version tracks make deltas computable
