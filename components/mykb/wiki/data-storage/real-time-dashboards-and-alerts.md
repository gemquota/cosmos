---
type: "concept"
title: "Real-Time Dashboards and Alerts"
description: "Serving fresh metrics with low latency"
tags: ["dashboards", "real-time", "alerts", "monitoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Real-Time Dashboards and Alerts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Real-time dashboards need fast ingestion, low-latency queries, and periodic refresh.
- Pushdown engines (Pinot, Druid, ClickHouse) serve these at scale.
- Alerting evaluates rules on streams and notifies on threshold breaches.
- Separate interactive latency from exactness: approximate is usually fine.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — processing
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — serving engines
- [[wiki/data-storage/pinot-real-time-analytics|Pinot Real Time Analytics]] — serving engine
- [[wiki/data-storage/anomaly-detection-in-metrics|Anomaly Detection In Metrics]] — alert basis
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
