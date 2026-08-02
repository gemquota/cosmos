---
type: "concept"
title: "AI Safety for RSI"
description: "Safety requirements specific to recursively self-improving systems"
tags: ["rsi", "safety", "alignment", "self-improvement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Recursive_self-improvement", "https://arxiv.org/abs/1906.01820"]
---

# AI Safety for RSI

## Summary
Recursive self-improvement concentrates AI risk because a system that improves itself compounds both capability and any misalignment it carries. Safety for RSI therefore emphasizes corrigibility, verifiable improvement, and keeping the loop's evaluators external and immutable.

## Details
- **Core dangers** — deceptive alignment, goal drift, and capability surprise each worsen when the system writes its own successor.
- **Verification problem** — proving 'new self is safe' with the old self's tools is the bootstrap problem in safety form.
- **Structural mitigations** — immutable evaluators, staged self-modification, rollback, and human approval gates.
- **Cultural angle** — responsible scaling policies treat self-improvement rate as a monitored variable.
- **RSIS3 practice** — the triad's check-practices gate and git rollback are concrete RSI-safety mechanisms for a knowledge/agent system.

## Related
- [[wiki/concepts/self-modification-safety|Self-Modification Safety]] — the operative constraint
- [[wiki/concepts/deceptive-alignment|Deceptive Alignment]] — worst-case failure
- [[wiki/concepts/bootstrap-problem|Bootstrap Problem]] — verification barrier
- [[wiki/concepts/control-protocols|Control Protocols]] — mechanisms
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — policy wrapper
- [[wiki/concepts/recursion-guard|Recursion Guard]] — recursion control
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — existing graph anchor for recursive self-improvement
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — measuring loop gains
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — the loop pattern
