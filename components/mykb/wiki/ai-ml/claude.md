---
type: "concept"
title: "Claude"
description: "Anthropic's frontier LLM family, known for long contexts, safety research, and agentic tool use"
tags: ["claude", "anthropic", "llm", "models"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Claude

## Summary
Claude is Anthropic's assistant model family, built with a focus on safety, long context windows, and tool use. Its documentation and model cards are reference material for prompt and agent engineering, and it is one of the most commonly embedded frontier models in agentic systems.

## Details
Anthropic publishes detailed model cards, system-prompt guidance, and tool-use documentation for the Claude family, which makes it one of the best-documented frontier models from a practitioner standpoint. The family has evolved through several generations, each expanding context windows and improving long-horizon agentic behaviour. Writing, coding, and instruction-following have been the consistently strong areas, while the models are also notable for being trained heavily with preference methods and constitutional principles rather than raw scale alone.

The large context window is a defining operational feature. It lets agents load entire codebases, long conversation histories, or full document corpora into a single prompt, which removes the need for aggressive chunking in many workflows. The practical trade-off is that effective context use still demands good retrieval hygiene: dumping hundreds of thousands of tokens into a prompt increases latency and cost, and models still perform best when the most relevant material is placed near the query. Caching and careful prompt ordering matter as much as raw context capacity.

Claude's tool-calling support is a flagship capability and the main reason it appears in agent frameworks. Structured tool schemas, parallel tool calls, and explicit tool-result routing let an L1-style loop hand the model real actions rather than just text completions. Failure modes include malformed tool schemas, models hallucinating arguments when the schema is ambiguous, and loops where the model re-invokes the same failing tool without a corrective signal. Robust agent code therefore validates tool arguments, caps retries, and feeds errors back into the prompt.

Claude-class models are common backbones for agentic systems like RSIS3's L1 loops. For mykb, model cards are the practical artifact: they document context limits, known limitations, and safety boundaries, and they should be consulted when deciding which model class backs a loop, how large a context budget to grant, and what eval set to use for regression checks.

## Related
- [[wiki/ml-frameworks/anthropic-api|Anthropic API]] — The interface to Claude
- [[wiki/ai-ml/constitutional-ai|Constitutional AI]] — The alignment method behind it
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — A flagship Claude capability
- [[wiki/ai-ml/model-cards|Model Cards]] — Claude's documented limitations
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Frontier eval comparisons
