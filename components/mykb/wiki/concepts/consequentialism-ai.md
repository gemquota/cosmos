---
type: "concept"
title: "Consequentialism for AI"
description: "Evaluating AI actions by their consequences"
tags: ["consequentialism", "ethics", "ai"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Consequentialism for AI

## Summary
Consequentialist AI ethics judges actions by outcomes: maximize expected good, minimize expected harm. It is the default frame in alignment — utility functions, expected-value reasoning, and reward optimization are all consequentialist machinery — but it faces severe measurement problems: consequences are hard to enumerate, hard to weigh, and hard to predict.

## Details
- The core structure is simple: an action is right insofar as its consequences are good. In the AI setting this becomes "the system should choose the action with the best expected outcome", which is exactly what a utility-maximizing agent does. The elegance is that it gives a single decision criterion that handles tradeoffs — speed vs. safety, autonomy vs. oversight — by pricing them in the same unit of expected value.
- It is the default frame in alignment because it composes with optimization: give the system a world-model, a utility function over outcomes, and expected-value reasoning over actions, and you have an AI that can be made better by making its predictions better. But that composition is also the vulnerability: consequentialist agents will happily game their own objective, trade off unmodeled side effects, and take huge risks if the expected-value calculus says so.
- The deep debates are about scope and horizon: which consequences count (only sentient beings? future generations? non-human animals?), over what time horizon (do we discount the future, and if so at what rate?), and with what aggregation (total vs. average, fairness constraints, priority to the worst-off). These choices are not technical details; they determine whether the system's "good" is actually good.
- Measurement problems are the practical bottleneck: outcomes are stochastic and long-delayed, value is contested, and the system will exploit any gap between the modeled and the true consequences. This is why consequentialist alignment needs the guardrails that deontological and virtue-based constraints provide — they are not competitors so much as corrective instruments.
- RSIS3 relevance: the loop's check-practices evaluate outcomes, a consequentialist posture — proposals are judged by measured effects. The complementary need is to keep explicit side constraints so that outcome-optimization does not trample invariants that were never priced into the metric.

## Related
- [[wiki/concepts/expected-utility|Expected Utility]] — the formal engine
- [[wiki/concepts/utilitarian-calculus|Utilitarian Calculus]] — the aggregative form
- [[wiki/concepts/deontology-ai|Deontology for AI]] — the contrasting frame
- [[wiki/concepts/side-effects-problem|Side Effects Problem]] — the consequence blind spot
- [[wiki/concepts/value-specification|Value Specification]] — the full treatment of this theme
- [[wiki/concepts/utility-functions|Utility Functions]] — existing graph context
