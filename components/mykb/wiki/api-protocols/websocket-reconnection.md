---
type: "concept"
title: "WebSocket Reconnection"
description: "Reconnect strategies and state resync"
tags: ["websockets", "reconnection", "reliability", "state-sync", "realtime"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event", "https://www.ably.com/blog/websockets-reconnect-strategies"]
---

# WebSocket Reconnection

## Summary
WebSockets drop: network blips, proxies on idle timeouts, and server restarts all kill a connection. Reconnection strategy — when to retry, how fast to back off, and how to resync state — determines whether a realtime app feels solid or flaky.

## Details
- Detect the drop: onclose fires on any close; distinguish clean close (close code 1000) from abnormal drops (1006), and treat ping timeouts as drops.
- Exponential backoff with jitter: start at ~1s, double per attempt up to a cap (30-60s), add randomness to avoid thundering herds after outages.
- Respect the server's retry hint: a close code like 1008 (policy violation) should stop reconnecting; 1012 (service restart) invites a quick retry.
- Resync state: the client must catch up on everything missed while disconnected — request a snapshot, replay events from a cursor, or refetch via REST.
- Idempotent subscribe: on reconnect, re-subscribe to topics; servers dedupe by client id or the client sends the last known event id.
- Visibility: surface connection state (connecting, open, retrying) in the UI and log reconnect counts for operations.
- Heartbeats: application-level ping/pong (or protocol-level) detects half-open connections that onclose never fires for.

## Related
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — ping/pong and close codes drive reconnection
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the retry schedule behind reconnects
- [[wiki/api-protocols/jitter|Jitter]] — randomization prevents reconnect storms
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — cursor-based resync gives no-loss catch-up
- [[wiki/api-protocols/websockets|WebSockets]] — the parent protocol article
