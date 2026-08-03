---
type: "concept"
title: "Cognitive Diagnosis Models"
description: "Models that infer fine-grained knowledge states from response patterns"
tags: ["diagnosis", "models", "assessment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://cran.r-project.org/web/packages/CDM/index.html", "https://dictionary.apa.org/cognitive-diagnosis-models"]
---

# Cognitive Diagnosis Models

## Summary

Cognitive Diagnosis Models — Models that infer fine-grained knowledge states from response patterns.

## Details

- Cognitive diagnosis models (CDMs) infer which specific skills or attributes a learner has mastered from their response patterns, rather than estimating a single ability score. The DINA model, for example, assumes a set of attributes, a Q-matrix mapping items to attributes, and a conjunctive rule: mastery of all required attributes is needed to answer correctly.
- Output is a profile — mastered, partial, or unmastered per skill — which is more actionable for remediation than a total score. CDMs connect psychometrics to cognitive theory and to intelligent tutoring.
- Worked example: a student misses every item requiring 'carrying in addition' but passes all others; the CDM attributes a specific deficit, and the tutor targets exactly that skill.
- Advances: general diagnostic models, attribute hierarchies, and neural variants; challenges include attribute definition and Q-matrix validation.
- mykb relevance: cognitive-diagnosis-models are the fine-grained sibling of knowledge-tracing — the wiki's gap reports would approximate them per topic.

## Related

- [[wiki/meta-learning/knowledge-tracing|Knowledge Tracing]] — mastery modeling
- [[wiki/meta-learning/item-response-theory|Item Response Theory]] — measurement base
- [[wiki/meta-learning/adaptive-learning-systems|Adaptive Learning Systems]] — use case
- [[wiki/meta-learning/formative-assessment|Formative Assessment]] — feedback loop
- [[wiki/concepts/internal-models|Internal Models]] — adjacent stub in this cluster
- [[wiki/concepts/generative-models|Generative Models]] — adjacent stub in this cluster
- [[wiki/concepts/world-models|World Models]] — existing wiki article
- [[wiki/agent-systems/tool-use-patterns|Tool Use Patterns]] — existing wiki article
