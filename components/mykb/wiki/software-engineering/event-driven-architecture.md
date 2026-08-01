---
type: "concept"
title: "Event-Driven Architecture"
description: "Software architecture built around the production, detection, and consumption of events"
tags: ["architecture", "events", "messaging", "async"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/201701-event-driven.html"]
---

# Event-Driven Architecture

## Summary
Event-driven architecture (EDA) organizes systems around events — records of something that happened — rather than around request/response calls. Producers emit events without knowing who consumes them, which decouples components, improves scalability, and makes systems reactive to change.

## Details
- An event is a fact: 'order placed', 'payment captured'. It is immutable and named in the past tense, and carries enough context for consumers to react.
- Three collaboration styles exist: event notification (a signal to fetch state), event-carried state transfer (the event contains the data), and event sourcing (events become the system of record).
- Producers and consumers are decoupled in time and space: a consumer can be down or added later without changing the producer.
- Messaging infrastructure (Kafka, RabbitMQ, Redis Streams) provides durability, ordering guarantees, and replay; ordering and exactly-once semantics remain hard problems.
- Testing shifts from request-response assertions to verifying event sequences; observability of event flows is essential.
- RSIS3 relevance: agent telemetry and memory updates are naturally event streams; mykb can treat knowledge changes as events to trigger curation.
- Worked example: order service emits OrderPlaced; inventory, billing, and analytics each subscribe and react independently.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — EDA is the dominant async collaboration style for microservices
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]] — pattern for reliably publishing events alongside database commits
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]] — competing ways to coordinate event-driven workflows
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — storing application state as an immutable event log
- [[wiki/api-protocols/message-queues|Message Queues]] — transport for decoupling producers and consumers
- [[wiki/api-protocols/kafka|Apache Kafka]] — the most common event-streaming platform
- [[wiki/data-storage/data-versioning|Data Versioning]] — events give natural version history for state
