---
type: "concept"
title: "Lease-Based Locks"
description: "Locks with a time limit so a dead holder releases automatically"
tags: ["lease-based-locks", "locks", "coordination", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lease-Based Locks

## Summary
Lease-based locks expire after a timeout, so a holder that crashes stops blocking others automatically. The holder renews the lease to keep the lock; the price is a window where a slow holder may lose the lock mid-work.

## Details
- Lease duration balances recovery speed against premature-loss risk.
- Renewal is a background heartbeat; loss of renewal triggers lock release and fencing.
- The holder must stop work on lease loss — fencing tokens make that safe.
- mykb relevance: the wiki writer renews its publish lease every heartbeat.

## Related
- [[wiki/compositions/distributed-locks|Distributed Locks]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/tooling/keepalives|Keepalives]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
