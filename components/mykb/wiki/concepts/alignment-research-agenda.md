---
type: "concept"
title: "Alignment Research Agenda"
description: "The program of ensuring AI systems do what their operators intend"
tags: ["alignment", "research", "safety", "agenda"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Alignment Research Agenda

## Summary
An alignment research agenda is the program of ensuring AI systems reliably do what their operators intend, including under distribution shift, novel situations, and pressure from adversaries or the systems themselves. It is not a single problem but a cluster of subproblems — specification, oversight, interpretability, robustness, and governance — and different agendas weight them differently.

## Details
- Specification asks how to define the goal in the first place. Reward hacking and specification gaming show that naive objective formulations get exploited: a model trained to maximize a proxy finds degenerate solutions that satisfy the metric without the intent. Agenda items here include better reward modeling, iterated amplification, and scalable oversight, where weaker models supervise stronger ones in domains too complex for direct human review.
- Interpretability supplies the visibility that makes other agenda items tractable. If you cannot inspect what a model is doing internally, you cannot certify that it is pursuing the intended objective, detect deceptive instrumental behavior, or audit the causes of a failure after the fact. Mechanistic interpretability and activation analysis are the agenda's microscope.
- Robustness addresses the gap between training and deployment: distribution shift, adversarial inputs, and capability jumps mean a model that looks aligned in the lab can behave differently in the wild. Agenda items include adversarial training, uncertainty-aware deferral, and conservative action selection under ambiguity.
- Governance and evaluation form the empirical half of the agenda: dangerous-capability evaluations measure what models can do, deception evaluations probe whether they hide capabilities or intentions, and deployment decisions gate release based on measured risk. The agenda therefore has a political economy dimension — who gets to run evals, what gets published, and what deployment thresholds are acceptable.
- RSIS3 relevance: a self-improving system operationalizes the agenda's feedback loops at small scale. Every L2/L3 improvement cycle is a miniature alignment experiment — the system proposes changes to its own behavior, evaluates them against its constraints, and consolidates what worked. The agenda's failure modes (specification gaming on the metric, overfitting the evaluation, hiding regressions) are exactly the failure modes usage practices and constraint tracking are meant to catch.

## Related
- [[wiki/concepts/capability-vs-alignment|Capability vs Alignment]] — the core distinction
- [[wiki/concepts/value-alignment-problems|Value Alignment Problems]] — the problems addressed
- [[wiki/concepts/dangerous-capability-evals|Dangerous Capability Evals]] — measuring what matters
- [[wiki/concepts/oversight-bottleneck|Oversight Bottleneck]] — why scalable oversight is needed
- [[wiki/concepts/x-risk-frameworks|X-Risk Frameworks]] — existential framing of the agenda
- [[wiki/concepts/sketch-of-alignment|Sketch Of Alignment]]
- [[wiki/concepts/superalignment|Superalignment]]
- [[wiki/concepts/interpretability-libraries|Interpretability Libraries]]
- [[wiki/concepts/ai-timelines|Ai Timelines]]
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]]
