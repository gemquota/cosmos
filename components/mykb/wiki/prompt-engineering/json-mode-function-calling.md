---
type: "concept"
title: "JSON Mode and Function Calling"
description: "API features that constrain or route model output to structured JSON and tool invocations"
tags: ["function-calling", "structured", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# JSON Mode and Function Calling

## Summary
API features that constrain or route model output to structured JSON and tool invocations

## Details
- JSON mode guarantees syntactically valid JSON output; function calling declares callable tools.
- Tool schemas let the model emit arguments that the application executes safely.
- Both reduce parsing failures and are the backbone of agent tool use.
- They work best with explicit schemas and validation on the caller side.

## Related
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — broader family of guarantees
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — schema quality determines reliability
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — hard decoding approach
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — core primitive for agents
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — agreeing on shapes
