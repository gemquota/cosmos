---
type: "concept"
title: "GCS Nearline & Coldline"
description: "Google Cloud storage classes between hot and archive"
tags: ["gcs", "nearline", "coldline", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GCS Nearline & Coldline

## Summary

GCS storage classes — standard, nearline, coldline, archive — price per GB and per access: nearline for data read monthly, coldline quarterly, archive yearly. Lifecycle management automates movement, but retrieval economics still surprise teams that guess instead of measure.

## Details
- Mechanism: classes differ in storage cost, retrieval fee (per GB), minimum storage duration (30/90/365 days), and availability; lifecycle rules transition objects (age-based, name/prefix, or labels) and can delete; object autoclass moves objects between classes automatically based on access patterns; retrieval from coldline/archive is synchronous with per-GB fees.
- Concrete example: a dataset ingested to standard for 7 days of hot processing, transitioned to coldline at 30 days and archive at 90 via lifecycle rules; a compliance corpus stays in archive and is restored per request; autoclass on an unknown-pattern bucket removes the guesswork at a small premium.
- Failure modes: choosing archive for data read monthly (retrieval fees exceed savings); lifecycle churn (objects moving up and down classes, each transition costing an operation); forgetting minimum-duration penalties on early deletion; and treating classes as instant — restore of large archives takes time and money that RTO planning must include.
- Operational tradeoffs: tier by measured access frequency; autoclass is a reasonable default for unpredictable access; manual rules suit known patterns. Test restore cost/time annually and budget retrieval fees in the cost model rather than discovering them in the bill, and rehearse restoring the largest archive object before it is needed.
- RSIS3/mykb relevance: the wiki's artifact buckets would use lifecycle rules documented here, and retrieval telemetry would tell the loop when a class change is warranted.
- Class mapping: nearline for monthly reads, coldline for quarterly, archive for yearly — and measure actual reads before assigning; the assignment is the cost decision.
- Min-duration awareness: check minimum retention periods before tiering; moving data down and back up early triggers early-deletion fees. Count per-class retrieval and listing operations too, since they are billed separately from storage.

## Related
- [[wiki/cloud-infra/coldline-and-archive-storage-classes|Coldline & Archive Storage Classes]]
