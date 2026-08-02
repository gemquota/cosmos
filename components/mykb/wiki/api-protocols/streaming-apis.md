---
type: "concept"
title: "Streaming APIs"
description: "Streaming request/response patterns and trade-offs"
tags: ["streaming", "api-design", "realtime", "protocols", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/patterns/async-request-reply", "https://www.infoq.com/articles/streaming-architecture/"]
---

# Streaming APIs

## Summary
Streaming APIs deliver data incrementally instead of as one complete response — token-by-token LLM output, log tails, price feeds, and job progress. The choice of transport (chunked HTTP, SSE, WebSocket, gRPC streams, or message queues) trades latency, complexity, replayability, and client coupling.

## Details
- Why stream: time-to-first-byte drops from the full generation time to milliseconds, memory use drops, and consumers can act on partial results.
- Request streaming: uploads and aggregates (client-streaming) let senders start before the payload completes; most APIs still pair a final response.
- Response streaming: server pushes a sequence of chunks; the client must handle partial-state rendering and terminal markers.
- Transports: SSE for simple one-way browser push, WebSocket for bidirectional, gRPC streams for typed high-throughput RPC, chunked HTTP/1.1 for raw bytes.
- Buffering is the enemy: proxies, gateways, and CDNs must disable buffering or streams stall; test through every hop.
- Resumability: streams break; designs either replay from an id/cursor (SSE Last-Event-ID, Kafka offsets) or accept restarts.
- Error semantics: a stream that dies midway needs a distinct error signal (trailer status, a final error event, or reconnect) so clients do not mistake truncation for completion.

## Related
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — the one-way HTTP push transport
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — typed RPC streaming call types
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — bidirectional streaming transport
- [[wiki/api-protocols/backpressure|Backpressure]] — flow control matters once you stream
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — streams vs discrete events as API shapes
