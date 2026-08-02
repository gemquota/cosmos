---
type: "concept"
title: "Cloud Providers: AWS, Azure, GCP"
description: "The three major clouds and their shared service patterns"
tags: ["aws", "azure", "gcp", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://aws.amazon.com/",
  "https://azure.microsoft.com/",
  "https://cloud.google.com/",
]
---

# Cloud Providers: AWS, Azure, GCP

## Summary
AWS, Azure, and GCP dominate public cloud, each offering compute, storage, network, and managed services with distinct naming and semantics. The abstractions converge: regions, VPCs, instances, and object storage appear in all three. Multi-cloud skill is mostly translating these maps.

## Details
- AWS's breadth makes it the default enterprise target; its documentation spans hundreds of services.
- Azure's deep Microsoft integration suits Windows and hybrid workloads.
- GCP's global networking and data services appeal to Kubernetes and analytics teams.
- Common patterns map across providers: security groups vs NSGs, IAM roles vs service principals, S3 vs Blob vs GCS.
- Pricing models differ in commitment options and egress charges, driving cost engineering.
- In mykb, this node anchors the provider-specific articles: VPC design, managed disks, parameter stores, and compute shapes.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.
- Cost and latency tradeoffs for this choice are quantified in the capacity planning and cost-of-bandwidth articles.

## Related
- [[wiki/cloud-infra/parameter-stores-aws-ssm-azure-keyvault-gcp-secretmanager|Cloud Parameter Stores]]
- [[wiki/cloud-infra/gcp-vpc-and-cloud-nat|GCP VPC & Cloud NAT]]
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]]
- [[wiki/cloud-infra/cloud-emulators|Cloud Emulators]]
