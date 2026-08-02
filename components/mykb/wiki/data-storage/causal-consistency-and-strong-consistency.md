---
type: "concept"
title: "Causal and Strong Consistency"
description: "Ordering guarantees between eventual and linearizable"
tags: ["causal-consistency", "strong-consistency", "ordering", "distributed-systems"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Causal and Strong Consistency

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Causal consistency preserves cause-effect ordering without global total order.
- Strong (linearizable) consistency makes operations appear in a single real-time order.
- Causal reads use version vectors; strong reads use quorum or consensus.
- Costs grow with strength: causal needs metadata, strong needs coordination.

## Related

- [[wiki/data-storage/consistency-models|Consistency Models]] — model spectrum
- [[wiki/data-storage/cap-theorem|CAP Theorem]] — CAP framing
- [[wiki/data-storage/vector-clocks-and-version-vectors|Vector Clocks And Version Vectors]] — causal machinery
- [[wiki/api-services/read-your-writes-and-consistency-apis|Read Your Writes And Consistency Apis]] — API exposure
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
