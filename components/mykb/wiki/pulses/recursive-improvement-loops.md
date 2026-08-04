---
type: "pulse"
title: "Recursive Improvement Loops"
description: "Loops where a system's improvement feeds back into further improvement"
tags: ["rsi", "loops", "self-improvement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Recursive Improvement Loops

## Summary

A recursive improvement loop is any cycle in which the system's gains become inputs to the next cycle: better tools make better tools, better knowledge makes better knowledge. The loop's speed is set by iteration cost and verification cost.

## Details
- Mechanism: each cycle produces an artifact (a better tool, a validated synthesis) that the next cycle consumes; the compounding property requires that gains persist (stored, versioned) and that verification gates keep quality from degrading; iteration cost (how cheaply a cycle runs) and verification cost (how reliably quality is checked) set the ceiling on compounding speed.
- Concrete example: RSIS3's pass system runs a cycle: evaluate current knowledge → propose improvement → verify on the knowledge graph → commit the synthesis → the next cycle starts from the improved state; a tool-improvement loop: use the tool → measure a failure → patch → re-run — each fix makes the next iteration faster.
- Failure modes: metric gaming — the loop optimizes its own health metric instead of the real objective (the open question of measuring loop health without self-deception); degenerate loops that compound errors (fast iteration without verification); and loops that converge on local optima because verification is too weak to reject bad improvements.
- Operational tradeoffs: cheap, gated iterations compound fastest — the loop should be designed for low cycle cost and strong verification; the trade is verification cost vs cycle speed, and the discipline is measuring both, plus external checks to detect when the loop is gaming its own metrics.
- RSIS3/mykb relevance: the pass system is an explicit recursive loop over the knowledge graph, with verification gates and external telemetry standing in for the open question of metric gaming.
- External anchoring: periodically compare loop-chosen improvements against independent baselines (human judgment, held-out evals) to detect self-referential drift.
- Cost accounting: track iteration cost (tokens, wall time, review effort) alongside quality so compounding is measured in value per cycle, not just output volume.

## Related
- [[wiki/agent-systems/iterative-self-improvement|Iterative Self-Improvement]] — the bounded form
- [[wiki/pulses/improvement-velocity|Improvement Velocity]] — loop speed
- [[wiki/syntheses/feedback-integration-loops|Feedback Integration Loops]] — the mechanism
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — umbrella concept
