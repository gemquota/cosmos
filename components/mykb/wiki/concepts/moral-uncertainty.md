---
type: "concept"
title: "Moral Uncertainty"
description: "Knowing which moral theory is correct"
tags: ["moral-uncertainty", "ethics", "normative"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Moral Uncertainty

## Summary
Moral uncertainty is the epistemic state of being unsure which moral theory or value system is right. Just as we are uncertain about empirical facts, we are uncertain about normative facts — whether consequences or duties ground morality, whether aggregate welfare or rights protection comes first, whether future beings count as much as present ones. Decision theories under moral uncertainty try to act well despite that disagreement.

## Details
- The structure: a decision-maker faces an action and a set of candidate moral theories (utilitarianism, deontology, virtue ethics, rights-based views) with some credence attached to each. Because the theories disagree about which action is right — one says sacrifice the few for the many, another forbids using people as means — the decision requires aggregating across theories rather than picking one and ignoring the rest. The obvious aggregation is expected moral value: weight each theory's assessment by your credence in it and choose the action with the best weighted score, exactly as expected-value reasoning handles empirical uncertainty.
- The technical complications are substantial. Theories must be comparable (how does a utility unit in one theory compare to a duty violation in another?), the normalization problem is severe (each theory's value scale needs a common zero and unit, and the choice of normalization can flip the decision), and some theories are incommensurable with each other. There is also the regress worry: if you are uncertain about the aggregation rule itself, that uncertainty must itself be handled, and the recursion can continue indefinitely.
- It is increasingly studied as a real alignment input, not just philosophy. An AI system must act even though the true moral theory is unsettled, so alignment practice needs a decision procedure under moral disagreement: weigh candidate value systems by credence, apply risk-averse aggregation when stakes are high, and remain corrigible so that better moral understanding can revise the objective later. Moral uncertainty thereby becomes a specification problem — the objective function must encode the decision procedure, not just one theory.
- The failure modes: pretending certainty (hard-coding one theory as if the debate were settled), paralysis (refusing to act because theories conflict), and overconfidence in aggregation (treating the normalization choice as neutral when it quietly decides the outcome).
- RSIS3 relevance: contested practices are handled with explicit uncertainty, not false certainty. The wiki records normative disagreements as open and weights them by confidence, so the system's ethics stack stays honest about what is settled and what is not.

## Related
- [[wiki/concepts/normative-uncertainty|Normative Uncertainty]] — the broader frame
- [[wiki/concepts/moral-weights|Moral Weights]] — the aggregation question
- [[wiki/concepts/axiology|Axiology]] — what is valuable at all
- [[wiki/concepts/value-alignment-problems|Value Alignment Problems]] — the applied layer
- [[wiki/concepts/value-specification|Value Specification]] — the full treatment of this theme
- [[wiki/ai-ml/shard-theory|Shard Theory]] — existing graph context
