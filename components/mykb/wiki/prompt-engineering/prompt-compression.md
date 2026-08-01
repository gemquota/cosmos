---
type: "concept"
title: "Prompt Compression"
description: "Techniques for shrinking prompts — summarization, distillation, or learned compressors — while preserving task-relevant information"
tags: ["prompt-compression", "context-windows", "cost", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Prompt Compression

## Summary
Prompt compression reduces the token footprint of context to fit budgets, cut cost, and improve instruction-following. It is the practical answer when history or retrieved material outgrows the window.

## Details
- Approaches: extractive selection, LLM summarization, and learned compression models trained to reconstruct answers.
- Compression quality is task-dependent; aggressive compression destroys the evidence needed for reasoning.
- Best practice: compress early and often in agent loops instead of letting history grow unbounded.
- RSIS3 relevance: long RRP sessions are prime compression candidates before they are written into mykb.

## Related
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity constraint compression addresses
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The budget that compression keeps under control
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — The umbrella discipline
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Chains compress state between stages
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]] — Token-level basis of the budget
