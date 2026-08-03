---
type: "concept"
title: "Tool Schemas"
description: "JSON Schema declarations describing a tool's name, description, and typed arguments for LLM tool calling"
tags: ["tool-schemas", "tool-calling", "json-schema", "agents"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Tool Schemas

## Summary

Tool schemas are the JSON Schema descriptions that teach a model what functions exist and how to call them: names, parameter types, descriptions, and constraints. Schema quality is the single biggest lever on tool-calling reliability — it is the model's API documentation.

## Details
- Mechanism: schemas ride in the request (tools parameter on chat completions, native tools on Gemini/Claude); the model returns structured calls referencing tool names and argument objects; the runtime validates arguments against the schema before execution; strict modes (json_schema, forced tool choice) constrain output; descriptions guide selection, parameter semantics guide filling.
- Concrete example: a search tool schema declares query (string, required, described), filters (enum), and limit (integer 1-50); clear descriptions make the model choose it over a vague sibling; strict mode guarantees parseable calls; the failure pattern is schemas so loose the model invents parameters or so terse it misuses them.
- Failure modes: description drift — schemas that do not match implementations; ambiguous/overlapping tool names causing wrong routing; overly strict validation rejecting legitimate model calls; and injection through tool arguments (a "filename" parameter that can hold a path traversal unless validated).
- Operational tradeoffs: schema quality trades authoring effort for routing accuracy and safety; the discipline is schema-first tool design, validation at the boundary, logging actual calls against schema expectations, and iterating descriptions based on observed misroutes.
- RSIS3/mykb relevance: the wiki's tool registry would be schema-first; this note records the conventions (descriptions, enums, validation) the loop would apply to every new tool.
- Schema iteration: log every schema-validation failure and misroute; those events are the data that tells you which descriptions or enums to fix.
- Security: treat tool arguments as untrusted input — schema validation is not sanitization; apply allowlists and path checks at the tool boundary.

## Related
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — The capability schemas enable
- [[wiki/prompt-engineering/function-calling|Function Calling]] — The API pattern using schemas
- [[wiki/prompt-engineering/structured-output|Structured Output]] — The same schema discipline for outputs
- [[wiki/prompt-engineering/tool-selection|Tool Selection]] — Good schemas make selection reliable
- [[wiki/prompt-engineering/model-context-protocol|Model Context Protocol]] — MCP standardizes tool schemas
