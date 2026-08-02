---
type: "concept"
title: "Decorator Pattern"
description: "Adding behavior to objects by wrapping them with the same interface"
tags: ["decorator", "patterns", "design", "composition"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Decorator Pattern

## Summary
The decorator pattern wraps an object with another object of the same interface, adding behavior — logging, caching, retries — without changing the original. Decorators compose recursively and stack cleanly.

## Details
- Each decorator forwards calls to its wrapped object, adding its own behavior before or after.
- Streams (BufferedInputStream) and middleware chains are classic decorators.
- Deep wrapper stacks can obscure types and debugging; name the layers in logs.
- mykb relevance: decorate the fetcher with retry, cache, and metrics wrappers in any order.

## Related
- [[wiki/software-engineering/proxy-pattern|Proxy Pattern]]
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/composition-over-inheritance|Composition Over Inheritance]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
