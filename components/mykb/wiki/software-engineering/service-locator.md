---
type: "concept"
title: "Service Locator"
description: "A central registry that hands out dependencies on request"
tags: ["di", "patterns", "service-locator", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Service Locator

## Summary
The service locator pattern provides a registry that returns dependencies on demand, decoupling clients from construction details. It is widely criticized because it hides dependencies and makes testing harder; dependency injection is usually preferred.

## Details
- Clients pull from the locator (container.Get<Thing>) instead of receiving dependencies explicitly.
- Hidden dependencies: a service's needs are not visible in its signature, complicating tests and analysis.
- It can degenerate into a global mutable registry — the anti-pattern core.
- mykb relevance: prefer constructor injection in the wiki pipeline so each stage's needs are explicit.

## Related
- [[wiki/software-engineering/dependency-injection|Dependency Injection]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/factory-pattern|Factory Pattern]]
- [[wiki/software-engineering/singleton-pitfalls|Singleton Pitfalls]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
