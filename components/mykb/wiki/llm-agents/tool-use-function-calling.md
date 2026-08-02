---
type: "concept"
title: "Tool Use and Function Calling"
description: "Giving models structured tools they can call by name with arguments"
tags: ["tools", "function-calling", "llm", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/function-calling", "https://docs.anthropic.com/en/docs/build-with-claude/tool-use"]
---

# Tool Use and Function Calling

## Summary
Function calling gives a model a catalog of typed tools and lets it emit structured calls the runtime executes. It converts language models from text generators into actors. The pattern is the backbone of every agentic system: the model proposes, the runtime validates and executes.

## Details
- **Schema** — tools are declared with JSON Schema: name, description, and typed parameters; good descriptions measurably improve call quality.
- **Execution flow** — the model returns a tool call, the runtime executes it, and the result returns as a new message; loops continue until the model produces a final answer.
- **Parallel calls** — models can emit several independent tool calls in one turn, cutting latency on fan-out tasks.
- **Worked example** — a weather agent receives "forecast Berlin", calls get_weather(city="Berlin"), then answers with the tool result.
- **Failure modes** — hallucinated arguments, wrong tool choice, and tool result bloat; mitigated by schema validation and structured output modes.
- **mykb relevance** — function calling and tool schemas are existing mykb topics, and RSIS3's sub-agents use tool calls for code changes and testing.

## Related
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — declaring tool schemas
- [[wiki/prompt-engineering/function-calling|Function Calling]] — existing function-calling concept
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — designing good tool schemas
- [[wiki/prompt-engineering/json-mode-function-calling|JSON Mode and Function Calling]] — structured call formats
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — choosing among tools
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — tool use patterns in mykb
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — validated model output
- [[wiki/prompt-engineering/tool-parallelism|Tool Parallelism]] — parallel tool calls
