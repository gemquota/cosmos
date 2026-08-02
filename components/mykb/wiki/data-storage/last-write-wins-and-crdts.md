---
type: "concept"
title: "Last-Write-Wins and CRDTs"
description: "Simple vs principled conflict resolution"
tags: ["lww", "crdts", "conflict-resolution", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Last-Write-Wins and CRDTs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- LWW keeps the write with the latest timestamp — simple but can lose updates and is clock-dependent.
- CRDTs (counters, sets, registers) merge concurrently by mathematically sound rules.
- CRDTs avoid coordination but constrain data structures.
- Pick LWW for low-stakes fields, CRDTs where lost updates are unacceptable.

## Related

- [[wiki/data-storage/crdts|CRDTs]] — CRDT fundamentals
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication context
- [[wiki/data-storage/conflict-free-replicated-data-types|Conflict Free Replicated Data Types]] — CRDT family
- [[wiki/data-storage/vector-clocks-and-version-vectors|Vector Clocks And Version Vectors]] — ordering metadata
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
