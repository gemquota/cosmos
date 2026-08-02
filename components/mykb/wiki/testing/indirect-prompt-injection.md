---
type: "concept"
title: "Indirect Prompt Injection"
description: "Attacks where malicious instructions arrive through retrieved content, web pages, or tool outputs"
tags: ["security", "prompt-injection", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Indirect Prompt Injection

## Summary
Attacks where malicious instructions arrive through retrieved content, web pages, or tool outputs

## Details
- The injected text lives in data the model processes, not in the user message.
- RAG and browsing agents are the main exposure surface.
- Mitigations include content provenance, sandboxing, and instruction separation.
- Harder to defend than direct injection because data is trusted by design.

## Related
- [[wiki/prompt-engineering/prompt-injection-defense|Prompt Injection Defense]] — defense framework
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — symptom monitoring
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — provenance-aware generation
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — containing tool effects
- [[wiki/testing/data-poisoning-llm|Data Poisoning of LLMs]] — similar attack via training data
