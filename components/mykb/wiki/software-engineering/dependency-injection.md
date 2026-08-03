---
type: "concept"
title: "Dependency Injection"
description: "Technique for supplying an object with its dependencies from outside rather than constructing them internally"
tags: ["design", "testing", "ioc", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Dependency Injection

## Summary

Dependency injection (DI) supplies an object's dependencies from outside rather than letting it construct them, decoupling code from concrete implementations and making behavior replaceable in tests. It ranges from manual constructor injection to container-managed graphs.

## Details
- Mechanism: instead of new Database() inside a service, the service receives a Database via constructor (or setter/interface); composition happens at the root (main, a container, or a factory); interfaces define the contract so implementations swap without changing consumers. Containers (Spring, Guice, DI libraries) automate wiring, scoping, and lifecycle.
- Concrete example: an order service takes a PaymentGateway interface; tests inject a fake; production wires a real provider; a config change (new gateway) touches only the composition root. Without DI, the service hard-codes its dependency and tests reach for brittle mocks or real infrastructure.
- Failure modes: over-engineering — a DI container for an app with three classes; service locators hiding dependencies (the anti-pattern DI replaces); lifecycle leaks (transient dependencies injected into singletons); and constructor explosions that signal a design problem, not a DI one.
- Operational tradeoffs: DI costs indirection and wiring effort; it pays in testability, flexibility, and change isolation. The middle ground is manual composition (no container) for small codebases and containers where graphs are large; either way, dependencies should be visible at the boundary.
- RSIS3/mykb relevance: the wiki's services would be wired at composition roots with interfaces, so the loop's experiments swap real and simulated components without touching internals.
- Composition root: keep all wiring in one place per app entry point; wiring scattered through code recreates the hidden-dependency problem DI removes.
- Scoping: match dependency lifetimes (transient/singleton/scoped) to their state; the classic bug is a request-scoped dependency captured in a singleton.

## Related
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]] — the principle DI implements
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — DI wires adapters into the core's ports
- [[wiki/testing/entities/test-patterns|Testing Patterns]] — injected fakes make tests fast
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — DI relates to factory and service locator patterns
