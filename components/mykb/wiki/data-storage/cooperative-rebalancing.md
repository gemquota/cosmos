---
type: "concept"
title: "Cooperative Rebalancing"
description: "Incremental partition reassignment that avoids stopping all consumers"
tags: ["kafka", "rebalancing", "cooperative", "sticky"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cooperative Rebalancing

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Cooperative rebalancing moves a subset of partitions at a time, keeping most consuming.
- Consumers that support it revoke only partitions being moved, then rejoin.
- It reduces the stop-the-world effect of eager rebalances on large groups.
- KIP-429 brought cooperative sticky assignment to modern Kafka clients.

## Related

- [[wiki/data-storage/consumer-rebalancing-and-assignment|Consumer Rebalancing and Assignment]] — rebalance mechanics
- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups And Offsets]] — group coordination
- [[wiki/data-storage/offset-commits-and-checkpointing|Offset Commits And Checkpointing]] — offsets during rebalances
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
