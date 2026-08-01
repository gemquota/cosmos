---
type: "concept"
title: "gRPC"
description: "High-performance RPC framework using HTTP/2 and Protocol Buffers for typed service contracts"
tags: ["grpc", "rpc", "http2", "protobuf", "microservices"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# gRPC

## Summary
gRPC is a Google-developed RPC framework that runs over HTTP/2 with Protocol Buffers as the default interface definition language. It supports unary, server-streaming, client-streaming, and bidirectional streaming calls.

## Details
- `.proto` files define services and messages; code generators emit clients and servers for many languages.
- Binary, strongly typed payloads are faster and smaller than JSON; mTLS and deadlines are built in.
- Use it for internal service-to-service calls where REST's text overhead or GraphQL's query cost is not worth it.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — the dominant alternative style
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — gRPC's contract language
- [[wiki/api-protocols/timeouts|Timeouts]] — gRPC deadlines bound call duration
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — protects gRPC call graphs
- [[wiki/devops-infra/envoy|Envoy]] — proxies gRPC traffic and load balancing
- [[wiki/security/zero-trust|Zero Trust Architecture]] — mTLS per call
