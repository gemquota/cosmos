---
type: "concept"
title: "Context Engineering"
description: "Deliberately designing what goes into a model's context — prompts, retrieval, memory, and structure — to maximize output quality"
tags: ["context-engineering", "prompt-engineering", "retrieval", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Context Engineering

## Summary
Context engineering treats the context window as a designed system rather than a passive buffer: choosing, ordering, and formatting information for the task at hand. It unifies prompting, retrieval, memory, and compression under one discipline.

## Details
- Ordering matters: instructions and key evidence placed early or late can dominate behaviour; recency effects are real.
- Includes retrieval strategy (what to fetch), memory policy (what to persist), and formatting (what structure helps).
- Concretely: system prompt, few-shot exemplars, retrieved passages, tool results, and conversation history are all context-design decisions.
- RSIS3 relevance: the L1 loop's context assembly — pulse context, wiki retrieval, tool results — is context engineering in action.

## Related
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The retrieval side of context design
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The resource being engineered
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — The compression side of context design
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The allocation framework
- [[wiki/prompt-engineering/in-context-learning|In-Context Learning]] — Why context content drives behaviour
