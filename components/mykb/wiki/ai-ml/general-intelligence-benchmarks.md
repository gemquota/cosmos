---
type: "concept"
title: "General Intelligence Benchmarks"
description: "Suites aiming to measure broad cognitive skill rather than single tasks"
tags: ["benchmarks", "evaluation", "intelligence"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# General Intelligence Benchmarks

## Summary
General intelligence benchmarks are suites designed to measure broad cognitive skill rather than performance on a single task. They matter because narrow tests can be gamed by memorization, while broad suites give a more honest picture of capability. They are the standard tool for capability assessment and leaderboards. Broad suites measure capability breadth, which is not the same as deployability.

## Details
- **Definition** — a general benchmark aggregates diverse tasks spanning knowledge, reasoning, mathematics, coding, and instruction following into one score.
- **Examples** — widely used suites include MMLU, ARC, GPQA, and agentic generalist suites that combine many task types.
- **Why breadth helps** — coverage across domains reduces overfitting to any one task and gives a more transferable capability signal.
- **Correlation limits** — benchmark scores correlate with practical usefulness only imperfectly; real-world success depends on robustness, tools, and context.
- **Worked example** — a team compares two models across a general suite, finding one better overall but both failing the same reasoning cluster, which guides training effort.
- **Failure modes** — contamination from training data, benchmark saturation, and cultural or language bias distort comparisons.
- **Relation to other suites** — general benchmarks sit alongside specialized code-benchmarks, instruction-following-benchmarks, and safety-benchmarks.
- **Practical relevance** — general benchmarks are the backbone of llm-leaderboards and model capability tracking over time.
- **Contamination** — training-data overlap with benchmark items inflates scores and is hard to fully prevent.
- **Interpretation** — score deltas are more meaningful than absolute scores as models evolve.
- **Worked example** — a team tracks a general suite quarterly to see whether gains on new benchmarks transfer broadly.
- **Failure example** — a model that excels on a general suite still fails on the specific tool use the product needs.

## Related
- [[wiki/ai-ml/model-capabilities-frontier|Model Capabilities Frontier]] — what these benchmarks track
- [[wiki/ai-ml/code-benchmarks|Code Benchmarks]] — the specialized sibling
- [[wiki/ai-ml/instruction-following-benchmarks|Instruction-Following Benchmarks]] — behavioral axis
- [[wiki/ai-ml/llm-leaderboards|LLM Leaderboards]] — aggregation of scores
- [[wiki/ai-ml/safety-benchmarks|Safety Benchmarks]] — the safety axis
