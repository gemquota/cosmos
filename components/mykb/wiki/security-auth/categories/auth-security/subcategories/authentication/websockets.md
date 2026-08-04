---
type: "entity"
title: "WebSockets"
resource: ""
---
description: "The WebSocket protocol for full-duplex, persistent client-server communication"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "websockets", "realtime"]
timestamp: "2026-07-19T22:41:43Z"

# WebSockets

## Summary
WebSockets is a protocol that keeps a single, full-duplex connection open between a client and server for low-latency, bidirectional messages. It matters because real-time features such as chat, dashboards, and live collaboration need server push, not client polling. Unlike HTTP request-response, a WebSocket connection persists, and both sides can send messages at any time after the handshake completes.

## Details
- **Definition** — WebSocket upgrades an HTTP connection via a handshake, then exchanges framed messages over a persistent TCP connection between the two peers.
- **Handshake** — the client sends an Upgrade request with a key; the server responds with status 101, after which both sides speak the WebSocket protocol.
- **Frames** — messages are split into text and binary frames with size limits; fragmentation, ping, and pong frames keep the connection healthy.
- **Full-duplex** — either side may initiate messages at any time, which removes the request-response bottleneck of classic HTTP.
- **Reconnection** — connections drop for many reasons; clients must reconnect with backoff and resume state, because the protocol has no built-in resume.
- **Security** — origins must be validated to prevent cross-site hijacking, and authentication typically happens before or just after the handshake.
- **Scaling** — a server must track and fan out to many sockets; horizontal scaling requires a shared pub-sub layer for broadcasts.
- **Heartbeats** — periodic ping-pong detects dead connections so servers can reclaim resources from silent clients.
- **Common failure modes** — silent dead connections, unbounded message sizes, and missing heartbeat handling that leaks resources.
- **Worked example** — a dashboard opens a WebSocket, receives live metric pushes, and reconnects with backoff when the connection drops during a deploy.
- **Practical relevance** — WebSockets are the standard foundation for interactive, real-time web features.

## Related
- [[wiki/api-protocols/websockets|WebSockets]] — protocol reference
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — upgrade mechanics
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — message framing
- [[wiki/api-protocols/websocket-reconnection|WebSocket Reconnection]] — recovery patterns
- [[wiki/api-protocols/websocket-security|WebSocket Security]] — authentication and origin checks
- [[wiki/devops-infra/websocket-proxying|WebSocket Proxying]] — operating behind proxies
