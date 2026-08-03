---
type: "concept"
title: "Expected Value Reasoning"
description: "Deciding by probability-weighted outcomes"
tags: ["expected-value", "decision", "rationality"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Expected Value Reasoning

## Summary
Expected value reasoning multiplies each outcome's value by its probability and sums, choosing the highest total. It is the standard rational decision rule: instead of comparing best cases, worst cases, or the most likely scenario, it weighs every possibility by how likely it is and how much it is worth, then acts on the best weighted average.

## Details
- The calculation is deceptively simple: EV = sum of P(outcome) × V(outcome) over all outcomes. Its power is that it forces the decision-maker to enumerate outcomes explicitly, assign probabilities honestly, and price values — the discipline of writing down the model is often worth more than the arithmetic. For a coin flip paying $2 on heads and $0 on tails, EV is $1; for a 1% chance of a $10,000 gain and 99% of nothing, EV is $100. The rule says compare the EVs, not the headline stakes.
- It is the standard rational decision rule and the engine of consequentialist AI ethics. Expected-utility theory generalizes it by replacing value with utility, which is what allows risk aversion to be represented (a concave utility function discounts large gains), and decision theory adds the refinements: subjective probabilities, updating by Bayes' rule, and the distinction between one-shot and repeated decisions. In AI alignment, "act to maximize expected value" is the operational core of a utility-maximizing agent.
- Inputs (probabilities, values) are often uncertain; sensitivity analysis helps. The rule is only as good as its inputs, and the classic failure is the certainty illusion — assigning precise probabilities and values to things you actually know only vaguely. Sensitivity analysis varies each input over its plausible range and asks whether the decision flips; if it does, the model is not robust and the decision should be treated as close, not settled.
- The structural failure modes: neglecting tail outcomes (events with tiny probability and huge value dominate the sum but are easy to forget), double-counting, and applying the rule in the wrong domain — where stakes are catastrophic and probabilities unknowable, expected-value reasoning still applies but the uncertainty band dominates the answer.
- RSIS3 relevance: loop decisions weigh expected knowledge gains against churn risk. Choosing whether to run an experiment, consolidate a synthesis, or promote an article is an expected-value problem — the right frame is not "will it work?" but "what is the probability-weighted value across outcomes?"

## Related
- [[wiki/concepts/expected-utility|Expected Utility]] — the formal engine
- [[wiki/concepts/risk-benefit-analysis|Risk-Benefit Analysis]] — the applied form
- [[wiki/concepts/utilitarian-calculus|Utilitarian Calculus]] — the aggregative form
- [[wiki/concepts/off-switch-game|Off-Switch Game]]
- [[wiki/concepts/utility-functions|Utility Functions]]
