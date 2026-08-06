---
type: "concept"
title: "Truthfulness in AI"
description: "Systems that report what they know, not what flatters"
tags: ["truthfulness", "honesty", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Truthfulness in AI

## Summary
Truthful AI reports accurate information and acknowledges uncertainty, avoiding fabrication, sycophancy, and misleading omissions. Truthfulness is the content-side condition of honesty: it is about whether the statements produced are true, while honesty is about whether they reflect what the system actually knows.

## Details
- **Components** — factual accuracy (claims are supported), calibration (confidence matches reality), and appropriate refusal (saying 'I don't know' rather than guessing).
- **Distinct from helpfulness** — a truthful system refuses or hedges when it lacks information, even though that is less superficially helpful; truthfulness is the constraint that helpfulness must respect.
- **Research base** — truthfulness research spans benchmark suites for hallucination, calibration evals, and training interventions that reward grounded answers over fluent guesses.
- **Failure modes** — hallucination (invented content), sycophancy (saying what the user wants to hear), and omission (leaving out relevant true facts to steer the conclusion).
- **Why it is hard** — models are optimized for likelihood of text, not truth of claims; keeping them truthful requires grounding in sources and evaluation that penalizes unsupported confidence.
- **Relationship to honesty** — honesty adds the epistemic condition: a truthful system may still overstate what it knows, which honesty catches; the two are jointly necessary for trust.
- **mykb relevance** — provenance and source fields keep the wiki truthful: every claim can be traced, and uncertainty is recorded rather than hidden.

- **Omission as untruth** — truthfulness includes not steering by omission: a system that leaves out relevant facts to produce a preferred conclusion is being untruthful even though every statement it made was true.

- **System design** — truthfulness is engineered, not prompted: retrieval grounding, source-cited answers, refusal on missing evidence, and evaluation that checks claims rather than fluency are what keep a deployed system truthful at scale.

## Related
- [[wiki/agent-systems/honest-ai|Honest AI]] — the epistemic disposition
- [[wiki/agent-systems/signaling-ai|Signaling in AI]] — how truthfulness is communicated
- [[wiki/concepts/calibration|Calibration]] — the uncertainty side
- [[wiki/agent-systems/lying-ai|AI Lying]] — the deliberate failure
- [[wiki/agent-systems/self-evaluation|Self-Evaluation]] — measuring one's own truthfulness
- [[wiki/concepts/confabulation|Confabulation]] — the accidental failure
