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

- **Signal requirement** — each cycle needs a trustworthy improvement signal (tests, verified answers, human feedback); without one, the loop optimizes noise and the system degrades while appearing to improve.
- **Evaluator ceiling** — improvement cannot exceed the evaluator's ability to recognize good output; improving the evaluator is often the highest-leverage cycle.
- **Diversity guard** — self-generated experience collapses toward what the system already does well; mixing in external data and novel tasks keeps the loop from narrowing.
- **Failure mode** — self-flattery loops: when the system evaluates its own output too generously, each cycle ratifies the previous one and errors compound quietly.
- **Deployment shape** — iterative self-improvement in production is staged and gated (improve, verify, roll back on regression), not a single unbroken ascent.

## Related
- [[wiki/pulses/recursive-improvement-loops|Recursive Improvement Loops]] — general loop shape
- [[wiki/agent-systems/self-play|Self-Play]] — generating experience
- [[wiki/agent-systems/curriculum-self-improvement|Curriculum Self-Improvement]] — ordering experience
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — the gate on each cycle
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — how passes become durable
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — prior pass experience
- [[wiki/agent-systems/agent-loop|Agent Loop]] — the base agent loop in the existing graph
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
