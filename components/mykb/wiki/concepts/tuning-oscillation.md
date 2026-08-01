---
type: "concept"
title: "Tuning Oscillation"
description: "The thrash signal: a tuned loop flips its adjustments back and forth, and the meta-tuner widens the deadband"
tags: [oscillation, deadband, stability, rsis3, meta-tuning]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Tuning Oscillation

## Summary
Tuning oscillation is the pattern where a loop's adjustments alternate sign across cycles — up, down, up, down — because its response threshold is too tight around the equilibrium. It is a stability signal: the loop is reacting to noise instead of trend. The meta-tuner responds by widening the deadband so the loop stops thrashing. RSIS3 uses this in two places: L7 widens L4's success deadband on oscillating deltas, and L9 widens L6's identity band on alternating shrink/grow.

## Details
- **Detection**: look at accepted history entries; if consecutive deltas alternate sign (+, −, +), classify as oscillation.
- **Response**: widen the band — L7 moves `target_success_low` down and `target_success_high` up; L9 moves `shrink_below` down and `grow_above` up.
- **Guardrail**: the band gap never collapses below a minimum (e.g. 0.05); at the bound the loop no-ops.
- **Complementary signal**: stall (no applied tuning while success is low) narrows the band instead — the symmetric correction.
- Worked example: L6 fires shrink, grow, shrink, grow on alternating outcome ratios; L9 reads that history and widens `[0.5, 0.8]` → `[0.45, 0.85]`.

## Related
- [[wiki/concepts/deadband-control|Deadband Control]] — the mechanism being adjusted
- [[wiki/concepts/fitness-stagnation|Fitness Stagnation]] — the plateau counterpart
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — the tuning act itself
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — L7/L9 observe and widen