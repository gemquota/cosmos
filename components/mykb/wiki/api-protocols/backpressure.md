---
type: "concept"
title: "Backpressure"
description: "Flow control across streaming and messaging pipelines"
tags: ["backpressure", "flow-control", "streaming", "reliability", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.reactivemanifesto.org/glossary#Back-Pressure", "https://medium.com/@jayphelps/backpressure-explained-the-flow-of-data-through-software-2350b3e3533e"]
---

# Backpressure

## Summary
Backpressure is the mechanism that lets a slow consumer tell a fast producer to slow down, preventing unbounded buffering and memory exhaustion. In streams, queues, and RPC pipelines, backpressure answers one question: what happens when the downstream cannot keep up?

## Details
- Why it matters: without backpressure, producers buffer without limit until memory dies, or drop data silently; with it, systems degrade by slowing, not crashing.
- Push vs pull: pull-based (lazy iterators, reactive streams) requests work on demand; push-based (WebSockets, raw pub/sub) needs explicit control signals.
- TCP and HTTP/2: flow-control windows bound in-flight bytes — the receiver grants credit, and the sender pauses when credit runs out.
- Message queues: broker queues absorb bursts, but unbounded queues are backpressure in disguise; use queue caps, TTLs, or rejections (503) instead.
- Reactive Streams: the backpressure standard (Publisher/Subscriber with demand signaling) underpins Project Reactor, RxJava, and Akka Streams.
- Drop policies: when a consumer is too slow, choices are block, drop-oldest, drop-newest, or shed load — each with different consistency effects.
- Application-level signals: WebSocket clients can stop reading or send a pause frame; gRPC respects HTTP/2 windows; SSE consumers can close the connection.

## Related
- [[wiki/api-protocols/http2-flow-control|HTTP/2 Flow Control]] — window-based credit at the protocol level
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — limiting in-flight work is load-side backpressure
- [[wiki/api-protocols/load-shedding|Load Shedding]] — rejecting work when buffers overflow
- [[wiki/api-protocols/message-queues|Message Queues]] — queue caps implement bounded backpressure
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — streams are where backpressure bites
