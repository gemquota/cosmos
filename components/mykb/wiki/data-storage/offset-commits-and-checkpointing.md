---
type: "concept"
title: "Offset Commits and Checkpointing"
description: "Recording stream position for exactly-once or at-least-once recovery"
tags: ["offsets", "checkpointing", "kafka", "flink"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Offset Commits and Checkpointing

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Consumers commit offsets to mark processed positions; auto vs manual commit changes semantics.
- Flink checkpoints capture operator state and source offsets atomically.
- Commit-before-process risks loss; process-before-commit risks duplicates.
- Transactional commits unify the two for exactly-once results.

## Related

- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — semantic context
- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups And Offsets]] — Kafka offset model
- [[wiki/data-storage/checkpointing-and-recovery-flink|Checkpointing And Recovery Flink]] — Flink checkpointing
- [[wiki/data-storage/processing-guarantees-at-least-once|Processing Guarantees At Least Once]] — guarantee tradeoffs
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
