---
type: "concept"
title: "Inversion of Control"
description: "Design principle where a framework or container controls the flow and calls user code, not the reverse"
tags: ["design", "ioc", "frameworks", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Inversion of Control

## Summary
Inversion of control (IoC) flips control: instead of your code calling library functions, a framework or container drives the flow and invokes your components. Hollywood principle: don't call us, we'll call you.

## Details
- Frameworks, event loops, and DI containers all implement IoC in different forms.
- It enables pluggability and testability but can make flow hard to follow.
- RSIS3 relevance: agent loops invert control over tool calls, a familiar pattern to mykb.

## Related
- [[wiki/software-engineering/dependency-injection|Dependency Injection]] — the most common concrete IoC technique
- [[wiki/software-engineering/hexagonal-architecture|Hexagonal Architecture]] — ports invert dependency direction
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the runtime loop that calls agent hooks
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — template method is a classic IoC pattern
