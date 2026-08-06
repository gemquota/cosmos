---
type: "concept"
title: "Self-Play"
description: "Training by playing against copies of oneself"
tags: ["self-play", "rl", "training", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1712.01815", "https://en.wikipedia.org/wiki/AlphaGo_Zero"]
---

# Self-Play

## Summary
Self-play trains an agent by competing or cooperating with copies of itself, generating an endless curriculum of increasingly hard problems. AlphaGo Zero's 2017 result — superhuman Go from self-play alone — made it a canonical method, and it generalizes to debate, dialogue, and two-player games.

## Details
- **Mechanism** — the agent plays itself; the policy improves, raising the difficulty for the next iteration.
- **Why powerful** — no external data needed beyond rules; the difficulty curve is self-generated.
- **Risks** — distribution collapse into narrow strategies, reward gaming in the self-play game, and pathological equilibria.
- **Modern use** — adversarial training for safety (red vs blue), and self-play for consistency in LLM debate.
- **RSIS3 parallel** — pulses 'compete' with past pulses: telemetry and outcomes are compared across iterations to select better practices.

- **Variants** — symmetric self-play (both sides identical), asymmetric (red team vs blue team), and league play (a population of agents) cover different training needs.
- **Equilibrium risk** — self-play can converge to degenerate equilibria (both sides exploiting a quirk); regularization and diverse opponents mitigate this.
- **Safety use** — adversarial self-play trains robustness by letting an attacker agent probe the defender, producing failure modes that static evals miss.
- **Efficiency** — self-play generates unlimited training data at the cost of compute and distribution collapse risk; it is not free data, it is expensive data with a bias.

- **Measurement** — the value of self-play is measured by transfer: does the policy trained in self-play perform on the real task or evaluation distribution, not just on the self-play game itself.

## Related
- [[wiki/agent-systems/adversarial-self-play|Adversarial Self-Play]] — competitive variant
- [[wiki/agent-systems/curriculum-self-improvement|Curriculum Self-Improvement]] — ordering self-generated tasks
- [[wiki/agent-systems/iterative-self-improvement|Iterative Self-Improvement]] — the cycle self-play drives
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — comparison note
- [[wiki/concepts/markov-decision-processes|Markov Decision Processes]] — equilibrium framing
- [[wiki/agent-systems/agent-loop|Agent Loop]] — host loop
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
