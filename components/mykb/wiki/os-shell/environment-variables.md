---
type: "concept"
title: "Environment Variables"
description: "Named values inherited by processes that parameterize program behavior without CLI flags"
tags: ["environment", "variables", "config", "processes"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Environment Variables

## Summary
Environment variables are key-value pairs that a process inherits from its parent and passes to its children. They parameterize behavior without CLI flags — `PATH` finds executables, `HOME` locates the user's directory, `LANG` selects locale — and they are the standard channel for configuration, feature switches, and secrets in containers and CI systems.

## Details
- Mechanism: the kernel stores each process's environment as a simple string array; `fork` + `exec` copies the parent's environment into the child, and `execve` can replace it entirely. The shell layer adds the semantics people actually use: `export FOO=bar` marks a variable for inheritance, `FOO=bar cmd` sets it for one command only, `env` prints the current environment, `env -i` starts with a clean slate, and `env -u FOO cmd` removes a variable. Programs read them via `getenv` or language equivalents, and the convention is UPPER_CASE names with a project prefix (`REACT_APP_*`, `AWS_*`, `MYKB_*`) to avoid collisions.
- Concrete examples: a cron job fails because its minimal environment lacks the `PATH` your interactive shell has — the canonical environment gotcha; a container gets `DATABASE_URL` and `API_KEY` from `docker run -e` or Compose's `env_file`; a CI pipeline injects secrets and build flags via environment; a daemon reads `MYKB_WIKI_ROOT` to locate its corpus; `PYTHONUNBUFFERED=1` and `NO_COLOR=1` tame tool output in scripts.
- Failure modes: the classic failures are secret leakage (env vars are visible to any process that can read `/proc/<pid>/environ` on the same host, and to any child process, so secrets in env are convenient but risky — they also leak into crash dumps, CI logs, and `printenv`-style debugging), unset-variable bugs (a script that assumes a var exists reads an empty string silently), and environment drift between machines (works on your laptop, breaks in prod because a var is missing or different). Prefix collisions and case sensitivity (`Path` vs `PATH` on case-sensitive systems) add confusion.
- Operational tradeoffs: env vars are the simplest cross-language configuration channel and fit the 12-factor model (config in the environment), but they are static per process, untyped, and hard to version; the modern practice is a layered approach — defaults in code, overrides via env, secrets via dedicated secret stores mounted as files or injected at deploy time, and schema validation at boot (parsing `process.env` through Zod, for example) so a missing or malformed variable fails fast instead of failing subtly later.
- RSIS3/mykb relevance: the agent harness passes API keys and workspace paths through env vars; the same discipline applies as for any boundary — validate at startup, never log the values, and keep secrets out of the process environment where a mounted secret file or a secret manager is feasible.

## Related
- [[wiki/os-shell/process-management|Process Management]] — env is inherited through process creation
- [[wiki/os-shell/dotfiles|Dotfiles]] — dotfiles often set environment variables
- [[wiki/security/secrets-management|Secrets Management]] — env vars are a common (risky) secret channel
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — scripts read env as input
- [[wiki/devops-infra/docker-compose|Docker Compose]] — compose env files set variables
