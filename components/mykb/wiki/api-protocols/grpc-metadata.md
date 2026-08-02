---
type: "concept"
title: "gRPC Metadata"
description: "Header and trailer metadata exchange"
tags: ["grpc", "metadata", "headers", "trailers", "rpc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/what-is-grpc/core-concepts/#metadata", "https://grpc.io/docs/guides/metadata/"]
---

# gRPC Metadata

## Summary
gRPC metadata is a set of key-value pairs sent alongside calls — before the request (initial metadata), after the response headers, and in trailers. It carries authentication tokens, tracing IDs, and application context without polluting the typed request messages.

## Details
- Two kinds: initial metadata (request headers, response headers) and trailing metadata (response trailers, including the status code and message).
- Keys are lowercase ASCII strings; binary values use the -bin suffix and are base64-encoded; keys may repeat.
- Common uses: Authorization or x-api-key, distributed-tracing headers (traceparent, x-request-id), client version, and deadline hints.
- Lifecycle: clients attach outgoing metadata per call; servers read it in the call context, and responses carry header and trailer metadata to the client.
- Interceptors are the idiomatic place to add or propagate metadata — auth middleware, tracing injection, and rate-limit counters all hook here.
- Deadlines are not metadata per se: they ride in a dedicated grpc-timeout field, though many frameworks expose them via the same context object.
- Security: never place secrets in metadata that is logged; use TLS or mTLS for transport and keep tokens in standard auth headers.

## Related
- [[wiki/api-protocols/grpc-interceptors|gRPC Interceptors]] — the middleware layer that reads and writes metadata
- [[wiki/api-protocols/grpc-deadlines|gRPC Deadlines]] — deadlines are transmitted like metadata
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — trace IDs travel in metadata
- [[wiki/api-protocols/grpc|gRPC]] — metadata is part of the gRPC core concepts
- [[wiki/api-protocols/mtls|mTLS]] — transport security for gRPC channels
