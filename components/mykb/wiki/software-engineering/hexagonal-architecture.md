---
type: "concept"
title: "Hexagonal Architecture"
description: "Ports-and-adapters style that isolates the application core from external technologies"
tags: ["architecture", "ports-and-adapters", "ddd", "testability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://alistair.cockburn.us/hexagonal-architecture/"]
---

# Hexagonal Architecture

## Summary
Hexagonal architecture, also called ports and adapters, was proposed by Alistair Cockburn to isolate the application's business logic from the technologies around it. The core exposes ports — interfaces — and adapters translate between those ports and the outside world, whether a database, an HTTP API, or a CLI.

## Details
- The domain core knows nothing about frameworks: it defines use cases and domain rules, and depends only on its own ports.
- Ports are interfaces on the core's boundary: driving ports (what the application offers, e.g. a payment use case) and driven ports (what the application needs, e.g. a payment gateway).
- Adapters live outside the core: a REST controller, a message listener, a Postgres repository, or a test double all implement the same port.
- The dependency rule is inwards: outer layers depend on ports, never on concrete adapters, which keeps the core framework-free and swappable.
- Testing improves dramatically: the core is exercised against fake adapters at high speed, while real adapters get their own thin integration tests.
- RSIS3 relevance: mykb's memory client can implement a driven port for persistence, letting RSIS3 swap storage backends without touching agent logic.
- Comparison: hexagonal and clean architecture share the same inward dependency rule; hexagonal is the older, more technology-neutral formulation.

## Related
- [[wiki/software-engineering/clean-architecture|Clean Architecture]] — refines the same inward dependency rule with concentric layers
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — supplies the tactical patterns that live inside the core
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — the wiring technique that connects adapters to ports
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]] — the principle hexagonal architecture embodies
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — fake adapters make core tests fast and focused
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — how ports and adapters relate to classic design patterns
- [[wiki/concepts/triad-architecture|Triad Architecture]] — RSIS3's own layered structure follows the same boundary discipline
