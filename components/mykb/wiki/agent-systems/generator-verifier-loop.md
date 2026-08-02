---
type: "concept"
title: "Generator-Verifier Loop"
description: "Pattern pairing a generating model with a verifying model to raise output quality"
tags: ["gen-verifier", "agents", "verification", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Generator-Verifier Loop

## Summary
Pattern pairing a generating model with a verifying model to raise output quality

## Details
- Generator proposes, verifier checks, loop repeats within bounds.
- Verifiers catch errors the generator cannot self-correct.
- Applied in code, reasoning, and retrieval tasks.
- Related to self-reflection-agents.

## Related
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — verification role
- [[wiki/agent-systems/critic-agents|Critic Agents]] — critique role
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — internal loop
- [[wiki/llm-agents/self-consistency-voting|Self-Consistency Voting]] — aggregation alternative
- [[wiki/agent-systems/code-repair-agents|Code Repair Agents]] — applied loop
