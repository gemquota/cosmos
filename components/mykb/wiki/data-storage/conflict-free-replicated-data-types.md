---
type: "concept"
title: "Conflict-Free Replicated Data Types"
description: "Data structures that converge without coordination"
tags: ["crdts", "replication", "conflict-resolution", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Conflict-Free Replicated Data Types

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- CRDTs define merge operations that are commutative, associative, and idempotent.
- Types: G-Counter, PN-Counter, grow-only sets, OR-sets, LWW-registers, and maps.
- Used in collaborative editing, offline mobile, and multi-region stores.
- They shift complexity from runtime coordination to data-structure design.

## Related

- [[wiki/data-storage/crdts|CRDTs]] — CRDT note
- [[wiki/data-storage/last-write-wins-and-crdts|Last Write Wins And Crdts]] — resolution comparison
- [[wiki/data-storage/eventual-consistency-and-conflict-resolution|Eventual Consistency And Conflict Resolution]] — convergence context
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication model
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
