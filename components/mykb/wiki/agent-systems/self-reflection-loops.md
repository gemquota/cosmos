---
type: "concept"
title: "Self-Reflection Loops"
description: "Agents that examine their own outputs and improve on the next attempt"
tags: ["reflection", "agents", "llm", "self-improvement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2303.11366", "https://arxiv.org/abs/2303.17651"]
---

# Self-Reflection Loops

## Summary
A self-reflection loop is an agent architecture where the model produces an output, critiques it (itself or via a critic), and revises. Reflexion (2023) and Self-Refine (2023) showed this loop measurably improves reasoning and code generation tasks.

## Details
- **Reflexion** — verbal self-feedback stored in memory and reused on the next attempt, evaluated in coding and decision-making tasks.
- **Self-Refine** — a single model generates, critiques, and refines iteratively without extra training.
- **Where it works** — tasks with verifiable feedback (compilation, tests, retrieval hits); it is weaker on open-ended quality.
- **Limits** — self-critique without external signal can amplify biases; loop depth has diminishing returns.
- **RSIS3 parallel** — the pulse protocol's reflection phase is a self-reflection loop: past pulses and checkpoints inform the next planning cycle.

- **Termination** — bound the loop by depth, budget, or convergence (two consecutive revisions with no change); unbounded reflection is a cost bug.
- **Memory** — the strongest variants persist reflections across sessions (Reflexion), so lessons from one task carry into the next instead of being lost.
- **Risk** — without an external signal, each reflection pass can amplify an initial error; the loop needs a ground-truth check at least at the end.
- **Diminishing returns** — most improvement comes in the first one or two revision passes; later passes mostly re-word, so budget accordingly.

- **Variants** — the loop can be internal (model critiques its own draft), tool-grounded (compiler or tests critique), or population-based (critic models review); reliability rises in that order.

## Related
- [[wiki/agent-systems/reflection-agents|Reflection Agents]] — the architecture family
- [[wiki/agent-systems/self-critique|Self-Critique]] — the critique step
- [[wiki/agent-systems/self-correction|Self-Correction]] — the repair step
- [[wiki/agent-systems/recursive-feedback-loops|Recursive Feedback Loops]] — the general pattern
- [[wiki/syntheses/lessons-to-actions|Lessons to Actions]] — turning reflection into change
- [[wiki/agent-systems/agent-loop|Agent Loop]] — host loop
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — how agents are evaluated in the graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
- [[wiki/pulses/self-benchmarking|Self-Benchmarking]] — internal benchmarks
