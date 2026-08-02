---
type: "concept"
title: "Column-Level Lineage"
description: "Tracing data from source column to report"
tags: ["lineage", "column-level", "governance", "observability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Column-Level Lineage

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Column-level lineage maps how each column is produced and consumed.
- It powers impact analysis: what breaks if a column changes.
- Parsing SQL and dbt models automates much of the graph.
- Lineage depth beats breadth: prioritize critical pipelines.

## Related

- [[wiki/data-storage/data-lineage|Data Lineage]] — lineage
- [[wiki/data-storage/data-observability|Data Observability]] — observability
- [[wiki/data-storage/data-lineage-and-provenance|Data Lineage And Provenance]] — lineage systems
- [[wiki/infrastructure/schema-change-management-and-branching|Schema Change Management And Branching]] — impact
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
