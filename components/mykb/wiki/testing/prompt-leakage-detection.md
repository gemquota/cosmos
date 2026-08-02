---
type: "concept"
title: "Prompt Leakage Detection"
description: "Detecting when hidden instructions or system prompts are extracted or echoed by the model"
tags: ["security", "prompts", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prompt Leakage Detection

## Summary
Detecting when hidden instructions or system prompts are extracted or echoed by the model

## Details
- Leakage surfaces when a model reveals system prompts verbatim in output.
- Detection combines canary tokens, output monitoring, and red-team tests.
- Defense includes least-privilege prompting and prompt obfuscation.
- A first symptom of broader prompt-injection pressure.

## Related
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — main defensive framework
- [[wiki/testing/indirect-prompt-injection|Indirect Prompt Injection]] — attack that triggers leakage
- [[wiki/testing/prompt-recovery-attacks|Prompt Recovery Attacks]] — adversarial extraction
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — finding leakage in testing
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — recording leakage incidents
