---
type: "concept"
title: "Replication Lag"
description: "The delay between a write on the primary and its appearance on replicas"
tags: ["replication", "lag", "databases", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Replication Lag

## Summary
Replication lag is how far behind replicas are from the primary. It is normally milliseconds but grows under load, and it decides which consistency guarantees you can honestly claim — read-your-writes needs lag below user tolerance.

## Details
- Monitor lag per replica; sustained lag signals overload or a broken sync stream.
- Lag amplifies under failover: promoting a lagging replica loses the newest writes.
- Design reads that tolerate lag (cache stamps, staleness bounds) to survive it.
- mykb relevance: wiki read replicas can serve the search index with bounded staleness.

## Related
- [[wiki/tooling/read-replicas|Read Replicas]]
- [[wiki/compositions/bounded-staleness|Bounded Staleness]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/tooling/quorum-reads|Quorum Reads]]
