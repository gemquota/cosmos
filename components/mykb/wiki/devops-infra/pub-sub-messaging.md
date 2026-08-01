---
type: "concept"
title: "Pub/Sub Messaging"
description: "Publish-subscribe messaging where publishers broadcast to many independent subscribers"
tags: ["pubsub", "messaging", "events", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Pub/Sub Messaging

## Summary
Pub/sub decouples publishers from subscribers: a message is published to a topic and every interested subscriber receives it. It is the backbone of event-driven integrations.

## Details
- Topics are the abstraction; subscribers get their own delivery offset/state.
- Semantics: at-least-once delivery is typical, so consumers must be idempotent.
- Scale and fan-out come free, but ordering guarantees vary by broker.
- Open question: how to evolve topic schemas without breaking subscribers.

## Related
- [[wiki/devops-infra/message-broker-patterns|Message Broker Patterns]] — the family pub/sub belongs to
- [[wiki/devops-infra/event-streaming|Event Streaming]] — the durable log variant
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]] — subscribers as functions
- [[wiki/api-protocols/kafka|Apache Kafka]] — pub/sub at scale
