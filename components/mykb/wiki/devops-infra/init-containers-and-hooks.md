---
type: "concept"
title: "Init Containers & Hooks"
description: "Setup containers and lifecycle hooks before main containers start"
tags: ["init-containers", "hooks", "kubernetes", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Init Containers & Hooks

## Summary
Init containers run to completion before a pod's main containers start — fetching data, waiting for dependencies, rendering config; container lifecycle hooks (postStart, preStop) run commands or HTTP calls at specific lifecycle moments. Both let a pod prepare its own environment and drain cleanly without custom orchestrator logic.

## Details
- Init-container mechanics: declared in `initContainers`, they run in order, each to completion, sharing volumes with the main container; a failing init container restarts the pod (per restartPolicy), making it a natural gate — wait-for-db, migrate-schema, fetch-secrets.
- Hook mechanics: `postStart` runs right after the container starts (no guarantee before the main process, so race conditions are possible); `preStop` runs before termination and, with terminationGracePeriod, gives the app time to drain connections and finish work; hooks can be exec or HTTP GET.
- Concrete example: an init container runs `migrate` before the app starts; another waits for the database with a retry loop; `preStop` calls the app's /shutdown endpoint and sleeps briefly so the load balancer deregisters the pod before the process exits.
- Failure modes: init containers that never succeed (a wait loop with no timeout) leaving pods stuck Pending; postStart hooks racing the main process and mutating shared state; preStop hooks that exceed the grace period, killing the pod mid-drain; hooks running on every restart when only first-run work was intended; scripts without logging, making stuck pods mysterious.
- Tradeoffs: init containers and hooks keep lifecycle logic in the pod spec, portable across clusters, but they are imperative escapes from declarative Kubernetes — logic lives in scripts, not manifests, and must be tested; the alternative is operator-level orchestration, which is more powerful but heavier.
- Operational notes: always add timeouts to wait loops, log hook output, and test termination behavior in game days.
- RSIS3 relevance: the wiki daemon's startup (check the store, render indexes) and shutdown (flush state, drain requests) map directly to init containers and preStop hooks.

## Related
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — related coverage in the same cluster
- [[wiki/os-shell/systemd-and-init-systems|systemd & Init Systems]] — related coverage in the same cluster
- [[wiki/devops-infra/provisioners-packer-cloud-init|Provisioners: Packer & cloud-init]] — related coverage in the same cluster
- [[wiki/devops-infra/healthcheck-and-sidecar-containers|Healthcheck & Sidecar Containers]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
