---
type: "concept"
title: "Metamorphic Testing"
description: "Deriving expected outputs from input relationships when no oracle exists"
tags: ["metamorphic-testing", "testing", "oracles", "ml"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://spectrum.ieee.org/metamorphic-testing", "https://www.ibm.com/topics/metamorphic-testing"]
---

# Metamorphic Testing

## Summary
Metamorphic testing checks relations between outputs of transformed inputs when no ground-truth oracle exists. If a given input change should cause a predictable output change, a violation reveals a defect even when the correct output is unknown.

## Details
- Applies to search, machine learning, translation, and simulation systems lacking exact oracles.
- Metamorphic relations: invariance, permutation, additivity, scaling, and consistency properties.
- Example: sorting two permutations yields the same multiset; search results ignore input order.
- Combine with generated inputs to scale coverage without hand-written expected outputs.
- ML systems: small image perturbations should not change a label unless adversarial.
- Works where snapshot and golden tests cannot, because outputs legitimately vary.
- Define relations explicitly and review them like test assertions.

## Related
- [[wiki/testing/test-oracles|Test Oracles]] — relations substitute for missing oracles
- [[wiki/testing/property-based-testing|Property-Based Testing]] — generated inputs drive relations
- [[wiki/testing/differential-testing|Differential Testing]] — another oracle-free comparison strategy
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — relations for open-ended model outputs
- [[wiki/testing/fuzzing|Fuzz Testing]] — transformation-based input exploration
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — relations monitor model drift
