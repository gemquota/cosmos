---
type: "concept"
title: "Erasure Coding"
description: "Redundant encoding that rebuilds data with less overhead than replication"
tags: ["erasure-coding", "storage", "redundancy", "raid"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Erasure Coding

## Summary
Erasure coding is a redundant encoding scheme that protects data against failures while using far less overhead than replication: instead of storing k full copies, it stores k data shards plus m parity shards, so the data survives any m shard failures. It is the mathematical descendant of RAID parity, and it is what makes petabyte-scale storage affordable — the same reliability at a fraction of the capacity cost.

## Details
- The mechanism: a file is split into k data shards, and an encoder computes m parity shards such that any k of the k+m shards reconstruct the original data. This is the magic property — you do not need the specific failed shards; any subset of k shards suffices, because the code is designed for erasures (known missing pieces) rather than corruption. The classic parameterization is Reed-Solomon coding: with 6+3 (k=6 data, m=3 parity), a 9-shard system survives any 3 shard losses at 1.5x storage overhead — versus 3x overhead for triple replication with weaker guarantees. The tradeoff knob is (k, m): more parity = more resilience at more overhead; more data shards = less overhead but more compute per rebuild and larger blast radius per failure.
- The arithmetic in practice: encoding and decoding are finite-field matrix operations — each parity shard is a linear combination of data shards, and reconstruction solves the linear system for the missing pieces using the surviving shards. The compute cost scales with shard count and size, which is why erasure coding used to be "too expensive" and became standard once CPUs got cheap: modern systems (Ceph, MinIO, cloud object stores) encode at GB/s per core with SIMD-optimized libraries (Intel ISA-L, Jerasure).
- The system-level reasons it matters: rebuild efficiency and durability. With replication, a failed disk is rebuilt by copying a full replica; with erasure coding, the rebuild reads k shards from k different disks and computes the replacement — distributing the read load and reducing the network blast radius of a rebuild. Durability is also better for the same overhead: 4+2 erasure coding tolerates 2 simultaneous failures with 1.5x overhead, while 3x replication tolerates only 2 failures of the same block at 3x overhead.
- Failure modes: partial failure (a shard that is corrupt rather than missing requires detection via checksums, because erasure codes assume erasures), slow rebuilds when k is large (reading k shards across a degraded network), and the silent killer — a second failure during rebuild, which is why the parity budget (m) must exceed the expected rebuild window's failure rate.
- For mykb: erasure coding is the storage-reliability node — it connects to RAID, replication strategies, and backup design, and it is the reason "three copies" is not the only (or the best) reliability answer.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]] — related coverage in the same cluster
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
