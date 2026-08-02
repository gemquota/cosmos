---
type: "concept"
title: "Stop Sequences"
description: "Explicit token strings that terminate generation when the model emits them"
tags: ["decoding", "control", "generation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Stop Sequences

## Summary
Explicit token strings that terminate generation when the model emits them

## Details
- Stop sequences cut output at a defined boundary, such as newline or JSON closing brace.
- They make outputs parseable and prevent runaway continuation.
- Should be tested against model outputs since whitespace variants occur.
- A cheap, deterministic complement to sampling controls.

## Related
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — schema-level sibling of stop control
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — agreement on boundaries
- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — harder constraint mechanism
- [[wiki/prompt-engineering/json-mode-function-calling|JSON Mode and Function Calling]] — typical stop sequence use
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — recovering from cut-off output
