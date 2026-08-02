---
type: "concept"
title: "Ports and Adapters"
description: "Isolating the core from the outside world via interfaces (ports) and implementations (adapters)"
tags: ["ports-and-adapters", "architecture", "hexagonal", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Ports and Adapters

## Summary
Ports and adapters (hexagonal architecture) draws a boundary: the application core defines ports — interfaces it needs — and adapters implement them for real infrastructure. Databases, UIs, and APIs become swappable peripherals.

## Details
- Driving adapters call in (web, CLI, tests); driven adapters are called out to (DB, mail, HTTP).
- The core knows nothing about frameworks; adapters translate between worlds.
- Testability is the payoff: swap a real adapter for a fake in tests.
- mykb relevance: the wiki core defines ports for storage and sources; files and curl are adapters.

## Related
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/repositories-pattern|Repositories Pattern]]
- [[wiki/software-engineering/clean-architecture|Clean Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
