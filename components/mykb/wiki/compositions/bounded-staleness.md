---
type: "concept"
title: "Bounded Staleness"
description: "A consistency guarantee that limits how old the data a read may return"
tags: ["bounded-staleness", "consistency", "replication", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Bounded Staleness

## Summary
Bounded staleness caps the maximum age of served data — reads return state at most N seconds (or versions) old. It is a tunable middle ground between eventual and strong consistency, popular in cloud databases (Cosmos DB).

## Details
- Bound by time (N seconds) or by versions (N operations behind).
- It is a guarantee, not a behavior: the system promises reads never exceed the bound.
- Cheaper than strong consistency because it allows replica lag within the bound.
- mykb relevance: the wiki search index promises at most 60-second-old results.

## Related
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/tooling/replication-lag|Replication Lag]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/compositions/monotonic-reads|Monotonic Reads]]
