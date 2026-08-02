---
type: "concept"
title: "Operational Transform"
description: "Transforming concurrent edits so they compose into one consistent document"
tags: ["operational-transform", "collaboration", "editing", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Operational Transform

## Summary
Operational transform (OT) is the classic approach to collaborative editing: concurrent operations are transformed against each other so they apply in any order with the same result. Google Wave and many collaborative editors use variants of it.

## Details
- Transform function (OT/OT-fusion) rewrites operations to account for prior concurrent ops.
- OT is stateful and tricky to get right; CRDTs offer a simpler convergence story for new systems.
- Used for character-level and object-level collaborative editing.
- mykb relevance: co-editing a wiki article with OT keeps two writers' keystrokes consistent.

## Related
- [[wiki/compositions/crdt-practice|CRDT Practice]]
- [[wiki/compositions/conflict-resolution-strategies|Conflict Resolution Strategies]]
- [[wiki/compositions/sync-engines|Sync Engines]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
