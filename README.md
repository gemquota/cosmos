# 🌌 COSMOS

**C**ognitive **O**rchestration **S**ystem for **M**eta-cognitive **O**ptimization & **S**ynthesis

RSIS3 (core) + MyKB (memory) + SPACE (ideation) — unified under one dashboard.

## Architecture

```
RSIS3 ─── core cognitive engine, 3-loop self-improvement
  ├── MyKB  ─── long-term persistent memory store
  └── SPACE ─── RRP prompt engine for ideation cycles
```

## Quick Start

```bash
cosmos dashboard          # Launch dashboard + all services
# or
./start.sh                # Same thing
# then open http://localhost:9000
```

## Components

| Component | Role | Language | Files |
|-----------|------|:--------:|:-----:|
| **RSIS3** | Core cognitive engine (3-loop RSI) | Python + JS | 112 |
| **MyKB** | Long-term memory for RSIS3 | Python | 2,436 |
| **SPACE** | RRP ideation engine | TypeScript | 333 |

## Deployed

- **Cosmos:** https://gemquota.github.io/cosmos/
- **Hub:** https://gemquota.github.io/hub/ (all non-COSMOS projects)

Short MyKB links (redirect to `components/mykb/`):
- Wiki: https://gemquota.github.io/cosmos/mykb/
- Stats: https://gemquota.github.io/cosmos/mykb/stats
- Guidance: https://gemquota.github.io/cosmos/mykb/#guidance
- Stub audit (redirects to Guidance): https://gemquota.github.io/cosmos/mykb/stub-audit
- Knowledge graph: https://gemquota.github.io/cosmos/mykb/graph
- Deep wiki paths (e.g. `mykb/wiki/<path>.md`) redirect via the root `404.html`.

## Commands

The dashboard (components/rsis3/dashboard/index.html) replicates the CLI:
the **MyKB → Guidance** view hosts the live guide (area direction, research &
feedback queue, stub triage with Save Queue, Plan / Apply + manifest, Rebuild
static), and Overview/Pulses/KG/Graphs/Constraints/Loops mirror `cosmos status`
telemetry.

```bash
cosmos dashboard   # Launch web dashboard + services
cosmos status      # Show component status
cosmos start       # Start component servers
cosmos stop        # Stop component servers
cosmos logs        # Tail service logs
cosmos guidance open  # Open the Guidance UI (direction, feedback, stub triage)
cosmos guidance status  # Show guidance + stub queue status
cosmos guidance build  # Rebuild guidance.json + stub-review.json
cosmos guidance plan  # Preview scaffolds from the research queue
cosmos guidance apply # Scaffold wanted/question pages + research manifest
cosmos stubs open  # Open the Guidance UI (alias of guidance open)
cosmos stubs plan  # Preview the queued stub decisions
cosmos stubs apply # Execute the queue + emit the inference manifest
cosmos stubs build # Rebuild the static stub data
```

## Structure

```
cosmos/
├── index.html          # Unified dashboard (single HTML file)
├── start.sh            # One-command launcher
├── cli/cosmos          # CLI entry point
├── AGENTS.md           # Agent instructions
├── ARCHITECTURE.md     # Full architecture docs
└── components/
    ├── rsis3/          # Core cognitive engine (Python)
    ├── mykb/           # Long-term memory (Python + wiki)
    └── space/          # RRP ideation engine (TypeScript)
```
