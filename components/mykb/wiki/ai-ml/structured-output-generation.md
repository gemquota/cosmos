---
type: "concept"
title: "Structured Output Generation"
description: "Guaranteeing model outputs conform to schemas, types, or grammars"
tags: ["structured-output", "schemas", "json", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/structured-outputs", "https://github.com/outlines-dev/outlines"]
---

# Structured Output Generation

## Summary
Structured output generation forces model responses into a defined schema — JSON, typed values, or grammar-constrained text — so downstream code can consume them safely. It converts probabilistic text into validated data. The strongest guarantees come from constrained decoding rather than prompting alone.

## Details
- **Approaches** — JSON mode (provider-level), JSON-schema decoding (grammar-guided sampling), and prompt-only instructions (weakest).
- **Mechanisms** — constrained decoding masks invalid tokens at each step so the output is valid by construction; tools like Outlines and guidance implement this.
- **Uses** — function-calling arguments, extraction pipelines, eval scoring, and agent state transitions all need reliable structure.
- **Worked example** — an extraction agent must return {name, amount, date}; schema decoding guarantees the types, and a validation pass checks semantics.
- **Tradeoffs** — constraints can degrade generation quality on open-ended content; they are best reserved for data-shaped outputs.
- **mykb relevance** — structured output and JSON mode are existing mykb topics; RSIS3 tool calls depend on schema-valid arguments.

## Related
- [[wiki/prompt-engineering/json-mode-function-calling|JSON Mode and Function Calling]] — JSON outputs for tool calls
- [[wiki/prompt-engineering/grammar-constrained-generation|Grammar-Constrained Generation]] — grammar decoding
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — schema-guided decoding
- [[wiki/prompt-engineering/structured-output|Structured Output]] — existing structured output concept
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — existing JSON mode
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — schemas for tools
- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — the decoding technique
- [[wiki/prompt-engineering/function-calling|Function Calling]] — structured calls
