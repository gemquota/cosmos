---
type: "concept"
title: "Tool Schemas"
description: "JSON Schema declarations describing a tool's name, description, and typed arguments for LLM tool calling"
tags: ["tool-schemas", "tool-calling", "json-schema", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Tool Schemas

## Summary
Tool schemas are the machine-readable contracts models use to emit valid tool calls: name, description, and a JSON Schema of arguments. Schema quality is the single biggest lever on tool-calling reliability.

## Details
- Fields: type, function name, description, parameters with types/enums/required lists.
- Strict mode enforces that arguments exactly match the schema, killing hallucinated fields.
- Descriptions should state when and why to call the tool, not just what it does.
- RSIS3 relevance: RSIS3's L1 tool registry (exec, apply_patch, web_fetch) is defined as tool schemas mykb can version.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The capability schemas enable
- [[wiki/prompt-engineering/function-calling|Function Calling]] — The API pattern using schemas
- [[wiki/prompt-engineering/structured-output|Structured Output]] — The same schema discipline for outputs
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — Good schemas make selection reliable
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP standardizes tool schemas
