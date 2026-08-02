---
type: "concept"
title: "Item Response Theory"
description: "Psychometric models linking item difficulty and ability to response probability"
tags: ["psychometrics", "testing", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Item_response_theory", "https://dictionary.apa.org/item-response-theory"]
---

# Item Response Theory

## Summary

Item Response Theory — Psychometric models linking item difficulty and ability to response probability.

## Details

- Item response theory (IRT) models the probability of a correct response as a function of person ability and item parameters. The one-parameter Rasch model varies difficulty only; two- and three-parameter models add discrimination and guessing.
- IRT's advantages over raw scores: ability estimates are item-independent (with proper linking), items are characterized independently of the sample, and measurement error is explicit per ability level. It underlies modern adaptive testing.
- Worked example: in a CAT, the algorithm selects the next item where the current ability estimate is most informative — a correct answer raises estimated ability and difficulty; an incorrect one lowers both.
- Applications: standardized tests, item banks, learner models, and survey validation. Assumptions (unidimensionality, local independence, monotonicity) must be checked.
- mykb relevance: item-response-theory pairs with knowledge-tracing to make flashcard and quiz data into genuine measurement.

## Related

- [[wiki/meta-learning/knowledge-tracing|Knowledge Tracing]] — learning-state modeling
- [[wiki/meta-learning/adaptive-learning-systems|Adaptive Learning Systems]] — computerized adaptive testing
- [[wiki/meta-learning/cognitive-diagnosis-models|Cognitive Diagnosis Models]] — fine-grained variant
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — statistical literacy
- [[wiki/concepts/internal-models|Internal Models]] — adjacent stub in this cluster
- [[wiki/concepts/world-models|World Models]] — existing wiki article
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — existing wiki article
