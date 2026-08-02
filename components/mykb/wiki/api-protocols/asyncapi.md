---
type: "concept"
title: "AsyncAPI"
description: "Spec for event-driven API contracts"
tags: ["asyncapi", "event-driven", "specification", "contracts", "documentation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.asyncapi.com/docs/reference/specification/latest", "https://www.asyncapi.com/docs/tutorials/getting-started/hello-world"]
---

# AsyncAPI

## Summary
AsyncAPI is the specification for describing event-driven and message-based APIs: channels, operations, message schemas, and brokers, expressed in YAML/JSON. It plays the role OpenAPI plays for REST — a machine-readable contract that drives codegen, documentation, validation, and tooling for Kafka, MQTT, AMQP, and WebSocket systems.

## Details
- Structure: asyncapi version, info, servers (broker endpoints), channels (topics/queues), operations (publish/subscribe), and components (message schemas).
- Channels are the resource analog: each channel has publish and subscribe operations with message payloads (usually JSON Schema).
- Servers: protocol (kafka, mqtt, amqp, ws, http), security (SASL, TLS, API keys), and connection bindings.
- Tooling: generators emit client/server stubs, docs (like AsyncAPI Studio), schema validators, and broker configuration.
- Contract testing: message schemas become the shared contract for producers and consumers, catching drift before production.
- Relationship to OpenAPI: AsyncAPI complements it for async surfaces; the two share tooling conventions but are separate specs.
- Adoption: widely used with Kafka ecosystems and IoT; versioning follows semver for the spec itself.

## Related
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — the pattern AsyncAPI describes
- [[wiki/api-protocols/openapi|OpenAPI]] — the REST-spec sibling
- [[wiki/api-protocols/mqtt|MQTT]] — a protocol AsyncAPI models as channels
- [[wiki/api-protocols/contract-testing|Contract Testing]] — schemas as the testable contract
- [[wiki/api-protocols/json-schema|JSON Schema]] — message payload validation
