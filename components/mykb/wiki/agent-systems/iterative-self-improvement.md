---
type: "concept"
title: "Iterative Self-Improvement"
description: "Repeatedly using one's own outputs to get better at a task"
tags: ["self-improvement", "agents", "bootstrapping", "reflection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Recursive_self-improvement", "https://arxiv.org/abs/2303.17651"]
---

# Iterative Self-Improvement

## Summary
Iterative self-improvement is the practice of using a system's own outputs — solutions, feedback, distilled data — to improve its later performance, cycle by cycle. It is the bounded, non-runaway cousin of recursive self-improvement and is already visible in LLM training pipelines and agent loops.

## Details
- **Examples** — self-distillation, expert iteration in AlphaZero, Reflexion's memory of past attempts, and RLHF's preference loops.
- **Key requirement** — each cycle needs a trustworthy signal that improvement actually happened.
- **Boundary** — improvement is limited by the evaluator's ceiling and by the diversity of generated experience.
- **Scaling** — self-play and curriculum generation expand experience cheaply but risk distribution collapse.
- **RSIS3 angle** — acquisition passes like this one are iterative self-improvement of the knowledge graph: each pass is evaluated against the wiki's link and practice checks.

## Related
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — general loop shape
- [[wiki/agent-systems/self-play|Self-Play]] — generating experience
- [[wiki/agent-systems/curriculum-self-improvement|Curriculum Self-Improvement]] — ordering experience
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the gate on each cycle
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — how passes become durable
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — prior pass experience
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
