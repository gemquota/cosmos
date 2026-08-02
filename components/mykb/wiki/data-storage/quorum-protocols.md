---
type: "concept"
title: "Quorum Protocols"
description: "Read/write quorum sizing and staleness bounds"
tags: ["quorum", "consistency", "replication", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html"]
---

# Quorum Protocols

## Summary
Quorum protocols let a replicated system treat a subset of responses as authoritative: a write is durable once `W` replicas acknowledge it, and a read is valid once `R` replicas answer. Sizing `W` and `R` relative to the replica count `N` bounds staleness and determines how much failure the system tolerates.

## Details
- **The core condition** — with `N` replicas, choosing `W` for writes and `R` for reads such that `W + R > N` guarantees every quorum read sees at least one replica holding the latest acknowledged write; the overlap is what makes the system appear consistent.
- **Dynamo/Cassandra defaults** — classic Dynamo settings are `N=3`, `W=2`, `R=2` (quorum), which tolerates one replica failure while keeping reads and writes fresh; `W=N` and `R=N` (ALL) give strong consistency but fail on any outage; `W=1` maximizes write availability at the cost of possible stale reads.
- **Read repair and anti-entropy** — a quorum read that finds stale replicas triggers read repair, and background anti-entropy reconciles the rest; without these, divergence can persist despite quorum arithmetic.
- **Sloppy quorums** — when the preferred replicas are unavailable, Dynamo accepts writes from other nodes and later hands them off (hinted handoff), trading consistency guarantees for availability during outages.
- **Consensus is not a quorum** — plain quorums do not order concurrent writes; Raft and Paxos add leader election and term-based ordering on top of majority (quorum) principles for linearizable consistency.
- **Sizing guidance** — pick `W` and `R` from the failure-tolerance and staleness budget: `W + R > N` is the minimum for freshness, larger sums reduce stale reads, and per-query consistency levels (Cassandra's `LOCAL_QUORUM`, `EACH_QUORUM`) let workloads choose per operation.

## Related
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — where quorums are the rule
- [[wiki/data-storage/consistency-models|Consistency Models]] — the guarantees quorums provide
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — majority-based agreement with ordering
- [[wiki/data-storage/cap-theorem|CAP Theorem]] — the trade-off quorums navigate
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — choosing which replicas to hit
