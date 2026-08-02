---
type: "concept"
title: "Scalable Oversight"
description: "Supervision techniques that remain effective as AI systems outpace human review"
tags: ["scalable-oversight", "supervision", "alignment", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1805.00899", "https://arxiv.org/abs/1811.07871"]
---

# Scalable Oversight

## Summary
Scalable oversight is the research program of keeping supervision effective when AI systems are smarter or faster than their human overseers. Techniques include debate, recursive reward modeling, AI-assisted review, and weak-to-strong generalization — supervision that scales with capability.

## Details
- **Debate** — two AIs argue; a weaker judge picks the better argument, outsourcing the hard evaluation.
- **Recursive reward modeling** — a small AI helper critiques a bigger one, with humans supervising the helper's critiques.
- **AI-assisted oversight** — stronger models review weaker ones under human-defined standards, as in RLAIF.
- **Weak-to-strong** — evidence that strong models can learn from weak supervision on tasks where the supervisor is wrong.
- **RSIS3 relevance** — the mykb graph supervises its own acquisition via link checks and practice gates: automated oversight of automated processes.

## Related
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — AI feedback as oversight
- [[wiki/concepts/weak-to-strong-generalization|Weak-to-Strong Generalization]] — capability side
- [[wiki/concepts/oversight|Oversight]] — the base practice
- [[wiki/concepts/cross-examination|Cross-Examination]] — adversarial variant
- [[wiki/concepts/supervisor-model|Supervisor Model]] — the helper model
- [[wiki/concepts/calibration|Calibration]] — judge reliability
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
