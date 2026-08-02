---
type: "concept"
title: "Linearizability"
description: "Making concurrent operations appear to occur at a single instant in real time"
tags: ["linearizability", "consistency", "concurrency", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Linearizability

## Summary
Linearizability makes a system behave as if every operation took effect atomically at some point between its start and end, in a real-time-consistent order. It is the gold standard for single-object operations — what people usually mean by strong consistency.

## Details
- Every operation appears instantaneous and ordered consistently with real time.
- Single-key operations in Spanner-like systems and quorum reads/writes aim for it.
- Provable only with tests (jepsen-style); informally, linearizable reads see the latest write.
- mykb relevance: the wiki lock service must be linearizable to prevent duplicate writers.

## Related
- [[wiki/compositions/serializability|Serializability]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
