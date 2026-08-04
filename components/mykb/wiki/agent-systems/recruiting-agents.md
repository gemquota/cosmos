---
type: "concept"
title: "Recruiting Agents"
description: "Agents that screen candidates, schedule interviews, and draft evaluations"
tags: ["recruiting-agents", "recruiting", "agents", "hr"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Recruiting Agents

## Summary
Recruiting agents screen candidates, schedule interviews, and draft evaluations, automating the administrative surface of hiring. They matter because hiring decisions are high-impact and bias-prone, so automation must be carefully constrained. Fairness and human review are not optional additions; they are the design center. Recruiting automation works when it augments human judgment instead of replacing it.

## Details
- **Definition** — a recruiting agent matches candidates to roles from resumes and profiles, drafts screening notes, and supports interview logistics.
- **Fairness** — bias-and-fairness-eval is critical because models can encode protected-attribute correlations; audits and mitigation are mandatory.
- **Human gates** — final hiring decisions stay with humans, with human-in-the-loop-approvals for any evaluative output.
- **Privacy** — candidate data is sensitive, so data-minimization-agents patterns limit what is collected, retained, and shared.
- **Worked example** — an agent screens applications against a rubric, surfaces the top candidates with evidence, and drafts interview questions, leaving the shortlist decision to the recruiter.
- **Failure modes** — resume-parsing errors, biased ranking signals, and automation that treats proxies as qualifications are the critical risks.
- **Accountability** — algorithmic-impact-assessments and responsible-ai-principles guide deployment, and decisions must be explainable.
- **Practical relevance** — recruiting agents are a case study in applying fairness and oversight to high-stakes, people-facing automation.
- **Explainability** — screening decisions must be explainable so candidates and recruiters can challenge them.
- **Data scope** — systems should use only job-relevant data and document the exclusion of protected attributes.
- **Worked example** — an agent ranks applicants against a rubric and shows the evidence for each rank.
- **Failure example** — an agent trained on historical hires propagates the biases in that history.

## Related
- [[wiki/testing/bias-and-fairness-eval|Bias and Fairness Evaluation]] — the fairness requirement
- [[wiki/llm-agents/data-minimization-agents|Data Minimization for Agents]] — limiting candidate data
- [[wiki/agent-systems/human-in-the-loop-approvals|Human-in-the-Loop Approvals]] — human decision gates
- [[wiki/testing/algorithmic-impact-assessments|Algorithmic Impact Assessments]] — impact review
- [[wiki/testing/responsible-ai-principles|Responsible AI Principles]] — the policy frame
