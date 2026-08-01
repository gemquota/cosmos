---
type: "concept"
title: "Meta-Parameter Tuning"
description: "Bounded, registry-driven adjustment of a loop's own parameters by a higher loop — the +3 diagonal in practice"
tags: [meta-parameters, tuning, registry, rsis3, optimization]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Meta-Parameter Tuning

## Summary
Meta-parameter tuning is the act of a loop adjusting the parameters of another loop (never its own live decisions) within explicit bounds. It is what makes the system self-improving rather than merely self-running. RSIS3 implements it as a registry: each tunable is declared with `(min, max, config path, kind)` in `config.py`, and a tuning loop may only write keys in its +3 target's registry.

## Details
- **Registry invariant**: every write key is owned by exactly one loop (L4 owns `l1.*`, L5 owns `l2.*`, …, L9 owns `l6.*`), so no two loops ever race on the same parameter.
- **Bounded writes**: values are clamped to registry bounds; int/float kinds are applied with the right coercion.
- **Startup injection**: `load_config()` reads persisted tuning state (`.rsis/*_state.json`) before any loop constructs, so consumers see tuned values without plumbing.
- **History**: accepted and rejected proposals are appended to each loop's state history — the raw material meta-tuners (L7/L8/L9) observe.
- Worked example: L4 sees success-rate 0.4, proposes `l1.max_retries +1`, the evaluator PASSes, the state persists, and the next L1 run uses retries=4.

## Related
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]] — the ownership rule
- [[wiki/concepts/deadband-control|Deadband Control]] — thresholds that decide when to tune
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — who tunes whom
- [[wiki/concepts/recursion-guard|Recursion Guard]] — why tuning stops at L9