---
type: "concept"
title: "Multi-Region"
description: "Running a service in multiple geographic regions for availability and latency"
tags: ["multi-region", "availability", "architecture", "geo"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Multi-Region

## Summary
Multi-region deployment runs the service in several regions so a regional outage does not take everything down and users connect to a nearby region. It multiplies complexity: data replication, failover, and traffic routing become first-class problems.

## Details
- Active-active serves all regions; active-passive runs standby regions for failover.
- Data is the hard part: cross-region replication and conflict handling dominate the design.
- DNS and traffic steering (anycast, geo-DNS) route users to the healthy region.
- mykb relevance: the wiki bundle could mirror to a second region for read availability.

## Related
- [[wiki/tooling/active-active|Active-Active]]
- [[wiki/tooling/active-passive|Active-Passive]]
- [[wiki/tooling/geo-redundancy|Geo-Redundancy]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
- [[wiki/tooling/business-continuity|Business Continuity]]
