---
type: "concept"
title: "Zones & Regions"
description: "Geographic isolation units that structure cloud redundancy"
tags: ["regions", "zones", "availability", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://aws.amazon.com/about-aws/global-infrastructure/",
  "https://cloud.google.com/about/locations",
]
---

# Zones & Regions

## Summary
Regions and zones are the geographic and fault-isolation units of cloud platforms. A region is a set of availability zones with independent power and networking; zones are where resources actually run. Multi-region and multi-zone design is how clouds deliver availability.

## Details
- AWS documents regions and availability zones as isolated failure domains within a geographic area, each zone with independent power, cooling, and networking.
- Google Cloud publishes its region and zone locations, including upcoming ones.
- Latency, compliance, and pricing differ by region, driving placement decisions for data residency and performance.
- Zone redundancy protects against facility-level failures; region redundancy protects against wider outages.
- Services are typically regional (VPCs, object buckets) or zonal (instances, disks), changing the failure model.
- In mykb, zones and regions anchor the availability architecture, multi-cloud, and disaster recovery articles.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/cloud-infra/availability-zones|Availability Zones]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
