---
type: "concept"
title: "REST vs gRPC"
description: "JSON-over-HTTP versus typed binary contracts over HTTP/2"
tags: ["api", "rest", "grpc", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# REST vs gRPC

## Summary
REST and gRPC represent two poles of API design: REST sends self-describing JSON over HTTP/1.1 with a uniform resource model, while gRPC sends compact protobuf frames over HTTP/2 with strict schemas, streaming, and generated clients. The right choice depends on whether you optimize for ecosystem reach and debuggability or for throughput, contract safety, and streaming.

## Details
- Mechanism: REST maps endpoints to resources and verbs, with headers and status codes doing the work; gRPC encodes structured messages as protobuf bytes over HTTP/2 multiplexed streams, using a binary framing that is roughly 3-5x smaller than equivalent JSON. HTTP/2 lets one connection carry many concurrent RPCs, avoiding head-of-line blocking, and gRPC supports unary, server-streaming, client-streaming, and bidirectional-streaming call shapes.
- Contract story: protobuf gives you a single source of truth (the .proto file) with typed fields, required/optional rules, and code generation for dozens of languages, so mismatched payloads fail at compile time instead of at runtime. REST has OpenAPI as its contract layer, but JSON Schema validation is opt-in and many teams drift between the spec and the implementation. gRPC also version-checks field numbers, so renames do not corrupt parsing, whereas JSON changes must be handled by convention.
- Concrete examples: internal service-to-service calls in a microservice fleet (payment processing, recommendations, event pipelines) typically choose gRPC for latency and streaming; public browser and mobile APIs choose REST because HTTP/2 framing, TLS, and JSON are natively supported and proxies, CDNs, and load balancers understand them. gRPC-web and Connect exist to bridge the browser gap, but they add a translation layer and still cannot expose raw bidirectional streams the way a WebSocket can.
- Failure modes: gRPC debugging is harder because payloads are binary; tools like grpcurl and reflection help but do not replace curl. Protocol changes that renumber or delete fields corrupt old clients silently, and any intermediary that buffers the body breaks streaming. REST's failure modes are different: schemas drift, payload bloat grows latency, and N+1 fan-out requests multiply round trips.
- Operational tradeoffs: gRPC shines for long-lived connections, polyglot microservices, and low-bandwidth devices, but requires health checking, load balancing tuned for HTTP/2, and a gateway to expose it to the web; REST trades efficiency for universality, cacheability (GET responses can be cached by CDNs), and human debuggability. Many teams run both behind one API gateway, choosing per-endpoint.
- RSIS3/mykb relevance: RSIS3 loops exchange structured artifacts between Python services; a typed contract (protobuf or validated JSON Schema) keeps registry entries and pulses machine-verifiable, and streaming fits telemetry flows that push many small updates without polling.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/rest-vs-rpc|REST vs RPC]]
- [[wiki/api-protocols/rest-vs-graphql|REST vs GraphQL]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/rpc-styles|RPC Styles]]
- [[wiki/api-protocols/graphql|GraphQL]]
