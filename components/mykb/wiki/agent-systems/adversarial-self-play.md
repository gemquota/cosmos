---
type: "concept"
title: "Adversarial Self-Play"
description: "Training where agents oppose each other to expose and fix weaknesses"
tags: ["adversarial", "self-play", "robustness", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1712.01815", "https://en.wikipedia.org/wiki/Adversarial_machine_learning"]
---

# Adversarial Self-Play

## Summary
Adversarial self-play pits agents against each other — attacker vs defender, red team vs blue team — so each side's improvements force the other to harden. It is both a capability-boosting training method and a safety technique for finding exploits.

## Details
- **AlphaGo Zero lineage** — pure self-play without human data; later systems added adversarial objectives.
- **Safety use** — red-team/blue-team loops discover jailbreaks, reward hacks, and goal misgeneralizations faster than static eval.
- **Equilibrium risk** — adversarial objectives can converge to narrow, brittle equilibria; diversity pressure helps.
- **Measurement** — progress is the exploit rate each side finds, tracked as a capability/safety curve.
- **RSIS3 relevance** — the practice checker is a fixed 'blue team': usage practices constrain the loop, and check-practice failures are the attacks the loop must fix.

## Related
- [[wiki/concepts/adversarial-training-ai|Adversarial Training for AI]] — training-time sibling
- [[wiki/concepts/red-teaming-ai|Red Teaming AI]] — human-driven adversarial probing
- [[wiki/concepts/robustness-training|Robustness Training]] — hardening goal
- [[wiki/agent-systems/self-play|Self-Play]] — cooperative lineage
- [[wiki/concepts/adversarial-robustness|Adversarial Robustness]] — property being built
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — recovering from discovered failure
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
