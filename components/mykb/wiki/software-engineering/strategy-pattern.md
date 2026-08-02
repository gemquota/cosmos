---
type: "concept"
title: "Strategy Pattern"
description: "Swapping interchangeable algorithms behind a common interface"
tags: ["strategy", "patterns", "design", "polymorphism"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Strategy Pattern

## Summary
The strategy pattern defines a family of algorithms behind one interface and lets the caller choose at runtime — sorting strategies, payment providers, retry policies. It replaces conditional spaghetti with polymorphic selection.

## Details
- Interface plus concrete strategies; context delegates without knowing which strategy it holds.
- Strategies are often small pure functions or objects with a single method.
- Combine with factories to pick the strategy from configuration or context.
- mykb relevance: the wiki link-resolver can plug strategies for strict, fuzzy, or legacy link matching.

## Related
- [[wiki/software-engineering/template-method|Template Method]]
- [[wiki/software-engineering/observer-pattern|Observer Pattern]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
