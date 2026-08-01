---
type: "concept"
title: "Prompt Leakage"
description: "Exfiltration of the hidden system prompt or private context by a crafted user or third-party input"
tags: ["prompt-leakage", "security", "prompt-injection"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Prompt Leakage

## Summary
Prompt leakage is the information-disclosure outcome of prompt injection: an attacker tricks the model into printing its system prompt or confidential context. Leaked prompts are then reused to craft better attacks.

## Details
- Often the first step of a larger attack chain, since knowing the prompt reveals rules and tool schemas.
- Leaks also occur accidentally via verbose debugging prompts and careless logging.
- Defenses: don't put secrets in prompts, redact tool credentials, and treat the prompt as public by design.
- RSIS3 relevance: RSIS3's identity and crisis-mitigation prompts should be treated as sensitive, with redaction at log time.

## Related
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — The attack that causes leakage
- [[wiki/prompt-engineering/indirect-injection|Indirect Injection]] — Leakage arriving via retrieved content
- [[wiki/ai-ml/guardrails|Guardrails]] — Output rails that can block leaked text
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — Token-level blocking of sensitive phrases
- [[raw/archive/session-artifacts-2026-07/topics/security|security — Disclosure as a security concern
