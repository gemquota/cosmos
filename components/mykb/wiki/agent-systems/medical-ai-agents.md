---
type: "concept"
title: "Medical AI Agents"
description: "Agents supporting clinical documentation, literature review, and decision support"
tags: ["medical-agents", "medical", "agents", "health"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Medical AI Agents

## Summary
Medical AI agents support clinical documentation, literature review, and decision support without replacing clinicians. They matter because medicine combines enormous stakes with strict regulation, so agents must assist rather than decide. Evaluation emphasizes recall of critical findings, where missing a signal is worse than raising a false one. The bar for medical agents is set by what a missed finding can cost.

## Details
- **Definition** — a medical agent performs bounded assistive tasks: summarizing records, retrieving evidence, drafting notes, and surfacing relevant literature.
- **Role boundary** — agents are decision-support tools; clinical judgment and final decisions remain with licensed professionals.
- **Safety** — guardrails-and-safety and human-in-the-loop-approvals are structural requirements, with clinician review built into every workflow.
- **Privacy** — protected health data demands privacy-preserving-ml practices, strict access controls, and minimized data collection.
- **Evaluation** — metrics emphasize recall of critical findings, patient-safety impacts, and calibration over raw accuracy.
- **Worked example** — a clinician asks an agent to summarize a patient's history and relevant guideline sections; the agent cites sources and flags gaps for the clinician to verify.
- **Failure modes** — missed critical findings, overconfident recommendations, and data mishandling are the unacceptable failure modes.
- **Regulatory context** — validation, auditability, and monitoring requirements are stringent, tying into ai-safety-evals and risk assessment.
- **Practical relevance** — medical agents define the high-water mark for safety-constrained agent design, informing every regulated domain.
- **Bounded scope** — agents should handle well-defined assistive tasks and refuse diagnostic conclusions.
- **Audit** — every suggestion must be traceable to sources and to the clinician who acted on it.
- **Worked example** — a literature agent retrieves guideline sections for a medication question and flags conflicting recommendations.
- **Failure example** — an agent that omits a contraindication from its summary creates a downstream risk.

## Related
- [[wiki/testing/privacy-preserving-ml|Privacy-Preserving ML]] — protecting patient data
- [[wiki/agent-systems/research-agents|Research Agents]] — evidence retrieval patterns
- [[wiki/testing/ai-safety-evals|AI Safety Evals]] — safety-focused evaluation
- [[wiki/ai-ml/guardrails-and-safety|Guardrails and Safety]] — runtime safety constraints
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — clinician oversight
