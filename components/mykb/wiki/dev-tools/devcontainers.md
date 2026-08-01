---
type: "concept"
title: "Devcontainers"
description: "Containerized development environments defined in the repository, so every contributor runs the same setup"
tags: ["containers", "environments", "dx", "reproducibility"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Devcontainers

## Summary
A devcontainer is a Docker container configured via a `devcontainer.json` that becomes the development environment: editor extensions, toolchain, and services included. It makes 'works on my machine' a solved problem.

## Details
- The spec is maintained by the Dev Containers project; VS Code and other editors open the repo inside the container.
- Env as code: base image, features, ports, and setup scripts are versioned with the repo.
- RSIS3 relevance: agents that resume sessions benefit from the same reproducible shell.

## Related
- [[wiki/software-engineering/developer-experience|Developer Experience]] — devcontainers remove setup friction
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]] — setup documentation collapses into a container
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — environment reproducibility is the build's sibling
- [[wiki/devops-infra/docker-compose|Docker Compose]] — multi-service dev stacks run with compose
- [[wiki/security/container-hardening|Container Hardening]] — dev images need hardening too
