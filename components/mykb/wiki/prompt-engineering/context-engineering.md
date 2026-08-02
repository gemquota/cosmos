---
type: "concept"
title: "Context Engineering"
description: "The discipline of designing, assembling, and maintaining the context given to a model"
tags: ["context", "prompting", "engineering", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents", "https://platform.openai.com/docs/guides/prompt-engineering"]
---

# Context Engineering

## Summary
Context engineering treats the model context as a designed artifact: what information is included, in what order, at what granularity. It matters because context determines output quality more than any other prompt lever. Good context engineering reduces hallucination, cost, and latency simultaneously.

## Details
- **Design dimensions** — content selection, ordering, formatting, repetition, and freshness.
- **Layers** — system prompt, task instructions, retrieved evidence, conversation history, and tool results.
- **Worked example** — for a support bot: system rules, then condensed history, then top-3 retrieved articles, then the user question, each section delimited and labeled.
- **Measurement** — ablation tests vary one context dimension at a time against golden-test-sets.
- **mykb relevance** — mykb retrieval is context engineering: the right knowledge in the right order beats a bigger model.
- **Worked example** — for a support bot: system rules, condensed history, top-3 retrieved articles, then the user question, each section delimited and labeled.
- **Measurement** — ablation tests vary one context dimension at a time against golden-test-sets to find what actually moves quality.

## Related
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — budgeting
- [[wiki/prompt-engineering/agentic-context-crafting|Agentic Context Crafting]] — agent variant
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — retrieval into context
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — grounded output
- [[wiki/prompt-engineering/system-prompt-design|System Prompt Design]] — system layer
- [[wiki/prompt-engineering/context-injection|Context Injection]] — related concept in this cluster
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation pipeline
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — context budgeting
