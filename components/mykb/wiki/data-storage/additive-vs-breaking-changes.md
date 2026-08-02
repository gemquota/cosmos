---
type: "concept"
title: "Additive vs Breaking Changes"
description: "Classifying schema changes by consumer impact"
tags: ["schema-evolution", "breaking-changes", "compatibility", "data-contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Additive vs Breaking Changes

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Additive changes (new optional fields, new columns) keep old readers working.
- Breaking changes (removals, renames, type changes, default removal) require consumer coordination.
- Versioning and compatibility rules make the distinction enforceable.
- Break glass paths: dual-write, shadow readers, or coordinated cutover.

## Related

- [[wiki/data-storage/schema-evolution|Schema Evolution]] — evolution basics
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — compatibility detail
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — streams context
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — contract enforcement
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
