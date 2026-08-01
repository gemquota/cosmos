---
type: "concept"
title: "Clean Architecture"
description: "Layering scheme that keeps business rules independent of frameworks, UI, and infrastructure"
tags: ["architecture", "layers", "dependency-rule", "ddd"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html"]
---

# Clean Architecture

## Summary
Clean Architecture, popularized by Robert C. Martin, organizes software into concentric layers — entities, use cases, interface adapters, and frameworks — with the dependency rule pointing inward. Business rules sit at the center and never depend on frameworks, databases, or the UI.

## Details
- The dependency rule: source code dependencies point only inward, so inner layers know nothing about outer layers' implementation details.
- Entities encapsulate enterprise-wide business rules; use cases contain application-specific rules and orchestrate entities; adapters translate data between layers; frameworks and drivers sit outermost.
- The center defines its own data structures; a use case does not receive a database row or an HTTP request object — it receives plain domain input.
- Crossing boundaries: use cases define interfaces that outer adapters implement, so swapping Postgres for SQLite or adding a CLI requires no core change.
- Common mistakes: over-layering small systems, leaking framework types inward, and letting the data model dictate the domain model.
- Criticism: the style adds indirection; for small tools or scripts the ceremony outweighs the benefit.
- RSIS3 relevance: agent planning logic is the inner core of mykb; persisting wiki state should be an outer detail that the core never sees.

## Related
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — the ports-and-adapters predecessor with the same dependency rule
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — the tactical modeling vocabulary for the inner layers
- [[wiki/software-engineering/technical-debt|Technical Debt]] — unmanaged boundary leaks accumulate as debt
- [[wiki/software-engineering/code-review|Code Review]] — the guard that keeps layers honest in practice
- [[wiki/devops-infra/feature-flags|Feature Flags]] — outer-layer switches that should not leak into the core
- [[wiki/concepts/cognitive-load|Cognitive Load]] — layers reduce the cognitive load of each change
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — wires adapters into the core without leaking technology
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — plain portable data keeps the core independent of wiki tooling
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]] — the dependency rule is IoC applied to layers
