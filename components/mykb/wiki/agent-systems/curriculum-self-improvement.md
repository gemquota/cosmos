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

## Related
- [[wiki/agent-systems/self-play|Self-Play]] — generates the experience to order
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — what the curriculum teaches
- [[wiki/agent-systems/bounded-agents|Bounded Agents]] — why pacing matters
- [[wiki/agent-systems/iterative-self-improvement|Iterative Self-Improvement]] — outer cycle
- [[wiki/concepts/robustness-training|Robustness Training]] — hardening via curriculum
- [[wiki/agent-systems/agent-loop|Agent Loop]] — host loop
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — how agents are evaluated in the graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
