---
type: "concept"
title: "Fail Fast"
description: "Detecting invalid state as early as possible instead of letting it cascade"
tags: ["fail-fast", "design", "validation", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fail Fast

## Summary
Fail-fast design validates inputs and invariants at the boundary so errors surface immediately, at the point of origin, instead of deep inside unrelated code. Early, loud failure is cheaper and easier to debug than late, weird failure.

## Details
- Validate inputs at API boundaries; assert invariants where they are established.
- Fail-fast suits programming errors and permanent conditions; transient failures need retries, not fast fails.
- Pair with health checks so the failure is visible to orchestration, not just the caller.
- mykb relevance: fail fast on malformed frontmatter so a bad article is rejected before it corrupts the graph.

## Related
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/dev-tools/exception-handling-practice|Exception Handling Practice]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
