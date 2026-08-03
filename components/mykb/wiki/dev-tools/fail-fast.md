---
type: "concept"
title: "Fail Fast"
description: "Detecting invalid state as early as possible instead of letting it cascade"
tags: ["fail-fast", "design", "validation", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fail Fast

## Summary
Fail-fast design validates inputs and invariants at the boundary so errors surface immediately, at the point of origin, instead of deep inside unrelated code. Early, loud failure is cheaper and easier to debug than late, weird failure — a malformed input rejected at the door beats a corrupted database discovered weeks later.

## Details
- Mechanism: validate inputs at API boundaries (types, ranges, formats); assert invariants where they are established, not where they are consumed; fail with a precise, actionable error naming the offending value; orchestration sees the failure through health checks and error channels, not just the caller.
- Concrete example: an ingestion pipeline rejects an article whose frontmatter is missing a required field at parse time, with the field and article ID in the error; a config loader fails at startup when a variable is missing or malformed, instead of three hours into a run; a function asserts its inputs are non-null before doing work.
- Failure modes: fail-fast applied to transient conditions — a flaky network call that hard-fails instead of retrying, turning a blip into an outage; validation so strict that legitimate edge cases are rejected; failure at the boundary but the error is vague, forcing a debugging session; fail-fast in code paths where the caller cannot handle the failure, crashing the whole process.
- Tradeoffs: fail-fast trades partial work for early detection — permanent and programming errors should fail fast, while transient failures need retries and degradation; the alternative, tolerate-and-continue, risks silent corruption and confusing downstream failures; the discipline is classifying errors first, then choosing fast-fail versus retry.
- Operational notes: pair fast failures with health checks so orchestration restarts or alerts, and log the rejected input (redacted) for reproduction.
- RSIS3 relevance: fail fast on malformed frontmatter so a bad article is rejected before it corrupts the graph — the same boundary validation RSIS3 applies to its own state inputs.

## Related
- [[wiki/dev-tools/fail-safe|Fail-Safe]]
- [[wiki/dev-tools/exception-handling-practice|Exception Handling Practice]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
