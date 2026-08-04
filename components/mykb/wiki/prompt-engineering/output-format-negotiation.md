---
type: "concept"
title: "Output Format Negotiation"
description: "Agreeing on output structure between requester and model before generation"
tags: ["format-negotiation", "structured", "format", "contracts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Output Format Negotiation

## Summary

Output format negotiation is the practice of agreeing on the structure of a model's response before generation begins, through explicit format specifications in the prompt. The contract covers schemas, delimiters, and edge cases, reducing parsing failures and rework. It matters because downstream automation depends on reliably shaped output, and format failures are among the most common causes of broken LLM integrations. The negotiation should be visible to the model as part of the task description, not buried in a long system prompt.

## Details

- **Definition** — format negotiation establishes, up front, what the output will look like: its structure, field names, and allowed content.
- **Explicit contracts** — a well-specified format turns open-ended generation into a fillable structure, making outputs predictable.
- **Schema specification** — JSON schemas, XML templates, and markdown layouts each define a different contract with different parsing tradeoffs.
- **Delimiter conventions** — agreeing on separators and framing tokens prevents ambiguity between content and structure.
- **Edge cases** — negotiation covers empty results, error states, and out-of-range values so consumers know how to handle them.
- **Enforcement** — prompting alone is probabilistic; constrained decoding and schema decoding make the negotiated format a hard guarantee.
- **Worked example** — an integration requests "JSON with keys name, amount, currency; amounts as numbers; unknown values as null", and the model complies because the contract is explicit.
- **Failure modes** — vague format requests, conflicting examples, and silent format drift across model versions cause parsing failures.
- **Practical relevance** — format negotiation is the first line of defense for structured output, tool calling, and agent pipelines.
- **Relation to validation** — negotiated formats should be validated at runtime, with retry strategies for violations.
- **Format examples** — showing one complete example of the expected output teaches structure more reliably than describing it abstractly.


## Related

- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — enforcement approaches
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — the schema-based contract
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — the tool-side contract
- [[wiki/prompt-engineering/error-messages-llm|Error Messages for LLMs]] — handling format failures
- [[wiki/prompt-engineering/markdown-output-rendering|Markdown Output Rendering]] — a format choice
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — the XML contract

