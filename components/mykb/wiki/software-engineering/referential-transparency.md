---
type: "concept"
title: "Referential Transparency"
description: "The property that an expression can be replaced by its value without changing behavior"
tags: ["functional-programming", "purity", "semantics", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Referential Transparency

## Summary
An expression is referentially transparent if it can be swapped for its computed value anywhere without changing the program's behavior. It is the formal cousin of purity and the property that makes equational reasoning and substitution valid.

## Details
- Referential transparency implies determinism and no side effects for the expression.
- It enables memoization, lazy evaluation, and refactoring by substitution.
- Impure operations break it; modeling effects as values (IO monads) restores it.
- mykb relevance: transparent link-resolution functions make the wiki graph deterministic and cacheable.

## Related
- [[wiki/software-engineering/pure-functions|Pure Functions]]
- [[wiki/software-engineering/side-effect-isolation|Side Effect Isolation]]
- [[wiki/software-engineering/immutability-practice|Immutability Practice]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/pure-functions|Referential Transparency]]
