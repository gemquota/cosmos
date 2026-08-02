---
type: "concept"
title: "Adapter Pattern"
description: "Translating one interface into another so incompatible components can work together"
tags: ["adapter", "patterns", "design", "integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Adapter Pattern

## Summary
The adapter pattern wraps a component with an incompatible interface so it satisfies the interface clients expect. It is the software version of a power-plug converter, and it is the backbone of integrating third-party libraries.

## Details
- Object adapters wrap an instance and translate calls; class adapters use inheritance.
- Adapters localize incompatibility, but too many layers of translation hide behavior.
- Distinguish adapters (interface translation) from facades (subsystem simplification).
- mykb relevance: an adapter maps a raw capture format onto the article interface without touching either.

## Related
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/proxy-pattern|Proxy Pattern]]
- [[wiki/software-engineering/bridge-pattern|Bridge Pattern]]
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
