---
type: "concept"
title: "X-Risk Frameworks"
description: "Analytical tools for studying existential risk"
tags: ["x-risk", "frameworks", "analysis"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# X-Risk Frameworks

## Summary
X-risk frameworks decompose risk into components — probability, capability, intent, control — to make analysis tractable. Existential risk is too large and too uncertain to analyze as a single number; frameworks split it into analyzable pieces, make assumptions explicit, and connect the pieces so that the analysis can be argued about, updated, and eventually acted on.

## Details
- The standard decomposition treats risk as a product or conjunction of factors: the probability of a harmful outcome roughly factors into "a dangerous system exists" (capability), "it does something harmful" (intent or accident), and "harm cannot be prevented" (control failure). Frameworks formalize this as P(harm) = P(development) × P(misalignment | development) × P(harm | misalignment), or variants with more factors — capability, access, deception, robustness. The decomposition's value is that each factor has different evidence, different experts, and different interventions: capability questions are empirical (evals), intent questions are behavioral (evals plus theory), control questions are engineering (sandboxes, kill switches). Splitting the risk makes the analysis where each factor is weak visible.
- Examples include risk taxonomies, scenario trees, and integrated assessment models. Risk taxonomies enumerate the pathways to catastrophe (misuse, accident, race dynamics, deceptive alignment) and their interactions; scenario trees branch from present conditions through decision points to outcomes, making the contingency structure explicit; integrated assessment models combine capability forecasting, economic models, and risk estimates into quantitative trajectories — with the caveat that their outputs inherit every assumption in the chain. Each framework type trades realism for tractability, and mature analyses use several types together.
- Good frameworks make assumptions explicit and falsifiable. The test of a framework is not whether it produces the right probability — it cannot, given the uncertainty — but whether it forces the assumptions into the open, where they can be challenged, measured, and updated. A framework that hides its assumptions (an implicit probability buried in a model, an unstated control assumption) is worse than no framework, because it produces false precision. Falsifiability means the framework's components are stated sharply enough that evidence could move them.
- The failure modes: false precision (treating framework outputs as measurements), framework capture (analyzing the map instead of the territory — optimizing the framework's variables rather than reducing actual risk), and decomposition error (factors that are not independent, so the product misleads).
- RSIS3 relevance: the wiki uses frameworks to organize its risk pages coherently — every risk concept gets placed in the capability/intent/control structure, so a reader can see which factor a given page addresses and which factors remain unanalyzed.

## Related
- [[wiki/concepts/existential-risk|Existential Risk]] — the subject
- [[wiki/concepts/catastrophic-risk|Catastrophic Risk]] — the broader class
- [[wiki/concepts/risk-assessment-ai|Risk Assessment for AI]] — the applied method
- [[wiki/concepts/tail-risks|Tail Risks]] — the probability layer
- [[wiki/concepts/transformative-ai|Transformative AI]] — the full treatment of this theme
- [[wiki/agent-systems/risk-bounded-agents|Risk-Bounded Agents]] — existing graph context
