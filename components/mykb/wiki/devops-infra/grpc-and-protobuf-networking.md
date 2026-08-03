---
type: "concept"
title: "gRPC & Protobuf Networking"
description: "HTTP/2 based RPC with binary framing and streaming semantics"
tags: ["grpc", "protobuf", "http2", "rpc"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# gRPC & Protobuf Networking

## Summary
gRPC is an RPC framework built on HTTP/2 and Protocol Buffers: strongly typed service definitions in .proto files generate clients and servers, with multiplexed streaming, binary encoding, and built-in deadlines. Protobuf defines the wire format; gRPC defines the call semantics — unary, server-streaming, client-streaming, and bidirectional streaming.

## Details
- Mechanism: `.proto` files declare messages and service methods; `protoc` generates code; messages serialize to a compact binary format with field numbers (forward/backward compatible if numbering rules are followed); gRPC multiplexes many calls over one HTTP/2 connection, supports deadlines and cancellation, and attaches metadata (headers); servers stream responses and clients stream requests.
- Concrete example: a recommendation service exposes `GetRecs(UserID) returns (stream Rec)` — the client opens one HTTP/2 connection and receives a stream; errors use rich status codes (INVALID_ARGUMENT, DEADLINE_EXCEEDED); a gateway (grpc-gateway, Envoy) translates REST/JSON for browser clients.
- Failure modes: protobuf field-number reuse corrupts data across versions — never reuse numbers, never change types; message sizes without limits let a peer exhaust memory (set max receive size); long-lived streams that leak without keepalive or deadlines; connection pooling issues under HTTP/2 multiplexing (too many streams, flow control stalls); server reflection or health-checking absent, making ops harder.
- Tradeoffs: gRPC's efficiency, streaming, and typed contracts come at the cost of tooling and debuggability — payloads are binary, so tracing and curl-style debugging need reflection or grpcurl; the alternative, REST/JSON, is universally debuggable but slower and untyped; teams often run both via a gateway.
- Operational notes: version protos, run breaking-change checks, set deadlines and retry policies, and expose health and reflection endpoints.
- Balancing: HTTP/2 multiplexing breaks naive per-connection load balancing — use client-side pick-first with subchannel sharing or a stream-aware proxy, and enable keepalive pings to detect dead peers.
- RSIS3 relevance: RSIS3's component-to-component calls (mykb daemon, SPACE) would benefit from typed protobuf contracts with built-in deadlines — versioned schemas keep loop upgrades safe.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
