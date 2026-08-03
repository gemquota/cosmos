---
type: "concept"
title: "Devcontainers"
description: "Containerized development environments defined in the repository, so every contributor runs the same setup"
tags: ["containers", "environments", "dx", "reproducibility"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://containers.dev/", "https://containers.dev/implementors/spec/"]
---

# Devcontainers

## Summary
A devcontainer is a Docker container configured via a `devcontainer.json` that becomes the development environment: editor extensions, toolchain, and services included. It makes 'works on my machine' a solved problem.

## Details
- The spec is maintained by the Dev Containers project; VS Code and other editors open the repo inside the container.
- Env as code: base image, features, ports, and setup scripts are versioned with the repo.
- RSIS3 relevance: agents that resume sessions benefit from the same reproducible shell.
- Development containers package a project's full dev environment — runtime, tools, extensions, and config — into a container image described by a devcontainer.json.
- The specification (devcontainer.json plus a Dockerfile or image) makes onboarding deterministic: clone, open, and the environment is identical to the maintainer's.
- The tradeoff is discipline: the environment must be defined entirely in the container, which surfaces 'works on my machine' problems as configuration errors.
- Devcontainers fit the reproducible-builds story and are the standard for editor-integrated (VS Code / Codespaces) development.
- **Worked example / comparison** — Worked example — the wiki's devcontainer would pin Python, Node, and the markdown toolchain versions; a new contributor would open the repo and run the build without installing anything.
- For mykb, devcontainers are documented as the environment half of reproducible development, complementing reproducible-builds.

- The discipline cost: the environment must be defined entirely in the container; anything outside it is 'works on my machine' again, which is why the container spec is the contract.
- Fit with reproducible builds: devcontainers are the environment half of reproducible development; the standing rule is that a contributor's environment is identical to the maintainer's, not merely similar.
- Agent sessions: the same containerized environment would let resumed agent work start from a known toolchain instead of an ad-hoc shell, which is the reproducibility property the loop relies on.
## Related
- [[wiki/software-engineering/developer-experience|Developer Experience]]
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]]
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]]
- [[wiki/devops-infra/docker-compose|Docker Compose]]
- [[wiki/security/container-hardening|Container Hardening]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
