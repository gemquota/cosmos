---
type: "concept"
title: "Deploy Safety Checks"
description: "Gates that stop bad deployments before they reach users"
tags: ["deployment", "safety", "checks", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Deploy Safety Checks

## Summary
Deploy safety checks are automated gates evaluated before, during, and after a release: lint and schema validation before deploy, health and metric gates during rollout, and verification after. They replace "hope it's fine" with explicit, code-reviewed conditions that must pass for the deploy to proceed.

## Details
- Mechanism: pre-deploy checks run in CI — config validation, image signing verification, schema diffs, dependency and license gates; in-progress checks watch rollout health — readiness, error rate, latency percentiles against a threshold window; post-deploy checks run smoke and synthetic tests against the new version; any failed gate pauses or aborts the rollout.
- Concrete example: a GitOps pipeline that validates manifests with kubeconform, verifies image signatures, then syncs; Argo Rollouts or Flagger holds promotion until analysis steps pass; a smoke test suite hits the new pods directly before traffic shifts; on failure the controller reverts automatically.
- Failure modes: gates that check the wrong thing (readiness passing while logic is broken — so add request-level checks); thresholds tuned to normal variance, causing false aborts or false confidence; checks that silently skip (missing secrets, empty test runs); too many gates slowing every deploy until teams disable them; checks running only in CI while production behaves differently.
- Tradeoffs: safety checks cost pipeline time and complexity but dramatically reduce mean time to recovery by catching failures early; the art is choosing few, high-signal gates — one schema check, one signature check, one health window, one smoke suite — and making every gate auditable.
- Operational notes: version the gates with the code, log gate results, and run post-deploy verification for at least the traffic-window duration.
- RSIS3 relevance: RSIS3's own upgrades (new loop versions, parameter migrations) deserve the same gates — validate the new artifacts and observe telemetry before trusting them in the live loop.

## Related
- [[wiki/devops-infra/deployment-verification-synthetic-checks|Deployment Verification & Synthetic Checks]]
- [[wiki/devops-infra/smoke-tests-after-deploy|Smoke Tests After Deploy]]
- [[wiki/devops-infra/preflight-checks-and-guards|Preflight Checks & Guards]]
