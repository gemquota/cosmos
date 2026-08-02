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

- [API Analytics](api-analytics.md) — API Analytics
- [API Authentication Methods](api-authentication-methods.md) — API Authentication Methods
- [API Backward Compatibility](api-backward-compatibility.md) — API Backward Compatibility
- [API Deprecation](api-deprecation.md) — API Deprecation
- [Design-First APIs](api-design-first.md) — Design-First APIs
- [API Gateway](api-gateway.md) — API Gateway
- [API Keys](api-keys.md) — API Keys
- [API Versioning](api-versioning.md) — API Versioning
- [AsyncAPI](asyncapi.md) — AsyncAPI
- [At-Least-Once Delivery](at-least-once-delivery.md) — At-Least-Once Delivery
- [Backend for Frontend](backend-for-frontend.md) — Backend for Frontend
- [Backpressure](backpressure.md) — Backpressure
- [Basic Authentication](basic-authentication.md) — Basic Authentication
- [Bulkhead Pattern](bulkhead-pattern.md) — Bulkhead Pattern
- [Chunked Transfer Encoding](chunked-transfer-encoding.md) — Chunked Transfer Encoding
- [Circuit Breaker](circuit-breaker.md) — Circuit Breaker
- [Concurrency Limits](concurrency-limits.md) — Concurrency Limits
- [Content Negotiation](content-negotiation.md) — Content Negotiation
- [Contract Testing](contract-testing.md) — Contract Testing
- [CORS](cors.md) — CORS
- [CQRS](cqrs.md) — CQRS
- [CSRF](csrf.md) — CSRF
- [Cursor Pagination](cursor-pagination.md) — Cursor Pagination
- [Deadline Propagation](deadline-propagation.md) — Deadline Propagation
- [DNS Load Balancing](dns-load-balancing.md) — DNS Load Balancing
- [DNS SRV Records](dns-srv-records.md) — DNS SRV Records
- [Error Contract Design](error-contract-design.md) — Error Contract Design
- [Event-Driven APIs](event-driven-apis.md) — Event-Driven APIs
- [Event Sourcing](event-sourcing.md) — Event Sourcing
- [Exponential Backoff](exponential-backoff.md) — Exponential Backoff
- [Graceful Shutdown](graceful-shutdown.md) — Graceful Shutdown
- [GraphQL Connections](graphql-connections.md) — GraphQL Connections
- [GraphQL Error Handling](graphql-error-handling.md) — GraphQL Error Handling
- [GraphQL Federation](graphql-federation.md) — GraphQL Federation
- [GraphQL Fragments](graphql-fragments.md) — GraphQL Fragments
- [GraphQL N+1 Problem](graphql-n-plus-one.md) — GraphQL N+1 Problem
- [GraphQL Queries & Mutations](graphql-queries-mutations.md) — GraphQL Queries & Mutations
- [GraphQL Resolvers](graphql-resolvers.md) — GraphQL Resolvers
- [GraphQL Schema Design](graphql-schema-design.md) — GraphQL Schema Design
- [GraphQL Security](graphql-security.md) — GraphQL Security
- [GraphQL Subscriptions](graphql-subscriptions.md) — GraphQL Subscriptions
- [GraphQL](graphql.md) — GraphQL
- [gRPC Deadlines](grpc-deadlines.md) — gRPC Deadlines
- [gRPC Gateway](grpc-gateway.md) — gRPC Gateway
- [gRPC Interceptors](grpc-interceptors.md) — gRPC Interceptors
- [gRPC Load Balancing](grpc-load-balancing.md) — gRPC Load Balancing
- [gRPC Metadata](grpc-metadata.md) — gRPC Metadata
- [gRPC Status Codes](grpc-status-codes.md) — gRPC Status Codes
- [gRPC Streaming](grpc-streaming.md) — gRPC Streaming
- [gRPC-Web](grpc-web.md) — gRPC-Web
- [gRPC](grpc.md) — gRPC
- [HATEOAS](hateoas.md) — HATEOAS
- [Health Checks](health-checks.md) — Health Checks
- [HPACK](hpack.md) — HPACK
- [HTTP Caching](http-caching.md) — HTTP Caching
- [HTTP Compression](http-compression.md) — HTTP Compression
- [HTTP Conditional Requests](http-conditional-requests.md) — HTTP Conditional Requests
- [HTTP Cookies](http-cookies.md) — HTTP Cookies
- [HTTP Headers](http-headers.md) — HTTP Headers
- [HTTP Keep-Alive](http-keep-alive.md) — HTTP Keep-Alive
- [HTTP Methods](http-methods.md) — HTTP Methods
- [HTTP Status Codes](http-status-codes.md) — HTTP Status Codes
- [HTTP/2 Flow Control](http2-flow-control.md) — HTTP/2 Flow Control
- [HTTP/2](http2.md) — HTTP/2
- [HTTP/3](http3.md) — HTTP/3
- [Idempotency Keys](idempotency-keys.md) — Idempotency Keys
- [Idempotency](idempotency.md) — Idempotency
- [Jitter](jitter.md) — Jitter
- [JSON:API](json-api-spec.md) — JSON:API
- [JSON Patch](json-patch.md) — JSON Patch
- [JSON-RPC](json-rpc.md) — JSON-RPC
- [JSON Schema](json-schema.md) — JSON Schema
- [JWT](json-web-tokens.md) — JWT
- [Apache Kafka](kafka.md) — Apache Kafka
- [Keyset Pagination](keyset-pagination.md) — Keyset Pagination
- [Liveness Probes](liveness-probes.md) — Liveness Probes
- [Load Balancing](load-balancing.md) — Load Balancing
- [Load Shedding](load-shedding.md) — Load Shedding
- [Media Type Versioning](media-type-versioning.md) — Media Type Versioning
- [Message Queues](message-queues.md) — Message Queues
- [MQTT](mqtt.md) — MQTT
- [mTLS](mtls.md) — mTLS
- [NDJSON Streaming](ndjson-streaming.md) — NDJSON Streaming
- [Authorization Code Flow](oauth2-authorization-code.md) — Authorization Code Flow
- [Client Credentials](oauth2-client-credentials.md) — Client Credentials
- [PKCE](oauth2-pkce.md) — PKCE
- [Refresh Tokens](oauth2-refresh-tokens.md) — Refresh Tokens
- [OAuth Scopes](oauth2-scopes.md) — OAuth Scopes
- [OAuth 2.0](oauth2.md) — OAuth 2.0
- [Offset Pagination](offset-pagination.md) — Offset Pagination
- [OpenAPI](openapi.md) — OpenAPI
- [OpenID Connect](openid-connect.md) — OpenID Connect
- [Optimistic Concurrency](optimistic-concurrency.md) — Optimistic Concurrency
- [Problem Details](problem-details.md) — Problem Details
- [Protocol Buffers](protobuf.md) — Protocol Buffers
- [QUIC](quic.md) — QUIC
- [RabbitMQ](rabbitmq.md) — RabbitMQ
- [Rate Limit Algorithms](rate-limit-algorithms.md) — Rate Limit Algorithms
- [Rate Limit Headers](rate-limit-headers.md) — Rate Limit Headers
- [Rate Limiting](rate-limiting.md) — Rate Limiting
- [Readiness Probes](readiness-probes.md) — Readiness Probes
- [Redis Streams](redis-streams.md) — Redis Streams
- [Response Envelopes](response-envelopes.md) — Response Envelopes
- [REST APIs](rest-apis.md) — REST APIs
- [REST Maturity Model](rest-maturity-model.md) — REST Maturity Model
- [REST Non-CRUD Actions](rest-non-crud-actions.md) — REST Non-CRUD Actions
- [REST Partial Updates](rest-partial-updates.md) — REST Partial Updates
- [REST Query Parameters](rest-query-parameters.md) — REST Query Parameters
- [REST Resource Design](rest-resource-design.md) — REST Resource Design
- [Retry & Backoff](retry-backoff.md) — Retry & Backoff
- [Retry Policies](retry-policies.md) — Retry Policies
- [RPC Styles](rpc-styles.md) — RPC Styles
- [Saga Pattern](saga-pattern.md) — Saga Pattern
- [SDK Generation](sdk-generation.md) — SDK Generation
- [SemVer for APIs](semver-for-apis.md) — SemVer for APIs
- [Server-Sent Events](server-sent-events.md) — Server-Sent Events
- [Service Mesh](service-mesh.md) — Service Mesh
- [Streaming APIs](streaming-apis.md) — Streaming APIs
- [Timeouts](timeouts.md) — Timeouts
- [TLS Certificates](tls-certificates.md) — TLS Certificates
- [TLS Handshake](tls-handshake.md) — TLS Handshake
- [Webhooks](webhooks.md) — Webhooks
- [WebSocket Broadcast](websocket-broadcast.md) — WebSocket Broadcast
- [WebSocket Frames](websocket-frames.md) — WebSocket Frames
- [WebSocket Handshake](websocket-handshake.md) — WebSocket Handshake
- [WebSocket Reconnection](websocket-reconnection.md) — WebSocket Reconnection
- [WebSocket Security](websocket-security.md) — WebSocket Security
- [WebSockets](websockets.md) — WebSockets
