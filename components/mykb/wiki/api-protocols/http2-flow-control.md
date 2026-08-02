---
type: "concept"
title: "HTTP/2 Flow Control"
description: "Stream- and connection-level flow-control windows"
tags: ["http2", "flow-control", "backpressure", "windows", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9113#name-flow-control", "https://http2.github.io/faq/#why-the-flow-control-window"]
---

# HTTP/2 Flow Control

## Summary
HTTP/2 flow control uses credit-based windows at two levels: each stream has its own window, and the whole connection has a shared window. Receivers advertise WINDOW_UPDATE credits as they consume data, so a slow consumer throttles its own stream without blocking unrelated streams.

## Details
- Two windows: per-stream (each stream starts at SETTINGS_INITIAL_WINDOW_SIZE, default 65535 bytes) and per-connection (default 65535).
- Mechanics: senders must not exceed the minimum of stream and connection windows; receivers grant more credit with WINDOW_UPDATE frames.
- Granularity: data frames update consumption; the receiver controls the pacing by when it sends WINDOW_UPDATE — the application's read loop.
- Why two levels: the connection window bounds total buffering (protecting memory), while stream windows prevent one stream from hogging the pipe.
- Interaction with streams: a stalled stream consumes its own window but leaves others running — unlike TCP head-of-line blocking.
- Backpressure mapping: frameworks expose this as read buffering and pause semantics (for example gRPC's flow control for streaming).
- Beware: huge windows allow fast transfer but permit large buffering; small windows add latency — tune for your payload sizes.

## Related
- [[wiki/api-protocols/http2|HTTP/2]] — flow control lives inside the HTTP/2 framing
- [[wiki/api-protocols/backpressure|Backpressure]] — credit windows are protocol-level backpressure
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — gRPC streams rely on HTTP/2 windows
- [[wiki/api-protocols/quic|QUIC]] — QUIC has its own flow-control model
- [[wiki/api-protocols/http3|HTTP/3]] — flow control carried into HTTP/3
