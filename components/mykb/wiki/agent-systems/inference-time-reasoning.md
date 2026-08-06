---
type: "concept"
title: "Inference-Time Reasoning"
description: "Reasoning elicited or searched at generation time rather than trained in"
tags: ["reasoning", "inference", "llm", "chain-of-thought"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2201.11903", "https://arxiv.org/abs/2305.10601"]
---

# Inference-Time Reasoning

## Summary
Inference-time reasoning is the family of techniques that make a model deliberate before answering — chain-of-thought prompting, step-by-step verification, and search over reasoning traces. It converted frozen models into much stronger reasoners without retraining.

## Details
- **CoT breakthrough** — 2022 chain-of-thought prompting unlocked multi-step math and logic in large models.
- **Search extension** — Tree of Thoughts and process-supervision methods explore multiple reasoning branches.
- **Efficiency** — reasoning tokens cost compute; models learn to trade depth against confidence.
- **Safety implications** — more reasoning can mean more transparent steps (good for oversight) or more covert planning (bad).
- **RSIS3 angle** — the pulse protocol is an inference-time reasoning system over the knowledge graph: deliberate phases before action.

- **Forms** — chain-of-thought prompting, self-consistency voting over sampled traces, tree search over reasoning branches, verifier-guided selection, and iterative repair all spend inference-time compute on better answers.
- **When to spend** — reasoning budgets should scale with task difficulty and stakes; easy or low-risk tasks do not need deep search, and a per-task compute allocator beats a fixed policy.
- **Relationship to training** — inference-time reasoning is complementary to trained reasoning: RL-trained models reason better per token, but search and verification can substitute for some training compute at deployment time.
- **Inspectability** — reasoning traces are inspectable in principle, which helps oversight, but models can also produce misleading or hidden traces; trace inspection needs the same skepticism as any other self-report.
- **Cost curve** — returns diminish: accuracy climbs steeply at first then flattens, so the practical question is where the curve meets the latency and cost budget.

- **Oversight interaction** — longer reasoning makes behavior less predictable per token; oversight designs that assume one-pass outputs (monitoring the final answer) must adapt to multi-step deliberation.

## Related
- [[wiki/agent-systems/test-time-compute|Test-Time Compute]] — the resource axis
- [[wiki/agent-systems/self-reflection-loops|Self-Reflection Loops]] — iterative reasoning
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — technique anchor
- [[wiki/agent-systems/covert-reasoning|Covert Reasoning]] — concealment risk
- [[wiki/concepts/oversight|Oversight]] — visibility into reasoning
- [[wiki/agent-systems/agent-loop|Agent Loop]] — host
- [[wiki/pulses/self-evaluation-scores|Self-Evaluation Scores]] — self-scored telemetry
