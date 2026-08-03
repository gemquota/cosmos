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

## Long-Horizon Techniques
Anthropic's "Effective context engineering for AI agents" details three techniques for tasks whose token count exceeds the context window:
- **Context rot** — as tokens in the window increase, the model's recall and long-range reasoning degrade (n² pairwise attention relationships, training distributions dominated by short sequences); context is a finite resource with diminishing marginal returns, not a hard cliff.
- **Compaction** — summarizing a conversation nearing the limit and reinitiating with the summary; the art is selecting what to keep, and the safest lightweight form is clearing redundant tool results.
- **Structured note-taking (agentic memory)** — writing notes to a persistent store outside the window and pulling them back later; Claude playing Pokémon shows maps, tallies, and strategy notes surviving context resets.
- **Sub-agent architectures** — specialized sub-agents explore with clean windows and return condensed summaries (1,000-2,000 tokens), isolating search context from the lead agent.
- **Just-in-time retrieval** — maintaining lightweight identifiers (file paths, queries, URLs) and loading data at runtime via tools, instead of pre-embedding everything up front; a hybrid (CLAUDE.md dropped in, glob/grep fetched live) balances speed and freshness.
- **Right altitude** — prompts that are neither brittle if-else scaffolds nor vague guidance; organize into labeled sections (background, instructions, tool guidance, output description) and curate diverse canonical examples rather than laundry-list edge cases.
