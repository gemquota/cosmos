---
type: "concept"
title: "Azure Blob Access Tiers"
description: "Hot, cool, cold, and archive tiers for blobs"
tags: ["azure", "blob", "tiers", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Azure Blob Access Tiers

## Summary

Azure Blob access tiers (hot, cool, cold, archive) trade cost for latency: hot for frequent reads, archive for 99-year-retention data. Choosing and moving between tiers is where storage bills are won or lost.

## Details
- Mechanism: hot optimizes for high-frequency access (highest storage cost, no retrieval fee); cool and cold trade lower storage cost for retrieval fees and minimum retention periods (30/90 days); archive drops storage cost further with ~hours of retrieval latency (rehydration) and a 180-day minimum. Automatic tiering (lifecycle rules and Blob Storage auto-tiering) moves blobs based on last-access patterns.
- Concrete example: a media pipeline writes to hot for immediate processing, moves results to cool after 30 days via a lifecycle rule, and archives old source footage after 90; a compliance dump sits in archive, restored on request. The wrong choice shows up in bills: leaving data in hot forever is the most common storage overspend.
- Failure modes: lifecycle rules that churn — moving blobs hot↔cool repeatedly accrues per-operation costs; ignoring retrieval fees for read-heavy-but-cold data (reading a 10TB archive frequently is ruinously expensive); archive blobs unavailable synchronously, breaking apps that assume instant access; and minimum-retention surprises deleting young blobs.
- Operational tradeoffs: tier by access pattern measured from real telemetry, not assumptions; enable auto-tiering for unknown patterns and reserve manual policies for known access classes. Rehydration time and cost should be part of the RTO story for archived data.
- RSIS3/mykb relevance: the wiki's artifact storage uses tiered blobs with lifecycle rules documented here, and retrieval telemetry feeds the loop's cost reviews.
- Access tracking: enable last-access-time tracking before choosing tiers; tiering decisions without access data are guesses with a billing consequence.
- Lifecycle automation: encode tier moves as lifecycle rules rather than manual scripts; manual tiering is the process that stops happening after the second month.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/remote-access-methods|Remote Access Methods]]
- [[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]
- [[wiki/infrastructure/azure-synapse|Azure Synapse]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
