---
type: "concept"
title: "Accumulating Snapshot Facts"
description: "Facts that track a process through its milestones"
tags: ["accumulating-snapshot", "facts", "modeling", "process"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Accumulating Snapshot Facts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- One row per business process instance, updated as milestones complete.
- Date keys per milestone (ordered_date, shipped_date, delivered_date) enable lead-time analysis.
- Updates overwrite the row; history of changes is not kept.
- Good for order fulfillment, claims, and pipeline tracking.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — modeling
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — facts
- [[wiki/data-storage/periodic-snapshot-facts|Periodic Snapshot Facts]] — periodic variant
- [[wiki/data-storage/grain-and-additivity|Grain And Additivity]] — grain
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
