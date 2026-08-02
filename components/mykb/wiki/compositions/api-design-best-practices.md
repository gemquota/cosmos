---
type: "concept"
title: "API Design Best Practices"
description: "The conventions that make APIs predictable, evolvable, and usable"
tags: ["api", "design", "rest", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/REST", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status"]
---

# API Design Best Practices

## Summary
API design best practices are the conventions that make interfaces predictable: clear resource modeling, correct HTTP semantics, consistent errors, versioning, and backward compatibility. Good APIs are boring — they follow conventions so consumers can guess how they work.

## Details
- Model resources and collections with nouns; use HTTP methods for the verbs and status codes for outcomes.
- Design errors as a contract: consistent shape, machine-readable codes, human messages, and request IDs.
- Version explicitly (URL or header) and evolve backward compatibly: additive fields, deprecation windows.
- Pagination, filtering, and idempotency keys are table stakes for real-world APIs.
- Design with consumers: document with OpenAPI, test with contract tests, and keep examples honest.
- For the mykb bundle, the wiki API follows these practices so agent and human clients behave identically.
- Worked example — an API returns 201 with Location on create, 409 on conflict, and 429 with Retry-After when throttled; errors always carry {code, message, request_id}.

Worked example — an API returns 201 with Location on create, 409 on conflict, and 429 with Retry-After when throttled; errors always carry {code, message, request_id}.

## Related
- [[wiki/software-engineering/requirements-engineering|Requirements Engineering]]
- [[wiki/dev-tools/error-codes|Error Codes]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/compositions/backward-compatible-schema|Backward-Compatible Schema]]
- [[wiki/api-protocols/openapi|OpenAPI]]
