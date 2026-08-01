---
type: "concept"
title: "Domain-Driven Design"
description: "Approach to modeling software around the business domain and its language, contexts, and rules"
tags: ["ddd", "modeling", "bounded-context", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/DomainDrivenDesign.html"]
---

# Domain-Driven Design

## Summary
Domain-driven design (DDD) is an approach by Eric Evans for building software whose model reflects the business domain. It pairs strategic tools — bounded contexts and context maps — with tactical patterns like aggregates, entities, and value objects, all expressed in a shared ubiquitous language.

## Details
- Ubiquitous language: the domain model and the code share one vocabulary, so developers and domain experts mean the same thing when they say 'order' or 'refund'.
- Bounded contexts are explicit boundaries where a model applies; the same word can mean different things in different contexts, and context maps document the translations between them.
- Tactical building blocks: entities have identity, value objects have no identity, aggregates enforce invariants, repositories retrieve aggregates, and domain services express operations that fit no single entity.
- Strategic design pays off most: teams that skip bounded contexts end up with a god model that no one owns.
- DDD pairs naturally with microservices (one service per bounded context) and with event-driven designs (domain events communicate across contexts).
- RSIS3 relevance: mykb is a knowledge domain in itself; 'memory', 'session', and 'article' are concepts that deserve explicit bounded contexts and invariants.
- Sources: Evans' blue book (2003) and Fowler's bliki article anchor the terminology used here.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — bounded contexts are the natural service boundaries
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — domain events are how contexts communicate
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — the style that protects the domain core
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — captures DDD boundary decisions
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — tactical DDD patterns relate to classic design patterns
- [[wiki/api-protocols/cqrs|CQRS]] — a read/write split often used inside bounded contexts
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — a domain model expressed as nodes and edges
- [[wiki/software-engineering/modular-monoliths|Modular Monoliths]] — bounded contexts as internal modules with strong boundaries
