---
type: "concept"
title: "Preflight Checks & Guards"
description: "Validating prerequisites before destructive operations"
tags: ["preflight", "checks", "guards", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Preflight Checks & Guards

## Summary
Preflight checks and guards are validation gates that run before an action — a deploy, a migration, a cluster upgrade, a release — and abort if the environment is not in the expected state. They catch the cheap failures (missing secrets, wrong versions, unschedulable manifests) before they become expensive ones.

## Details
- Mechanism: a preflight step collects environment facts (cluster version, quota, secret existence, image availability, network reachability) and asserts expectations; failures fail fast with a clear message; guards also run at later stages (pre-sync, pre-traffic, pre-promotion) as the action progresses; tools embed them (helm template --validate, kubeconform, terraform plan, argocd appset dry-run, kubectl diff).
- Concrete example: a deploy pipeline checks that the target namespace exists, secrets are present, the image digest resolves, and the manifest passes schema validation before applying; a migration guard checks the database is reachable and the migration is reversible; an upgrade guard verifies the Kubernetes version is supported.
- Failure modes: guards checking the wrong environment (checked staging, applied to prod); guards that pass because they test presence, not validity (a secret that exists but holds stale credentials); guard code that becomes untrusted (skipped via bypass flags) after blocking a legitimate release; race conditions where the environment changes between check and apply.
- Tradeoffs: preflights convert failures from mid-rollout incidents into pre-rollout errors, which are far cheaper, but they add pipeline latency and need maintenance as the environment evolves; the cost is worth it for anything stateful or hard to roll back; the alternative — check nothing and react — only works for fully idempotent, stateless deployments.
- Operational notes: keep guards in the repo, make their failure messages actionable, log guard results, and test that guards actually catch a broken environment.
- RSIS3 relevance: RSIS3's loop runs should preflight too — verify the store is writable, telemetry targets reachable, and parameters valid before starting an experiment, so failures are clear and cheap.

## Related
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]]
- [[wiki/devops-infra/deployment-verification-synthetic-checks|Deployment Verification & Synthetic Checks]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
