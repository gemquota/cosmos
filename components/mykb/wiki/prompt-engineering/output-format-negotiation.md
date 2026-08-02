---
type: "concept"
title: "Output Format Negotiation"
description: "Agreeing on output structure between requester and model before generation"
tags: ["format-negotiation", "structured", "format", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Output Format Negotiation

## Summary
Agreeing on output structure between requester and model before generation

## Details
- Explicit format specs reduce parsing failures and rework.
- Negotiation covers schema, delimiters, and edge cases.
- Tooling enforces via constrained-decoding.
- Supports structured-output-generation.

## Related
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — enforcement
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — schema example
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — tool side
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — failure UX
