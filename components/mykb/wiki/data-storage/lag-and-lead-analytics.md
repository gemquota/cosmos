---
type: "concept"
title: "LAG and LEAD Analytics"
description: "Comparing rows with previous and next values"
tags: ["lag", "lead", "window-functions", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# LAG and LEAD Analytics

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- LAG fetches a prior row's value; LEAD fetches a later one within a partition.
- They enable deltas, growth rates, and change detection in SQL.
- Defaults and partition order define the comparison.
- Combine with window frames for rolling comparisons.

## Related

- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — analytics
- [[wiki/data-storage/window-functions-in-sql|Window Functions In Sql]] — window functions
- [[wiki/data-storage/ranking-and-tiling-window-functions|Ranking And Tiling Window Functions]] — related functions
- [[wiki/data-storage/cohort-and-retention-analytics|Cohort And Retention Analytics]] — usage
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
