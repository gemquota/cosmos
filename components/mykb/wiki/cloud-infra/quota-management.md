---
type: "concept"
title: "Quota Management"
description: "Hard per-account limits on cloud resources that prevent runaway consumption and enforce governance"
tags: ["quota", "limits", "governance", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Quota Management

## Summary

Cloud quotas (limits) cap resources per account/region — instances, IPs, API calls, storage. They protect providers from runaway usage and customers from surprise bills; hitting them mid-incident is a classic operational failure that planning prevents.

## Details
- Mechanism: each service defines quota dimensions (EC2 vCPU per family, S3 buckets per account, API rate limits, GCP quotas per project/region); quotas are soft (raiseable via requests) or hard (API call rates); some track usage (vCPUs in use) vs capacity; IAM can restrict quota visibility and raise permissions. Bursting past a quota fails API calls with explicit error codes.
- Concrete example: an autoscaling group hits the vCPU quota during a spike and cannot launch — the incident compounds because the fix (raise quota) needs a support request; a CI pipeline hits the API rate limit and fails builds; a storage quota blocks a backup job silently, so retention gaps appear months later.
- Failure modes: discovering quotas during incidents; quota requests taking days for large raises; per-region quotas duplicating (forgot the new region); and confusing soft capacity quotas with rate limits — each needs its own headroom plan.
- Operational tradeoffs: raising quotas costs nothing but planning (and sometimes approval); the discipline is a quota registry: what is used, headroom, owner, and review cadence. Automate quota monitoring (usage/limit metrics) and pre-raise before launches, not during them.
- RSIS3/mykb relevance: the wiki's quota registry would track per-service limits and headroom, so the loop's capacity plans include quota raises in the pre-launch checklist.
- Request patterns: batch quota increases with usage projections (providers ask for justification); keep a template with peak measurements ready so incident-time raises are not blocked by paperwork.
- Rate-limit planning: API rate quotas need headroom for retries and bursts; design clients with exponential backoff and monitor 429/403 rate-limit responses as a health signal.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — scaling loops can hit ceilings
- [[wiki/cloud-infra/budget-alerts|Budget Alerts]] — financial twin of quotas
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]] — quota variance across providers
- [[wiki/devops-infra/kubernetes|Kubernetes]] — resource quotas inside clusters
