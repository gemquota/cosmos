---
type: "concept"
title: "Guardrails and Safety"
description: "Layers that constrain model and agent behavior to safe, policy-compliant outputs"
tags: ["safety", "guardrails", "policy", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2210.11610", "https://huggingface.co/docs/transformers/index"]
---

# Guardrails and Safety

## Summary
Guardrails are the layered controls — input filtering, refusal tuning, output validation, and policy enforcement — that keep model and agent behavior within safety bounds. They are defense in depth because no single layer is reliable. Guardrails sit at the boundary between model capability and organizational policy.

## Details
- **Input guardrails** — detect prompt injection, PII, and out-of-policy requests before they reach the model.
- **Output guardrails** — validate structure, redact sensitive content, and score toxicity or policy violations after generation.
- **Policy integration** — guardrail decisions are policy-as-code rules enforced at the gateway, not just prompt instructions.
- **Worked example** — a customer-facing agent runs every response through a classifier; flagged responses are blocked and routed to a human reviewer.
- **Costs** — every guardrail adds latency and false-positive friction; thresholds must be tuned against business impact.
- **mykb relevance** — guardrails, safety tuning, and agentic rails are existing mykb topics; RSIS3 policy enforcement applies them to its own loops.

## Related
- [[wiki/prompt-engineering/safety-tuning|Safety Tuning]] — safety in weights
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — refusal patterns
- [[wiki/ai-ml/guardrails|Guardrails]] — existing guardrails concept
- [[wiki/prompt-engineering/agentic-rails|Agentic Rails]] — rails for agents
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — related concept in this cluster
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — red-teaming practice
- [[wiki/ai-ml/safety-benchmarks|Safety Benchmarks]] — related concept in this cluster
