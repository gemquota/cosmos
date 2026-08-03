---
type: "concept"
title: "Utilitarian Calculus"
description: "Aggregating welfare across individuals to choose actions"
tags: ["utilitarianism", "calculus", "ethics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Utilitarian Calculus

## Summary
The utilitarian calculus aggregates wellbeing across all affected beings to identify the best action. It is the operational core of consequentialist ethics: enumerate who is affected, measure how each is affected, sum the gains and losses, and choose the action with the best total — the moral problem reduced to a welfare computation.

## Details
- The classic formulation (Bentham's felicific calculus) lists the dimensions to weigh: intensity, duration, certainty, propinquity (how soon), fecundity (whether the pleasure leads to more), purity (whether pain accompanies it), and extent (how many are affected). Mill's refinement shifts the emphasis from quantity to quality of pleasures. The modern form replaces the checklist with expected-utility aggregation: sum over individuals and outcomes of probability-weighted welfare, and maximize. The calculus's appeal is its transparency — every moral judgment becomes a visible arithmetic operation.
- It makes moral tradeoffs explicit but requires interpersonal welfare comparisons. The load-bearing assumption is that welfare can be measured on a common scale across different people (and beings): one person's suffering must be comparable to another's for the sum to mean anything. This is the classic objection site — critics argue the comparisons are impossible in principle (no public unit of welfare), and defenders argue we make them implicitly all the time (policy, pricing, triage), so making them explicit is an improvement. The comparison problem is also where the calculus's operational weakness lives: the numbers can always be contested, and the contested numbers decide the action.
- AI-scale applications raise questions of moral weights and tail outcomes. When the calculus is applied at AI scale, two quantities dominate: the weights (how much different beings count — the moral-weights problem) and the tails (low-probability, enormous outcomes that can dominate the sum — the tail-risks problem). A utilitarian AI that gets either wrong is systematically harmful: wrong weights misallocate its action; ignored tails expose it to catastrophic outcomes. The calculus does not resolve these — it makes them visible.
- The critics' catalogue: it permits intuitively abhorrent acts (sacrificing the few for the many), it requires impossible information (all outcomes, all probabilities, all welfare), and its aggregation can be gamed by the optimizer that uses it — the same specification-gaming risk as any objective function.
- RSIS3 relevance: the wiki's ethics pages keep the calculus and its critics in view so that any welfare-style objective the system adopts is assessed with both its power and its failure modes explicit.

## Related
- [[wiki/concepts/expected-utility|Expected Utility]] — the formal basis
- [[wiki/concepts/moral-weights|Moral Weights]] — the aggregation weights
- [[wiki/concepts/consequentialism-ai|Consequentialism for AI]] — the broader frame
- [[wiki/concepts/suffering-risk|Suffering Risk]] — the extreme application
- [[wiki/concepts/value-specification|Value Specification]]
- [[wiki/concepts/utility-functions|Utility Functions]]
