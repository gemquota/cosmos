# COSMOS — Unification Specification

**Version:** 0.1.0
**Status:** Draft
**Last Updated:** 2026-07-29

---

## 1. Purpose

COSMOS unifies five RSI-family projects — SPACE, myKB, myRSIKB, myRSISKB, and RSIS3 —
into a coherent ecosystem with shared infrastructure, a unified orchestrator CLI, and a
consolidated dashboard.

## 2. Component Map

| ID | Component | Source | Role | Language |
|:--:|-----------|--------|------|:--------:|
| C1 | **SPACE** | `~/dev/space/` | Prompt engine, CLI, spec generation | TypeScript |
| C2 | **myKB** | `~/dev/codex/mykb/` | Daily knowledge base (Obsidian wiki) | Markdown/Python |
| C3 | **myRSIKB** | `~/dev/codex/myrsikb/` | RSI knowledge base, audit reports | Python |
| C4 | **myRSISKB** | Bridge between RSIS3 and myKB | RSI knowledge bridge | Python |
| C5 | **RSIS3** | `~/dev/codex/rrp+/rsis/` | 3-loop RSI system | Python |
| C6 | **RSISB** | `~/dev/codex/rrp+/rsisb/` | Earlier RSI version (archived) | Python |

### 2.1 Relationship Diagram

```
myKB ──► myRSISKB ◄── RSIS3
  ▲          ▲
  │          │
  └── myRSIKB
         ▲
         │
       SPACE
```

- **myRSISKB** is the bridge between RSIS3 (the 3-loop RSI engine) and myKB (the knowledge base)
- **myRSIKB** feeds into myRSISKB with audit reports and analysis
- **SPACE** provides prompt/spec generation that feeds into the knowledge ecosystem
- **RSISB** is an earlier version of RSIS3, kept for reference

## 3. Directory Structure

```
cosmos/
├── COSMOS-SPEC.md              # This document
├── ARCHITECTURE.md              # Architecture overview
├── ROADMAP.md                   # Development roadmap
├── README.md                    # Entry point
├── components/                  # Duplicated project sources
│   ├── space/                   # C1 — TypeScript prompt engine
│   ├── mykb/                    # C2 — Obsidian knowledge base
│   ├── myrsikb/                 # C3 — RSI knowledge base
│   ├── myrsiskb/                # C4 — RSI knowledge bridge
│   ├── rsis3/                   # C5 — 3-loop RSI system
│   └── rsisb/                   # C6 — Earlier RSI version
├── infra/                       # Shared infrastructure
│   ├── heartbeat/               # Sentry monitoring (watches.json)
│   ├── ci/                      # Shared CI/CD
│   └── deployment/              # Deploy scripts
├── cli/                         # Orchestrator CLI
│   └── cosmos                   # Unified command
├── dashboard/                   # Unified web dashboard
├── docs/                        # Shared documentation
└── meta/                        # Cycle audit/review docs
```

## 4. Shared Infrastructure

### 4.1 Sentry Heartbeat
A unified `watches.json` monitoring all COSMOS component servers.
Each component that serves a port gets a watch entry with auto-restart.

### 4.2 CI/CD
Shared GitHub Actions workflows that:
- Run tests for all components on push
- Lint all codebases
- Build all artifacts
- Deploy dashboard to GitHub Pages

### 4.3 Logging
Centralized logging directory at `cosmos/logs/` with component-prefixed files.

## 5. Orchestrator CLI (`cosmos`)

A single entry point that can control all components:

```
cosmos status              # Show status of all components
cosmos start <component>   # Start a component's server
cosmos stop <component>    # Stop a component
cosmos run <component>     # Run a component's CLI
cosmos logs <component>    # Tail logs
cosmos update              # Pull latest for all components
cosmos build               # Build all components
cosmos test                # Test all components
```

## 6. Dashboard

A single web UI showing:

- **Status panel** — Which components are up/down (via Sentry)
- **Component cards** — Quick links, descriptions, last activity
- **System health** — Uptime, test counts, build status
- **Meta viewer** — Embedded cycle audit/review/docs browser

## 7. Implementation Phases

| Phase | Focus | Deliverables |
|:-----:|-------|-------------|
| 0 | Specification & Structure | COSMOS-SPEC.md, ARCHITECTURE.md, component copies, ROADMAP.md |
| 1 | Shared Infrastructure | Sentry heartbeat for all components, CI/CD, deploy scripts |
| 2 | Orchestrator CLI | `cosmos` command with all subcommands |
| 3 | Dashboard | Unified web UI with status, cards, embedded meta viewer |
| 4 | Integration | Cross-component data flow, myRSISKB bridge wiring |
