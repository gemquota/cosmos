---
type: "concept"
title: "Singleton Pitfalls"
description: "The problems that make the singleton pattern an anti-pattern in many systems"
tags: ["singleton", "anti-pattern", "design", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Singleton Pitfalls

## Summary

The singleton pattern (one instance, global access) is usually an anti-pattern: it hides dependencies, couples everything to global state, and makes testing and lifecycle management harder. The legitimate uses are few — genuinely process-wide resources — and even they are better as injected instances.

## Details
- Mechanism: a singleton exposes one instance via a static accessor and private constructor; the pitfalls: implicit global state (any code can read/mutate it), hidden initialization order (who constructs it first?), test pollution (state persists across tests), and lifecycle rigidity (can't be recreated, torn down, or scoped per request).
- Concrete example: a Logger singleton seems harmless until tests must capture output per-test; a Config singleton hides which module reads what; a connection-pool singleton becomes untestable when it must be faked. The fix: create one instance at the composition root and inject it — same single instance, but visible dependency.
- Failure modes: singletons that hold request-scoped state (thread safety bugs in parallel tests); initialization-order crashes (A needs B which needs A); singletons created lazily with hidden timing (first call does heavy work); and refactors that silently add state to a "constant" singleton.
- Operational tradeoffs: the singleton's convenience (no wiring) is exactly its cost (no control); the standard is dependency injection with explicit single-instance scope, reserving true singletons for immutable, side-effect-free utilities. Test by resetting or scoping state explicitly.
- RSIS3/mykb relevance: the wiki's services manage process-wide resources as injected single instances, so the loop's tests can isolate state between passes.
- Detection: a class with a static instance() or getInstance() is the smell; treat review comments about globals as a correctness issue, not style.
- Migration path: extract the instance to the composition root one consumer at a time, keeping behavior identical while the dependency becomes visible.
- Immutable singletons: constants, registries of pure functions, and stateless utilities are safe as singletons; the rule is no mutable state, no lifecycle, no hidden I/O.
- Thread-safety illusion: a "thread-safe" singleton (locks) only serializes access — it still hides contention and ordering from the code that depends on it.

## Related
- [[wiki/software-engineering/service-locator|Service Locator]]
- [[wiki/software-engineering/dependency-injection|Dependency Injection]]
- [[wiki/software-engineering/object-pool|Object Pool]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
