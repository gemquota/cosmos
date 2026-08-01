---
type: "concept"
title: "Context Windows"
description: "The maximum number of tokens a model can attend to in a single forward pass and conversation"
tags: ["context-windows", "llm", "architecture", "memory"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/models", "https://docs.anthropic.com/en/docs/about-claude/models/overview"]
---

# Context Windows

## Summary
The context window is the model's working memory: the token budget shared by system prompt, conversation history, retrieved material, and generated output. Window size has grown from GPT-3's 2K tokens to hundreds of thousands, but effective use still requires budgeting, not just capacity.

## Details
- Input and output share the window; a 128K window with 8K max output leaves 120K for inputs.
- Long windows degrade retrieval precision: relevant evidence can drown in filler, so positioning and retrieval still matter.
- OpenAI and Anthropic model overview pages publish current context sizes per model (e.g., 128K-1M ranges across the 2025-2026 model lines).
- Attention cost is superlinear in sequence length, so long contexts cost more in compute and price even when they fit.
- Context engineering strategies — summarization, retrieval, compression — matter more as windows grow.
- RSIS3 relevance: mykb retrieval must fit within the window; session memory is window-managed, and pulse telemetry tracks usage per call.

## Related
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — The practical allocation discipline for the window
- [[wiki/prompt-engineering/context-engineering|Context Engineering]] — Techniques for making the window carry the right information
- [[wiki/prompt-engineering/prompt-compression|Prompt Compression]] — Shrinking material to fit the window
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — Fetching relevant slices instead of loading everything
- [[wiki/prompt-engineering/message-format|Message Format]] — How turns consume window tokens
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — Window growth tracks model-scale trends
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Wiki retrieval sized for window constraints
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Retrieval sized to the window in the wiki loop
