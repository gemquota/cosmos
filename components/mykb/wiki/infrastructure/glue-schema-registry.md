---
type: "entity"
title: "Glue Schema Registry"
description: "AWS-managed schema registry for streaming and message data"
tags: ["glue", "schema-registry", "aws", "avro"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Glue Schema Registry

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Glue Schema Registry stores Avro/JSON/Protobuf schemas with compatibility checks.
- It integrates with MSK, Kinesis, and Glue jobs; checkpoints reduce payload size.
- Schema versions are auditable and can be shared across accounts.
- AWS-native alternative to Confluent Schema Registry for AWS-heavy stacks.

## Related

- [[wiki/data-storage/schema-evolution|Schema Evolution]] — schema management
- [[wiki/infrastructure/confluent-cloud-and-schema-registry|Confluent Cloud And Schema Registry]] — cross-cloud option
- [[wiki/data-storage/schema-registry-and-evolution|Schema Registry And Evolution]] — registry concept
- [[wiki/infrastructure/aws-msk-and-managed-kafka|Aws Msk And Managed Kafka]] — typical integration
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
