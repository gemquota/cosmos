---
type: "concept"
title: "Singleton Pitfalls"
description: "The problems that make the singleton pattern an anti-pattern in many systems"
tags: ["singleton", "anti-pattern", "design", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Singleton Pitfalls

## Summary
The singleton pattern guarantees one instance per process, but it smuggles global mutable state, hides dependencies, and breaks test isolation. Most systems are better served by dependency injection with a single configured instance.

## Details
- Global state hides coupling: every consumer silently shares the instance and its lifecycle.
- Testing suffers — singletons are hard to reset, fake, or parallelize.
- Thread-safe lazy initialization adds subtle concurrency bugs.
- Single-instance semantics are fine; enforce them via composition root, not via a global accessor.
- mykb relevance: the wiki index should be constructed once and injected, not fetched from a global.

## Related
- [[wiki/software-engineering/service-locator|Service Locator]]
- [[wiki/software-engineering/dependency-injection|Dependency Injection]]
- [[wiki/software-engineering/object-pool|Object Pool]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
