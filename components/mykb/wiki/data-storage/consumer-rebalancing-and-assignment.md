---
type: "concept"
title: "Consumer Rebalancing and Assignment"
description: "How Kafka assigns partitions to consumers as groups change"
tags: ["kafka", "consumer-groups", "rebalancing", "partition-assignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Consumer Rebalancing and Assignment

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A rebalance redistributes partitions among group members when members or topics change.
- Eager rebalancing stops all consumers; incremental/cooperative rebalancing is gentler.
- Assignment strategies (range, round-robin, sticky) trade evenness against stickiness.
- Frequent rebalances from short-lived consumers cause lag and thrash.

## Related

- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups And Offsets]] — group semantics
- [[wiki/data-storage/cooperative-rebalancing|Cooperative Rebalancing]] — incremental rebalancing
- [[wiki/data-storage/offset-commits-and-checkpointing|Offset Commits And Checkpointing]] — commit behavior during rebalances
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
