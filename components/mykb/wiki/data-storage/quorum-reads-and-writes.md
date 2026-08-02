---
type: "concept"
title: "Quorum Reads and Writes"
description: "Majority-based consistency tuning in replicated systems"
tags: ["quorum", "replication", "consistency", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quorum Reads and Writes

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A quorum requires R reads or W writes to succeed out of N replicas.
- R + W > N gives strong-ish (regular) consistency; smaller quorums trade consistency for availability.
- Cassandra, DynamoDB, and etcd expose or implement quorum logic.
- Quorum choice interacts with repair and hinted handoff behavior.

## Related

- [[wiki/data-storage/quorum-protocols|Quorum Protocols]] — quorum protocols
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication
- [[wiki/api-services/read-your-writes-and-consistency-apis|Read Your Writes And Consistency Apis]] — client view
- [[wiki/data-storage/virtual-nodes-and-replication-factors|Virtual Nodes And Replication Factors]] — RF tuning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
