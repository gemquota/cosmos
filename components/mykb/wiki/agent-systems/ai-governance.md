---
type: "concept"
title: "AI Governance"
description: "The institutions and rules steering AI development"
tags: ["governance", "policy", "institutions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# AI Governance

## Summary
AI governance is the system of norms, laws, and institutions that steer AI development and use. It spans lab self-regulation, national policy, and international coordination, and it decides whether safety research translates into safety outcomes. Governance is not a single rulebook but a stack of layers, each with different levers and accountabilities.

## Details
- **Layer stack** — internal lab policy (safety frameworks, red-team programs), national regulation (binding law, licensing), and international coordination (standards, treaties, information sharing).
- **Levers** — compute governance (who gets hardware), disclosure rules (incident reporting), evaluation mandates (pre-deployment audits), and liability rules (who pays for harm).
- **Why it matters** — safety research only changes outcomes when institutions act on it; governance is the translation layer between technical findings and field behavior.
- **Tensions** — speed of development versus verification, national competition versus international norms, and corporate secrecy versus public accountability.
- **For mykb** — the bundle's own practices are self-governance at workspace scale: rules, checkpoints, and audits applied to a small autonomous system as a model for larger ones.
- **Measurement** — governance quality is judged by outcomes: incident rates, audit pass rates, and whether reported risks get fixed, not by the volume of policy documents.

- **Institutions vs rules** — durable governance needs institutions that enforce rules, not just documents that state them; the enforcement capacity is what separates governance from advice.
- **Emergent practice** — governance is iterative: incidents and audits feed rule changes, and the rulebook is versioned like software so changes are traceable.
- **Scope limits** — governance of frontier labs and governance of deployed agents differ in levers and speed; a workspace-scale system like mykb applies the same audit-and-checkpoint pattern at its own scale.
## Related
- [[wiki/agent-systems/ai-regulation|AI Regulation]] — the law layer
- [[wiki/concepts/compute-governance|Compute Governance]] — the resource lever
- [[wiki/testing/ai-governance-frameworks|AI Governance Frameworks]] — frameworks in mykb
- [[wiki/concepts/responsible-scaling|Responsible Scaling]] — the lab layer
- [[wiki/agent-systems/accountability-ai|AI Accountability]] — the principle
- [[wiki/agent-systems/legal-accountability|Legal Accountability for AI]] — liability layer
