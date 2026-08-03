---
type: "concept"
title: "Layered Architecture"
description: "Organizing code into stacked layers with one-directional dependencies"
tags: ["layered-architecture", "architecture", "design", "structure"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Layered Architecture

## Summary

Layered architecture organizes code into horizontal strata — presentation, application/domain, and infrastructure — with dependencies pointing inward. It is the default architecture because it is simple to explain, test, and refactor; it fails when layers leak or become anemic.

## Details
- Mechanism: each layer depends only on the layer below (or on abstractions from it): UI calls application services, services orchestrate domain logic, repositories mediate infrastructure; dependency inversion lets the inner layers define interfaces that outer layers implement, keeping the core independent of frameworks and databases.
- Concrete example: a payment feature has a controller (HTTP), a service (use cases, transactions), a domain model (money, policies), and a repository (Postgres); swapping Postgres for another store changes only the repository implementation. The failure pattern: business rules leaking into controllers, SQL scattered across services, and layers that are just pass-through.
- Failure modes: dependency violations creeping in (UI touching repositories); anemic domain — layers that only shuffle data, so logic lives nowhere; circular dependencies between layers; and over-layering — five thin layers adding indirection to a CRUD app that needed two.
- Operational tradeoffs: layers give testability (mock at boundaries) and change isolation at the cost of ceremony; the standard is a clean core (domain/application) with adapters at the edges, and a rule that dependencies point inward, enforced by architecture tests.
- RSIS3/mykb relevance: the wiki's backend follows layers with a pure domain core, so loop experiments swap infrastructure (stores, APIs) without touching business rules.
- Architecture tests: enforce the dependency direction with tests (import/namespace checks) so violations fail CI instead of being discovered in code review.
- Testing strategy: unit-test the core without frameworks, integration-test through the application layer, and keep the outer adapters thin enough to swap in tests.
- Layer granularity: add layers only when they earn their keep — a presentation/service/repository split covers most services; extra layers (dto, mapper, facade) multiply mapping code without adding isolation.
- Change localization: a well-layered system lets you change storage, transport, or UI without touching domain logic; when a feature change ripples through every layer, the boundaries are misdrawn.

## Related
- [[wiki/software-engineering/onion-architecture|Onion Architecture]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/pipeline-architecture|Pipeline Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
