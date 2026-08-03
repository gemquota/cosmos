---
type: "concept"
title: "Knowledge Tracing"
description: "Modeling whether a learner has mastered a skill from performance history"
tags: ["knowledge-tracing", "modeling", "learners"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Bayesian_knowledge_tracing", "https://dictionary.apa.org/knowledge-tracing"]
---

# Knowledge Tracing

## Summary

Knowledge Tracing — Modeling whether a learner has mastered a skill from performance history.

## Details

- Knowledge tracing estimates a learner's mastery of a skill from their response history. The classic Bayesian knowledge-tracing model (Corbett & Anderson) tracks a latent binary state — mastered or not — with parameters for guess, slip, learning, and initial knowledge, updated after each response.
- Modern variants add deep networks (DKVMs), item difficulty, and forgetting. Knowledge tracing powers mastery learning: when mastery probability crosses a threshold, the skill is considered learned and practice moves on.
- Worked example: a tutoring system presents fraction problems; after each answer, mastery probability updates — guessing right once raises it little, consistent success raises it steadily, and a slip lowers it briefly.
- Uses: adaptive problem selection, knowledge-gap diagnosis, and learning-curve analytics. Limits: skill definition granularity, and mastery of logged problems does not guarantee transfer.
- mykb relevance: the wiki's gap detector would be a coarse knowledge-tracer for the knowledge base — locating weak regions rather than skills.

## Related

- [[wiki/meta-learning/mastery-learning|Mastery Learning]] — the pedagogy
- [[wiki/meta-learning/adaptive-learning-systems|Adaptive Learning Systems]] — the application
- [[wiki/meta-learning/item-response-theory|Item Response Theory]] — measurement sibling
- [[wiki/meta-learning/learning-analytics|Learning Analytics]] — dashboards
- [[wiki/memory/knowledge-articulation|Knowledge Articulation]] — adjacent stub in this cluster
- [[wiki/memory/knowledge-map-research|Knowledge Map Research]] — adjacent stub in this cluster
- [[wiki/concepts/knowledge-graph-memory|Knowledge-Graph Memory]] — existing wiki article
- [[wiki/memory/knowledge-capture|Knowledge Capture]] — existing wiki article
