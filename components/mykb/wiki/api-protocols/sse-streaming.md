---
type: "concept"
title: "Server-Sent Events (SSE)"
description: "One-way HTTP streaming where the server pushes events to the browser over a long-lived connection"
tags: ["sse", "streaming", "http", "realtime", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events", "https://html.spec.whatwg.org/multipage/server-sent-events.html"]
---
# Server-Sent Events (SSE)

## Summary
Server-Sent Events deliver a stream of text events from server to client over a single HTTP response. The EventSource API handles reconnection and last-event-id resumption automatically. SSE is simpler than WebSockets when the server is the only talker — progress feeds, notifications, and model token streams.

## Details
- **Wire format** — lines like `data:`, `event:`, `id:`, and `retry:` form events; blank lines delimit them; UTF-8 text only.
- **Auto-reconnect** — EventSource reconnects on failure and can resume from the last id, giving at-least-once semantics with a server-held replay buffer.
- **HTTP compatibility** — SSE rides plain HTTP, works through most proxies, and benefits from HTTP/2 multiplexing.
- **Compared with WebSocket** — no client-to-server channel and no binary, but far less infrastructure; a fetch-based fallback can polyfill it.
- **Worked example** — an agent task runner streams `log:` events to a browser panel; the wiki notes SSE as the lightest realtime option for one-way feeds.
- **Relevance** — RSIS3's pulse stream is a natural SSE payload for live status views.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/retry-after-web|Retry-After]] — adjacent concept in this wiki
- [[wiki/api-protocols/503-handling|Handling 503]] — adjacent concept in this wiki
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — existing coverage
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — existing coverage
- [[wiki/api-protocols/ndjson-streaming|NDJSON Streaming]] — existing coverage
