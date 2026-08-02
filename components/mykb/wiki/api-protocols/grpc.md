---
type: "concept"
title: "gRPC"
description: "High-performance RPC framework using HTTP/2 and Protocol Buffers for typed service contracts"
tags: ["grpc", "rpc", "http2", "protobuf", "microservices"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/what-is-grpc/introduction/", "https://grpc.io/docs/what-is-grpc/core-concepts/"]
---

# gRPC

## Summary
gRPC is a Google-developed RPC framework that runs over HTTP/2 with Protocol Buffers as the default interface definition language. It supports unary, server-streaming, client-streaming, and bidirectional streaming calls.

## Details
- `.proto` files define services and messages; code generators emit clients and servers for many languages.
- Binary, strongly typed payloads are faster and smaller than JSON; mTLS and deadlines are built in.
- Use it for internal service-to-service calls where REST's text overhead or GraphQL's query cost is not worth it.
- gRPC is a high-performance RPC framework built on HTTP/2 and Protocol Buffers: services and messages are defined in .proto files, and code is generated for many languages.
- HTTP/2 multiplexing lets many RPCs share one connection, reducing latency and connection churn compared to HTTP/1.1.
- The core patterns are unary, server streaming, client streaming, and bidirectional streaming, all expressed in the same IDL.
- Deadlines, cancellation, and metadata are first-class; interceptors handle cross-cutting concerns like auth and tracing.
- **Worked example / comparison** — Comparison — gRPC over HTTP/2 trades REST's human-readable JSON for compact binary frames and generated clients; it shines for internal service-to-service calls.
- For mykb, gRPC is documented as the default internal RPC choice, with protobuf as its payload format.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/protobuf|Protocol Buffers]]
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/devops-infra/envoy|Envoy]]
- [[wiki/security/zero-trust|Zero Trust Architecture]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
