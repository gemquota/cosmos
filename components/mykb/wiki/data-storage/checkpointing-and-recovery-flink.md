---
type: "concept"
title: "Checkpointing and Recovery in Flink"
description: "Snapshot-based fault tolerance for stateful Flink jobs"
tags: ["flink", "checkpointing", "recovery", "state"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Checkpointing and Recovery in Flink

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Flink periodically snapshots operator state and source offsets into checkpoints.
- On failure, the job restarts from the latest checkpoint and replays input.
- Exactly-once mode uses aligned checkpoints and transactional commits.
- Checkpoint frequency and state size set recovery time and overhead.

## Related

- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — guarantee
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — recovery fundamentals
- [[wiki/data-storage/offset-commits-and-checkpointing|Offset Commits And Checkpointing]] — offset checkpointing
- [[wiki/data-storage/stateful-stream-processing|Stateful Stream Processing]] — state being checkpointed
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
