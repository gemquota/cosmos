---
type: "concept"
title: "Gossip Protocols and Distributed Consensus"
description: "Epidemic dissemination and agreement in distributed systems"
tags: ["gossip", "consensus", "distributed-systems", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Gossip Protocols and Distributed Consensus

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Gossip spreads state peer-to-peer with bounded staleness, used for membership and failure detection.
- Consensus (Raft, Paxos) achieves agreement on a total order with a leader/quorum.
- Gossip is cheaper and eventually consistent; consensus is stronger and costlier.
- Systems mix both: gossip for membership, consensus for replicated logs.

## Related

- [[wiki/data-storage/raft-consensus|Raft Consensus]] — consensus algorithm
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — gossip replication
- [[wiki/data-storage/quorum-reads-and-writes|Quorum Reads And Writes]] — quorum mechanics
- [[wiki/data-storage/anti-entropy-and-hinted-handoff|Anti-Entropy and Hinted Handoff]] — gossip repair
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
