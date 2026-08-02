---
type: "concept"
title: "WebSocket Protocols"
description: "Full-duplex, persistent message channels over a single TCP connection, upgraded from HTTP"
tags: ["websocket", "realtime", "http", "protocols", "streaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API", "https://www.rfc-editor.org/rfc/rfc6455"]
---
# WebSocket Protocols

## Summary
WebSocket is a protocol that upgrades an HTTP connection to a persistent, full-duplex channel. After the handshake, either side can push text or binary frames without request-response pairing. It is the foundation for chat, live dashboards, collaborative editing, and realtime agent UIs.

## Details
- **Handshake** — the client sends `Upgrade: websocket` with a Sec-WebSocket-Key; the server answers 101 with a computed accept key. Proxies and load balancers must support the upgrade.
- **Frames** — messages split into FIN-framed frames: text, binary, ping/pong for keepalive, and close frames with status codes.
- **Reconnection** — connections drop; clients need backoff, heartbeat detection, and resume logic.
- **Scaling** — servers broadcast to many sockets; pub/sub backends (Redis) and sticky sessions or broadcast buses scale fan-out.
- **Worked example** — a realtime log view for the mykb daemon streams pulses over WebSocket while HTTP serves the historical graph.
- **Relevance** — RSIS3's long-running sessions benefit from push channels for live telemetry instead of polling.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — adjacent concept in this wiki
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]] — adjacent concept in this wiki
- [[wiki/api-protocols/websockets|WebSockets]] — existing coverage
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — existing coverage
- [[wiki/api-protocols/websocket-reconnection|WebSocket Reconnection]] — existing coverage
