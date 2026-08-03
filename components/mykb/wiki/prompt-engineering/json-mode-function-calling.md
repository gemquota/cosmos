---
type: "concept"
title: "JSON Mode and Function Calling"
description: "API features that constrain or route model output to structured JSON and tool invocations"
tags: ["function-calling", "structured", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# JSON Mode and Function Calling

## Summary
JSON mode guarantees syntactically valid JSON output; function calling declares callable tools with schemas so the model emits structured arguments the application executes safely. Both reduce parsing failures and are the backbone of agent tool use.

## Details
- Mechanism: JSON mode constrains the response to a valid JSON object (fields must be present in the prompt or schema); function calling presents tool schemas to the model, which emits a function-call message with arguments matching the schema; the application validates, executes, and returns a tool result in the next turn.
- Concrete example: an agent loop declares a search tool with an arguments schema; the model emits search(query, limit); the application validates the types, runs the search, and appends the results; a pipeline requests JSON mode with an explicit schema so downstream parsing never fails on malformed output.
- Failure modes: schemas too loose, so arguments are ambiguous or wrong; validation missing on the caller side, so malformed arguments reach execution; JSON mode producing valid JSON with semantically wrong values; function calling loops where the model never terminates (cap tool turns); schemas that drift from the real tool interface.
- Tradeoffs: structured output trades model flexibility for reliability — the schema constrains what the model can express; the alternative, free-text output with parsing, is fragile; the mature pattern is explicit schemas, caller-side validation, and bounded tool loops.
- Operational notes: validate every function call, version tool schemas, and log the call/result pairs for debugging.
- RSIS3 relevance: RSIS3's loops calling tools depend on the same structured contracts — schema quality determines whether loop steps fail cleanly or corrupt state.

## Related
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — broader family of guarantees
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — schema quality determines reliability
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — hard decoding approach
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — core primitive for agents
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — agreeing on shapes
