# Cosmos — Agent Instructions

This repo contains the original components. The active monorepo is now at `/dev/cosmos-ts/`.

## Current State

- **Original components** remain at `components/{space,mykb,rsis3}/` for reference
- **myrsikb** has been removed (integrated into rsis3)
- **TypeScript monorepo** lives at `/dev/cosmos-ts/`

## TypeScript Monorepo (`/dev/cosmos-ts/`)

| Package | Source | Status |
|---|---|---|
| `@cosmos/core` | Shared types | ✅ |
| `@cosmos/space` | Prompt Engineering Tool | ✅ ported from TS |
| `@cosmos/mykb` | Knowledge OS | ✅ ported from Python |
| `@cosmos/rsis3` | Cognitive Engine | ✅ ported from Python |
| `@cosmos/dashboard` | Dashboard | ✅ integrated |

Build: `cd /dev/cosmos-ts && npm install && npm run build`
