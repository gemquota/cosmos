---
type: "concept"
title: "Proxy Pattern"
description: "A stand-in object that controls access to a real target"
tags: ["proxy", "patterns", "design", "indirection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Proxy Pattern

## Summary

The proxy pattern interposes a stand-in object between a client and a real subject, controlling access, adding behavior, or deferring work without changing the subject's interface. It is the pattern behind lazy loading, access control, remote stubs, caching, and instrumentation.

## Details
- Mechanism: the proxy implements the same interface as the subject and forwards calls, adding behavior around them: a virtual proxy lazily constructs the expensive subject on first use; a protection proxy checks authorization; a remote proxy marshals calls over the wire; a cache proxy memoizes results; a logging proxy instruments calls.
- Concrete example: an image proxy loads the file only when displayed; a service client proxy injects auth tokens and retries transparently; a metrics proxy wraps every repository call with timing; frameworks (Java dynamic proxies, ES Proxies) generate proxies without hand-writing them — the pattern is everywhere precisely because it is invisible.
- Failure modes: proxies that swallow or alter errors (transparent proxies must preserve semantics); proxy chains multiplying latency and failure modes; leakage of proxied-object identity (equality, instanceof break); and proxies used for what should be a first-class design (permission checks in a proxy instead of the domain).
- Operational tradeoffs: proxies add a layer of indirection for behavior that would otherwise litter every caller; the discipline is keeping the proxy thin, preserving the subject's contract exactly, and documenting where proxies sit so debugging is not a maze.
- RSIS3/mykb relevance: the wiki's API clients use thin proxies for auth, retry, and metrics, so the loop's integrations get consistent telemetry without duplicated client code.
- Transparency contract: a proxy must preserve the subject's interface and semantics, including error types and identity where clients depend on them.
- Lifecycle: manage proxy construction/destruction explicitly (per-scope proxies) to avoid accumulating stale wrappers around recreated subjects.

## Related
- [[wiki/software-engineering/decorator-pattern|Decorator Pattern]]
- [[wiki/software-engineering/adapter-pattern|Adapter Pattern]]
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
