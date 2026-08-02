---
type: "concept"
title: "Tool Schema Design"
description: "Designing the JSON schemas that describe tools to models for reliable function calling"
tags: ["tools", "schemas", "function-calling", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/function-calling", "https://docs.anthropic.com/en/docs/build-with-claude/tool-use"]
---

# Tool Schema Design

## Summary
Tool schemas are the interface between a model and your functions: names, descriptions, parameters, and constraints. They matter because model reliability depends on schema clarity — ambiguous schemas cause wrong calls. Good schemas are the cheapest quality win in agent systems.

## Details
- **Principles** — short unambiguous names, rich descriptions, required fields, enums, and examples in descriptions.
- **Common failure** — overlapping tool purposes or vague parameter descriptions produce hallucinated arguments.
- **Worked example** — a calendar tool declares `create_event` with required `start_time` ISO format and enum `calendar`; the model calls it correctly at 98%.
- **Iteration** — log real calls, find failure patterns, and refine schemas like code.
- **mykb relevance** — RSIS3 tool schemas should follow the same discipline for knowledge actions.
- **Worked example** — a calendar tool declares create_event with required start_time in ISO format and an enum calendar; the model calls it correctly at 98%.
- **Iteration** — log real calls, find failure patterns, and refine schemas like code.

## Related
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — calling mechanism
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — schema enforcement
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — schema discipline
- [[wiki/agent-systems/tool-selection-policies|Tool Selection Policies]] — selection rules
- [[wiki/agent-systems/agent-testing-strategies|Agent Testing Strategies]] — schema testing
- [[wiki/prompt-engineering/function-calling|Function Calling]] — API surface
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — structured output mode
