---
type: "concept"
title: "Transaction Isolation Practice"
description: "Choosing and testing isolation levels against the anomalies you accept"
tags: ["transaction-isolation", "practice", "databases", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Transaction Isolation Practice

## Summary
Isolation practice means picking a level per workload, knowing which anomalies it permits, and testing the actual behavior of your engine — vendor defaults and documentation often differ from reality. The level is a contract with your data.

## Details
- Map levels to anomalies: dirty reads, non-repeatable reads, phantoms, write skew, lost updates.
- Know your engine: MySQL repeatable read, PostgreSQL read committed, Oracle read committed — all differ.
- Test with adversarial workloads (jepsen-style) before trusting a claim.
- mykb relevance: wiki sync transactions pin the isolation level per operation class.

## Related
- [[wiki/compositions/read-committed|Read Committed]]
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
- [[wiki/compositions/write-skew|Write Skew]]
- [[wiki/compositions/serializability|Serializability]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
