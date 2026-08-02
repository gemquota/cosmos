---
type: "concept"
title: "Avro and Protobuf Serialization"
description: "Compact, schema-driven binary formats for event data"
tags: ["avro", "protobuf", "serialization", "schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Avro and Protobuf Serialization

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Avro stores schema with data (or by reference) and supports rich evolution rules.
- Protobuf compiles .proto definitions to code in many languages with forward/backward compatibility.
- Both beat JSON on size and parsing speed at the cost of tooling and human readability.
- Schema Registry integration makes either format safe for streaming pipelines.

## Related

- [[wiki/data-storage/schema-evolution|Schema Evolution]] — evolution rules
- [[wiki/data-storage/schema-registry-and-evolution|Schema Registry And Evolution]] — storing schemas centrally
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — streams context
- [[wiki/data-storage/json-ld|JSON-LD]] — schema-rich JSON alternative
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
