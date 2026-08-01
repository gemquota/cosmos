---
type: "concept"
title: "Recursion Guard"
description: "Untuned fixed points: the top three loops tune others but are never tuned themselves, capping self-modification depth"
tags: [recursion, fixed-point, rsis3, safety, architecture]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Recursion Guard

## Summary
The recursion guard is the rule that the top three loops (L7, L8, L9) are untuned fixed points: they tune the levels below them but no loop tunes them, and there is no L10+. This caps self-modification depth at exactly three meta-levels — core → tuners → meta-tuners — and prevents unbounded recursion of tuning loops tuning tuning loops.

## Details
- **Enforcement**: the tunable registry contains no entries for `l7.*`, `l8.*`, or `l9.*` params; the practices checker asserts this.
- **Spec tie-in**: the cap matches the max-3 self-modification depth limit in SPACE's recursive-depth analysis.
- **Cost**: the meta-tuners' own thresholds (windows, steps) are manually set defaults — the price of bounded recursion.
- **Diagonal termination**: L9 → L6 → L3 → substrate, with L3's consolidation as the loop that most directly curates the artifact layer.
- If an L10 were added, it would shift the fixed points and require a spec change — by design, not an accident.

## Related
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]] — the ownership rule it caps
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — L7–L9 are the fixed points
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — bounded by the guard
- [[wiki/concepts/metacognition|Metacognition]] — the cognitive framing of thinking about thinking