---
type: "concept"
title: "Data Skew and Salting"
description: "Handling hot keys that unbalance parallel work"
tags: ["data-skew", "salting", "shuffle", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Data Skew and Salting

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Skew concentrates work on a few keys (hot partitions), slowing the whole job.
- Salting adds a random suffix to keys to spread load across partitions.
- Two-phase aggregation (local then global) fixes skewed aggregations.
- AQE skew joins and custom partitioners automate mitigation.

## Related

- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — hot partition problem
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — related partitioning concepts
- [[wiki/data-storage/adaptive-query-execution|Adaptive Query Execution]] — runtime skew handling
- [[wiki/data-storage/join-strategies-in-streams|Join Strategies In Streams]] — skew in stream joins
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
