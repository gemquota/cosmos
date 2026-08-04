---
type: "entity"
title: "OpenAI API"
description: "OpenAI's hosted API surface: chat completions, embeddings, fine-tuning, and tool calling"
tags: ["openai-api", "apis", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# OpenAI API

## Summary

The OpenAI API is the reference hosted LLM interface: chat completions, embeddings, fine-tuning, structured outputs, and tool calling, with exact token accounting. Its conventions became the de-facto wire standard other providers and local runtimes clone.

## Details
- Mechanism: the API surface includes chat completions (messages → completion), responses (unified endpoint), embeddings, fine-tuning, and assistants/batches; parameters cover sampling, response_format (json_schema), tools, and streaming; usage fields return exact prompt/completion token counts; API keys are bearer-scoped and auditable per key.
- Concrete example: the wiki's loop would call chat completions with a tool schema for note operations and json_schema output for structured extractions; streaming would render token-by-token in the dashboard; batch API would process large offline jobs at lower cost with delayed completion.
- Failure modes: cost drift from unbounded token usage (cap context and log usage per call); prompt injection through user content (treat all message content as untrusted); model-version drift when "gpt-4o" style aliases move; and key hygiene — keys in configs leaking is the top incident class.
- Operational tradeoffs: hosted APIs trade per-token cost and data egress for zero infrastructure; the pattern is provider abstraction (OpenAI-compatible adapters) so the same prompting and tooling run on local and alternative endpoints, with cost telemetry per model.
- RSIS3/mykb relevance: the wiki's L1 loop would target OpenAI-compatible endpoints across hosted and local runtimes, recording usage so model choice stays cost-informed.
- Retry semantics: transient failures (429, 5xx, timeouts) need jittered backoff with Retry-After respect; idempotency keys prevent duplicate side-effecting calls.
- Evaluation loop: log prompts, completions, and human/automated scores per call to build a dataset for regression testing before model or prompt changes.
- Context discipline: keep the system prompt lean and put dynamic content where caching applies; token spend per turn is the unit the loop budgets.
- Governance: scope API keys per environment with usage alerts, and route key rotation through the parameter store rather than config files.

## Related
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The core endpoint
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — Vector retrieval endpoint
- [[wiki/ai-ml/gpt-4|GPT-4]] — The flagship models served
- [[wiki/prompt-engineering/function-calling|Function Calling]] — Tool support in the API
- [[wiki/prompt-engineering/json-mode|JSON Mode]] — Structured output modes
