---
type: "concept"
title: "Curriculum Self-Improvement"
description: "Ordering self-generated training tasks from easy to hard"
tags: ["curriculum", "self-improvement", "training", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Curriculum_learning", "https://arxiv.org/abs/1712.01815"]
---

# Curriculum Self-Improvement

## Summary
Curriculum self-improvement arranges a system's own training experience in an order that maximizes learning: start easy, increase difficulty as competence grows. Combined with self-play and generation, it removes the dependency on fixed human datasets.

## Details
- **Classic results** — curriculum learning improves convergence and final performance across RL and supervised tasks.
- **Self-generation** — the agent proposes its own next tasks (learnt-to-learn curricula), avoiding human bottlenecks.
- **Difficulty estimation** — needs a competence metric; mis-estimation wastes cycles or produces collapse.
- **Safety angle** — a curriculum that only explores easy regions hides goal misgeneralization until deployment.
- **RSIS3 analogy** — the pulse loop's escalating check-practices and staged passes are a curriculum for the knowledge graph.

- **Pacing and bounds** — curriculum pacing is a bound: too-fast difficulty spikes cause collapse, too-slow wastes cycles; competence metrics gate the step up.
- **Coverage** — the curriculum must cover the distribution that matters at deployment, including hard regions; easy-only curricula hide generalization gaps until they surface in production.
- **Difficulty estimation** — a competence metric (pass rate, task complexity) ranks tasks and triggers advancement; mis-estimation wastes cycles on too-easy tasks or collapses on too-hard ones.
- **Classic results** — curriculum learning improves convergence speed and final performance across RL and supervised tasks compared with random ordering, especially early in training.
- **Safety angle** — a curriculum that only explores easy regions hides goal misgeneralization until deployment; curricula should intentionally sample the hard, adversarial distribution.
- **RSIS3 analogy** — the pulse loop's escalating check-practices and staged passes are a curriculum for the knowledge graph: each pass raises the difficulty bar as the graph densifies.
## Related
- [[wiki/agent-systems/self-play|Self-Play]] — generates the experience to order
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — what the curriculum teaches
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — why pacing matters
- [[wiki/agent-systems/iterative-self-improvement|Iterative Self-Improvement]] — outer cycle
- [[wiki/concepts/robustness-training|Robustness Training]] — hardening via curriculum
- [[wiki/agent-systems/agent-loop|Agent Loop]] — host loop
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — how agents are evaluated in the graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
