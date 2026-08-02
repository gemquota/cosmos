---
type: "concept"
title: "Hybrid Logical Clocks and TrueTime"
description: "Combining physical and logical clocks for database ordering"
tags: ["hlc", "truetime", "clocks", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hybrid Logical Clocks and TrueTime

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- HLCs carry a physical component plus a logical counter, giving near-physical timestamps with causality.
- Spanner's TrueTime bounds clock uncertainty to order transactions globally.
- HLCs give good ordering without special hardware; TrueTime needs GPS/atomic clocks.
- Timestamp assignment quality limits consistency guarantees (e.g., MVCC snapshots).

## Related

- [[wiki/data-storage/consistency-models|Consistency Models]] — consistency
- [[wiki/infrastructure/clock-drift-and-ntp|Clock Drift And Ntp.Md]] — clock sync
- [[wiki/data-storage/logical-clocks-and-timestamps|Logical Clocks And Timestamps]] — lighter clocks
- [[wiki/data-storage/ordering-and-timestamp-assignment|Ordering And Timestamp Assignment]] — assignment
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
