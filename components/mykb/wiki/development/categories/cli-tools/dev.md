---
type: "entity"
title: "Dev"
description: "Dev: developer workflows spanning terminals, editors, and automation queues"
tags: ["entity", "ast", "cli", "ide", "queue", "terminal", "workflow"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# Dev

## Summary

Dev captures the day-to-day developer workflow in this cluster: terminals, editors, task queues, and the automation that connects them. It is the practical layer where CLI tools, scripts, and tooling decisions meet real work. It matters because small workflow frictions compound into large productivity losses. The entity functions as a hub for the workspace's tooling conventions and workflow decisions.

## Details

- **Definition** — Dev refers to the developer experience loop: writing code, running tools, reading feedback, and repeating.
- **Terminal workflows** — Fast, scriptable shells remain the hub for builds, tests, and automation because they compose.
- **Task queues** — Queues and task runners serialize work with retries and ordering, keeping long operations off the interactive path.
- **Toolchain integration** — Editors, linters, and runners that share configuration reduce the gap between writing and verifying code.
- **Automation** — Scripts that capture repeated commands turn tribal knowledge into executable, auditable process.
- **Context switching** — The cost of switching between tools is real; workflows that minimize mode changes protect focus.
- **Failure modes** — Manual steps, undocumented commands, and environment drift break reproducible workflows.
- **Practical relevance** — Recording dev workflow entities in the wiki preserves the workspace's own tooling conventions for future sessions.
- **Onboarding** — Documented workflows let new sessions and new humans start contributing without reverse-engineering the setup.
- **Reproducibility** — Pinning tool versions and providing setup scripts makes the dev environment a checked-in artifact.
- **Feedback speed** — The fastest workflows put build and test results within a single keystroke of the edit.
- **Workflow review** — Periodic review of the developer workflow removes steps that stopped paying for themselves as tools and code evolved.

## Related

- [[wiki/development/categories/cli-tools/cognitive|Cognitive]] — workflow and mental load
- [[wiki/development/categories/cli-tools/reality|Reality]] — verifying what workflows produce
- [[wiki/development/categories/cli-tools/while|While]] — loops inside scripts and queues
- [[wiki/development/categories/cli-tools/senior-dev|Senior Dev]] — experienced workflow judgment
- [[wiki/development/categories/cli-tools/performance|Performance]] — workflow speed
- [[wiki/development/categories/cli-tools/technical-reality|Technical Reality]] — verifying workflow outcomes
