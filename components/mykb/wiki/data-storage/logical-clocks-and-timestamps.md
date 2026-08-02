---
type: "concept"
title: "Logical Clocks and Timestamps"
description: "Ordering events without synchronized wall clocks"
tags: ["logical-clocks", "timestamps", "ordering", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Logical Clocks and Timestamps

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Lamport clocks give a total order of events but not causality detection.
- Physical timestamps break under clock skew; logical clocks do not.
- Hybrid approaches combine both for database and stream ordering.
- Ordering guarantees are only as strong as the clock used to assign them.

## Related

- [[wiki/data-storage/consistency-models|Consistency Models]] — ordering context
- [[wiki/data-storage/hybrid-logical-clocks-and-true-time|Hybrid Logical Clocks And True Time]] — hybrid clocks
- [[wiki/data-storage/ordering-and-timestamp-assignment|Ordering And Timestamp Assignment]] — assignment practice
- [[wiki/data-storage/vector-clocks-and-version-vectors|Vector Clocks And Version Vectors]] — causal clocks
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
