---
type: "concept"
title: "Recursive Feedback Loops"
description: "Loops where a system's output feeds back into its own next iteration"
tags: ["feedback", "recursion", "self-improvement", "control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1906.01820", "https://en.wikipedia.org/wiki/Feedback"]
---

# Recursive Feedback Loops

## Summary
A recursive feedback loop closes the system's output back into its input: an agent's performance evaluation shapes its next action, and its actions generate new evaluation. When the loop's signal is honest, the system compounds improvement; when corrupted, it compounds error.

## Details
- **Structure** — sense, evaluate, revise, repeat; each iteration starts from the previous output.
- **Honesty condition** — the feedback must measure the objective, not the system's self-report, or the loop collapses into self-flattery.
- **Stability** — damping (conservative deltas, rollback) prevents oscillation and runaway.
- **Worked example** — Reflexion stores verbal feedback across attempts; RSIS3 stores pulse outcomes in the wiki and reads them in the next planning phase.
- **Failure mode** — without external anchors, error and bias compound exponentially.

- **Signal design** — the feedback must be measurable, timely, and causally connected to the action being evaluated; vague or delayed signals produce oscillations instead of convergence.
- **Damping** — limit the per-cycle change (conservative deltas, rollback on regression) so the loop converges rather than overshooting; undamped recursive feedback is how systems oscillate into failure.
- **External anchors** — benchmarks, test suites, and human review break the loop's self-reference; without anchors, the system optimizes its own echo.
- **Application pattern** — RSIS3 closes the loop by writing pulse outcomes into the wiki and reading them in the next planning phase, so improvement compounds across sessions.

- **Runaway detection** — oscillating or exponentially diverging loop metrics (error doubling, plans flip-flopping) are the signature of an unstable recursive loop; monitors should look for these shapes, not just average error.

- **Worked example** — a code agent evaluates each patch with tests, feeds failures back into the next patch, and rolls back when the feedback trend degrades, converting evaluation into a compounding improvement signal.

## Related
- [[wiki/agent-systems/self-reflection-loops|Self-Reflection Loops]] — agent-level instance
- [[wiki/syntheses/feedback-integration-loops|Feedback Integration Loops]] — how feedback becomes durable change
- [[wiki/pulses/improvement-velocity|Improvement Velocity]] — the loop's speed
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — keeping feedback honest
- [[wiki/syntheses/loop-closure|Loop Closure]] — termination and handoff
- [[wiki/concepts/telemetry|Workspace Telemetry]] — signal source
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
