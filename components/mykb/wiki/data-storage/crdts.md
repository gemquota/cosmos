---
type: "concept"
title: "CRDTs"
description: "Conflict-free replicated data types for convergent merges"
tags: ["crdt", "replication", "eventual-consistency", "conflict-resolution"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://redis.io/glossary/crdt/", "https://cassandra.apache.org/doc/latest/cassandra/architecture/guarantees.html"]
---

# CRDTs

## Summary
Conflict-free replicated data types (CRDTs) are data structures designed so that replicas can apply updates locally and merge them later without coordination, always converging to the same state. They give application developers a principled path to eventual consistency without hand-written conflict resolution.

## Details
- **The convergence property** — every CRDT operation is deterministic and mergeable: if all replicas receive the same set of updates in any order, they converge to identical state. No leader, no locking, no two-phase commit needed.
- **Two families** — state-based CRDTs (CvRDTs) merge full state via a join that is commutative, associative, and idempotent; operation-based CRDTs (CmRDTs) broadcast operations that commute or are applied once. State-based types are easier to reason about but heavier to sync.
- **Common types** — grow-only counters (G-Counter), PN-counters that allow decrements, grow-only sets, OR-sets with tombstones to handle re-add, last-writer-wins registers (LWW), and multi-value registers (MVR) that preserve concurrent values.
- **Real systems** — Riak's CRDT support, Redis Enterprise's CRDT-based Active-Active databases, and Figma's multiplayer document model are production examples; Cassandra's last-write-wins cell conflicts are a restricted LWW-register application.
- **Limitations** — tombstones grow unbounded unless garbage-collected with coordination; LWW registers silently lose updates under clock skew; not every application semantic is expressible, so systems still need custom conflict policies for non-CRDT-friendly operations.
- **Trade-offs** — CRDTs trade simple, always-available writes for storage overhead and occasional counterintuitive semantics; they suit collaboration, shopping carts, and counters better than financial ledgers.

## Related
- [[wiki/data-storage/consistency-models|Consistency Models]] — eventual consistency made deterministic
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — the replication context for CRDTs
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — concurrent write scenarios
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — reclaiming tombstone overhead
