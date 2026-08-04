---
type: "concept"
title: "Data Minimization Agents"
description: "Agents that limit collection and use of personal data to the minimum necessary"
tags: ["minimization-agents", "privacy", "data", "agents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Minimization Agents

## Summary

Data minimization agents limit the collection and use of personal data to the minimum necessary for their task. Minimization is a privacy principle and increasingly a legal requirement. It matters because every datum an agent stores is a datum it can leak, misuse, or be compelled to disclose. Minimization is a design constraint that pays off in security, trust, and compliance.

## Details

- **Definition** — Data minimization means collecting only what is needed, using it only for its stated purpose, and deleting it when done.
- **Collection discipline** — Agents should request the smallest set of fields a task requires instead of capturing everything available.
- **Purpose limitation** — Data gathered for one purpose is not silently repurposed; purpose boundaries are enforced and logged.
- **Retention coupling** — Minimization pairs with retention policies: data that was needed yesterday may be excess tomorrow.
- **On-device processing** — Local processing avoids transmitting personal data at all, the strongest form of minimization.
- **Failure modes** — Whole-context logging, telemetry that captures payloads, and model training on stored conversations violate the principle.
- **Worked example** — A customer-support agent extracts the order number and issue description, ignoring unrelated profile fields.
- **Practical relevance** — Minimization reduces breach blast radius and simplifies compliance, making it an engineering win, not just a constraint.
- **Data flow maps** — Documenting where personal data flows reveals collection points that minimization can trim.
- **Default off** — Optional data collection defaults to off, making capture a deliberate choice.
- **Pseudonymization** — Replacing identifiers with pseudonyms preserves function while limiting exposure.
- **Review** — Periodic audits of what agents collect reveal data that no longer serves its purpose and should be deleted.

## Related

- [[wiki/llm-agents/consent-and-privacy-agents|Consent and Privacy Agents]] — consent alongside minimization
- [[wiki/llm-agents/retention-policies-agents|Retention Policies for Agents]] — how long data is kept
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — privacy techniques in modeling
- [[wiki/ml-frameworks/on-device-llm|On-Device LLM]] — local processing alternatives
- [[wiki/agent-systems/agent-logs-and-audits|Agent Logs and Audits]] — auditing data practices
