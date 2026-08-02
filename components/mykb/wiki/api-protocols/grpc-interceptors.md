---
type: "concept"
title: "gRPC Interceptors"
description: "Client- and server-side middleware"
tags: ["grpc", "interceptors", "middleware", "rpc", "observability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/guides/interceptors/", "https://grpc.github.io/grpc/python/grpc.html#grpc.UnaryUnaryClientInterceptor"]
---

# gRPC Interceptors

## Summary
Interceptors are gRPC middleware: functions that wrap unary and streaming calls on the client or server to add cross-cutting behavior — logging, auth, tracing, retries, and rate limiting — without touching the generated service code.

## Details
- Server interceptors: wrap each incoming call before the handler; typical uses are authentication, request logging, panic recovery, and deadline checks.
- Client interceptors: wrap outgoing calls; typical uses are auth header injection, tracing propagation, retry and backoff, and circuit breaking.
- Kinds: unary-unary, unary-stream, stream-unary, and stream-stream interceptors cover every call type; languages differ in granularity (Python has one interceptor interface per kind).
- Ordering: interceptors compose like middleware chains — on the client, the first interceptor is outermost; on the server, the first registered is outermost.
- Observability: interceptors are the canonical place to emit per-call metrics (latency, status code, message counts) and to attach trace spans.
- Context: interceptors can enrich the CallContext with values (user identity, tenant, request ID) that handlers read without parameter plumbing.
- Performance: keep interceptors cheap — they run on every message, so expensive work belongs in dedicated services, not middleware.

## Related
- [[wiki/api-protocols/grpc-metadata|gRPC Metadata]] — interceptors read and write metadata
- [[wiki/api-protocols/grpc-deadlines|gRPC Deadlines]] — interceptors enforce and propagate deadlines
- [[wiki/api-protocols/grpc|gRPC]] — interceptors are part of the gRPC core model
- [[wiki/devops-infra/distributed-tracing|Distributed Tracing]] — trace spans attach in interceptors
- [[wiki/api-protocols/retry-policies|Retry Policies]] — client interceptors implement retries
