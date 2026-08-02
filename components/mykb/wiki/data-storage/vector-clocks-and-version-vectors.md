---
type: "concept"
title: "Vector Clocks and Version Vectors"
description: "Capturing causality between replicas"
tags: ["vector-clocks", "version-vectors", "causality", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Vector Clocks and Version Vectors

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Vector clocks track per-node counters to order concurrent updates causally.
- Version vectors (without tombstones) suffice when only the current value matters.
- They enable conflict detection: concurrent versions need merge or user resolution.
- Metadata grows with replica count; pruning bounds it.

## Related

- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication
- [[wiki/data-storage/consistency-models|Consistency Models]] — consistency
- [[wiki/data-storage/causal-consistency-and-strong-consistency|Causal Consistency And Strong Consistency]] — causality use
- [[wiki/data-storage/logical-clocks-and-timestamps|Logical Clocks And Timestamps]] — lighter clocks
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
