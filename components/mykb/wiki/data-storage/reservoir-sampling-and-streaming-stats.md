---
type: "concept"
title: "Reservoir Sampling and Streaming Stats"
description: "Uniform samples and incremental statistics over streams"
tags: ["reservoir-sampling", "streaming", "statistics", "sampling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reservoir Sampling and Streaming Stats

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Reservoir sampling keeps a uniform random sample of fixed size over a stream.
- Incremental moments (Welford) compute mean/variance without storing data.
- Streaming stats feed dashboards, drift detection, and monitoring.
- Combine with sketches for approximate histograms over time.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — streaming
- [[wiki/data-storage/data-sampling-and-approximate-queries|Data Sampling And Approximate Queries]] — sampling
- [[wiki/data-storage/anomaly-detection-in-metrics|Anomaly Detection In Metrics]] — stats for anomalies
- [[wiki/data-storage/sketch-based-analytics|Sketch Based Analytics]] — sketch complements
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
