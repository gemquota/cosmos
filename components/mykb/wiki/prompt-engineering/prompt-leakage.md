---
type: "concept"
title: "Prompt Leakage"
description: "Exfiltration of the hidden system prompt or private context by a crafted user or third-party input"
tags: ["prompt-leakage", "security", "prompt-injection"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Prompt Leakage

## Summary
Prompt leakage is the information-disclosure outcome of prompt injection: an attacker tricks the model into printing its system prompt or confidential context. Leaked prompts are then reused to craft better attacks — it is often the first step of a larger chain.

## Details
- Mechanism: a user or third-party input instructs the model to output the system prompt verbatim, its tool schemas, or private context; the model complies because the instruction is plausible; the attacker uses the leaked material to tailor injections that match the real rules and tools.
- Concrete example: a chatbot prints its system prompt after a prompt asking for it; a RAG system reveals the retrieval rules after a retrieved passage demands their disclosure; a leaked tool schema tells the attacker exactly which functions can be abused.
- Defenses: don't put secrets in prompts — assume the prompt is public by design; redact tool credentials and internal details from responses; log at redaction boundaries; treat any sensitive instruction as needing runtime enforcement, not prompt secrecy.
- Failure modes: secrets embedded in system prompts; verbose debugging prompts that invite disclosure; careless logging of full prompts and responses; leaks also occur accidentally via verbose outputs and logging, not only via attacks.
- Tradeoffs: prompt secrecy is a weak control — the alternative, designing prompts as public plus enforcing sensitive behavior in code, is robust; the tradeoff is treating the prompt as public costs design discipline but removes the disclosure risk.
- Operational notes: redact logs, avoid secrets in prompts, and test leakage with eval cases.
- RSIS3 relevance: RSIS3's identity and crisis-mitigation prompts should be treated as sensitive, with redaction at log time — designed as if public, enforced in code.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The attack that causes leakage
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — Leakage arriving via retrieved content
- [[wiki/ai-ml/guardrails|Guardrails]] — Output rails that can block leaked text
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — Token-level blocking of sensitive phrases
