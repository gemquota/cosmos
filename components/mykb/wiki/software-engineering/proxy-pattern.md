---
type: "concept"
title: "Proxy Pattern"
description: "A stand-in object that controls access to a real target"
tags: ["proxy", "patterns", "design", "indirection"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Proxy Pattern

## Summary
The proxy pattern places an object with the same interface in front of a real target to control access — lazy init, caching, authorization, remote calls. Callers cannot tell whether they talk to the proxy or the real thing.

## Details
- Virtual proxies defer expensive construction; protection proxies gate access; remote proxies hide network calls.
- Proxies and decorators look alike: decorators add behavior, proxies control access to a target.
- Interface fidelity matters — a leaking proxy breaks the caller's assumptions.
- mykb relevance: a caching proxy in front of the source fetcher would deduplicate curl calls.

## Related
- [[wiki/software-engineering/decorator-pattern|Decorator Pattern]]
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
