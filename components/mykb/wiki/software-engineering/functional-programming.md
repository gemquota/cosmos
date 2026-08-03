---
type: "concept"
title: "Functional Programming"
description: "Paradigm that builds programs from pure functions and immutable data"
tags: ["programming", "paradigm", "fp", "immutability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Functional Programming

## Summary

Functional programming emphasizes pure functions, immutable data, and explicit data flow over mutable state and hidden side effects. It is not a language niche — its principles (purity, immutability, referential transparency) improve correctness and testability in any language.

## Details
- Mechanism: pure functions map inputs to outputs with no observable side effects, making them deterministic and testable; immutability prevents aliasing bugs (sharing a structure never means sharing mutations); higher-order functions and composition (map/filter/reduce, function combinators) replace loops and mutable accumulators; types encode structure and constraints.
- Concrete example: a reducer (state, action) => state keeps application state transitions pure and replayable (Redux, Elm); a data pipeline written as compose(validate, transform, persist) is trivially unit-tested; replacing a mutable cache with a pure function + memoization removes a whole class of race and staleness bugs.
- Failure modes: forcing purity where IO is inherent (the boundary must admit effects — discipline them, do not deny them); performance myths — immutability has costs, but structural sharing and persistent data structures mitigate them; and over-abstraction (monad stacks, point-free soup) that hurts readability.
- Operational tradeoffs: functional discipline buys predictability and testability at the cost of a learning curve and some ceremony; the pragmatic path is functional core / imperative shell — pure logic inside, effects at the edges.
- RSIS3/mykb relevance: the wiki's transformation pipelines are written as pure functions with immutable inputs, so loop experiments replay deterministically on the same data.
- Error handling: model failures as values (Option/Result) rather than exceptions where the flow is expected to branch; reserve exceptions for truly exceptional boundary failures.
- Practical adoption: start with immutability and pure helpers in the hot path of logic; full FP discipline is a language-level choice, but the principles pay off incrementally.

## Related
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]] — the contrasting mainstream paradigm
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — FP meets asynchronous event streams
- [[wiki/software-engineering/type-systems|Type Systems]] — algebraic types are FP's strength
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — unix pipes are functional composition in the shell
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — FP idioms appear in patterns like strategy and observer
