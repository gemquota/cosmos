---
type: "concept"
title: "Resource Tagging"
description: "Labeling cloud resources with metadata for cost allocation, ownership, and automation"
tags: ["tagging", "cost", "governance", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Resource Tagging

## Summary

Resource tagging attaches key-value metadata to cloud resources for cost allocation, ownership, environment, and automation. Tags are the backbone of cloud governance — untagged resources are invisible to cost reports and drift from policy; tagging discipline is a team behavior, not a tool feature.

## Details
- Mechanism: providers support tags on most resources (AWS, Azure, GCP labels) with IAM enforcement (tag-on-create, required tags), cost-allocation reports (AWS), and automation triggers (start/stop, cleanup). Effective schemes define a small required set — environment, owner, cost-center, app — with values from controlled vocabularies enforced at the API.
- Concrete example: a cost report groups spend by cost-center and environment because every resource is tagged at creation; a nightly cleanup job deletes non-production instances older than 24h keyed on environment=dev; an audit shows the 3% untagged resources because a script created them without tags — policy enforcement catches it next time.
- Failure modes: tag sprawl (free-form keys that defeat reporting); resources created outside IaC without tags; tags used for secrets or mutable identity (IAM should decide access, not tags); and cleanup/reporting logic depending on tags that nobody enforces, silently missing resources.
- Operational tradeoffs: tagging costs a little process and pays in visibility and automation; enforce at creation (policy/IaC), keep the vocabulary small, and audit drift monthly. Treat tags as data: versioned, documented, and tested.
- RSIS3/mykb relevance: the wiki's environments would enforce the tag schema at provisioning time; this note records the vocabulary so the loop's resource lifecycle automation stays accurate.
- Access control: tags should describe, not authorize; IAM policies that read tags can be bypassed by untagged or mis-tagged resources, so combine with identity-based controls.
- Cost hygiene: require tags on cost-allocatable resources and reconcile the untagged bucket in the monthly cost review, shrinking it toward zero.

## Related
- [[wiki/cloud-infra/finops-practices|FinOps Practices]] — tags power cost allocation
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — clean reports need clean tags
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]] — tags defined in code
- [[wiki/devops-infra/terraform|Terraform]] — tag enforcement at apply time
