---
type: "concept"
title: "JSON Mode"
description: "An API mode that guarantees the model returns valid JSON, removing the need for fragile text parsing"
tags: ["prompt-engineering", "json", "apis", "structured-output"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/json-mode"]
---

# JSON Mode

## Summary
JSON mode instructs the API to guarantee that the completion parses as valid JSON, which eliminates the most common parsing failure in LLM pipelines. It does not enforce a particular schema — that is the job of structured outputs — so callers must still validate shape.

## Details
- Guarantees syntactic validity: the model is constrained so the output is always parseable JSON.
- Still schema-agnostic: the caller must check required keys, types, and nesting, or pair JSON mode with prompt-level instructions.
- Works best when the prompt says 'return JSON' and includes an example of the expected shape; the API also requires the word 'JSON' to appear in the messages.
- Failure modes shift from parse errors to semantic errors: valid JSON with wrong or missing fields.
- RSIS3 relevance: dashboard data.json, pulse telemetry, and knowledge-graph edges are JSON artifacts, so JSON mode is the workhorse for mykb/RSIS3 ingestion endpoints.

## Related
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Schema-enforced evolution of JSON mode
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — JSON Schema defines tool argument contracts
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Function arguments are returned as JSON
- [[wiki/prompt-engineering/message-format|Message Format]] — JSON payloads flow inside chat messages
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Parsing success is a baseline eval metric
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — JSON ingestion endpoints implemented in the mykb buildout
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — JSON artifacts feed wiki analysis
