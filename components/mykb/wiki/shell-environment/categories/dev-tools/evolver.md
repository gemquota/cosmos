---
type: "entity"
title: "Evolver"
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---
description: "A component that iteratively improves solutions through variation and selection"
tags: ["entity", "bash", "bootstrap", "bun", "ide", "json", "evolution", "optimization"]

# Evolver

## Summary
An evolver is a component that improves solutions iteratively by generating variations, evaluating them, and keeping the best. It matters because search spaces are too large to explore exhaustively, and evolution finds good regions cheaply. Evolvers underpin everything from hyperparameter tuning to strategy refinement in agent systems.

## Details
- **Definition** — an evolution loop mutates candidates, evaluates fitness, selects survivors, and repeats over generations.
- **Variation** — mutations and recombinations explore the space around existing solutions, balancing exploration against exploitation.
- **Fitness** — a clear scoring function is the entire compass; a bad fitness function evolves the wrong thing confidently.
- **Selection** — keeping the best candidates focuses effort, while some randomness prevents premature convergence.
- **Generations** — successive rounds refine solutions, and the trajectory of fitness scores shows whether progress is real.
- **Budget** — evolution needs explicit limits on generations, evaluations, and compute, or it runs forever.
- **Common failure modes** — fitness that rewards cheating the metric, premature convergence to a local optimum, and drift when the environment changes.
- **Worked example** — a prompt evolver varies system prompts, scores responses on a held-out set, and keeps the top variants across generations.
- **Practical relevance** — an evolver automates the tedious loop of trial and improvement, especially for prompts, parameters, and strategies.

- **Logging** — recording each generation's fitness enables analysis of convergence and stagnation.
- **Seeding** — starting from known-good candidates accelerates evolution compared to random initialization.
- **Constraints** — enforcing hard constraints during variation keeps candidates valid and saves wasted evaluations.
- **Reproducibility** — recording seeds and parameters lets any generation be replayed and its results audited.
- **Parallelism** — evaluating multiple candidates per generation spreads compute across machines and speeds convergence.
## Related
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — improving the improver
- [[wiki/agent-systems/skill-acquisition-loops|Skill Acquisition Loops]] — learning by iteration
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — fitness for agents
- [[wiki/testing/property-based-testing|Property-Based Testing]] — systematic variation
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — model-level optimization
- [[wiki/agent-systems/agent-factories|Agent Factories]] — generating variants
