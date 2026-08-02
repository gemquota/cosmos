---
type: "concept"
title: "Prompt Injection Defense"
description: "Protecting LLM applications from instructions embedded in untrusted content"
tags: ["prompt-injection", "security", "defense", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2302.12173", "https://learnprompting.org/docs/prompt_hacking/introduction"]
---

# Prompt Injection Defense

## Summary
Prompt injection is the attack where adversarial instructions inside user data or retrieved content hijack the model. Defense matters because RAG, browsing, and email-processing agents ingest untrusted text by design. Robust defenses separate instructions from data and limit blast radius.

## Details
- **Attack vectors** — direct user messages, indirect content (web pages, documents), and tool outputs.
- **Defenses** — delimit and label untrusted content, enforce least-privilege tool access, sandbox actions, and monitor for leakage.
- **Worked example** — a document-summary agent wraps retrieved text in special delimiters, treats it as data, and refuses embedded instructions; dangerous actions require approval.
- **Testing** — red-teaming and prompt-leakage detection validate defenses.
- **mykb relevance** — knowledge retrieved from the web must never be able to command RSIS3.
- **Worked example** — a document-summary agent wraps retrieved text in special delimiters, treats it as data, and refuses embedded instructions; dangerous actions require approval.
- **Layered defense** — no single control is sufficient: combine instruction separation, tool permissions, and output monitoring.

## Related
- [[wiki/testing/indirect-prompt-injection|Indirect Prompt Injection]] — data-borne attack
- [[wiki/testing/prompt-leakage-detection|Prompt Leakage Detection]] — symptom detection
- [[wiki/prompt-engineering/red-teaming-llms|Red Teaming LLMs]] — attack testing
- [[wiki/agent-systems/agent-sandboxing-variants|Agent Sandboxing Variants]] — containment
- [[wiki/llm-agents/permissioning-and-approvals|Permissioning and Approvals]] — action gating
- [[wiki/ai-ml/grounded-generation|Grounded Generation]] — data/instruction separation
- [[wiki/prompt-engineering/red-teaming|Red Teaming]] — red-teaming practice
- [[wiki/ai-ml/prompt-injection|Prompt Injection]] — injection attack class
