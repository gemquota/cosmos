---
type: "concept"
title: "JSON Schema Validation"
description: "Declarative validation of JSON documents: types, formats, constraints, and references"
tags: ["json", "schema", "validation", "contracts", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://json-schema.org/", "https://json-schema.org/understanding-json-schema/"]
---
# JSON Schema Validation

## Summary
JSON Schema describes the shape of JSON data: required fields, types, enums, numeric bounds, string formats, and nested structures via `$ref`. Validators check documents against the schema, and tooling derives types, docs, and mocks. It is the backbone of OpenAPI and AsyncAPI payload definitions.

## Details
- **Keywords** — `type`, `properties`, `required`, `enum`, `minimum/maximum`, `minLength/maxLength`, `pattern`, `oneOf/anyOf/allOf`, and `$ref` compose constraints.
- **Formats** — `format` hints like email, date-time, and uri; support is implementation-defined, so treat formats as advisory or enforce explicitly.
- **Draft versions** — 2020-12 is current; vocabulary differences matter when mixing tools.
- **Practice** — validate at trust boundaries (API input, webhook payloads) and generate client types from schemas to keep contracts in sync.
- **Worked example** — the mykb daemon validates every inbound pulse against a JSON Schema before writing the wiki.
- **Relevance** — RSIS3's tool-call arguments are perfect JSON Schema candidates: validated before execution, typed for the agent.

## Related
- [[wiki/frontend-frameworks/zod-validation|Zod Validation]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/yup-schemas|Yup Schemas]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/schema-coercion|Schema Coercion]] — adjacent concept in this wiki
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]] — adjacent concept in this wiki
- [[wiki/api-protocols/json-schema|JSON Schema]] — existing coverage
- [[wiki/api-protocols/json-api-spec|JSON:API]] — existing coverage
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — existing coverage
