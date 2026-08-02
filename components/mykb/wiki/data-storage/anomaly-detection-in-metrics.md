---
type: "concept"
title: "Anomaly Detection in Metrics"
description: "Finding unusual patterns in time-series data"
tags: ["anomaly-detection", "metrics", "time-series", "monitoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Anomaly Detection in Metrics

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Statistical methods (z-score, moving average, seasonality decomposition) flag outliers.
- ML approaches (isolation forest, Prophet-style models) learn normal patterns.
- Alert fatigue comes from too-sensitive thresholds; tune per metric.
- Anomaly detection complements alert rules on explicit thresholds.

## Related

- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — TSDB
- [[wiki/concepts/telemetry|Workspace Telemetry]] — telemetry
- [[wiki/data-storage/changepoint-detection-and-seasonality|Changepoint Detection And Seasonality]] — changepoints
- [[wiki/data-storage/real-time-dashboards-and-alerts|Real Time Dashboards And Alerts]] — alerting
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
