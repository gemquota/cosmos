---
type: "concept"
title: "Admission Controllers & Webhooks"
description: "Intercepting API requests to validate or mutate resources"
tags: ["admission", "webhooks", "kubernetes", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Admission Controllers & Webhooks

## Summary
Admission control is the last gate before a Kubernetes API request is persisted: controllers run inside kube-apiserver and can validate or mutate objects during CREATE, UPDATE, and CONNECT (and DELETE for some built-ins). Mutating controllers run first, then validating ones, and both execute on every request in scope, which makes them the natural home for cluster policy, defaulting, and safety checks that CRD schema validation cannot express.

## Details
- Mechanism: mutating webhooks can edit the object (inject sidecars, set resource defaults, add tolerations) before it is validated and persisted; validating webhooks only accept or reject. Mutating admission runs before validating, and within each phase controllers execute in registered order, so later hooks see earlier mutations.
- Concrete examples: a mutating webhook that defaults resource requests for pods that omit them; a validating webhook that rejects images without a digest or from an unknown registry; the built-in PodSecurity admission provides a similar gate without custom code.
- Failure modes: a webhook that times out or is unreachable blocks the entire API path unless `failurePolicy: Ignore` is set; the classic outage is a misconfigured webhook certificate taking down cluster operations. `sideEffects: None` is required for dry-run safety, otherwise dry-run requests can trigger real side effects.
- Operational tradeoffs: webhooks add latency to every matching request, so scope them with `matchPolicy` and namespace selectors, keep `timeoutSeconds` low, and make mutations idempotent because requests may be retried. Version webhook and its configuration together: a stale webhook that mutates an object in an unexpected way causes repeated validation failures.
- Version skew: kube-apiserver upgrades can change webhook protocol behavior, so pin the admissionregistration API version and test upgrades against staging first.
- RSIS3/mykb relevance: the same gate-and-default pattern applies to RSIS3 loop pipelines — validate inputs before they are persisted, default what the loops forget, and fail closed on unknown request shapes rather than letting corrupt state enter the registry.

## Related
- [[wiki/devops-infra/ingress-controllers|Ingress Controllers]]
- [[wiki/infrastructure/sdn-controllers|SDN Controllers]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
