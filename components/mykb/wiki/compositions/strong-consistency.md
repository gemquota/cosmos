---
type: "concept"
title: "Strong Consistency"
description: "Guaranteeing every read reflects the latest acknowledged write"
tags: ["strong-consistency", "consistency", "databases", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Strong Consistency

## Summary
Strong consistency promises that a read returns the most recent acknowledged write, regardless of which replica answers. It is the behavior of single-node databases and quorum systems, bought with coordination cost and availability tradeoffs.

## Details
- Linearizability is the strongest flavor; serializability adds transaction ordering.
- Strong consistency requires quorum or single-leader reads — more latency, less availability under partition.
- Choose it where correctness beats latency: ledgers, auth state, inventory.
- mykb relevance: wiki slugs must be strongly consistent to avoid duplicate article creation.

## Related
- [[wiki/compositions/linearizability|Linearizability]]
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/serializability|Serializability]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
