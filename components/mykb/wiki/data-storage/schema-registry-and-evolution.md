---
type: "concept"
title: "Schema Registry and Evolution"
description: "Centralized schema governance for streaming and messaging"
tags: ["schema-registry", "avro", "evolution", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.confluent.io/platform/current/schema-registry/index.html", "https://avro.apache.org/docs/"]
---

# Schema Registry and Evolution

## Summary

A schema registry stores and versions schemas so producers and consumers stay compatible.
Compatibility rules make schema evolution safe.
It is standard infrastructure in Kafka ecosystems.
A registry turns schema change from an incident into a reviewable process.

## Details

- Schemas are stored once and referenced by ID in messages.
- Compatibility modes: backward, forward, full, and none.
- Registry checks block incompatible producer changes.
- Avro, Protobuf, and JSON schemas are supported.
- Managed options: Confluent Schema Registry, AWS Glue, and others.
- Compatibility checks run in CI before deployment.
- Store registry metadata alongside lineage for full context.
- Schema governance is what allows streams and tables to evolve without breaking consumers.

## Related

- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — streams
- [[wiki/data-storage/avro-and-protobuf-serialization|Avro And Protobuf Serialization]] — formats
- [[wiki/data-storage/backward-compatible-schema-changes|Backward Compatible Schema Changes]] — compatibility
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — existing note
- [[wiki/infrastructure/glue-schema-registry|Glue Schema Registry]] — AWS option
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions

