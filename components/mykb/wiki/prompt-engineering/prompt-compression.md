---
type: "concept"
title: "Prompt Compression"
description: "Techniques for shrinking prompts — summarization, distillation, or learned compressors — while preserving task-relevant information"
tags: ["prompt-compression", "context-windows", "cost", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Prompt Compression

## Summary
Prompt compression reduces the token footprint of context to fit budgets, cut cost, and improve instruction-following. It is the practical answer when history or retrieved material outgrows the window — compress early and often instead of letting context grow unbounded.

## Details
- Approaches: extractive selection keeps the highest-value passages; LLM summarization distills while preserving key facts; learned compression models are trained to reconstruct answers from compressed context; the right choice depends on whether the task needs exact evidence or gist.
- Mechanism: in agent loops, old turns are summarized into a running digest, retrieved passages are deduplicated and trimmed, and raw tool output is reduced to essentials; the compressed context replaces the original for subsequent turns.
- Concrete example: a 50-turn session is compressed to a 5-turn digest plus pointers; a RAG prompt keeps the top-3 passages with sentence-level trimming instead of full documents; a long RRP session is summarized before being written to the wiki.
- Failure modes: aggressive compression destroying the evidence needed for reasoning (a key number or quote lost); summaries that hallucinate details; compression applied per-turn without a policy, causing drift; measuring tokens after compression but forgetting the summarization cost itself.
- Tradeoffs: compression trades fidelity for budget and cost — the tighter the compression, the more information loss; the alternative, unbounded context, is faithful and expensive; the mature pattern is tiered retention (verbatim recent, summarized history) with compression quality evals.
- Operational notes: eval compressed-context tasks against full-context baselines, and log compression ratios.
- RSIS3 relevance: long RRP sessions are prime compression candidates before they are written into mykb — distillation is compression with a curation intent.

## Related
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity constraint compression addresses
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The budget that compression keeps under control
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — The umbrella discipline
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Chains compress state between stages
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]] — Token-level basis of the budget
