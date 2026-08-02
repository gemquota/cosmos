---
type: "concept"
title: "WebRTC in Practice"
description: "Peer-to-peer audio, video, and data channels in the browser with NAT traversal"
tags: ["webrtc", "realtime", "p2p", "media", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API", "https://webrtc.org/"]
---
# WebRTC in Practice

## Summary
WebRTC establishes encrypted peer-to-peer connections for audio, video, and arbitrary data. Signaling exchanges session descriptions over any channel (WebSocket, HTTP), while ICE/STUN/TURN punch through NATs. It powers video calls, live streaming, and P2P file and data sync.

## Details
- **Signaling** — SDP offers/answers and ICE candidates exchange over the app's channel; WebRTC itself transports media only.
- **NAT traversal** — STUN discovers public addresses; TURN relays when direct paths fail; ICE picks the best candidate pair.
- **Media** — getUserMedia captures cameras/mics; tracks flow through peer connections with codec negotiation.
- **Data channels** — ordered/unordered, reliable/unreliable modes for chat, games, and file transfer.
- **Worked example** — a peer sync mode for the mykb notes uses a WebRTC data channel after WebSocket signaling.
- **Relevance** — for RSIS3's distributed agents, WebRTC offers low-latency direct links without server relay.
- **Connection quality** — RTCPeerConnection exposes stats via getStats(): round-trip time, packet loss, and jitter; adaptive bitrate and simulcast keep calls usable on flaky links.

## Related
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — adjacent concept in this wiki
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/api-protocols/websockets|WebSockets]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
