---
type: "concept"
title: "Generator-Verifier Loop"
description: "Pattern pairing a generating model with a verifying model to raise output quality"
tags: ["gen-verifier", "agents", "verification", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Generator-Verifier Loop

## Summary
The generator-verifier loop pairs a generating model with a verifying model to raise output quality through iterative checks. It matters because a generator alone cannot reliably detect its own errors, while a separate verifier provides an independent check. The loop turns one-shot generation into a bounded, quality-gated process. The loop's power comes from the verifier's independence, not its intelligence alone.

## Details
- **Definition** — the pattern has a generator propose output and a verifier check it, repeating within budget until the output passes or time runs out.
- **Why separate roles** — a verifier with different context, instructions, or a different model catches errors the generator cannot self-correct.
- **Termination** — the loop needs explicit stop conditions: pass, maximum iterations, or quality-threshold met, so it cannot run forever.
- **Applications** — the pattern is applied to code, reasoning, retrieval, and content tasks wherever a checkable quality signal exists.
- **Relation to self-reflection** — self-reflection-agents run the same idea internally in one model; the generator-verifier split is the multi-model, more independent variant.
- **Worked example** — a generator drafts a SQL query; the verifier checks it against the schema, catches a missing join, and the generator revises before submission.
- **Failure modes** — a verifier that shares the generator's blind spots, over-lenient checks, and unbounded loops are the classic failures.
- **Practical relevance** — the loop is the backbone of verifier-agents and critic-agents in production agent systems.
- **Budgeting** — iteration budgets prevent the loop from becoming an infinite refinement spiral.
- **Verifier diversity** — different models or prompts for verification reduce shared blind spots.
- **Worked example** — a reasoning task repeats at most three times, with each round passing the verifier's critique to the generator.
- **Failure example** — a verifier that always passes makes the loop a costly single pass.

## Related
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — the checking half of the loop
- [[wiki/agent-systems/critic-agents|Critic Agents]] — the feedback-giving variant
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — the single-model alternative
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — aggregation instead of iteration
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — a concrete application of the loop
