---
type: "concept"
title: "Structured Output"
description: "Constraining an LLM to return machine-parseable, schema-validated responses instead of free text"
tags: ["prompt-engineering", "structured-output", "schemas", "reliability"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/structured-outputs"]
---

# Structured Output

## Summary
Structured output forces the model's response to conform to a declared schema (types, fields, nesting, sometimes enums and regex), so downstream code can parse it without error-prone heuristics. It is the difference between 'return a JSON list' and 'return exactly this schema, validated at generation time'.

## Details
- OpenAI's structured outputs mode guarantees responses match a supplied JSON Schema, including strict schema adherence and correct field types.
- Prompt-level techniques (asking for JSON, few-shot JSON exemplars) are probabilistic; schema-constrained generation is deterministic and is the production-grade option.
- Structured output pairs naturally with tool calling: tool arguments are themselves structured outputs with typed schemas.
- Common uses: extraction pipelines, form filling, eval harnesses, and any place where an LLM result flows into typed code.
- Design rules: keep schemas small, prefer enums over free strings, and reserve an error field so the model can report refusal or uncertainty inside the schema.
- RSIS3 relevance: pulse outcomes, RRP state transitions, and dashboard telemetry all require strict schemas, so structured output is the contract layer for mykb ingestion.

## Related
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — The looser precursor that guarantees JSON but not a schema
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Typed tool arguments as a structured-output use case
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — JSON Schema definitions that tools expose
- [[wiki/testing/golden-tests|Golden Tests]] — Schema-validated outputs are ideal golden-test subjects
- [[wiki/testing/eval-sets|Eval Sets]] — Eval scorers consume structured outputs
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Structured wiki entries feed the analysis engine
- [[wiki/prompt-engineering/message-format|Message Format]] — Messages carry structured outputs
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Schema-validated entries feed the wiki pipeline
