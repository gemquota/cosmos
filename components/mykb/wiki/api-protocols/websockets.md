---
type: "concept"
title: "WebSockets"
description: "Full-duplex, persistent TCP-based protocol for low-latency bidirectional browser-server communication"
tags: ["websockets", "realtime", "protocols", "http", "networking"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6455"]
---

# WebSockets

## Summary
WebSockets (RFC 6455) provide a full-duplex, persistent communication channel between client and server over a single TCP connection. After an HTTP Upgrade handshake, both sides push frames at any time with low overhead. They underpin chat, live dashboards, multiplayer games, and agent-to-server telemetry where request-response polling is too slow.

## Details
- Handshake: the client sends an HTTP request with `Upgrade: websocket`; the server responds 101 Switching Protocols, then frames flow bidirectionally.
- Frames: text or binary messages with masking on the client side; ping/pong keepalives detect dead connections.
- Protocols and extensions: `Sec-WebSocket-Protocol` negotiates subprotocols; permessage-deflate compresses payloads.
- Server-side: FastAPI supports WebSocket endpoints natively, which fits RSIS3's pulse engine broadcasting telemetry to the dashboard.
- Scaling: connections are stateful, so load balancers need sticky sessions or a shared pub/sub bus (Redis Streams, Kafka) to fan events across instances.
- Fallback: when proxies block upgrade headers, SSE (Server-Sent Events) provides one-way server push over plain HTTP.
- Relevance: the mykb daemon could stream live note-indexing events to editors over WebSockets instead of polling.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — request-response baseline; WebSockets for realtime
- [[wiki/api-protocols/message-queues|Message Queues]] — backplane for scaling WebSocket fan-out
- [[wiki/api-protocols/redis-streams|Redis Streams]] — pub/sub bus for cross-instance broadcasts
- [[wiki/api-protocols/kafka|Apache Kafka]] — durable event log for realtime pipelines
- [[wiki/api-protocols/timeouts|Timeouts]] — idle and keepalive handling for persistent sockets
- [[wiki/concepts/triad-architecture|Triad Architecture]] — dashboard telemetry flows from engine to UI
- [[wiki/api-protocols/entities/graphql|GraphQL]] — subscriptions reuse WebSocket transport
- [[wiki/ops/gap-report|Gap Analysis Report]] — realtime delivery gaps noted
