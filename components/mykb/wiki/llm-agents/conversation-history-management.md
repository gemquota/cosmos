---
type: "concept"
title: "Conversation History Management"
description: "Deciding what conversation context to keep, compress, or drop across turns"
tags: ["history-management", "conversation", "context", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Conversation History Management

## Summary

Conversation history management decides what context to keep, compress, or drop across turns so the model has what it needs within its context window. It is the operational heart of long conversations. It matters because how history is managed determines both the quality and the cost of every subsequent turn. History management is where conversation quality meets token economics.

## Details

- **Definition** — History management curates the conversation record: retaining essentials, compressing the rest, and discarding what no longer matters.
- **Retention** — Full transcripts preserve fidelity but consume tokens; retention policies decide how much raw history survives.
- **Compression** — Summarization and extraction shrink old turns into durable facts while losing verbatim detail.
- **Recency bias** — Windows that keep only recent turns lose early constraints, goals, and commitments made long ago.
- **Structured state** — Extracted slots and goals survive compression, so dialog state persists even when the transcript is truncated.
- **Cost control** — Token budgets make history management a direct cost lever, not just a quality question.
- **Failure modes** — Summaries that drop constraints, verbatim spam that wastes the window, and injection risk in compressed content.
- **Practical relevance** — Agents with long-running loops depend on history management to stay coherent across many turns.
- **Token budgets** — Explicit budgets per history segment make the tradeoff between fidelity and cost visible.
- **Salience scoring** — Ranking past turns by relevance keeps high-value context even when the window shrinks.
- **Repair** — When a summary loses detail, the system should know it can re-read the raw transcript on demand.

## Related

- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — fitting context into the window
- [[wiki/prompt-engineering/context-compression|Context Compression]] — shrinking history without losing meaning
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — structured state beyond the transcript
- [[wiki/llm-agents/memory-hierarchy-agentic|Memory Hierarchy Agentic]] — tiers of memory in agents
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — risks in compressed history
