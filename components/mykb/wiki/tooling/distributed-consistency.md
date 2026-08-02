---
type: "concept"
title: "Distributed Consistency"
description: "The spectrum of guarantees for what replicas observe in distributed systems"
tags: ["consistency", "distributed-systems", "models", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Consistency_model", "https://jepsen.io/consistency"]
---

# Distributed Consistency

## Summary
Distributed consistency describes what a replicated system promises about the order and freshness of reads: from linearizable (strongest) through causal and session guarantees down to eventual consistency. Choosing a model is a business decision about correctness versus availability and latency.

## Details
- The consistency spectrum: linearizability, sequential, causal, read-your-writes, monotonic reads, bounded staleness, eventual.
- Stronger models cost coordination: quorum reads/writes, consensus, and single-leader routing add latency.
- Weaker models allow divergence: replica lag, stale reads, and conflicts that need resolution policies.
- CAP/PACELC frame the trade: under partition, availability versus consistency; normally, latency versus consistency.
- Test claims: jepsen-style verification exposes models that were promised but not delivered.
- For the mykb bundle, the wiki picks per-read consistency: strong for slug uniqueness, eventual for search freshness.
- Worked example — the wiki's search index promises bounded staleness of one minute; slug allocation is linearizable via a single writer, so article identity never races.

Worked example — the wiki's search index promises bounded staleness of one minute; slug allocation is linearizable via a single writer, so article identity never races.

## Related
- [[wiki/compositions/eventual-consistency-practice|Eventual Consistency Practice]]
- [[wiki/compositions/strong-consistency|Strong Consistency]]
- [[wiki/compositions/causal-consistency|Causal Consistency]]
- [[wiki/tooling/pacelc-theorem|PACELC Theorem]]
- [[wiki/compositions/bounded-staleness|Bounded Staleness]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
- [[wiki/compositions/read-your-writes|Read-Your-Writes]]
- [[wiki/compositions/monotonic-reads|Monotonic Reads]]
- [[wiki/devops-infra/isolation-levels|Isolation Levels]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
