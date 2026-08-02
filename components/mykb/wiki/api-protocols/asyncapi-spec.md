---
type: "concept"
title: "AsyncAPI Specification"
description: "The OpenAPI counterpart for event-driven and message-based APIs"
tags: ["asyncapi", "events", "specification", "messaging", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.asyncapi.com/docs", "https://www.asyncapi.com/docs/reference/specification/v3.0.0"]
---
# AsyncAPI Specification

## Summary
AsyncAPI describes event-driven APIs: channels, messages, brokers, and bindings, the way OpenAPI describes HTTP endpoints. It covers Kafka, MQTT, WebSockets, and AMQP backends. Teams use it to document event schemas, generate code, and validate message contracts.

## Details
- **Document anatomy** — info, servers (brokers), channels with subscribe/publish operations, messages with payload schemas, and bindings for protocol specifics.
- **Message contracts** — payload and headers are JSON Schema; correlation and reply patterns model request-response over events.
- **Tooling** — generators emit publish/subscribe code, mock event streams, and documentation; validators gate schema changes.
- **Use cases** — event catalogs, onboarding for new consumers, and change impact analysis when schemas evolve.
- **Worked example** — the mykb pulse bus documents its topics in AsyncAPI so new workers know payload shapes without reading source.
- **Relevance** — RSIS3's event-driven loops benefit from a machine-readable contract for every channel.

## Related
- [[wiki/api-protocols/webhook-topics|Webhook Topics]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/asyncapi|AsyncAPI]] — existing coverage
- [[wiki/api-protocols/event-driven-apis|Event-Driven APIs]] — existing coverage
- [[wiki/api-protocols/message-queues|Message Queues]] — existing coverage
