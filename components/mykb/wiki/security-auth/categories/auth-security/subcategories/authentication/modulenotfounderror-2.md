---
type: "entity"
title: "ModuleNotFoundError"
resource: ""
---
description: "Import failures caused by missing dependencies, wrong environments, or bad paths"
tags: ["android", "api", "ast", "auth", "authentication", "aws", "bash", "entity", "errors", "python"]
timestamp: "2026-07-19T22:41:41Z"

# ModuleNotFoundError

## Summary
ModuleNotFoundError is the Python error raised when an import cannot find its target module. It is usually an environment problem: a package not installed, the wrong interpreter, or a path misconfiguration. Because it appears at import time, one missing dependency can take down an entire application, so prevention is cheap insurance.

## Details
- **Definition** — the error means the import system could not locate a module by that name in any path on sys.path.
- **Common causes** — uninstalled packages, mismatched virtual environments, wrong working directories, and renamed or moved modules.
- **Environment drift** — code that runs locally but fails elsewhere usually means dependencies were installed but never recorded.
- **Locking** — pinning dependencies with lock files makes environments reproducible and import failures predictable.
- **Namespacing** — local files that shadow installed packages, or packages with the same name as standard library modules, cause subtle breakage.
- **Diagnosis** — checking the interpreter, environment, and pip list narrows the cause quickly; the traceback names the missing module.
- **Common failure modes** — fixing the symptom by installing globally, committing environment-specific paths, and ignoring version mismatches.
- **Worked example** — a deploy fails with ModuleNotFoundError for a new library; the fix is adding it to the lock file and rebuilding the environment image.
- **Practical relevance** — disciplined dependency management prevents the most common class of environment-related failures.

- **Startup check** — a smoke test that imports the application in the target environment catches missing modules at deploy time.
- **Tooling** — dependency lock files and container builds make the installed set explicit and repeatable across machines.
- **Triage** — a fresh environment, correct interpreter, and installed lockfile resolve most import failures within minutes.
## Related
- [[wiki/tooling/environment-management|Environment Management]] — reproducible environments
- [[wiki/testing/test-configuration-management|Test Configuration Management]] — test environment setup
- [[wiki/software-engineering/refactoring|Refactoring]] — module reorganization
- [[wiki/software-engineering/code-review|Code Review]] — catching missing deps
- [[wiki/testing/smoke-testing|Smoke Testing]] — catching import failures early
- [[wiki/tooling/containerization-practice|Containerization Practice]] — packaging dependencies
