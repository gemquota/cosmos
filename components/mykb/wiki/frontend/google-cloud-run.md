---
type: "entity"
title: "Google Cloud Run"
description: "Serverless container platform on GCP scaling requests to zero with per-request billing"
tags: ["google-cloud", "cloud-run", "serverless", "containers", "gcp"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Google Cloud Run

## Summary
Google Cloud Run runs stateless containers as serverless services: it scales to zero, bills per request, and manages revisions with traffic splitting. Any OCI container deploys directly.

## Details
- Port-based HTTP serving with autoscaling; revisions enable canary traffic splits.
- Knative-based — the same model runs on any Knative platform.
- A good middle ground: containers without Kubernetes cluster management.

## Related
- [[wiki/frontend/serverless|Serverless]] — containerized serverless model
- [[wiki/devops-infra/kubernetes|Kubernetes]] — Knative lineage
- [[wiki/security/container-hardening|Container Hardening]] — image security still applies
- [[wiki/frontend/edge-functions|Edge Functions]] — latency-optimized alternative
- [[wiki/devops-infra/terraform|Terraform]] — GCP provisioning
