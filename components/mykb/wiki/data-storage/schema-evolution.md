---
type: "concept"
title: "Schema Evolution"
description: "Additive changes, backfills, and cross-version compatibility"
tags: ["schema-evolution", "compatibility", "backfill", "data-engineering"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://iceberg.apache.org/spec/", "https://docs.aws.amazon.com/glue/latest/dg/update-schemas.html"]
---

# Schema Evolution

## Summary
Schema evolution is the disciplined process of changing a schema without breaking running writers or readers. Additive, backward-compatible changes (new nullable columns, renamed fields with aliases) move first, while destructive changes are phased so old and new versions can coexist.

## Details
- **Compatibility axes** — backward compatibility lets old readers consume new data (new fields ignored); forward compatibility lets new readers consume old data (missing fields get defaults); full compatibility is the safe default for shared tables.
- **Additive changes** — adding nullable columns or optional fields is cheap in most engines; Postgres makes it metadata-only, and formats like Parquet/Avro append fields with defaults.
- **Breaking changes** — dropping columns, changing types, or removing enum values break consumers; rename with `ALTER TABLE RENAME` plus a shadow column during a transition window is the standard trick.
- **Format-level evolution** — open table formats (Iceberg, Delta) version table metadata so each writer appends its schema version and readers resolve per-file schemas; the format, not the engine, owns compatibility rules.
- **Operational sequence** — deploy reader compatibility first, evolve the schema, backfill defaults, then remove deprecated fields; monitors and data contracts catch consumers that were silently broken.

## Related
- [[wiki/data-storage/schema-migrations|Schema Migrations]] — the mechanism of change
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — engine-independent schema versioning
- [[wiki/data-storage/expand-contract-migrations|Expand-Contract Migrations]] — the phased pattern
- [[wiki/data-storage/data-contracts|Data Contracts]] — explicit compatibility promises
- [[wiki/data-storage/backfilling|Backfilling]] — filling values for new fields
