---
type: "concept"
title: "WebSocket Handshake"
description: "Upgrade request, keys, and subprotocols"
tags: ["websockets", "handshake", "upgrade", "http", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6455#section-4", "https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"]
---

# WebSocket Handshake

## Summary
The WebSocket connection begins with an HTTP/1.1 Upgrade handshake: the client sends Upgrade: websocket with Sec-WebSocket-Key, the server replies 101 Switching Protocols with Sec-WebSocket-Accept, and the socket then speaks raw frames. The handshake exists so WebSockets pass through existing HTTP infrastructure.

## Details
- Client request: GET with Connection: Upgrade, Upgrade: websocket, Sec-WebSocket-Version: 13, Sec-WebSocket-Key (16 random bytes base64), and optional Sec-WebSocket-Protocol and Sec-WebSocket-Extensions.
- Server accept: 101 Switching Protocols with Sec-WebSocket-Accept, computed as base64(SHA1(key + GUID)) where GUID is 258EAFA5-E914-47DA-95CA-C5AB0DC85B11.
- Purpose of the key: it is not authentication — it proves the server actually parsed the handshake and prevents cache poisoning by intermediaries.
- Subprotocols: Sec-WebSocket-Protocol negotiates an application protocol (graphql-ws, mqtt, chat); the server must echo exactly one chosen value.
- Extensions: permessage-deflate negotiates compression; the server confirms which extensions it will use in its response.
- Origin checks: servers validate the Origin header against an allowlist to block cross-site WebSocket hijacking before 101 is sent.
- Failures: a non-101 response means the server declined; clients must handle redirects (3xx) and proxy errors explicitly.

## Related
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — what flows after the handshake
- [[wiki/api-protocols/websockets|WebSockets]] — the parent protocol article
- [[wiki/api-protocols/websocket-security|WebSocket Security]] — origin and key checks protect the handshake
- [[wiki/api-protocols/grpc-web|gRPC-Web]] — an HTTP-based alternative avoiding upgrades
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 101 Switching Protocols is the handshake result
