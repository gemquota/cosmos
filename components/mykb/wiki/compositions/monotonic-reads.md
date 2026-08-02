---
type: "concept"
title: "Monotonic Reads"
description: "The guarantee that successive reads never go back in time"
tags: ["monotonic-reads", "consistency", "replication", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Monotonic Reads

## Summary
Monotonic reads promise that if a client reads a value, later reads return that value or something newer — never an older one. It prevents the jarring experience of data flipping backward when reads hit different replicas.

## Details
- Broken by replica hopping: a fresh replica read followed by a lagging replica read.
- Implement via session pinning or staleness-aware routing.
- Monotonic reads is one of the classic session guarantees alongside read-your-writes.
- mykb relevance: wiki readers on replicas never see a page revert to an older version.

## Related
- [[wiki/compositions/read-your-writes|Read-Your-Writes]]
- [[wiki/compositions/bounded-staleness|Bounded Staleness]]
- [[wiki/tooling/replication-lag|Replication Lag]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
