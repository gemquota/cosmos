---
type: "concept"
title: "Processing Guarantees: At-Least-Once"
description: "Delivery guarantee that records may be processed more than once"
tags: ["at-least-once", "guarantees", "streaming", "delivery"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Processing Guarantees: At-Least-Once

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- At-least-once guarantees no loss but allows duplicates after failures.
- Sources replay from checkpoints; sinks must tolerate duplicates.
- It is the pragmatic default for many pipelines when idempotency is cheap.
- Upgrade paths: idempotent sinks, deduplication, or engine-level exactly-once.

## Related

- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — the stronger guarantee
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — making duplicates harmless
- [[wiki/data-storage/exactly-once-processing|Exactly Once Processing]] — end-to-end exactly-once
- [[wiki/data-storage/offset-commits-and-checkpointing|Offset Commits and Checkpointing]] — where replays originate
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
