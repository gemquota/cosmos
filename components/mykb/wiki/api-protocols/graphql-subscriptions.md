---
type: "concept"
title: "GraphQL Subscriptions"
description: "Realtime events and pub/sub wiring"
tags: ["graphql", "subscriptions", "realtime", "websockets", "pubsub"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/subscriptions/", "https://www.apollographql.com/docs/apollo-server/data/subscriptions/"]
---

# GraphQL Subscriptions

## Summary
GraphQL subscriptions push realtime events to clients over a persistent transport (usually WebSocket). A subscription operation registers interest in an event stream; the server publishes matching events through a pub/sub broker and delivers them as query-shaped payloads.

## Details
- Subscriptions are a third root operation type alongside query and mutation, using the same selection syntax so clients receive exactly the fields they asked for.
- Transport: most implementations run subscriptions over WebSocket (graphql-ws protocol) because HTTP request-response cannot hold a push channel.
- Server wiring: mutations or external events publish to a pub/sub broker (Redis, Kafka, or an in-process emitter); subscription resolvers subscribe and return an async iterator of events.
- Filtering: subscription arguments (for example topic: "order:42") scope events server-side; the broker must route by topic or the server filters on arrival.
- Resync: clients that reconnect miss events, so designs pair subscriptions with a query snapshot or an event cursor for catch-up.
- Scaling: subscriptions are stateful per connection, so horizontal scaling needs a shared broker plus sticky routing or broadcast fan-out.
- Use deliberately: a polling or SSE stream is often simpler; subscriptions earn their complexity for chat, notifications, and live dashboards.

## Related
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — the transport subscriptions run over
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — operations that trigger published events
- [[wiki/api-protocols/redis-streams|Redis Streams]] — a broker backing subscription fan-out
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — simpler one-way push alternative
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — events as a first-class API pattern
