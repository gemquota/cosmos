---
type: "concept"
title: "Event Sourcing Databases"
description: "Storing state as an append-only log of events"
tags: ["event-sourcing", "events", "cqrs", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/eaaDev/EventSourcing.html", "https://kafka.apache.org/documentation/"]
---

# Event Sourcing Databases

## Summary

Event sourcing persists every state change as an immutable event rather than the current state.
Current state is derived by replaying events, enabling audit trails and temporal queries.
It pairs with CQRS and stream processing for scalable, auditable systems.
Event sourcing pays off when audit, replay, and temporal queries are core requirements.

## Details

- Events are facts: immutable, timestamped, and ordered.
- Projections materialize read models from the event log.
- Rebuilding state enables new read models without new writes.
- Event stores must handle schema evolution of event shapes.
- Tradeoffs: replay cost, versioning complexity, and eventual consistency.
- Versioning events and migrations are unavoidable operational work.
- Snapshotting bounds replay cost as logs grow.
- Event-sourced systems excel where history is the product, not a byproduct.

## Related

- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — events as truth
- [[wiki/data-storage/event-sourcing-databases|Event Sourcing Databases]] — log as source
- [[wiki/data-storage/outbox-pattern-for-transactions|Outbox Pattern For Transactions]] — reliable event capture
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event platforms
- [[wiki/data-storage/kappa-architecture|Kappa Architecture]] — replay architecture
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

