---
type: "concept"
title: "Server-Sent Events"
description: "SSE stream format, fields, and reconnection"
tags: ["sse", "server-sent-events", "streaming", "realtime", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events", "https://html.spec.whatwg.org/multipage/server-sent-events.html"]
---

# Server-Sent Events

## Summary
Server-Sent Events (SSE) is a one-way push protocol over plain HTTP: the server keeps a response open and streams text/event-stream messages. Because it rides on HTTP, SSE gets caching, proxies, compression, and automatic reconnection for free — the simplest realtime channel for browsers.

## Details
- Wire format: a stream of events separated by blank lines, each with optional fields: event, data (can be multi-line), id, and retry.
- The EventSource API auto-connects, auto-reconnects (with Last-Event-ID resumption), and dispatches named events to listeners.
- Connection mechanics: the server never closes the response; HTTP/1.1 needs chunked transfer encoding, and proxies must not buffer the response body.
- id + Last-Event-ID: clients send the last seen id on reconnect so servers can resume from a cursor — built-in at-least-once delivery.
- Compared to WebSockets: SSE is one-way (server to client), auto-reconnects, works over normal HTTP tools, but has connection limits (browsers cap ~6 per origin on HTTP/1.1).
- Use cases: live dashboards, progress bars, model token streams, notifications — anything where the client only listens.
- Fields and format: "event: message" names the event; retry: N milliseconds sets the reconnection delay; comments (lines starting with :) are keepalives.

## Related
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — the bidirectional alternative
- [[wiki/api-protocols/ndjson-streaming|NDJSON Streaming]] — a simpler JSON-per-line stream format
- [[wiki/api-protocols/chunked-transfer-encoding|Chunked Transfer Encoding]] — how HTTP/1.1 delivers the stream
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — Last-Event-ID gives resumable delivery
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — SSE as a streaming API pattern
