---
type: "concept"
title: "Backend Architecture Patterns"
description: "The recurring shapes of server-side systems and when to use them"
tags: ["backend", "architecture", "patterns", "services"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Service_(systems_architecture)", "https://en.wikipedia.org/wiki/Web_service"]
---

# Backend Architecture Patterns

## Summary
Backend architecture patterns are the recurring shapes of server-side systems — layered, hexagonal, microservices, event-driven, serverless, and CQRS among them. Each pattern is a tradeoff profile of coupling, scaling, and operational cost, and choosing one is choosing the profile you can live with.

## Details
- Layered and modular designs win for simplicity; microservices and event-driven designs win for independent scaling and ownership.
- Ports and adapters (hexagonal) keep business logic framework-free; CQRS separates reads from writes when workloads diverge.
- Event-driven backends decouple producers and consumers but trade in consistency and debugging ease.
- Serverless backends remove infrastructure management at the cost of cold starts, vendor coupling, and cost unpredictability.
- Patterns compose: a hexagonal core behind an API gateway, with an outbox feeding an event stream, is a common mature shape.
- For the mykb bundle, the backend is a small hexagonal service: ports for storage and sources, adapters for files and curl.
- Worked example — the wiki backend exposes one API, persists via a repository port, and publishes curation events through an outbox; swapping the file store for a database touches only the adapter.

Worked example — the wiki backend exposes one API, persists via a repository port, and publishes curation events through an outbox; swapping the file store for a database touches only the adapter.

## Related
- [[wiki/software-engineering/ports-and-adapters|Backend Architecture Patterns]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]]
- [[wiki/tooling/serverless-architecture|Serverless Architecture]]
- [[wiki/software-engineering/outbox-pattern|Outbox Pattern]]
- [[wiki/software-engineering/layered-architecture|Layered Architecture]]
- [[wiki/software-engineering/microkernel-architecture|Microkernel Architecture]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
