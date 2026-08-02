---
type: "concept"
title: "Compaction and Retention in Kafka"
description: "Controlling how long and how much data topics keep"
tags: ["kafka", "retention", "compaction", "topics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Compaction and Retention in Kafka

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Retention policies: time-based, size-based, or log compaction by key.
- Compaction keeps the latest value per key, useful for changelog topics and tables.
- Compact, delete, or both: the policy shapes storage cost and replay semantics.
- Tombstones (null values) mark deletions in compacted topics.

## Related

- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — compaction general concept
- [[wiki/data-storage/log-compaction-and-keys|Log Compaction And Keys]] — compaction details
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — changelog topics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
