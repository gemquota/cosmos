---
type: "concept"
title: "Anti-Entropy and Hinted Handoff"
description: "Background reconciliation of divergent replicas"
tags: ["anti-entropy", "hinted-handoff", "repair", "replication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Anti-Entropy and Hinted Handoff

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Anti-entropy compares replica state (merkle trees) and syncs differences in the background.
- It bounds divergence even when writes are lost or hints expire.
- Read repair fixes inconsistencies encountered by reads.
- Scheduling anti-entropy keeps steady-state repair costs predictable.

## Related

- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication
- [[wiki/data-storage/hint-handoff-and-repair-paths|Hint Handoff And Repair Paths]] — handoff
- [[wiki/data-storage/gossip-protocols-and-distributed-consensus|Gossip Protocols And Distributed Consensus]] — dissemination
- [[wiki/data-storage/crdts|CRDTs]] — mergeable state
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
