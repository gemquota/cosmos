---
type: "concept"
title: "Environment Variables"
description: "Named values inherited by processes that parameterize program behavior without CLI flags"
tags: ["environment", "variables", "config", "processes"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Environment Variables

## Summary
Environment variables are key-value pairs inherited from parent to child process. They configure behavior — PATH, HOME, LANG — and carry secrets or feature switches into programs.

## Details
- Export to pass down: `export FOO=bar`; `env` prints the environment; `env -i` starts clean.
- Naming conventions (UPPER_CASE, prefixes like REACT_APP_) prevent collisions.
- RSIS3 relevance: the agent harness passes API keys and workspace paths through env vars.

## Related
- [[wiki/os-shell/process-management|Process Management]] — env is inherited through process creation
- [[wiki/os-shell/dotfiles|Dotfiles]] — dotfiles often set environment variables
- [[wiki/security/secrets-management|Secrets Management]] — env vars are a common (risky) secret channel
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — scripts read env as input
- [[wiki/devops-infra/docker-compose|Docker Compose]] — compose env files set variables
