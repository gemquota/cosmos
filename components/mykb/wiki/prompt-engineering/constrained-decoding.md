---
type: "concept"
title: "Constrained Decoding"
description: "Forcing generation to respect hard constraints such as schemas or grammars"
tags: ["constrained-decoding", "decoding", "constraints", "structured"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Constrained Decoding

## Summary

Constrained decoding forces generation to respect hard constraints — schemas, grammars, regexes, or banned tokens — at token-selection time rather than hoping prompts hold. It guarantees structural compliance by masking invalid tokens at every step. The technique matters because it converts unreliable prompt-following into deterministic output contracts for production systems. Constraints are a contract, and like any contract they need versioning and testing when requirements change.

## Details

- **Definition** — constrained decoding restricts the model's token choices during generation so the output satisfies declared constraints.
- **Mechanism** — at each step, a validator computes the set of tokens that can continue a valid prefix and blocks the rest.
- **Constraint types** — JSON schemas, formal grammars, regular expressions, prefix requirements, and length limits are common constraints.
- **Reliability gain** — constraints remove entire failure classes, such as malformed JSON, invalid SQL, or wrong output formats.
- **Costs** — decoding overhead and reduced token freedom are the tradeoffs; heavy constraints can slightly lower fluency.
- **Interaction with prompts** — constraints complement prompting: the prompt sets semantics, the decoder guarantees syntax.
- **Worked example** — a tool-calling pipeline constrains arguments to a JSON schema, so the agent can never emit a call the runtime cannot parse.
- **Failure modes** — over-constrained output rejects valid completions, and constraint bugs can silently corrupt generation.
- **Practical relevance** — constrained decoding is the enforcement layer of structured output, tool use, and agent contracts.
- **Tooling** — libraries and inference engines provide outline-style and grammar-based decoders for common formats.
- **Constraint testing** — validating the constraint implementation itself with edge cases prevents silent generation corruption.


## Related

- [[wiki/prompt-engineering/grammar-constrained-generation|Grammar-Constrained Generation]] — the grammar variant
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — the schema variant
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — the goal
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — the format family
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — the constraint source
- [[wiki/prompt-engineering/output-format-negotiation|Output Format Negotiation]] — the contract layer

