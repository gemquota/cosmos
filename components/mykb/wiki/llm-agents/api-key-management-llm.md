---
type: "concept"
title: "API Key Management for LLMs"
description: "Storing, scoping, and rotating the credentials agents use to call LLM APIs"
tags: ["llm", "secrets", "api-keys", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/guides/error-codes", "https://platform.openai.com/docs/guides/rate-limits"]
---

# API Key Management for LLMs

## Summary
API key management for LLMs covers where keys live, how they are scoped, and how they rotate. Keys are the credentials that control spend and access, so they belong in a secrets manager, never in prompts, logs, or model contexts. Compromised keys are the most common LLM security incident.

## Details
- **Storage** — a secrets manager or vault injects keys into the runtime; prompts and traces must never contain them.
- **Scoping** — per-project keys, per-agent keys, and keys with spending caps limit blast radius and enable attribution.
- **Rotation** — scheduled rotation plus automatic rotation on suspected leakage; monitoring usage anomalies flags theft.
- **Worked example** — each agent service gets its own key with a monthly cap; the gateway signs requests and the audit log attributes spend to the key.
- **Threats** — api-key theft from logs, prompt extraction, or exposed environment files; key redaction in traces is mandatory.
- **mykb relevance** — RSIS3 and mykb pipelines call external LLM APIs, so key hygiene applies directly to their daemon runs.

## Related
- [[wiki/testing/api-key-theft|API Key Theft]] — theft of API keys
- [[wiki/security/secrets-management|Secrets Management]] — storing secrets safely
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — detecting keys leaked in prompts
- [[wiki/agent-systems/agent-runtime-security|Agent Runtime Security]] — runtime credential handling
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — quotas tied to keys
- [[wiki/testing/dependency-pinning-models|Dependency Pinning for Models]] — pin providers with keys
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — the API surface it uses
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — embeddings access
