---
type: "concept"
title: "Functional Programming"
description: "Paradigm that builds programs from pure functions and immutable data"
tags: ["programming", "paradigm", "fp", "immutability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Functional Programming

## Summary
Functional programming (FP) emphasizes pure functions — deterministic, side-effect-free computations — and immutable data. Purity makes code easy to test, reason about, and parallelize.

## Details
- Pure functions plus explicit data flow replace hidden state; monads and effects handle I/O.
- FP ideas (map, filter, reduce, immutability) have spread into mainstream languages.
- RSIS3 relevance: prompt pipelines are naturally expressed as function compositions.

## Related
- [[wiki/software-engineering/object-oriented-programming|Object-Oriented Programming]] — the contrasting mainstream paradigm
- [[wiki/software-engineering/reactive-programming|Reactive Programming]] — FP meets asynchronous event streams
- [[wiki/software-engineering/type-systems|Type Systems]] — algebraic types are FP's strength
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — unix pipes are functional composition in the shell
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — FP idioms appear in patterns like strategy and observer
