---
type: "concept"
title: "Backward Compatible Schema Changes"
description: "Schema changes that old readers can still process"
tags: ["schema-evolution", "backward-compatible", "migrations", "compatibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Backward Compatible Schema Changes

## Summary
A schema change is backward compatible if consumers running old code can read data written with the new schema. Adding optional fields with defaults is the classic safe change; removing or retyping fields is not. Backward compatibility is what lets producers evolve without coordinated consumer upgrades.

## Details
- Mechanism: old readers must tolerate new data — new fields must be optional or defaulted, field types must not change meaning, enum sets must only grow, and removed fields must remain parseable; schema registries (Confluent Avro/Protobuf compatibility modes) automate the check by diffing old and new schemas; the producer can ship as soon as the registry approves.
- Concrete example: adding an optional `status` field to a JSON record breaks nothing — old consumers ignore it; adding a required field breaks every old consumer at once; renumbering a protobuf field corrupts parsing for old readers; widening a string column is usually fine, narrowing it truncates data.
- Failure modes: assuming compatibility without checking — a registry diff or a compatibility test in CI catches what intuition misses; optional fields added but populated with values old code cannot handle; enum additions that old consumers switch on unsafely; semantic changes disguised as additive (a field whose meaning changes while its shape stays); coordination debt — a chain of one-off compat fixes that should have been a versioning policy.
- Tradeoffs: backward compatibility lets producers move independently at the cost of carrying old shapes longer; the alternative, coordinated breaking changes, is cleaner but blocks every consumer; the mature pattern is additive-by-default with registry-enforced checks and a deliberate, gated process for the rare breaking change.
- Operational notes: run compatibility checks in CI, keep the schema registry the source of truth, and document the versioning policy.
- RSIS3 relevance: RSIS3's internal artifacts (pulses, checkpoints) evolve schemas — backward-compatible changes let old loops read new state during L2/L3 transitions.

## Related

- [[wiki/data-storage/schema-evolution|Schema Evolution]] — schema evolution
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — migration practice
- [[wiki/data-storage/additive-vs-breaking-changes|Additive vs Breaking Changes]] — the taxonomy
- [[wiki/data-storage/schema-registry-and-evolution|Schema Registry And Evolution]] — automated checks
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
