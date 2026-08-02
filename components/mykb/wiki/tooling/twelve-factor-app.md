---
type: "concept"
title: "Twelve-Factor App"
description: "The twelve principles for building deployable, portable, cloud-ready apps"
tags: ["twelve-factor", "principles", "deployment", "config"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://12factor.net/", "https://en.wikipedia.org/wiki/Cloud_native_computing"]
---

# Twelve-Factor App

## Summary
The twelve-factor methodology is a checklist for software that deploys cleanly to the cloud: codebase, dependencies, config, backing services, build/release/run, processes, port binding, concurrency, disposability, dev/prod parity, logs, and admin processes. Each factor removes a class of environment-specific failure.

## Details
- One codebase per app, tracked in VCS, with many deploys from it — environments are configurations, not forks.
- Declare dependencies explicitly; keep config in environment variables; treat backing services as attached resources.
- Separate build, release, and run stages; processes are stateless and disposable, so they can start and die safely.
- Concurrency via process model, port binding for services, and logs as event streams to stdout.
- Dev/prod parity keeps surprises out; admin tasks run as one-off processes, not cron inside the app.
- The factors are defaults with reasons: each one names a failure mode the factor prevents.
- For the mykb bundle, the wiki reading service follows the factors; the content itself is data the app serves.

Worked example — the wiki app stores its DB URL in env, logs JSON to stdout, and is built once per commit; any environment can run it because nothing about the host leaks into the code.

## Related
- [[wiki/tooling/cloud-native-principles|Cloud Native Principles]]
- [[wiki/tooling/environment-management|Environment Management]]
- [[wiki/software-engineering/logging-strategies|Logging Strategies]]
- [[wiki/tooling/containerization-practice|Containerization Practice]]
- [[wiki/devops-infra/env-var-management|Env Var Management]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/dev-tools/structured-logs|Structured Logs]]
- [[wiki/dev-tools/log-levels|Log Levels]]
- [[wiki/devops-infra/configuration-management-revisited|Configuration Management]]
