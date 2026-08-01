---
type: "concept"
title: "Resource Tagging"
description: "Labeling cloud resources with metadata for cost allocation, ownership, and automation"
tags: ["tagging", "cost", "governance", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Resource Tagging

## Summary
Tags attach key-value metadata to cloud resources — team, environment, cost center, lifecycle. They are the plumbing that makes cost reports, budgets, and automated cleanup possible.

## Details
- A tagging standard (mandatory keys, allowed values) prevents tag sprawl and broken reports.
- Enforce tags at provisioning time (IaC validation, policies) instead of retrofitting.
- Tags drive automation: lifecycle rules, shutdown schedules, and cost anomaly detection.
- Open question: what tag taxonomy survives organizational growth without collapsing into chaos.

## Related
- [[wiki/cloud-infra/finops-practices|FinOps Practices]] — tags power cost allocation
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — clean reports need clean tags
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — tags defined in code
- [[wiki/devops-infra/terraform|Terraform]] — tag enforcement at apply time
