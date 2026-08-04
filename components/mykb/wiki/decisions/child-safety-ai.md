---
type: "decision"
title: "Child Safety and AI"
description: "Protecting children from AI-enabled harm"
tags: ["child-safety", "safety", "policy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Child Safety and AI

## Summary
Child safety and AI covers preventing CSAM generation, grooming via chatbots, and age-inappropriate exposure. It is the highest-priority content domain for many platforms — the domain where the cost of failure is not reputational but real-world harm.

## Details
- Mechanism: the policy stack includes input and output filters (image hashing against known CSAM databases), classifier models for text and images, age gates and parental controls, reporting and escalation systems with clear legal obligations, and human review for ambiguous cases.
- Concrete example: a chatbot detects and terminates a grooming pattern; an image generator refuses a request and hashes and reports attempts; a platform screens user uploads against hashed databases; moderation queues route child-safety flags to priority review with mandated reporting.
- Failure modes: filters that miss novel variants (generated content not in hash databases); over-blocking legitimate content, harming education and healthcare uses; detection gaps in languages the classifiers were not trained on; reporting workflows that are slow or unclear, failing legal obligations; systems that rely on detection alone without review.
- Tradeoffs: aggressive filtering protects children at the cost of some false positives and reduced utility; the alternative, permissive policy, is unacceptable in this domain; the mature pattern is layered detection (hashes, classifiers, review) with clear escalation and reporting, and the highest priority in the moderation queue, with hash databases updated continuously as new known content is added.
- Operational notes: treat this domain as non-negotiable, test filters against known and novel cases, and keep reporting paths exercised. Feed review-queue findings back into classifier training so each miss becomes a permanent test fixture.
- RSIS3 relevance: any generative deployment in the bundle space must treat child safety as non-negotiable — the same policy priority applied to whatever the loops generate.

## Related
- [[wiki/decisions/content-policy-ai|Content Policy for AI]] — the rules
- [[wiki/decisions/abuse-detection-ai|Abuse Detection]] — the detection
- [[wiki/decisions/safety-policies-ai|AI Safety Policies]] — the commitments
- [[wiki/concepts/election-integrity-ai|Election Integrity and AI]] — a sibling domain
- [[wiki/concepts/oversight|Oversight]]
- [[wiki/ai-ml/guardrails-and-safety|Guardrails And Safety]]
