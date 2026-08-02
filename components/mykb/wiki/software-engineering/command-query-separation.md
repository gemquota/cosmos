---
type: "concept"
title: "Command Query Separation"
description: "The principle that a method either changes state or returns data, never both"
tags: ["cqrs", "design", "commands", "queries"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Command Query Separation

## Summary
Command-query separation (CQS) says methods either mutate state (commands, returning void) or return values (queries, changing nothing). It makes interfaces predictable and is the seed of the larger CQRS architecture.

## Details
- The rule is about method contracts: no query that mutates, no command that answers.
- Mutations with return values (pop returning the element) are pragmatic exceptions — document them.
- CQS improves testability: queries are pure functions of the state they read.
- mykb relevance: the wiki API can split write commands from read queries cleanly.

## Related
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/pure-functions|Pure Functions]]
- [[wiki/software-engineering/command-pattern|Command Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
