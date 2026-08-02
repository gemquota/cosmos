---
type: "concept"
title: "Backward Compatible Schema Changes"
description: "Schema changes that old readers can still process"
tags: ["schema-evolution", "backward-compatible", "migrations", "compatibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backward Compatible Schema Changes

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A change is backward compatible if consumers running old code can read data written with the new schema.
- Adding optional fields with defaults is the classic safe change; removing or retyping fields is not.
- Compatibility checking is automated by schema registries (Avro/Protobuf compatibility modes).
- Plan a versioning policy: additive by default, breaking changes gated and coordinated.

## Related

- [[wiki/data-storage/schema-evolution|Schema Evolution]] — schema evolution
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — migration practice
- [[wiki/data-storage/additive-vs-breaking-changes|Additive vs Breaking Changes]] — the taxonomy
- [[wiki/data-storage/schema-registry-and-evolution|Schema Registry And Evolution]] — automated checks
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
