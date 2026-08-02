---
type: "concept"
title: "SDK Generation"
description: "Generating client SDKs from API specs"
tags: ["sdk", "codegen", "openapi", "developer-experience", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://openapi-generator.tech/", "https://www.moesif.com/blog/technical/api-development/Why-API-SDKs-Are-Important/"]
---

# SDK Generation

## Summary
SDK generation turns an API specification into typed client libraries: OpenAPI JSON produces Python, TypeScript, Go, and Java clients; protobuf produces gRPC stubs. Generated SDKs encode the contract in code — types, validation, and endpoints — cutting integration time and eliminating hand-written client drift.

## Details
- Inputs: OpenAPI v3 for REST, protobuf/IDL for gRPC, GraphQL SDL for typed query builders, and AsyncAPI for event clients.
- Generators: OpenAPI Generator, Swagger Codegen, Kiota, and per-language generators emit models, API clients, and serializers.
- What you get for free: typed request/response models, auth wiring, retry hooks, error types, and documentation from annotations.
- Publishing: CI regenerates and publishes SDKs to package registries (npm, PyPI, Maven) tagged with the API version.
- Contract quality is everything: codegen amplifies spec ambiguities — naming, nullability, and error shapes become user-facing API.
- Customization: generators support templates and vendor extensions, but heavy customization reduces regeneration gains; fix the spec first.
- Trade-offs: generated code can be verbose and lags hand-tuned ergonomics; many platforms generate SDKs and let teams patch only at the edges.

## Related
- [[wiki/api-protocols/openapi|OpenAPI]] — the spec SDKs are generated from
- [[wiki/api-protocols/api-design-first|Design-First APIs]] — spec quality drives SDK quality
- [[wiki/api-protocols/grpc|gRPC]] — protobuf codegen as the gRPC SDK
- [[wiki/api-protocols/contract-testing|Contract Testing]] — SDKs embody the contract in code
- [[wiki/software-engineering/developer-experience|Developer Experience]] — SDKs are the DX surface
