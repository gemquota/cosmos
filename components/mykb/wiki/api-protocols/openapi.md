---
type: "concept"
title: "OpenAPI"
description: "Vendor-neutral specification for describing REST APIs as machine-readable documents with endpoints, schemas, and security"
tags: ["openapi", "api", "documentation", "specification", "rest"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://spec.openapis.org/oas/v3.1.0"]
---

# OpenAPI

## Summary
OpenAPI (formerly Swagger) is a vendor-neutral, machine-readable specification for describing HTTP APIs: paths, methods, parameters, request/response bodies, authentication, and servers. A single OpenAPI document can drive interactive docs, SDK generation, mocking, and contract tests. OpenAPI 3.1 aligns its schema layer with JSON Schema 2020-12.

## Details
- Structure: `info`, `servers`, `paths`, `components`, and `security` top-level objects; each operation declares parameters, requestBody, responses, and tags.
- Ecosystem: Swagger UI renders interactive documentation, OpenAPI Generator and openapi-typescript emit clients, and stoplight/prism mock or validate traffic.
- FastAPI automatically derives an OpenAPI document from Python type hints — RSIS3's dashboard exposes `/docs` and `/openapi.json` with zero hand-written spec.
- Versioning the document: tools compare versions to detect breaking changes; `deprecated: true` marks operations slated for removal.
- Security schemes are declarative: `oauth2`, `bearer`, `apiKey`, and `openIdConnect` entries tell consumers how to authenticate.
- Best practice: keep the spec as the contract of record and generate server/client stubs from it, so drift between implementation and documentation is caught in CI.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — OpenAPI describes REST interfaces
- [[wiki/api-protocols/json-schema|JSON Schema]] — schema layer for request/response bodies
- [[wiki/api-protocols/api-versioning|API Versioning]] — specs make version diffs reviewable
- [[wiki/api-protocols/webhooks|Webhooks]] — async callbacks documented alongside operations
- [[wiki/security/oauth2|OAuth 2.0]] — declarative security schemes in the spec
- [[wiki/devops-infra/github-actions|GitHub Actions]] — contract tests can diff spec changes in CI
- [[wiki/concepts/triad-architecture|Triad Architecture]] — FastAPI generates the dashboard's spec
- [[wiki/api-protocols/grpc|gRPC]] — contract-first alternative to OpenAPI
- [[wiki/devops-infra/envoy|Envoy]] — gateway routing aligned with the spec
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — FastAPI-generated docs in the bundle
