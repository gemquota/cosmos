---
type: "concept"
title: "Log Compaction and Keys"
description: "Retaining the latest record per key in compacted topics"
tags: ["kafka", "log-compaction", "keys", "changelog"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Log Compaction and Keys

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Compacted topics keep the most recent value per key, discarding older versions.
- Keys determine compaction granularity; null keys are never compacted.
- Use cases: materialized state, table topics, and change logs.
- Compaction is asynchronous; readers see a mix of old/new until it completes.

## Related

- [[wiki/data-storage/compaction-and-retention-kafka|Compaction And Retention Kafka]] — policy context
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — table from compacted log
- [[wiki/data-storage/key-value-stores|Key Value Stores]] — compacted topic as KV store
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
