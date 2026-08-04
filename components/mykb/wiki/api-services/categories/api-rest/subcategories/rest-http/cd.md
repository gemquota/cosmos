---
type: "entity"
title: "CD"
description: "Acronym referenced in session 7a06f562"
tags: ["entity", "acronym", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# CD

## Summary
CD is an acronym entity from the wiki's session index whose body defines it as continuous delivery or continuous deployment: automatically shipping code changes to production. It matters because fast, reliable release automation is what separates deployable systems from fragile ones. This page documents the CD concept in that context. CD's value compounds when rollback is as automated as rollout.

## Details
- **Definition** — continuous delivery keeps every change releasable by automating the path to production; continuous deployment additionally ships every passing change automatically.
- **Pipeline** — CD pipelines build, test, and promote artifacts through environments, with gates at each stage.
- **Safety** — automated rollback, feature flags, and deploy-safety-checks make frequent releases safe rather than reckless.
- **Artifacts** — reproducible builds and versioned artifacts ensure the exact thing tested is the thing deployed.
- **Worked example** — a change merged to main runs tests, builds a container, deploys to staging, passes verification, and promotes to production with one-command rollback.
- **Failure modes** — flaky pipelines, environment drift, and untested rollback paths undermine CD's promises.
- **Relation to CI** — CD extends continuous integration: CI verifies every change, CD delivers every verified change.
- **Practical relevance** — CD is a standard practice in modern platform engineering and a recurring topic in devops and API service notes.
- **Rollback** — one-command rollback to the previous artifact makes failed releases survivable.
- **Progressive delivery** — canaries and feature flags let CD ship while risk stays bounded.
- **Verification** — post-deploy checks confirm the new version is actually healthy.
- **Failure example** — a pipeline that deploys without verification ships broken code and calls it done.
- **Environment promotion** — artifacts move through environments without rebuilds, so what was tested is what ships.
- **Audit** — deployment records should capture who, what, when, and why for every release.

## Related
- [[wiki/devops-infra/continuous-delivery-pipelines|Continuous Delivery Pipelines]] — the pipeline machinery
- [[wiki/devops-infra/ci-cd-best-practices|CI/CD Best Practices]] — the practice guidance
- [[wiki/devops-infra/deploy-safety-checks|Deploy Safety Checks]] — gates that make releases safe
- [[wiki/dev-tools/release-management|Release Management]] — coordinating releases
- [[wiki/dev-tools/reproducible-builds|Reproducible Builds]] — trustworthy artifacts
