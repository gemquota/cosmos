---
type: "concept"
title: "Repositories Pattern"
description: "An abstraction that makes data access look like an in-memory collection"
tags: ["repositories", "ddd", "persistence", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Repositories Pattern

## Summary
The repository pattern mediates between the domain and data storage, presenting persistence as a collection of aggregates you can add, find, and remove. It keeps domain code ignorant of databases and makes storage swappable.

## Details
- Repository interfaces live in the domain; implementations (SQL, files, HTTP) live outside.
- Methods are domain-flavored: findBySlug, save, remove — not generic CRUD passthrough.
- Beware the leaky repository: queries that assume SQL semantics break the abstraction.
- mykb relevance: an ArticleRepository over the file tree lets the graph use files, git, or a DB.

## Related
- [[wiki/software-engineering/unit-of-work|Unit of Work]]
- [[wiki/software-engineering/aggregates|Aggregates]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/domain-driven-design|Domain-Driven Design]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
