---
type: "concept"
title: "Google Cloud Spanner"
description: "Globally distributed relational database with external consistency"
tags: ["spanner", "gcp", "global", "distributed-sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Google Cloud Spanner

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Spanner combines SQL tables, synchronous replication across regions, and TrueTime for consistent reads.
- Interleaved tables and key-prefix design keep related rows co-located for low-latency access.
- It offers external consistency (linearizable) transactions across the planet.
- Schema changes and hotspots need careful key design; it is the flagship NewSQL managed service.

## Related

- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — global transactions
- [[wiki/data-storage/hybrid-logical-clocks-and-true-time|Hybrid Logical Clocks And True Time]] — TrueTime underpins consistency
- [[wiki/data-storage/causal-consistency-and-strong-consistency|Causal Consistency And Strong Consistency]] — consistency guarantees
- [[wiki/data-storage/storage-engines|Storage Engines]] — underlying tablet storage
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
