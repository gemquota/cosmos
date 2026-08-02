---
type: "concept"
title: "WebSocket Frames"
description: "Frame types, masking, and fragmentation"
tags: ["websockets", "frames", "protocols", "networking", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6455#section-5", "https://developer.mozilla.org/en-US/docs/Web/API/WebSocket"]
---

# WebSocket Frames

## Summary
After the handshake, WebSocket traffic is a sequence of frames: text, binary, close, ping, and pong. Frames carry an opcode, a payload length, optional masking, and a FIN bit that signals fragmentation — the mechanics that make the protocol bidirectional and message-oriented.

## Details
- Frame layout: FIN (1 bit), RSV bits (reserved for extensions), opcode (4 bits), mask bit, payload length (7, 16, or 64 bits), masking key, and payload.
- Opcodes: 0x1 text (UTF-8), 0x2 binary, 0x8 close, 0x9 ping, 0xA pong, and 0x0 continuation for fragmented messages.
- Masking: client-to-server frames MUST be masked with a 32-bit random key; server-to-client frames are never masked — the asymmetry stops cache-poisoning attacks.
- Fragmentation: a message can be split into one frame with FIN=0 followed by continuation frames; control frames may interleave between fragments but not data frames.
- Control frames: ping/pong keepalives measure liveness; close frames carry a status code (1000 normal, 1001 going away, 1008 policy violation) and optional reason.
- Limits: payload lengths up to 2^63-1 bytes; implementations cap message sizes to bound memory, and must close on protocol violations (for example unmasked client frames).
- Frames map to application messages: one message may be one frame or many, and libraries reassemble them transparently.

## Related
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — the upgrade that precedes framing
- [[wiki/api-protocols/websockets|WebSockets]] — the parent protocol article
- [[wiki/api-protocols/websocket-reconnection|WebSocket Reconnection]] — close codes guide reconnect decisions
- [[wiki/api-protocols/backpressure|Backpressure]] — message sizes and flow control interact
- [[wiki/api-protocols/websocket-security|WebSocket Security]] — masking and close codes are security surfaces
