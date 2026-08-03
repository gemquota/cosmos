---
type: "concept"
title: "Devcontainers"
description: "Containerized development environments defined in config"
tags: ["devcontainer", "containers", "development", "vscode"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Devcontainers

## Summary
Devcontainers package the entire development environment — toolchain, dependencies, extensions, and config — into a container described in `devcontainer.json`, so every contributor gets the same environment from a repository. "Revisited" reflects the current state: devcontainers are now a mature standard (VS Code, JetBrains, Codespaces, GitHub CLI) used for reproducible development and even CI parity.

## Details
- Mechanism: `devcontainer.json` declares the base image, features (language toolchains), post-create commands, mount points, forwarded ports, and extensions; the tooling builds or pulls the image, starts the container, mounts the workspace, and connects the editor; features compose additional layers without custom Dockerfiles.
- Concrete example: a Python repo with a devcontainer pinning Python 3.12, uv, and a formatter; a contributor clones and opens it — no local Python install needed; CI reuses the same image so "works on my machine" disappears; Codespaces provisions the identical environment in the cloud.
- Failure modes: image drift — base images change and break builds, so pin digests and rebuild periodically; slow first builds when every dependency is compiled from scratch (cache layers and prebuilt images fix this); permission and mount issues on different host filesystems (bind-mount ownership); features that conflict or install different versions than documented; environment parity illusion — the container matches CI, not production, so platform-specific bugs still leak.
- Tradeoffs: devcontainers trade image build and maintenance effort for onboarding speed and reproducibility; the alternative (setup scripts) drifts by nature; the middle path is a base image plus thin per-repo overlays.
- Operational notes: keep devcontainer config reviewed like code, test image builds in CI, and document the escape hatch for environment-specific debugging.
- RSIS3 relevance: the cosmos repo's three components could standardize on one devcontainer so any loop iteration runs against a known toolchain, removing environment variables from reproducibility concerns.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
