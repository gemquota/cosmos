---
type: "concept"
title: "Bridge Pattern"
description: "Decoupling an abstraction from its implementation so both can vary independently"
tags: ["bridge", "patterns", "design", "abstraction"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Bridge Pattern

## Summary
The bridge pattern separates an abstraction (what a thing does) from its implementation (how it does it), letting both evolve independently. It replaces combinatorial subclass explosion with two orthogonal hierarchies.

## Details
- Abstraction holds a reference to an implementation interface — the bridge.
- Use when you multiply dimensions: shapes x renderers, windows x platforms.
- Distinguish from adapter (makes interfaces fit) — bridge separates variation axes.
- mykb relevance: article rendering abstraction bridged to markdown, HTML, and JSON backends.

## Related
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
