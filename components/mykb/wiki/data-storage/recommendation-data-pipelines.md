---
type: "concept"
title: "Recommendation Data Pipelines"
description: "Feeding recommender systems with interaction data"
tags: ["recommendations", "pipelines", "features", "ml"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Recommendation Data Pipelines

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Recommendation pipelines collect interactions, build features, train, and serve scores.
- Online/offline split: batch features for training, real-time features for serving.
- Feedback loops make training data drift; monitor for model staleness.
- Evaluation offline (NDCG) plus online (A/B) both matter.

## Related

- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — feature stores
- [[wiki/data-storage/offline-vs-online-stores|Offline Vs Online Stores]] — online/offline
- [[wiki/data-storage/real-time-personalization|Real-Time Personalization]] — serving
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
- [[wiki/data-storage/data-warehousing-concepts|Data Warehousing Concepts]] — warehouse fundamentals
