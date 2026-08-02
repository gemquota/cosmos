---
type: "concept"
title: "Prompt Engineering Fundamentals"
description: "Core principles and techniques for designing prompts that reliably produce good outputs"
tags: ["prompt-engineering", "prompting", "fundamentals", "techniques"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/prompt-engineering", "https://www.promptingguide.ai/"]
---

# Prompt Engineering Fundamentals

## Summary
Prompt engineering is the practice of writing instructions that make language models behave predictably. It matters because prompts are the primary interface to model capability — small wording changes swing quality. Fundamentals cover clarity, context, examples, and iteration.

## Details
- **Principles** — be specific, provide context, break tasks into steps, show examples, and constrain output format.
- **Techniques** — chain-of-thought, few-shot examples, role framing, and structured output requests.
- **Worked example** — an extraction prompt: define the schema, give two filled examples, then the document, and request JSON.
- **Process** — iterate against golden-test-sets rather than vibes; version every prompt.
- **mykb relevance** — RSIS3 prompt hygiene directly controls knowledge-synthesis quality.
- **Worked example** — an extraction prompt defines the schema, gives two filled examples, then the document, and requests JSON.
- **Iteration** — change one variable at a time and measure against golden-test-sets.
- **Principles** — be specific, provide context, break tasks into steps, show examples, and constrain the output format.

## Related
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — reasoning technique
- [[wiki/ai-ml/few-shot-and-in-context-learning|Few-Shot and In-Context Learning]] — example technique
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — context design
- [[wiki/prompt-engineering/system-prompt-design|System Prompt Design]] — system layer
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — version control
- [[wiki/prompt-engineering/prompt-testing|Prompt Testing]] — evaluation
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — the curation pipeline
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — context budgeting
