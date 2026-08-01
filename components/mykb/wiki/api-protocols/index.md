## Overview

API protocols form the backbone of the mykb web domain. Session analysis reveals a REST-first approach that expands into WebSocket for real-time features and GraphQL for complex queries.

### REST
REST is the default API architectural style. FastAPI provides automatic OpenAPI documentation. Sessions show REST endpoints for CRUD operations on entities, concept search, and graph traversal. JSON is the universal interchange format.

### GraphQL
Appears in specific contexts where client-driven queries reduce over-fetching. The session data suggests GraphQL was explored but not adopted as a primary approach — it served specific use cases.

### WebSocket
Used for real-time features in agent tool communication. The LLM wiki daemon context suggests WebSocket bridges between agent processes and the wiki server for live updates.

### HTTP Protocol
HTTP/1.1 is the baseline. Sessions show HTTP servers (SimpleHTTPRequestHandler) embedded in agents for local tool APIs, plus production Nginx configurations.

## Concepts

- [API Versioning](api-versioning.md) — API Versioning
- [Circuit Breaker](circuit-breaker.md) — Circuit Breaker
- [CQRS](cqrs.md) — CQRS
- [Event Sourcing](event-sourcing.md) — Event Sourcing
- [Exponential Backoff](exponential-backoff.md) — Exponential Backoff
- [Graceful Shutdown](graceful-shutdown.md) — Graceful Shutdown
- [GraphQL](graphql.md) — GraphQL
- [gRPC](grpc.md) — gRPC
- [Health Checks](health-checks.md) — Health Checks
- [HTTP Caching](http-caching.md) — HTTP Caching
- [Idempotency](idempotency.md) — Idempotency
- [Jitter](jitter.md) — Jitter
- [JSON Schema](json-schema.md) — JSON Schema
- [Apache Kafka](kafka.md) — Apache Kafka
- [Liveness Probes](liveness-probes.md) — Liveness Probes
- [Message Queues](message-queues.md) — Message Queues
- [OpenAPI](openapi.md) — OpenAPI
- [Protocol Buffers](protobuf.md) — Protocol Buffers
- [RabbitMQ](rabbitmq.md) — RabbitMQ
- [Rate Limiting](rate-limiting.md) — Rate Limiting
- [Readiness Probes](readiness-probes.md) — Readiness Probes
- [Redis Streams](redis-streams.md) — Redis Streams
- [REST APIs](rest-apis.md) — REST APIs
- [Retry & Backoff](retry-backoff.md) — Retry & Backoff
- [Saga Pattern](saga-pattern.md) — Saga Pattern
- [Timeouts](timeouts.md) — Timeouts
- [Webhooks](webhooks.md) — Webhooks
- [WebSockets](websockets.md) — WebSockets
