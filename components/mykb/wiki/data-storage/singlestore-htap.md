---
type: "concept"
title: "SingleStore and HTAP"
description: "One engine for transactions and analytics (hybrid transactional/analytical processing)"
tags: ["singlestore", "htap", "olap", "oltp"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# SingleStore and HTAP

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- HTAP systems run operational and analytical workloads on one database, avoiding dual-copy pipelines.
- SingleStore keeps row-based tables for writes and columnar tables for scans, syncing internally.
- Benefits: fresher analytics and simpler architecture; costs: compromise tuning for both workload types.
- Real-time personalization and operational dashboards are the canonical HTAP use cases.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — the split HTAP tries to bridge
- [[wiki/data-storage/real-time-personalization|Real Time Personalization]] — HTAP-powered feature
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — alternative separation of workloads
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar side of SingleStore
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
