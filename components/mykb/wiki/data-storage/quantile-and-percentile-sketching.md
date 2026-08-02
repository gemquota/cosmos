---
type: "concept"
title: "Quantile and Percentile Sketching"
description: "Approximate order statistics without sorting everything"
tags: ["quantiles", "percentiles", "sketches", "approximation"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quantile and Percentile Sketching

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Quantile sketches (t-digest, GK, KLL) estimate percentiles in sublinear memory.
- t-digest is accurate at the tails, which is where SLAs usually matter.
- Sketching supports mergeable, distributed percentile computation.
- Use for latency monitoring, price distributions, and anomaly baselines.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/sketch-based-analytics|Sketch Based Analytics]] — sketch family
- [[wiki/infrastructure/pipeline-sla-and-latency-budgets|Pipeline SLA and Latency Budgets]] — percentile SLAs
- [[wiki/data-storage/anomaly-detection-in-metrics|Anomaly Detection In Metrics]] — baselines from sketches
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
