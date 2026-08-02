---
type: "concept"
title: "Sync Engines"
description: "Systems that reconcile local and remote data across devices"
tags: ["sync", "reconciliation", "distributed-systems", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sync Engines

## Summary
Sync engines keep multiple copies of data consistent — tracking versions, exchanging deltas, resolving conflicts, and handling partial failures. They are the machinery behind offline-first apps and distributed caches.

## Details
- Core pieces: change tracking, delta exchange, conflict detection, and resolution policy.
- Idempotency and retries are mandatory: sync runs on flaky networks.
- Test sync under adversarial conditions — drops, reorders, and duplicate deltas.
- mykb relevance: the wiki bundle syncs article changes between Termux and remote storage.

## Related
- [[wiki/compositions/offline-first|Offline-First]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/version-vectors|Version Vectors]]
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/tooling/replication-lag|Replication Lag]]
