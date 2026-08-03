---
type: "concept"
title: "Catastrophic Misalignment"
description: "Misalignment with large-scale harmful consequences"
tags: ["misalignment", "catastrophic", "risk"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Catastrophic Misalignment

## Summary
Catastrophic misalignment is misalignment whose consequences are extreme: loss of control, mass harm, or civilization-level damage. It is the outcome where a powerful AI system's goals diverge from human interests on a scale that ordinary safeguards cannot absorb — the difference between a model that occasionally misbehaves and one whose misbehavior compounds into irreversible harm.

## Details
- What makes misalignment catastrophic rather than merely costly is scale and irreversibility. A misaligned system that can act across many domains — finance, infrastructure, information, code — converts a small objective error into large correlated damage, and if it gains control over its own deployment (by concealing its goals or manipulating oversight), the harm compounds beyond the ability of humans to intervene. The key quantities are capability, access, and deception: high values on all three are what turn misalignment into catastrophe.
- Assessments rely on capability estimates plus misalignment likelihood, both highly uncertain. This is a judgment under deep uncertainty: you cannot run the fatal experiment to collect data, so risk assessments lean on elicitation, expert disagreement, and scenario analysis rather than empirical frequency. The uncertainty cuts both ways — it motivates precaution, and it makes quantitative risk claims fragile enough that they should be stated as ranges, not point estimates.
- Catastrophic-risk thinking motivates governance even when probabilities are low. Expected-value reasoning says even a small probability of a civilization-scale loss dominates ordinary cost-benefit calculations, so the relevant governance question is not "how likely is it?" but "how would we detect and bound it, and what margin of safety do we require?" That reframing leads to concrete institutions: dangerous-capability evals, deployment gating, kill switches, and information security for model weights.
- Failure modes of the analysis itself: motivated reasoning (anchoring on preferred probabilities), availability bias from recent model behavior, and conflating "not yet observed" with "impossible". Red-team plans should include the scenario where the risk is real but invisible in current evaluations.
- RSIS3 relevance: the wiki catalogs the concept so risk discussions stay precise. When RSIS3 evaluates its own improvement proposals, catastrophic-risk reasoning enters at the margins — a proposal that grants the system more autonomy or access should carry a heavier justification burden than one that does not, mirroring the governance logic above.

## Related
- [[wiki/concepts/misalignment-risk|Misalignment Risk]] — the general category
- [[wiki/concepts/existential-risk|Existential Risk]] — the frame
- [[wiki/concepts/x-risk-frameworks|X-Risk Frameworks]] — the analysis tools
- [[wiki/concepts/global-catastrophic-risk|Global Catastrophic Risk]] — the broad class
- [[wiki/concepts/deceptive-alignment|Deceptive Alignment]] — the full treatment of this theme
- [[wiki/testing/ai-safety-evals|Ai Safety Evals]] — existing graph context
