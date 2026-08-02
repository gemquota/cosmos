---
type: "concept"
title: "Value Specification"
description: "Stating which values an AI system should embody and pursue"
tags: ["values", "specification", "alignment", "ethics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Value_learning", "https://arxiv.org/abs/2206.05862"]
---

# Value Specification

## Summary
Value specification is the normative half of goal specification: deciding what the system should care about — human welfare, autonomy, fairness — and encoding that in trainable form. Value learning approaches infer values from behavior and feedback because we cannot write a utility function for 'human flourishing' by hand.

## Details
- **Inputs** — constitutions, preference data, human behavior, and philosophical frameworks.
- **Challenges** — values are contested, context-dependent, and systematically hard to articulate (preference falsification, moral uncertainty).
- **Approaches** — RLHF learns a value proxy; Constitutional AI encodes principles in text; coherent extrapolated volition is the ambitious extrapolation target.
- **Failure modes** — value lock-in (freezing one snapshot of values), value drift, and evaluator bias.
- **RSIS3 relevance** — the triad's practices document is a written value specification for the workspace: what counts as good operation.

## Related
- [[wiki/concepts/goal-specification|Goal Specification]] — the descriptive half
- [[wiki/concepts/value-alignment-problems|Value Alignment Problems]] — why it is hard
- [[wiki/concepts/preference-elicitation|Preference Elicitation]] — inference route
- [[wiki/concepts/coherent-extrapolated-volition|Coherent Extrapolated Volition]] — ambitious target
- [[wiki/concepts/value-drift|Value Drift]] — the decay risk
- [[wiki/concepts/utility-functions|Utility Functions]] — formal substrate
- [[wiki/concepts/calibration|Calibration]] — measurement honesty in the existing graph
