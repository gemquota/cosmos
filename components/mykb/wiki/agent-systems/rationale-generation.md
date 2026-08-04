---
type: "concept"
title: "Rationale Generation"
description: "Producing reasons for actions or answers"
tags: ["rationale", "generation", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Rationale Generation

## Summary
Rationale generation produces step-by-step reasons for an agent's or model's outputs, making behavior legible and auditable. It matters because decisions without reasons cannot be reviewed, challenged, or improved. The central quality question is faithfulness: does the rationale describe why the output happened, or only justify it after the fact? Rationales are most valuable when they are checked, not just emitted.

## Details
- **Definition** — rationale generation is the practice of having a model or agent emit the reasoning behind its answer, alongside or before the answer itself.
- **Mechanism** — chain-of-thought prompting elicits reasoning during generation, while post-hoc rationales are written after the output exists.
- **Faithfulness** — a faithful rationale reflects the actual reasoning path; an unfaithful one rationalizes, which is a confabulation risk.
- **Uses** — rationales support explainable-decisions, debugging, audit trails, and user trust in high-stakes outputs.
- **Verification** — self-critique and consistency checks compare rationales against actions to catch post-hoc storytelling.
- **Worked example** — a routing agent explains why a support ticket was escalated, citing the policy clauses it matched, so the human can verify the decision.
- **Failure modes** — confident-but-wrong rationales are worse than no rationale because they mislead reviewers; decision-reports should separate fact from interpretation.
- **RSIS3 relevance** — generated syntheses include rationale for linking decisions, making the knowledge base's structure auditable.
- **Practical relevance** — rationale generation turns opaque model behavior into reviewable reasoning, a prerequisite for accountable agent systems.
- **Granularity** — step-level rationales help debugging, while summary rationales help communication.
- **Format** — structured rationales with claims and evidence are easier to verify than free text.
- **Audience** — rationale detail should match who will read it: users, engineers, or auditors.
- **Failure example** — a rationale that cites policy clauses the agent never actually consulted overstates its own reliability.

## Related
- [[wiki/agent-systems/explainable-decisions|Explainable Decisions]] — the primary use of rationales
- [[wiki/concepts/confabulation|Confabulation]] — the risk of unfaithful rationales
- [[wiki/agent-systems/self-critique|Self-Critique]] — checking the rationale against reality
- [[wiki/agent-systems/decision-reports|Decision Reports]] — the persistent record of decisions and reasons
