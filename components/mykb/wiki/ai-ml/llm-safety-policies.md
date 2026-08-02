---
type: "concept"
title: "LLM Safety Policies"
description: "Explicit policies defining what models and agents are allowed to do and say"
tags: ["safety", "policies", "governance", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/moderation", "https://arxiv.org/abs/2210.11610"]
---

# LLM Safety Policies

## Summary
LLM safety policies translate values into enforceable rules about content and behavior. They matter because models need consistent, testable boundaries — what to refuse, how to refuse, and how to handle edge cases. Policies are the contract between a deployment and its guardrails.

## Details
- **Policy scope** — harmful content, self-harm, disallowed actions, impersonation, and protected-group harms.
- **Enforcement** — refusal behavior, output filters, and post-hoc moderation backed by the policy text.
- **Worked example** — a customer-support assistant refuses refund manipulation requests, cites its policy, and offers the escalation path.
- **Testing** — safety-benchmarks and red-teaming validate that policies hold under attack.
- **mykb relevance** — personal agents need explicit policies about data use and action permissioning.
- **Worked example** — a customer-support assistant refuses refund manipulation requests, cites its policy, and offers the escalation path.
- **Versioning** — policies are versioned artifacts; output behavior changes when they change, so tests must track them.
- **Enforcement** — refusal behavior, output filters, and post-hoc moderation back the policy text at runtime.

## Related
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — guardrail system
- [[wiki/ai-ml/content-moderation-pipelines|Content Moderation Pipelines]] — filtering layer
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — refusal mechanics
- [[wiki/ai-ml/safety-benchmarks|Safety Benchmarks]] — testing policies
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — attacking policies
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — action policy
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — red-teaming practice
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — related concept in this cluster
