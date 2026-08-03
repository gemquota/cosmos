---
type: "concept"
title: "Modular Monoliths"
description: "A single deployable application whose internal modules follow strong boundaries"
tags: ["architecture", "monolith", "modularity", "ddd"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Modular Monoliths

## Summary

A modular monolith is one deployable unit with strongly separated internal modules and explicit boundaries — the benefits of microservices (decoupled teams, clear contracts) without the distributed-systems tax. It is increasingly the default starting architecture.

## Details
- Mechanism: modules own their data (no cross-module table sharing), expose public APIs (interfaces/events), and communicate through those contracts only; boundaries are enforced by code structure, tests, and tooling (ArchUnit, dependency checks); the whole is one deployment, so transactions, debugging, and versioning stay simple.
- Concrete example: an e-commerce monolith with catalog, cart, order, and billing modules, each owning its tables and exposing a service interface; teams own modules and meet at the module contract; when billing needs isolation later, its module extracts into a service with its API already in place.
- Failure modes: boundaries that erode (a module reaching into another's tables) — the silent path to spaghetti; modules that become hidden services (event flows inside the monolith that need orchestration); and premature extraction — splitting before contracts are stable, paying distributed costs for no benefit.
- Operational tradeoffs: modular monoliths give team autonomy and change isolation at deployment simplicity; the trade is that scale (independent scaling, deploy isolation) eventually favors services. Start modular, extract deliberately, and keep the boundary tooling from day one.
- RSIS3/mykb relevance: the wiki's backend would be a modular monolith with module APIs; the loop's service-extraction proposals must justify leaving this architecture.
- Boundary enforcement: use dependency-analysis tooling in CI and a lightweight module manifest so accidental cross-module imports fail the build.
- Extraction readiness: keep module APIs synchronous-callable and independently testable; an API that is already clean is trivial to extract when scale demands it.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — the distributed alternative a modular monolith can graduate to
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]] — bounded contexts define the modules
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — ports and adapters enforce module boundaries
- [[wiki/software-engineering/technical-debt|Technical Debt]] — weak boundaries turn modules into a big ball of mud
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — module boundaries are realized with design patterns
