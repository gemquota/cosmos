---
type: "entity"
title: "ON"
resource: ""
---
description: "The semantics of on/off flags and enable states in configuration and code"
tags: ["android", "api", "ast", "auth", "authentication", "entity", "configuration", "flags"]
timestamp: "2026-07-19T22:41:43Z"

# ON

## Summary
ON is the enabled state of a switch, flag, or feature in a configuration or code path. It sounds trivial, but on/off semantics quietly decide system behavior: defaults, precedence, and validation all hinge on how enable states are defined. Getting flag semantics explicit prevents the classic "it worked on my machine" class of bugs and keeps behavior predictable.

## Details
- **Definition** — an on state means a feature, behavior, or path is active; off means it is inactive, and the two must be mutually exclusive and complete.
- **Defaults** — the default state when no value is provided must be explicit, because silent defaults become the de facto behavior.
- **Precedence** — env vars, config files, and runtime overrides need a defined order so the effective state is predictable.
- **Validation** — flags should accept a small, documented set of values, rejecting typos like "ture" instead of true.
- **Explicit vs implicit** — an absent flag is not the same as an explicit off; systems should distinguish "unset" from "disabled".
- **Migration** — renaming or reinterpreting a flag breaks running systems, so deprecated flags need compatibility periods.
- **Common failure modes** — flags read differently across environments, defaults that silently enable unsafe behavior, and dead flags nobody removes.
- **Worked example** — a service enables debug logging only when the DEBUG flag is explicitly true; absent means off in production and on in dev tooling, documented in the config.
- **Practical relevance** — disciplined on/off semantics keep configuration predictable across environments and teams.

- **Auditability** — effective flag states should be observable at runtime so operators can confirm what is actually enabled.
- **Semantics by type** — booleans, tristate values, and strings each need defined meanings to avoid interpretation drift.
- **Documentation** — each flag deserves a comment or entry describing its purpose, default, and owner.
## Related
- [[wiki/tooling/environment-management|Environment Management]] — environment-scoped settings
- [[wiki/tooling/feature-flag-sdks|Feature Flag SDKs]] — flag infrastructure
- [[wiki/testing/test-configuration-management|Test Configuration Management]] — test-time flags
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — documenting defaults
- [[wiki/software-engineering/code-review|Code Review]] — catching flag misuse
- [[wiki/testing/acceptance-testing|Acceptance Testing]] — verifying flag behavior
