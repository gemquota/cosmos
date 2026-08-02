---
type: "concept"
title: "Hinted Handoff and Repair Paths"
description: "Surviving node downtime in leaderless stores"
tags: ["hinted-handoff", "repair", "replication", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hinted Handoff and Repair Paths

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Hinted handoff buffers writes for a down replica and replays them on recovery.
- Hints are ephemeral; anti-entropy repair reconciles replicas over time.
- Repair paths (read repair, merkle-tree repair) fix divergence.
- Without repair, hinted handoff alone cannot guarantee convergence.

## Related

- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication model
- [[wiki/data-storage/crdts|CRDTs]] — convergence
- [[wiki/data-storage/anti-entropy-and-hinted-handoff|Anti-Entropy and Hinted Handoff]] — repair mechanics
- [[wiki/data-storage/quorum-reads-and-writes|Quorum Reads And Writes]] — consistency under failure
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
