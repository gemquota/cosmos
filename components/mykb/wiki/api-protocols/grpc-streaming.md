---
type: "concept"
title: "gRPC Streaming"
description: "Unary, server-, client-, and bidi-streaming RPCs"
tags: ["grpc", "streaming", "rpc", "http2", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/what-is-grpc/core-concepts/#server-streaming-rpc", "https://grpc.io/docs/languages/python/basics/"]
---

# gRPC Streaming

## Summary
gRPC defines four call types on top of HTTP/2: unary, server-streaming, client-streaming, and bidirectional streaming. Streaming changes latency, backpressure, and error semantics, and each type fits a different workload — from request-response to long-lived data feeds.

## Details
- Unary: one request, one response — the classic RPC; used for most CRUD-like calls.
- Server-streaming: the client sends one request and receives a stream of messages (a feed, a big result set split into chunks); the client can cancel mid-stream.
- Client-streaming: the client uploads many messages and gets one response (bulk upload, aggregation); the server replies only after the stream completes.
- Bidi-streaming: both sides send an independent sequence of messages (chat, telemetry, coordination); message ordering is preserved per direction but interleaving is arbitrary.
- HTTP/2 mechanics: each call runs on its own stream with its own flow-control window, so one slow consumer does not block others.
- Backpressure: flow control limits in-flight bytes; producers should respect the window and pause instead of buffering unboundedly.
- gRPC status codes end streams; a stream that fails partway carries both delivered messages and a terminal status.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — the framework streaming call types belong to
- [[wiki/api-protocols/grpc-status-codes|gRPC Status Codes]] — streams terminate with a status
- [[wiki/api-protocols/http2-flow-control|HTTP/2 Flow Control]] — windows govern stream throughput
- [[wiki/api-protocols/backpressure|Backpressure]] — streaming forces explicit flow control
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — the general patterns behind RPC streams
