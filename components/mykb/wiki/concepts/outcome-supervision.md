---
type: "concept"
title: "Outcome Supervision"
description: "Training or evaluating on final outcomes rather than intermediate steps"
tags: ["supervision", "rl", "verification", "process-vs-outcome"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2305.20050", "https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"]
---

# Outcome Supervision

## Summary
Outcome supervision rewards or grades an agent only on final results, leaving intermediate steps unconstrained. 'Let's Verify Step by Step' (2023) found process supervision — grading each step — substantially outperforms outcome supervision on hard math, especially for detecting flawed reasoning that still reaches a right-looking answer.

## Details
- **Outcome vs process** — final-answer grades are cheaper; step grades are more informative and more robust to lucky guesses.
- **Evidence** — process-supervised verifiers improved MATH accuracy and generalizability of the learned verifier.
- **Cost** — step labels are expensive to collect; RLAIF and verifier models amortize the cost.
- **Safety angle** — outcome supervision rewards cheating that lands the answer; process supervision catches bad reasoning.
- **RSIS3 parallel** — pulse outcomes are scored, but check-practices also grades the process (practices followed, telemetry complete).

## Related
- [[wiki/concepts/rlaif|RLAIF (RL from AI Feedback)]] — AI-generated feedback granularity
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — internal grade analogue
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — when the grader is flawed
- [[wiki/concepts/outcome-supervision|outcome-supervision]] — the superior sibling
- [[wiki/concepts/oversight|Oversight]] — why grading matters
- [[wiki/concepts/calibration|Calibration]] — grader reliability
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
- [[wiki/concepts/oversight-bottleneck|Oversight Bottleneck]] — why oversight needs help
