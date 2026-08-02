---
type: "concept"
title: "Type Systems in Practice"
description: "Using static types to prevent errors and document intent"
tags: ["type-systems", "types", "correctness", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Type_system", "https://en.wikipedia.org/wiki/Functional_programming"]
---

# Type Systems in Practice

## Summary
A type system classifies values and operations so the compiler can reject invalid programs before they run. Practice means choosing a type discipline — sound and strict, gradual, or dynamic — and using types to express domain constraints, not just to satisfy the compiler.

## Details
- Types prevent whole classes of bugs: null dereferences, wrong shapes, and illegal operations.
- Expressiveness spectrum: enums and unions, generics, dependent-ish patterns, and refinement types encode more invariants.
- Sound types (Rust, Haskell) catch more at compile time; gradual types (TypeScript, Python type hints) scale pragmatically.
- Types are documentation that cannot drift: a well-typed signature explains itself.
- The cost is expressiveness friction and compile-time; the payoff compounds in large, long-lived codebases.
- For the mykb bundle, typed models for articles, sources, and statuses catch malformed content at build time.
- Worked example — the wiki model types ArticleStatus as a union (stub | growing | archived); the compiler rejects a typo like 'growingg' before validation even runs.

Worked example — the wiki model types ArticleStatus as a union (stub | growing | archived); the compiler rejects a typo like 'growingg' before validation even runs.

## Related
- [[wiki/software-engineering/static-analysis|Static Analysis]]
- [[wiki/software-engineering/type-systems|Type Systems]]
- [[wiki/software-engineering/functional-programming-principles|Functional Programming Principles]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/value-objects|Value Objects]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/software-engineering/null-object-pattern|Null Object Pattern]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
