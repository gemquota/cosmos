---
type: "concept"
title: "Side Effect Isolation"
description: "Concentrating I/O and state changes at the edges of pure logic"
tags: ["functional-programming", "side-effects", "architecture", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Side Effect Isolation

## Summary
Side-effect isolation keeps impure operations — network calls, file writes, random, clock — at the system boundary while core logic stays pure. Effects become injectable and mockable, which makes testing and reasoning dramatically easier.

## Details
- Dependency injection of effect handles (a clock, an HTTP client) lets tests substitute fakes.
- Effect systems (IO, Task, ZIO) model side effects as values you compose and run at the boundary.
- Pure core, impure shell is the layering; the shell is where retries, logging, and metrics live.
- mykb relevance: isolate curl fetches from link-checking logic so verification is testable offline.

## Related
- [[wiki/software-engineering/pure-functions|Pure Functions]]
- [[wiki/software-engineering/inversion-of-control|Inversion of Control]]
- [[wiki/software-engineering/referential-transparency|Referential Transparency]]
- [[wiki/software-engineering/functional-programming|Functional Programming]]
- [[wiki/software-engineering/repositories-pattern|Repositories Pattern]]
