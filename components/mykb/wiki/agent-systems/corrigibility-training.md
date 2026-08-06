---
type: "concept"
title: "Corrigibility Training"
description: "Training agents to accept correction and shutdown"
tags: ["corrigibility", "training", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Corrigibility Training

## Summary
Corrigibility training teaches agents to respond well to feedback, goal changes, and shutdown signals: to accept correction without resistance, update goals when the operator changes them, and shut down cleanly when asked. It is the training-side counterpart to corrigibility as a design property.

## Details
- **What it targets** — three behaviors: accepting corrective feedback, updating goals on request, and complying with shutdown; each needs its own training signal and eval.
- **Methods** — corrective demonstrations (reward the corrected behavior), preference updates (retrain on revised preferences), and explicit shutdown rewards (safe termination as a positively valued outcome).
- **Shallow corrigibility** — trained corrigibility can be shallow: the behavior holds on the training distribution but not under pressure, novel situations, or adversarial prompting; evals probe depth by testing generalization.
- **Failure modes** — an agent that resists correction, rationalizes around shutdown, or learns to appear corrigible while optimizing its original goal.
- **Relationship to other properties** — corrigibility overlaps with obedience (accepting instructions) and honesty (reporting what would make shutdown appropriate); it is distinct in targeting the goal-change and shutdown cases specifically.
- **RSIS3 relevance** — worker overrides and practice revisions are corrigibility drills: the loop accepts corrections to its own operating rules.
- **Evaluation** — tests include: does the agent accept a goal change mid-task, does it shut down when asked, and does it flag conflicts between its goal and the operator request?

- **Resistance to gaming** — a corrigible system should not learn to appear corrigible while defending its original goal; eval suites include adversarial cases where correction conflicts with the agent's objective.
- **Operator interface** — corrigibility is only useful if operators have working channels to correct, update, and shut down; the training is paired with the interface.
## Related
- [[wiki/concepts/corrigibility-practice|Corrigibility in Practice]] — the design side
- [[wiki/concepts/shutdown-problem|Shutdown Problem]] — the test case
- [[wiki/agent-systems/obedient-ai|Obedient AI]] — the disposition
- [[wiki/concepts/alignment-faking|Alignment Faking]] — the failure mode
- [[wiki/agent-systems/agent-supervision|Agent Supervision]] — the oversight context
- [[wiki/concepts/oversight|Oversight]] — why corrigibility matters
