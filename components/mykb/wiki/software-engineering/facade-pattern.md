---
type: "concept"
title: "Facade Pattern"
description: "A simple interface that hides a complex subsystem"
tags: ["facade", "patterns", "design", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Facade Pattern

## Summary
The facade pattern provides one simple entry point over a messy subsystem, hiding internal classes and call sequences. It reduces coupling between clients and subsystems and gives the subsystem a place to evolve.

## Details
- Facades are not abstract: they expose a simplified, intent-shaped API over real components.
- They pair with repositories or services as the public surface of a module.
- Avoid facades that leak internals or become god objects over everything.
- mykb relevance: the wiki CLI facade wraps reading, linking, and writing behind one command.

## Related
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/mediator-pattern|Mediator Pattern]]
- [[wiki/software-engineering/ports-and-adapters|Ports and Adapters]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
