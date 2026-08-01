---
type: "concept"
title: "JSON Schema"
description: "Declarative vocabulary for validating, annotating, and documenting JSON document structures"
tags: ["json", "schema", "validation", "data-contracts", "api"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://json-schema.org/"]
---

# JSON Schema

## Summary
JSON Schema is a declarative vocabulary that describes the shape, constraints, and semantics of JSON documents. It lets teams validate payloads, generate documentation and client code, and publish reusable data contracts independent of any programming language. It is the data-model foundation under OpenAPI and is widely used by API gateways, form builders, and LLM tool-calling pipelines.

## Details
- Core keywords: `type`, `properties`, `required`, `items`, `enum`, `format`, `minimum`, and `pattern` constrain values at structural and semantic levels.
- Validation happens against an instance document, while the schema itself is also a JSON document, which makes schemas machine-readable and shareable.
- Drafts evolve the standard; Draft 2020-12 introduced `prefixItems` and `unevaluatedProperties`, improving composition via `$ref` and `$defs`.
- Tooling: Ajv (JavaScript), jsonschema (Python), and IDE plugins validate and autocomplete; generators produce TypeScript types or UI forms.
- Worked example: a mykb session-capture schema could require `{title, timestamp, body}` and reject unknown keys, so daemon-written notes fail fast instead of corrupting the wiki.
- Integration: OpenAPI bundles JSON Schema for request/response bodies, and RSIS3's RRP prompt specs can be expressed as schemas for machine-checked outputs.

## Related
- [[wiki/api-protocols/openapi|OpenAPI]] — uses JSON Schema for request and response models
- [[wiki/api-protocols/rest-apis|REST APIs]] — schemas document JSON representations
- [[wiki/api-protocols/api-versioning|API Versioning]] — schema evolution must stay backward-compatible
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — typed alternative schema language
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — structured note formats rely on schemas
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — OKF validation mirrors schema validation
- [[wiki/devops-infra/database-indexing|Database Indexing]] — validated fields become indexable
