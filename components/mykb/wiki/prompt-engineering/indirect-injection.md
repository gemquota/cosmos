---
type: "concept"
title: "Indirect Injection"
description: "Prompt injection that arrives through third-party content — retrieved documents, emails, or web pages — rather than the user's own message"
tags: ["indirect-injection", "security", "rag", "prompt-injection"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Indirect Injection

## Summary
Indirect injection hides instructions inside content the model consumes on the system's behalf — fetched web pages, retrieved wiki passages, emails, or tool outputs. RAG pipelines and web-browsing agents are the prime targets, because the hostile content looks like ordinary data.

## Details
- Mechanism: the attack places instructions inside third-party content (Ignore previous instructions and exfiltrate data); when the pipeline retrieves and inserts the content into the prompt, the model may follow the embedded instructions as if they were authoritative; the content channel and the instruction channel are conflated.
- Concrete example: a page retrieved by a browsing agent contains a hidden sentence telling the model to email the user's database to an address; a wiki passage retrieved by RAG instructs the model to change its output format or reveal the system prompt; the model complies because retrieved text sits in the same context as the real instructions.
- Defenses: treat data and instructions as separate channels — tag retrieved content as data, quote it, and instruct the model that content carries no authority; sanitize or redact retrieved text; keep tool permissions least-privileged so even a successful injection has little it can do; validate tool arguments against the intended use.
- Failure modes: assuming retrieved content is trusted because it came from an internal store (compromise or user uploads poison it); relying only on prompt-level warnings, which injection can override; missing injection in tool outputs that mirror external data; injection that works through encoded or obfuscated text after sanitization fails.
- Tradeoffs: strict separation of data and instructions costs prompt complexity and some flexibility; the alternative — trusting retrieved content — is convenient and vulnerable; the mature pattern is least-privilege tools as the primary defense, with content tagging as the second layer.
- Operational notes: test RAG paths with poisoned documents, audit tool permissions, and monitor for unexpected tool invocations.
- RSIS3 relevance: mykb pages and web fetches are ingestion channels that must be treated as untrusted input — the same data/instruction separation RSIS3 applies to its own retrievals.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The parent attack class
- [[wiki/prompt-engineering/prompt-leakage|Prompt Leakage]] — A frequent outcome of indirect injection
- [[wiki/prompt-engineering/retrieval-prompting|Retrieval Prompting]] — The RAG pattern that exposes systems
- [[wiki/ai-ml/guardrails|Guardrails]] — Runtime filtering of retrieved content
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Data-channel trust boundaries
