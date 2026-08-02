---
type: "concept"
title: "Platform Engineering"
description: "Building internal platforms that make delivery fast and safe for product teams"
tags: ["platform-engineering", "internal-platforms", "developer-experience", "golden-paths"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Platform_engineering", "https://en.wikipedia.org/wiki/Internal_developer_platform"]
---

# Platform Engineering

## Summary
Platform engineering designs, builds, and runs internal developer platforms — the paved roads of CI/CD, environments, observability, and self-service infrastructure that product teams use. Its goal is developer productivity at scale: golden paths that make the safe way the easy way.

## Details
- An internal developer platform (IDP) abstracts infrastructure behind self-service interfaces: templates, APIs, and golden paths.
- Golden paths are blessed, supported ways to build and ship — fast by default, with escape hatches for the exceptional.
- The platform team treats developers as users: measure adoption, feedback, and time-to-production, not just uptime.
- Platform work is product work: documentation, onboarding, and APIs are features with backlogs.
- Top-down mandates fail; platforms win by being measurably faster and safer than the DIY path.
- For the mykb bundle, platform engineering is the curation pipeline as a platform: templates, validators, and a golden article path.
- Worked example — a golden path for a new wiki service: template repo, CI with link checks, staging environment, and one-command promotion — all self-service, all supported.

Worked example — a golden path for a new wiki service: template repo, CI with link checks, staging environment, and one-command promotion — all self-service, all supported.

## Related
- [[wiki/tooling/golden-paths|Golden Paths]]
- [[wiki/software-engineering/internal-developer-platforms|Internal Developer Platforms]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/software-engineering/internal-developer-platforms|Internal Developer Platforms]]
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
- [[wiki/communities/build-caching|Build Caching]]
- [[wiki/devops-infra/development-environments-as-code|Development Environments as Code]]
