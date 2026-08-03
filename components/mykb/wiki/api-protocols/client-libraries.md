---
type: "concept"
title: "API Client Libraries"
description: "Generated and hand-written SDKs that encode an API contract in code"
tags: ["api", "sdk", "tooling", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Client Libraries

## Summary
Generated or hand-written client libraries encode an API's request and response contract in code. They save integration time but become a second contract that must be versioned, generated, and kept honest with the spec.

## Details
A client library wraps an API's endpoints in typed functions: request building, authentication, error handling, pagination, and serialization are handled once instead of in every consumer. Libraries come from three sources: official (maintained by the provider), community (independent), and generated (from OpenAPI or AsyncAPI via generators like openapi-generator, or from gRPC protos with protoc).

The mechanism: a generated client derives types and methods from the spec — each operation becomes a function, each schema a class, parameters become typed arguments, and the transport layer (HTTP client, retries, auth header injection) is provided by the generator's runtime. Code-first libraries (like the official AWS SDKs) are hand-maintained against an internal contract. The client's behavior — which errors throw, how pagination loops, what retry policy applies — is part of the API's user-facing surface.

Concrete example: a team publishes an OpenAPI spec for the wiki API and generates clients for Python and TypeScript in CI. When a new endpoint ships, the generated clients pick it up automatically; consumers get typed callers and cannot easily misuse the payload. A hand-written client that lags the spec causes consumers to miss features or send stale schemas.

Failure modes: generated clients inherit spec bugs (wrong types, missing defaults) and produce noisy, breaking updates on every spec change; library auth handling that defaults to insecure transport or logs tokens leaks credentials; retry logic in the client that double-sends non-idempotent requests creates duplicate side effects; and unversioned clients paired with a versioned API drift until calls 4xx.

Operational tradeoffs: generated clients trade integration speed for churn — every spec tweak regenerates code — while official clients trade freshness for stability. The safe pattern is contract-first: keep the spec the source of truth, generate clients in CI with pinned generator versions, test the client against the real API in CI, and version both together. For gRPC, protos are already the contract, so codegen is the only realistic path.

RSIS3/mykb relevance: RSIS3's own tooling should call mykb's APIs through generated clients where they exist, so contract drift surfaces as compile errors instead of silent runtime mismatches.

## Related
- [[wiki/api-protocols/openapi-spec|OpenAPI Specification]]
- [[wiki/api-protocols/api-docs-generators|API Docs Generators]]
- [[wiki/api-protocols/openapi|OpenAPI]]
- [[wiki/api-protocols/sdk-generation|SDK Generation]]
- [[wiki/api-protocols/contract-testing|Contract Testing]]
