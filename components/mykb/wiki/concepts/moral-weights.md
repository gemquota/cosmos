---
type: "concept"
title: "Moral Weights"
description: "How much different entities or values count morally"
tags: ["moral-weights", "ethics", "suffering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Moral Weights

## Summary
Moral weights assign relative moral significance across beings and values — e.g., human vs animal suffering, present vs future lives. They are the comparative layer of ethics: once we agree that multiple kinds of beings or values count, we still need to decide how much each counts, and that ratio is what determines which actions are actually right when interests conflict.

## Details
- The canonical case is cross-species welfare comparison: a factory-farm policy that trades a certain amount of animal suffering for cheaper food, or a lab experiment that harms animals to cure human disease. A moral weight expresses the comparison as a number — "one unit of chicken suffering counts 0.1 units of human suffering" — and the expected-value calculus then decides the action. The weight is not a fact about the world but a normative judgment, which is exactly why it must be made explicit: hidden weights hide the ethics.
- Welfare-range and expected-value approaches make weights explicit and debatable. Welfare-range views estimate the range and intensity of welfare an entity can experience (a human can experience far more complex suffering than a chicken, so human weight exceeds chicken weight — but not by the default assumption of infinity); expected-value approaches multiply the probability of moral patiency by the expected welfare impact; and some frameworks treat weights as decision variables to be negotiated rather than discovered. All three agree that "humans count infinitely more" is a decision, not a datum.
- The stakes: wrong weights systematically misallocate AI action and policy. If an AI is trained to maximize expected welfare with an implicit weight of zero for animals or future generations, it will optimize accordingly — disregarding trillions of sentient experiences. If the weight is wrong in the other direction, policy sacrifices human interests. Since weights enter the objective function directly, a deployed system's behavior is a measurement of its weights, whether they were chosen consciously or by default.
- The epistemic problem compounds the normative one: we are uncertain about welfare capacities (how much can a chicken suffer? can a future AI suffer?), so the weight is uncertain, and the correct procedure multiplies the moral uncertainty through the decision — a large uncertainty band on a weight can dominate the whole calculation.
- RSIS3 relevance: the wiki's ethics pages keep these assumptions explicit and auditable — any objective the system acts on should state its weights, so that the ethics of the system's behavior can be reviewed rather than inferred.

## Related
- [[wiki/concepts/moral-patiency|Moral Patiency]] — who counts
- [[wiki/concepts/suffering-risk|Suffering Risk]] — the weighted outcome
- [[wiki/concepts/expected-value-reasoning|Expected Value Reasoning]] — the calculus
- [[wiki/concepts/moral-status-questions|Moral Status Questions]] — the boundary question
- [[wiki/concepts/value-specification|Value Specification]] — the full treatment of this theme
- [[wiki/ai-ml/shard-theory|Shard Theory]] — existing graph context
