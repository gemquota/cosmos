---
type: "concept"
title: "Tail Risks"
description: "Low-probability, high-impact outcomes"
tags: ["tail-risks", "probability", "risk"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Tail Risks

## Summary
Tail risks are outcomes in the far tails of probability distributions: rare and severe. The concept matters because standard decision-making — averages, most-likely scenarios, Gaussian intuition — systematically ignores the tails, and for AI the tails are where the catastrophic outcomes live: a small probability of enormous harm can dominate every other consideration in the expected-value calculation.

## Details
- The mathematical shape: in a Gaussian distribution, tail events are exponentially rare — 6-sigma events essentially never happen, so ignoring them is rational. In fat-tailed distributions, the tail decays as a power law rather than exponentially, so extreme events are orders of magnitude more likely than Gaussian intuition suggests — and, critically, the variance can even be undefined, which breaks the entire toolkit of mean-variance thinking. The distinction is not academic: whether AI outcomes are fat-tailed determines whether tail reasoning is a precautionary footnote or the main event.
- AI capability and harm distributions are plausibly fat-tailed, making tail events more likely than Gaussian intuition suggests. The argument: AI progress is driven by compounding feedback loops (better tools → better research → better tools), which produces super-exponential dynamics; the harms scale with capability, so the harm distribution inherits the fat tail; and tipping points (a model crossing a dangerous threshold, a race dynamic locking in) create discrete jumps rather than smooth degradation. The evidence is circumstantial — there is no historical distribution of "AI catastrophes" to fit — but the structural argument is strong enough that safety analysis assumes fat tails by default.
- Tail-risk analysis changes decision rules (expected value, worst-case reasoning). With fat tails, expected value can be dominated by the tail term — a 0.01% chance of civilization-scale loss swamps any ordinary gain — so the correct decision procedure emphasizes the tail: bound the worst case, avoid irreversible exposure, and treat "it hasn't happened yet" as no evidence of safety. The tension with expected-value reasoning is real: the expected value is only as trustworthy as the probability estimates, and tail probabilities are exactly the ones we cannot estimate — which is why tail-risk analysis supplements the calculus with robustness (avoid catastrophic outcomes regardless of probability) rather than relying on it alone.
- The failure mode of tail-risk thinking: paralysis — if the worst case dominates every decision, nothing can proceed; the resolution is to bound tails (sandboxes, gating, kill switches) rather than to eliminate them.
- RSIS3 relevance: the wiki's risk pages reason in tails, not averages — the system's own risk assessments weight irreversible downside above expected gains, the same logic its improvement passes apply to churn risk.

## Related
- [[wiki/concepts/fat-tailed-distributions|Fat-Tailed Distributions]] — the mathematical shape
- [[wiki/concepts/worst-case-reasoning|Worst-Case Reasoning]] — the decision rule
- [[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — the counterweight
- [[wiki/concepts/existential-risk|Existential Risk]] — the ultimate tail
- [[wiki/concepts/capability-forecasting|Capability Forecasting]] — the full treatment of this theme
- [[wiki/concepts/calibration|Calibration]] — existing graph context
