---
type: "concept"
title: "Design-First APIs"
description: "Spec-first workflow with review gates"
tags: ["api-design", "spec-first", "openapi", "workflow", "governance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://swagger.io/resources/articles/adopting-an-api-first-approach/", "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design"]
---

# Design-First APIs

## Summary
Design-first API development writes the contract before the implementation: the team authors an OpenAPI (or protobuf/AsyncAPI) spec, reviews it like code, and only then builds. The spec becomes the single source of truth driving mocks, SDKs, tests, and docs — catching design problems when they cost nothing to fix.

## Details
- The flow: draft spec -> design review (naming, semantics, errors, pagination) -> lint and validate -> mock server from spec -> implement against it.
- Review gates: breaking changes, ambiguous fields, and missing error contracts are caught in review, not after clients ship.
- Mocks first: tools (Prism, Mockoon) serve the spec, so frontend and integration teams build against agreed contracts immediately.
- Single source of truth: docs, SDKs, contract tests, and server validation all derive from one spec — no drift.
- Tooling: OpenAPI lint rules (spectral), spec diffing in CI, and generator pipelines keep the spec honest.
- Culture shift: the spec is code — reviewed, versioned, and owned; API reviewers are as important as code reviewers.
- When not to: tiny internal APIs and prototypes may skip ceremony, but the contract-first habit pays off before the second consumer appears.

## Related
- [[wiki/api-protocols/openapi|OpenAPI]] — the format design-first workflows use
- [[wiki/api-protocols/contract-testing|Contract Testing]] — specs feed contract verification
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — review gates prevent breaks
- [[wiki/api-protocols/sdk-generation|SDK Generation]] — specs drive SDK automation
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — errors are designed in the spec
