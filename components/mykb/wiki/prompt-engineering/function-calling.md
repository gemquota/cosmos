---
type: "concept"
title: "Function Calling"
description: "API support for declaring callable functions and having the model emit structured arguments to invoke them"
tags: ["prompt-engineering", "function-calling", "tools", "agents", "apis"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/function-calling", "https://arxiv.org/abs/2312.16171"]
---

# Function Calling

## Summary
Function calling lets a developer declare callable functions with JSON Schemas and lets the model return a structured call request instead of plain text when a function is relevant. The runtime then executes the function and feeds the result back, which is the core primitive of tool-using agents.

## Details
- The model never executes code; it emits a function name plus typed arguments, and the host application decides whether to run it.
- OpenAI's guide shows the full loop: declare tools, prompt the model, receive tool_calls, execute, and append tool results as a new message.
- Benchmarks in 'OpenAI Functions and Tools' show function-calling models outperform instruction-only prompting on structured tool tasks.
- Robustness notes: models can hallucinate arguments, call the wrong tool, or loop; schemas with enums and strict mode reduce that.
- Parallel function calling lets one turn emit several independent calls, cutting latency in multi-tool agents.
- RSIS3 relevance: the L1 action loop is literally a function-calling loop — each tool (exec, apply_patch, web_fetch) is a declared function mykb logs with its outcomes.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The vendor-neutral term for the same primitive
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — JSON Schema declarations behind every function
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — How agents choose among many declared functions
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — Standard transport for tool servers
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Tool arguments are schema-validated structured output
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Reference implementation of function calling
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Tool-call traces feed mykb enrichment
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Tool-call traces captured as wiki sources
