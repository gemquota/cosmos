---
type: "concept"
title: "Prototype Pattern"
description: "Creating new objects by cloning an existing prototype"
tags: ["prototype", "patterns", "design", "creation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prototype Pattern

## Summary
The prototype pattern creates objects by copying a prototype instance instead of calling constructors — useful when construction is costly or object shape varies. JavaScript's prototypal inheritance is the pattern elevated to a language model.

## Details
- Clone methods (copy, deep copy, clone) replace constructor calls; watch shallow vs deep copies.
- Prototypes shine for defaults: clone the template, then tweak a few fields.
- Cloning mutable internals is the classic bug — deep-clone or share immutable parts.
- mykb relevance: an article template cloned per task gives consistent structure with cheap variation.

## Related
- [[wiki/software-engineering/factory-pattern|Factory Pattern]]
- [[wiki/software-engineering/object-pool|Object Pool]]
- [[wiki/software-engineering/builder-pattern|Builder Pattern]]
- [[wiki/software-engineering/memento-pattern|Memento Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
