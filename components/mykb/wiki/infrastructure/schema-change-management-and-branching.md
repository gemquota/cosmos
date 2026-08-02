---
type: "concept"
title: "Schema Change Management and Branching"
description: "Versioning schemas like code, with branches and merges"
tags: ["schema-change", "branching", "versioning", "governance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Schema Change Management and Branching

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Treat schemas as code: reviewed, versioned, and promoted through environments.
- Branching (lakeFS/Nessie, dbt branches) isolates schema experiments.
- Merge to main must respect compatibility rules for consumers.
- Automated migration checks catch breaking changes before merge.

## Related

- [[wiki/data-storage/schema-migrations|Schema Migrations]] — migrations
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — evolution
- [[wiki/data-storage/data-versioning-and-branching|Data Versioning And Branching]] — data branching
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — compatibility
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
