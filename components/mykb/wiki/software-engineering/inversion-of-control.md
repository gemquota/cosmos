---
type: "concept"
title: "Inversion of Control"
description: "Design principle where a framework or container controls the flow and calls user code, not the reverse"
tags: ["design", "ioc", "frameworks", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Inversion of Control

## Summary

Inversion of control (IoC) flips who drives the flow: instead of your code calling a framework, the framework calls your code (Hollywood principle). It is the foundation of frameworks, dependency injection, event loops, and callbacks — and the source of "it works until you need to know who called what" confusion.

## Details
- Mechanism: the container/framework owns the control flow and invokes your registered components at the right time (routing, lifecycle hooks, event dispatch); your code expresses what it needs (dependencies, callbacks) and the framework supplies it. DI is the most visible form (constructor injection); IoC containers manage wiring and lifecycle; event-driven and test frameworks are IoC too.
- Concrete example: a web framework calls your controller when a route matches — you do not write the server loop; a DI container constructs your service graph and injects dependencies; a test runner discovers and calls your test functions. The anti-pattern: hidden magic — flow that cannot be traced because the container's call order is undocumented.
- Failure modes: IoC containers making control flow opaque (debugging "who constructed this when"); over-use — a container where a factory function would do; framework lock-in when the IoC model leaks into domain code; and lifecycle surprises (singletons, disposals) that frameworks decide for you.
- Operational tradeoffs: IoC buys extensibility, testability, and separation of concerns; it costs indirection and debugging difficulty. The discipline is explicit composition roots, documented hooks, and keeping domain code framework-agnostic.
- RSIS3/mykb relevance: the wiki's service layer uses an explicit composition root with documented hooks, so the loop's instrumentation can intercept without fighting framework magic.
- Debuggability: log composition (what was constructed, in what order) at startup in debug mode; the container's wiring is the least-obvious part of the system and the first place to instrument.
- Convention vs explicitness: prefer explicit registration and configuration over convention-based discovery; magic that infers wiring from names is the main source of IoC confusion.

## Related
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — the most common concrete IoC technique
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — ports invert dependency direction
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the runtime loop that calls agent hooks
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — template method is a classic IoC pattern
