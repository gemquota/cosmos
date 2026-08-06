---
type: "concept"
title: "Explainable AI"
description: "Techniques for explaining model decisions"
tags: ["explainability", "xai", "methods"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Explainable AI

## Summary
Explainable AI (XAI) produces human-understandable explanations for model behavior: feature attributions, counterfactuals, and rationales. The central caveat is fidelity: an explanation is only useful if it reflects the computation that actually produced the decision.

## Details
- **Method families** — feature attribution (which inputs mattered), counterfactuals (what would change the decision), and natural-language rationales (why, in words).
- **Fidelity problem** — many explanations are plausible but unfaithful to the real computation; a good-looking explanation of a wrong mechanism is worse than no explanation because it manufactures trust.
- **Purpose determines quality** — debugging needs mechanistic detail, audit needs verifiability, and user trust needs simplicity; an explanation optimized for one purpose fails the others.
- **Evaluation** — explanations are evaluated by faithfulness (do they match the computation?), stability (do small input changes alter them?), and usefulness (do they change reviewer decisions correctly?).
- **RSIS3 relevance** — rationale fields on generated notes are light XAI: they explain why a note was written, and they are only valuable if they reflect the actual reasoning.
- **Relationship to interpretability** — explainability is the user-facing layer; interpretability research (mechanistic analysis) is the deeper layer that explainability should rest on.

- **Deployment practice** — explanations ship with the model card and the decision log, not as a separate add-on; the artifact is only trustworthy when it is produced by the same pipeline that made the decision.
- **Local vs global explanations** — local explanations cover a single decision; global ones summarize model behavior across the distribution; audits usually need both, and the two can disagree when the model is inconsistent.
- **Human factors** — an explanation is judged by the reader: jargon, length, and format decide whether it actually changes a reviewer's decision, so evaluation includes end users.
## Related
- [[wiki/agent-systems/transparency-ai|Transparency in AI]] — the umbrella
- [[wiki/agent-systems/explainable-decisions|Explainable Decisions]] — the decision form
- [[wiki/agent-systems/rationale-generation|Rationale Generation]] — the mechanism
- [[wiki/concepts/interpretability-libraries|Interpretability Libraries]] — the tooling
- [[wiki/agent-systems/introspection-ai|Introspection in AI]] — the internal view
- [[wiki/agent-systems/justification-ai|Justification in AI]] — giving grounds for behavior
