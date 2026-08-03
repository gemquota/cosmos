---
type: "concept"
title: "AI Regulation"
description: "Laws and rules governing AI"
tags: ["regulation", "law", "policy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# AI Regulation

## Summary

AI regulation is the body of binding legal rules on AI development and deployment — from the EU AI Act to sectoral rules in finance, health, and elections. It sets minimums; good practice exceeds them, and the design tension is innovation vs safety vs enforceability.

## Details
- Mechanism: regulation operates through instruments: risk-based tiering (EU AI Act), sectoral rules (FDA for medical AI, financial conduct rules), liability regimes (who pays for harm), transparency and reporting duties, and enforcement bodies with sanctions; it interacts with data protection (GDPR), copyright, and product safety law, creating a layered compliance surface.
- Concrete example: an AI medical triage tool faces both medical-device regulation (safety, clinical evidence) and the AI Act (high-risk obligations); an election-related chatbot faces transparency duties and platform rules; a deployer in multiple jurisdictions reconciles divergent requirements (EU tiering vs US sectoral approach).
- Failure modes: regulation that freezes safety baselines while capability moves (compliance theater); enforcement gaps where systems are unregistered or cross-border; over-broad rules that burden small users without binding large actors; and the gap between legal minimums and actual safety practice — regulation is a floor, not a ceiling.
- Operational tradeoffs: compliance costs and design constraints trade against market access and social license; the pragmatic posture is building governance practices (evals, documentation, reporting) that satisfy the strictest plausible regime, so new rules are incremental rather than structural.
- RSIS3/mykb relevance: regulated domains (health, elections, finance) touch the wiki's content; the loop's governance layer tracks applicable rules per domain so generated advice reflects legal context.
- Regulatory watch: track rulemaking timelines per jurisdiction (EU phased entry, sectoral guidance) in the wiki so compliance work starts before obligations activate.
- Jurisdiction mapping: record which of the wiki's deployments touch which regimes; extraterritorial reach means a serving region change can move a system into a new compliance class.

## Related
- [[wiki/agent-systems/ai-act|EU AI Act]] — the EU case
- [[wiki/agent-systems/ai-governance|AI Governance]] — the broader frame
- [[wiki/decisions/safety-policies-ai|AI Safety Policies]] — the voluntary layer
- [[wiki/agent-systems/legal-accountability|Legal Accountability for AI]] — the enforcement
- [[wiki/concepts/compute-governance|Compute Governance]]
- [[wiki/testing/ai-governance-frameworks|Ai Governance Frameworks]]
