---
type: "concept"
title: "CQRS Pattern"
description: "Separating the command (write) model from the query (read) model"
tags: ["cqrs", "architecture", "read-model", "write-model"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CQRS.html", "https://en.wikipedia.org/wiki/Eventual_consistency"]
---

# CQRS Pattern

## Summary
Command Query Responsibility Segregation splits the model that processes commands (writes) from the model that answers queries (reads). When reads and writes have different shapes or scales, separate models let each optimize independently — synced by events when fully split.

## Details
- CQS is the method-level seed; CQRS applies the split at the model and storage level.
- Partial CQRS keeps one store but separates services; full CQRS uses separate stores with event sync.
- Read models are projections — denormalized for query shapes, rebuildable from the event stream.
- The tax is eventual consistency: writes and reads can disagree briefly, and the gap must be designed for.
- CQRS pays off when read/write asymmetry is real: complex writes, huge read volumes, or divergent shapes.
- For the mykb bundle, wiki writes are rare and reads are constant — a natural CQRS profile with a search read model.
- Worked example — the wiki writes articles via commands; a projection builds a search index read model from published events, so search never touches the write store.

Worked example — the wiki writes articles via commands; a projection builds a search index read model from published events, so search never touches the write store.

## Related
- [[wiki/software-engineering/command-query-separation|Command Query Separation]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/software-engineering/read-models|CQRS Pattern]]
- [[wiki/software-engineering/event-sourcing-practice|Event Sourcing Practice]]
- [[wiki/compositions/backend-architecture-patterns|Backend Architecture Patterns]]
- [[wiki/api-protocols/cqrs|CQRS]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
