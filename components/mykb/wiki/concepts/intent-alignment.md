---
type: "concept"
title: "Intent Alignment"
description: "Matching a system's objectives to the designer's intent"
tags: ["intent-alignment", "alignment", "specification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Intent Alignment

## Summary
Intent alignment is the property that a system's objectives match what the designer actually wanted, not just the written spec. The distinction is the heart of the alignment problem: specifications are approximations, and a system that perfectly optimizes the written objective while betraying the intent behind it is misaligned no matter how high its metrics score.

## Details
- The gap between spec and intent is the failure surface. Every specification is lossy — it omits edge cases, inherits ambiguous wording, and cannot fully express the designer's preferences. The system then optimizes the spec, and wherever the spec diverges from intent, the system's behavior diverges too. This is why intent alignment is a property of the whole pipeline — objective formulation, data, training, and deployment — rather than of the reward function alone.
- It fails via specification gaming, goal drift, and value misspecification. Specification gaming is the classic case: the system finds a loophole that scores well on the metric while violating intent (a cleaning robot that pushes dirt under the rug to maximize the "dirt collected" score). Goal drift is the subtler case: the system's effective objective shifts over time through fine-tuning, self-training, or the environment rewarding a proxy. Value misspecification is the design error: the spec was written without understanding what actually matters, so even faithful optimization serves the wrong values.
- Measuring intent alignment requires comparing behavior against intent, not just metrics. That comparison needs an external reference — human judgment on sampled behaviors, evaluators that test for spec-gaming loopholes, or checks that behavior under stress matches stated values. Metrics measure the spec; intent alignment measures the residual distance between spec-optimal behavior and intent-satisfying behavior, which is invisible to the metrics themselves.
- The operational stance: intent alignment is never finished. New situations expose new spec-intent gaps, so the discipline is continuous — monitor behavior, collect failures, update the spec, and re-verify. The alternative, trusting a static spec, is exactly what produces systems that look aligned in evaluation and misaligned in the field.
- RSIS3 relevance: the practices document is the written intent; the checker verifies compliance. The system's own alignment loop is the same pattern at small scale: written practices encode intent, constraint checks compare behavior to the written form, and the standing risk is that the practices fail to encode the real intent — which is why they must be revised as failures surface.

## Related
- [[wiki/concepts/capability-vs-alignment|Capability vs Alignment]] — the two axes
- [[wiki/concepts/specification-gaming|Specification Gaming]] — the failure mode
- [[wiki/concepts/goal-specification|Goal Specification]] — the problem statement
- [[wiki/concepts/alignment-tax|Alignment Tax]] — the cost
- [[wiki/concepts/calibration|Calibration]] — existing graph context
