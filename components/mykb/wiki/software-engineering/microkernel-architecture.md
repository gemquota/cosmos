---
type: "concept"
title: "Microkernel Architecture"
description: "A minimal core with pluggable extensions"
tags: ["microkernel", "architecture", "plugins", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Microkernel Architecture

## Summary
The microkernel (plugin) architecture keeps a small, stable core of essential functions and grows features through pluggable extensions. IDEs, browsers, and operating systems use it — the core is hard to change, plugins are easy to add.

## Details
- Core defines extension points (interfaces, registries); plugins implement and register themselves.
- Versioning and plugin isolation are the hard parts: one bad plugin must not break the core.
- Plugin markets create ecosystem dynamics — the community dimension of this architecture.
- mykb relevance: the wiki core can host source-format and lint plugins without forking.

## Related
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]]
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/modular-monoliths|Modular Monoliths]]
- [[wiki/software-engineering/mediator-pattern|Mediator Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
