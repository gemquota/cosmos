---
type: "concept"
title: "Case-Based Reasoning"
description: "Solving new problems by retrieving and adapting similar past cases"
tags: ["case-based-reasoning", "memory", "retrieval", "reasoning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Case-Based Reasoning

## Summary
Case-based reasoning (CBR) solves problems by retrieving the most similar past cases from memory and adapting their solutions. It matters because it leverages experience directly instead of abstract rules. Modern RAG agents are CBR with learned retrieval and adaptation.

## Details
- Cycle: retrieve → reuse → revise → retain.
- Similarity metrics determine which cases surface.
- Retained new cases grow the memory — a learning loop.
- Open questions: adaptation quality for open-ended tasks.

## Related
- [[wiki/llm-agents/memory-augmented-agents|Memory-Augmented Agents]] — the memory substrate
- [[wiki/concepts/episodic-memory|Episodic Memory]] — the case store
- [[wiki/concepts/analogical-reasoning|Analogical Reasoning]] — the cognitive foundation
- [[wiki/llm-agents/rag-agent|RAG Agent]] — the modern implementation
- [[wiki/concepts/semantic-memory|Semantic Memory]] — abstractions distilled from cases
