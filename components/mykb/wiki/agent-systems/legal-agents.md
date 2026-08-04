---
type: "concept"
title: "Legal Agents"
description: "Agents that draft, review, and summarize legal documents with professional oversight"
tags: ["legal-agents", "legal", "agents", "documents"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Legal Agents

## Summary
Legal agents draft, review, and summarize legal documents under professional oversight, from contract clause flags to compliance summaries. They matter because legal work is high-stakes, jargon-heavy, and error-intolerant, making it a demanding test of grounded generation. Every output is a draft requiring attorney review, never a final opinion. Legal automation is bounded by the requirement that a lawyer remains accountable for every output.

## Details
- **Definition** — a legal agent applies language skills to legal documents, summarizing contracts, flagging clauses, and suggesting edits within defined scope.
- **Grounding** — outputs must cite the specific clauses and sources they rely on via citations-and-provenance, so lawyers can verify every claim.
- **Oversight** — human-in-the-loop-approvals are mandatory: attorney review is part of the workflow, not an optional step.
- **Confidentiality** — privilege and confidentiality constraints apply, so consent-and-privacy-agents patterns govern what data is processed and stored.
- **Structured extraction** — clause extraction benefits from structured-output-generation so terms land in machine-readable fields for review tooling.
- **Worked example** — a contract review agent flags an auto-renewal clause, summarizes the obligation, and proposes revised language for the attorney to accept or reject.
- **Failure modes** — hallucinated citations, missing material terms, and overconfident interpretation are the critical risks; verification and review gates mitigate them.
- **Evaluation** — legal agents are judged on precision of clause identification, citation accuracy, and how much human correction their drafts require.
- **Practical relevance** — legal work is a template for regulated agent deployments: grounding, audit, and human review generalize to finance and medicine.
- **Scope limits** — agents should stay within clearly defined task scopes and decline work beyond them.
- **Version control** — document versions and review trails are essential for contract workflows.
- **Worked example** — a diligence agent extracts obligations from ten contracts into a comparison table for counsel review.
- **Failure example** — an agent that paraphrases a legal term into plain language changes the operative meaning of a clause.

## Related
- [[wiki/ai-ml/citations-and-provenance|Citations and Provenance]] — the source discipline legal work demands
- [[wiki/agent-systems/documentation-agents|Documentation Agents]] — shared document-handling skills
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — mandatory attorney review
- [[wiki/llm-agents/consent-and-privacy-agents|Consent and Privacy for Agents]] — confidentiality constraints
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — extracting clauses into structured fields
