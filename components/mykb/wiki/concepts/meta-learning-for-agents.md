---
type: "concept"
title: "Meta-Learning for Agents"
description: "Agents that learn how to learn, adapting quickly to new tasks"
tags: ["meta-learning", "agents", "adaptation", "learning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Meta-learning_(computer_science)", "https://arxiv.org/abs/1703.03400"]
---

# Meta-Learning for Agents

## Summary
Meta-learning for agents is learning at two levels: an inner loop learns a task quickly while an outer loop learns the learning procedure itself. MAML's 2017 formulation — learning initial weights that adapt fast — made the pattern standard, and it is the algorithmic heart of 'learn to learn' systems.

## Details
- **Inner/outer loops** — per-task training (inner) vs meta-objective over task distribution (outer).
- **Methods** — MAML (gradient-based), learned optimizers, memory-augmented networks, and in-context learning in LLMs.
- **Agent relevance** — meta-learned agents adapt to new environments, tools, and goals from few examples.
- **Risks** — meta-overfitting to the task distribution and fragile adaptation under distribution shift.
- **RSIS3 parallel** — reflection and practices are the triad's outer loop; each acquisition pass teaches the loop to learn better.

## Related
- [[wiki/concepts/learn-to-learn|Learn to Learn]] — the umbrella concept
- [[wiki/agent-systems/meta-cognition-in-agents|Meta-Cognition in Agents]] — the cognitive layer
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — the loop structure
- [[wiki/concepts/continual-self-improvement|Continual Self-Improvement]] — lifetime adaptation
- [[wiki/agent-systems/curriculum-self-improvement|Curriculum Self-Improvement]] — task-distribution design
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — existing concept
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — choosing states
- [[wiki/decisions/model-selection-practice|Model Selection in Practice]] — choosing configs
