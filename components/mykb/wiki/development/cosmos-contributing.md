---
type: "guide"
title: "Contributing to Cosmos — onboarding a collaborator"
description: "How a new collaborator runs the stack, gets a role, and is onboarded by the system itself (Phase 12)"
tags: ["cosmos", "contributing", "phase-12", "onboarding", "roles"]
timestamp: "2026-08-09T18:30:00Z"
status: "stable"
---

# Contributing to Cosmos

Cosmos is a self-improving loop stack (RSIS3) plus its memory (MyKB) and
ideation engine (SPACE). A collaborator does not need to read everything:
the system onboarded them the same way it improves itself — goal-sourced
candidates from the L2 loop.

## Run the stack

1. Install prerequisites: Python 3.11+, Node 20+, and the package deps
   (`pip install -r components/rsis3/requirements.txt` if present).
2. Start the bridge: `cd components/rsis3 && node rack/bridge/server.mjs`
   (port 8787; `/health` reports model + LLM connectivity).
3. Open the unified dashboard: repo-root `index.html` (Overview, Pulses,
   MyKB, SPACE tabs).
4. Run a cycle batch: `cd components/rsis3 && python3 -m rsis launch
   --cycles 1`. The daemon does this on a ~3-minute cadence when running.

## Get a role

Roles are granted in `.rsis/users.json` by an existing approver:

```
python3 -m rsis users add <id> --name "<Name>" --role observer \
    --projects <project> [--projects ...]
python3 -m rsis users token <id>      # prints a signed bearer token
```

- `observer` — read live telemetry, sessions, and staged approvals.
- `contributor` — also submit candidates through the normal pipeline
  (bridge chat / L2 goals) and propose changes.
- `approver` — also gate and apply staged approvals
  (`python3 -m rsis approve <id>` or the dashboard approvals view).

Authorization is scoped by project membership and policy, not role alone:
`User → Identity → Role → Project membership → Policy → Capability →
Action`. Being an approver does not mean approving every project; the
acting user is recorded in `.rsis/audit.jsonl` for every gated action.

## Be onboarded by the system

1. A goal-sourced L2 candidate finds real gaps in the repo and proposes a
   change; policy may stage it as `rack/approvals/<id>.json`.
2. The verification mesh (`rack/verification/`) records the gates the
   candidate passed; an approver reviews the rendered diff and approves or
   rejects.
3. Every applied candidate is attestable (invariant set + sha256) and
   rollback-restorable from its pre-state.
4. Durable conclusions land in `components/mykb/wiki/syntheses/` so future
   sessions inherit them.

## Rules of the road

- Never write directly to policy-gated paths (`rack/policy.json`,
  `rack/bridge/server.mjs`, `rack/approvals/`, `rsis/policy.py`) — stage
  and approve.
- Respect budgets: `.rsis/budgets.json` fail-closes LLM enrichment when a
  per-loop daily ceiling is breached.
- Cross-project work is profile-scoped: `rsis init --project <repo>`
  scaffolds `rack/projects/<name>.json`, and goal seeds are tagged
  `project:<name>` in MyKB.
- Federation only moves notes tagged `publishable`; provenance is never
  stripped.

## Related

- [[wiki/syntheses/rsis3-roadmap-sequels-2-3-2026-08-09|RSIS3 roadmap sequels II–III (Phases 6–15)]]
- [[wiki/syntheses/rsis3-sequel-2-phases-6-10-2026-08-09|RSIS3 Sequel II — Phases 6–10]]
