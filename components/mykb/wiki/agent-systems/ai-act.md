---
type: "entity"
title: "EU AI Act"
description: "The European Union's AI regulation"
tags: ["eu-ai-act", "regulation", "europe"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# EU AI Act

## Summary

The EU AI Act is the EU's comprehensive AI regulation, tiering systems by risk — unacceptable, high, limited, minimal — and imposing obligations from outright bans to transparency duties. It is the first major horizontal AI law and a global reference point.

## Details
- Mechanism: the Act classifies by risk: unacceptable risk (social scoring, some manipulation) is banned; high-risk systems (employment, credit, critical infrastructure, education) face conformity assessments, data governance, human oversight, and registration in an EU database; limited-risk systems (chatbots, deepfakes) get transparency duties; GPAI models (general-purpose) have their own obligations (documentation, copyright, systemic-risk duties for large models).
- Concrete example: a hiring tool is high-risk: it must document its data and performance, undergo a conformity assessment, and support human review before deployment; a customer-service chatbot must disclose it is a bot; a general-purpose model with systemic risk must conduct evaluations and report serious incidents.
- Failure modes: scope confusion (which systems are high-risk, exemptions for research/open source); the Act's tiering being applied as checklist compliance rather than real risk management; enforcement uncertainty while the phased timeline (risk tiers activate over 2025-2027+) unfolds; and extraterritorial reach catching non-EU deployers who serve EU users.
- Operational tradeoffs: compliance costs (assessments, documentation, audits) trade against market access and trust; the Act sets minimums — good practice exceeds them, and the wiki's own evals and transparency practices align with that direction.
- RSIS3/mykb relevance: EU users and tools in the loop must track obligations under the Act; the wiki maintains a compliance checklist that maps loop activities (evals, reporting, logging) to the Act's duties.
- Documentation trail: keep model cards, training-data summaries, and conformity records in the repo alongside the code they describe; regulators and audits will ask for the evidence that already exists.
- Monitoring obligations: high-risk systems require post-market monitoring and incident logging; wire those into the existing telemetry so compliance data is a byproduct of operations, not a separate project.

## Related
- [[wiki/agent-systems/ai-regulation|AI Regulation]] — the general frame
- [[wiki/concepts/risk-classification|Risk Classification]] — the tiering
- [[wiki/syntheses/transparency-reports|Transparency Reports]] — the transparency duties
- [[wiki/agent-systems/accountability-ai|AI Accountability]] — the principle
- [[wiki/concepts/compute-governance|Compute Governance]]
- [[wiki/testing/ai-governance-frameworks|Ai Governance Frameworks]]
