---
type: "concept"
title: "Modular Monoliths"
description: "A single deployable application whose internal modules follow strong boundaries"
tags: ["architecture", "monolith", "modularity", "ddd"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Modular Monoliths

## Summary
A modular monolith is one deployable unit built from well-separated modules, each owning its data and exposing a clear interface. It offers many of the maintainability benefits of microservices without distributed-systems costs.

## Details
- Modules mirror bounded contexts; communication happens through in-process interfaces, not network calls.
- It can be split into services later if scale demands, so it is a good starting architecture.
- RSIS3 relevance: cosmos keeps code and wiki as one repo; modular boundaries keep the parts independent.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — the distributed alternative a modular monolith can graduate to
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — bounded contexts define the modules
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — ports and adapters enforce module boundaries
- [[wiki/software-engineering/technical-debt|Technical Debt]] — weak boundaries turn modules into a big ball of mud
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — module boundaries are realized with design patterns
