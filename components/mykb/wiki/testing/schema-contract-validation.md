---
type: "concept"
title: "Schema Contract Validation"
description: "Validating request and response payloads against formal schemas"
tags: ["schema-validation", "testing", "json-schema", "openapi"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://json-schema.org/", "https://learn.openapis.org/"]
---

# Schema Contract Validation

## Summary
Schema contract validation checks request and response payloads against formal schemas, such as JSON Schema, OpenAPI, Protobuf, or Avro, rejecting drift before it reaches consumers. It is the cheapest, most automatable contract enforcement available.

## Details
- JSON Schema and OpenAPI validate REST payloads; Protobuf and Avro enforce wire format by generation.
- Apply validation in tests against fixtures, in CI against examples, and at runtime via middleware.
- Tools: Ajv and jsonschema for JSON Schema, Schemathesis for generative API testing.
- Catches wrong types, missing required fields, out-of-range values, and enum drift.
- Contracts add behavioral examples; schemas add structural guarantees, so use both.
- Runtime validation in dev and QA, optional in performance-critical production paths.
- Versioned schemas let old and new clients coexist during migrations.

## Related
- [[wiki/testing/contract-testing|Contract Testing]] — behavioral contracts on top of schemas
- [[wiki/testing/api-testing|API Testing]] — exercises payloads against schemas
- [[wiki/api-protocols/json-schema|JSON Schema]] — the core schema language
- [[wiki/api-protocols/openapi|OpenAPI]] — API description with embedded schemas
- [[wiki/api-protocols/api-versioning|API Versioning]] — schema evolution across releases
- [[wiki/testing/consumer-driven-contracts|Consumer-Driven Contracts]] — consumer expectations align with schemas
