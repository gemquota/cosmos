---
type: "concept"
title: "gRPC APIs"
description: "Typed, binary RPC framework over HTTP/2 with streaming, deadlines, and generated clients"
tags: ["grpc", "rpc", "protobuf", "http2", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/what-is-grpc/introduction/", "https://grpc.io/docs/what-is-grpc/core-concepts/"]
---
# gRPC APIs

## Summary
gRPC is a high-performance RPC framework that uses Protocol Buffers for typed contracts and HTTP/2 for transport. Services are defined in .proto files, then compiled into client and server stubs for many languages. It offers four call styles — unary, server streaming, client streaming, and bidirectional streaming — plus deadlines, cancellation, and rich metadata.

## Details
- **Contract-first** — the .proto schema is the single source of truth; generated code keeps client and server in lockstep and enables polyglot services.
- **HTTP/2 benefits** — multiplexing, header compression (HPACK), and binary framing reduce latency versus JSON over HTTP/1.1.
- **Streaming** — bidirectional streaming suits chat, telemetry, and live feeds; flow control is built in.
- **Deadlines and propagation** — per-call deadlines propagate across the call graph; gRPC status codes (OK, DeadlineExceeded, Unavailable) drive retry policy.
- **Worked example** — a knowledge service exposing memory-read/write as unary calls and pulse ingestion as a client-streaming call, with OpenTelemetry tracing across hops.
- **Relevance** — for RSIS3's multi-component runtime, gRPC gives typed contracts between agent loops and storage without JSON parsing overhead.

## Related
- [[wiki/api-protocols/rest-vs-grpc|REST vs gRPC]] — adjacent concept in this wiki
- [[wiki/api-protocols/rest-vs-rpc|REST vs RPC]] — adjacent concept in this wiki
- [[wiki/api-protocols/client-credentials-flow|Client Credentials Flow]] — adjacent concept in this wiki
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/grpc|gRPC]] — existing coverage
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — existing coverage
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — existing coverage
