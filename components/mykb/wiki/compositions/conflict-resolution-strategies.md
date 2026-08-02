---
type: "concept"
title: "Conflict Resolution Strategies"
description: "Policies for reconciling divergent concurrent edits"
tags: ["conflicts", "resolution", "sync", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Conflict Resolution Strategies

## Summary
Conflict resolution decides what happens when two copies diverge: last-write-wins, merge, manual pick, or domain-specific reconciliation. The choice trades autonomy for data integrity and defines the user experience of a sync system.

## Details
- LWW is simple but lossy; merge-based resolution preserves more intent at higher cost.
- CRDTs resolve automatically for convergent operations; OT handles collaborative editing.
- Manual conflict UIs must surface both versions clearly and record the resolution.
- mykb relevance: wiki articles resolve by field-level merge, not blind overwrite.

## Related
- [[wiki/compositions/last-write-wins|Last-Write-Wins]]
- [[wiki/compositions/crdt-practice|CRDT Practice]]
- [[wiki/compositions/operational-transform|Operational Transform]]
- [[wiki/compositions/sync-engines|Sync Engines]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
