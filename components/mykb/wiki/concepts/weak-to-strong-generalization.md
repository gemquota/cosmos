---
type: "concept"
title: "Weak-to-Strong Generalization"
description: "Strong models learning from weak supervisors and surpassing them"
tags: ["weak-to-strong", "superalignment", "supervision", "openai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2312.09390", "https://en.wikipedia.org/wiki/Superalignment"]
---

# Weak-to-Strong Generalization

## Summary
Weak-to-strong generalization asks whether strong models can be aligned by weaker supervisors, the regime OpenAI's superalignment agenda assumes. Their 2023 work found that strong models fine-tuned on weak labels can outperform the weak supervisor, but also that confident weak labels can mislead them — motivating auxiliary confidence and consistency losses.

## Details
- **Setup** — a strong model is supervised by a weak model's labels on tasks where the weak model errs.
- **Finding** — strong models often generalize past the weak supervisor's mistakes, but alignment degrades without interventions.
- **Methods** — unsupervised confidence weighting and auxiliary losses recover much of the gap.
- **Why it matters** — it is the empirical core of scalable oversight: humans are the 'weak supervisor' for superhuman AI.
- **RSIS3 relevance** — automated checkers and link validation are weak supervisors over the knowledge loop; humans audit the exceptions.

## Related
- [[wiki/concepts/superalignment|Superalignment]] — the research agenda
- [[wiki/concepts/scalable-oversight|Scalable Oversight]] — why it matters
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — AI feedback family
- [[wiki/concepts/supervisor-model|Supervisor Model]] — the weak supervisor
- [[wiki/concepts/outcome-supervision|Outcome Supervision]] — label quality
- [[wiki/concepts/calibration|Calibration]] — label reliability
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
- [[wiki/concepts/oversight-bottleneck|Oversight Bottleneck]] — why oversight needs help
