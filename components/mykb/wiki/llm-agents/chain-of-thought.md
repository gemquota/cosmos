---
type: "concept"
title: "Chain of Thought"
description: "Prompting models to reason step by step before answering"
tags: ["chain-of-thought", "reasoning", "prompting", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2201.11903", "https://arxiv.org/abs/2205.11916"]
---

# Chain of Thought

## Summary
Chain of thought elicits intermediate reasoning steps from a model before the final answer, improving performance on multi-step problems. It matters because it makes reasoning visible, auditable, and partially correctable. It is the baseline for most reasoning-adjacent agent techniques.

## Details
- **Mechanism** — few-shot examples with worked steps, or explicit "think step by step" instructions, shift the model into a stepwise mode.
- **Benefits** — better accuracy on arithmetic, logic, and planning; errors become inspectable intermediate steps.
- **Costs** — more output tokens and latency; verbose chains burn budget and can overfit prompt phrasing.
- **Variants** — self-consistency samples many chains and votes; tree of thought explores multiple branches; zero-shot CoT is the cheap default.
- **Worked example** — a debt-migration agent reasons: current state, target state, gaps, then a step order — each line visible in the log.
- **mykb relevance** — chain of thought is an existing mykb topic and the substrate for RSIS3's visible reasoning phases.

## Related
- [[wiki/prompt-engineering/multi-step-reasoning|Multi-Step Reasoning]] — existing reasoning concept
- [[wiki/prompt-engineering/step-back-prompting|Step-Back Prompting]] — abstracting before stepping through
- [[wiki/prompt-engineering/prompt-engineering-fundamentals|Prompt Engineering Fundamentals]] — the prompting home of CoT
- [[wiki/ai-ml/calibration-and-confidence|Calibration and Confidence]] — confidence over chains
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — related concept in this cluster
- [[wiki/prompt-engineering/tree-of-thoughts-variants|Tree of Thoughts Variants]] — related concept in this cluster
- [[wiki/llm-agents/tree-of-thought|Tree of Thought]] — reasoning search
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
