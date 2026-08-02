---
type: "concept"
title: "Template Method"
description: "Defining an algorithm's skeleton and letting subclasses fill in steps"
tags: ["template-method", "patterns", "design", "inheritance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Template Method

## Summary
The template method fixes an algorithm's overall structure in a base class and defers specific steps to subclasses via overridable hooks. It is the inheritance-based cousin of the strategy pattern, with the inversion: the base controls the flow.

## Details
- Hooks and abstract steps keep the invariant skeleton while varying details.
- Beware the fragile base class: every override tightens coupling to the template's order.
- Prefer composition (strategy) when steps vary independently; template method suits fixed choreographies.
- mykb relevance: an article-generation template method would fix section order while varying content sources.

## Related
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/object-oriented-principles|Object-Oriented Principles]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/software-engineering/factory-pattern|Factory Pattern]]
