---
type: "concept"
title: "Guardrails"
description: "Runtime validation, filtering, and policy layers that constrain LLM input, output, and tool use after generation"
tags: ["guardrails", "safety", "reliability", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://github.com/NVIDIA/NeMo-Guardrails", "https://www.guardrailsai.com/docs"]
---

# Guardrails

## Summary
Guardrails are the software layer around a model that validates inputs, outputs, and actions against policies — blocking unsafe content, enforcing formats, and limiting tool usage. They move safety from 'hope the model behaves' to 'enforce the contract in code'.

## Details
- NVIDIA NeMo Guardrails is an open framework for programmable rails: topical, safety, security, and fact-checking rails defined as Colang dialogue policies.
- Guardrails AI (guardrailsai.com) offers validators for output structure, PII, toxicity, and custom checks that run deterministically.
- Layering: input rails (before the model), output rails (after the model), and execution rails (around tool calls) cover the full loop.
- Guardrails complement, not replace, safety training: they catch failures that no model behavior will fully eliminate.
- Cost and latency trade-off: every rail is extra inference or code; rank rails by risk, and keep hot paths cheap.
- RSIS3 relevance: the L1 action loop's tool executions are exactly where rails pay off — least-privilege tool policies and output schema checks protect the host.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The attack class guardrails defend against
- [[wiki/ai-ml/jailbreaks|Jailbreaks]] — Guardrails catch what safety training misses
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — Output rails reinforce model-level refusals
- [[wiki/prompt-engineering/agentic-rails|Agentic Rails]] — Execution-level policy for agent tool use
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — The training-side complement to rails
- [[wiki/prompt-engineering/system-prompts|System Prompts]] — Rails enforce what the system prompt requests
- [[wiki/concepts/mykb-research-report|mykb Research Report: Personal LLM Wiki Systems — Methodologies, Architectures & Integration Blueprint]] — Safety research base for rail design
