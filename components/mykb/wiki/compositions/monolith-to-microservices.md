---
type: "concept"
title: "Monolith to Microservices"
description: "Incrementally splitting a monolithic application into services"
tags: ["microservices", "migration", "architecture", "strangler"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/articles/microservices.html", "https://en.wikipedia.org/wiki/Microservices"]
---

# Monolith to Microservices

## Summary
Moving from monolith to microservices is an incremental decomposition — extract bounded contexts, split databases, and strangler traffic module by module. It is a migration of operational complexity as much as code, and it should only be done when the monolith's constraints are actually binding.

## Details
- Start from seams: bounded contexts and module boundaries already present in the monolith are the extraction candidates.
- The strangler pattern routes new requests to extracted services while the monolith keeps serving the rest.
- Split data last: shared databases couple services even when code is separated; database extraction is the hard phase.
- Each extraction needs its own observability, deployment path, and rollback plan — services add ops cost per unit.
- Anti-pattern: microservices as organizational theater, splitting by team boundary rather than business capability.
- Monoliths are a legitimate end state; modular monoliths capture most benefits with less distributed complexity.
- For the mykb bundle, the pipeline's stages (capture, curate, publish) are natural extraction candidates if scale demands it.

Worked example — the wiki platform splits in three moves: extract link-verification as a service behind an API, move its data into a dedicated store, then strangler remaining callers off the monolith module.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]]
- [[wiki/software-engineering/legacy-code-strategies|Legacy Code Strategies]]
- [[wiki/compositions/strangler-pattern|Strangler Pattern]]
- [[wiki/compositions/backend-architecture-patterns|Backend Architecture Patterns]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/software-engineering/modular-monoliths|Modular Monoliths]]
- [[wiki/software-engineering/event-driven-design|Event-Driven Design]]
