---
type: "concept"
title: "OpenAPI Specification"
description: "Machine-readable description of REST APIs: paths, operations, schemas, and security"
tags: ["openapi", "api", "specification", "documentation", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://spec.openapis.org/oas/v3.1.0", "https://learn.openapis.org/"]
---
# OpenAPI Specification

## Summary
OpenAPI is the standard format for describing REST APIs: paths, methods, parameters, request/response bodies, and security schemes in one JSON or YAML document. From it, teams generate docs, SDKs, mocks, and tests. FastAPI, Express, and many frameworks produce OpenAPI automatically.

## Details
- **Document anatomy** — info (title/version), servers, paths with operations, components (schemas, parameters, security schemes), and tags.
- **Schema-first workflow** — the spec is the contract; codegen produces clients and server stubs, and contract tests validate both sides.
- **Tooling** — Swagger UI renders interactive docs, generators emit SDKs, and validators gate CI.
- **Security descriptions** — OAuth2, API keys, and HTTP auth schemes are declared per operation, enabling policy checks.
- **Worked example** — the mykb FastAPI service exposes `/docs` from auto-generated OpenAPI; the wiki keeps the spec as the contract record.
- **Relevance** — RSIS3's workers can read OpenAPI to discover tool endpoints instead of hard-coding URLs.

## Related
- [[wiki/api-protocols/api-docs-generators|API Docs Generators]] — adjacent concept in this wiki
- [[wiki/api-protocols/client-libraries|API Client Libraries]] — adjacent concept in this wiki
- [[wiki/api-protocols/openapi|OpenAPI]] — existing coverage
- [[wiki/api-protocols/sdk-generation|SDK Generation]] — existing coverage
- [[wiki/api-protocols/contract-testing|Contract Testing]] — existing coverage
