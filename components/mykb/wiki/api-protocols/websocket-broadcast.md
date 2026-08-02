---
type: "concept"
title: "WebSocket Broadcast"
description: "Room and topic fan-out design"
tags: ["websockets", "broadcast", "pubsub", "rooms", "scaling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://socket.io/docs/v4/rooms/", "https://www.ably.com/topic/websockets"]
---

# WebSocket Broadcast

## Summary
WebSocket broadcast fans one incoming message out to many connected clients — chat rooms, presence updates, and live dashboards. The design question is where fan-out happens: in-process for a single instance, or through a shared pub/sub bus so every instance delivers to its own clients.

## Details
- Room model: clients join named rooms (channel:42, user:7); the server tracks membership per connection and broadcasts to all members of a room.
- Single instance: an in-memory Map<room, Set<conn>> suffices; delivery is synchronous within the process.
- Multiple instances: the receiving instance publishes to a broker (Redis Pub/Sub, Redis Streams, Kafka, NATS); every instance subscribes and delivers to its local members.
- Membership state must be shared too: presence (who is online) needs a shared store (Redis sets with TTL) so any instance can answer.
- Delivery guarantees: broadcasts are usually at-most-once — add message ids and client-side dedup for at-least-once.
- Backpressure: a slow consumer should not block the room; buffer per connection with a cap, then disconnect or drop, rather than unbounded queues.
- Scale cues: >1 instance, sticky sessions, or cross-region rooms are the point where a broker becomes mandatory.

## Related
- [[wiki/api-protocols/websockets|WebSockets]] — the transport broadcasts run over
- [[wiki/devops-infra/pub-sub-messaging|Pub/Sub Messaging]] — the broker pattern behind fan-out
- [[wiki/api-protocols/redis-streams|Redis Streams]] — a shared bus for cross-instance delivery
- [[wiki/api-protocols/backpressure|Backpressure]] — per-connection flow control in broadcast
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — dedup for reliable broadcast
