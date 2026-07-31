# COSMOS — Development Roadmap

**Phase 0:** Specification & Structure ✅ (current)
**Phase 1:** Shared Infrastructure ⬜
**Phase 2:** Orchestrator CLI ⬜
**Phase 3:** Dashboard ⬜
**Phase 4:** Integration ⬜

---

## Phase 0 — Specification & Structure

- [x] Create COSMOS directory structure
- [x] Write COSMOS-SPEC.md
- [x] Write ARCHITECTURE.md
- [x] Write ROADMAP.md
- [ ] Copy SPACE into components/
- [ ] Copy myKB into components/
- [ ] Copy myRSIKB into components/
- [ ] Copy myRSISKB into components/
- [ ] Copy RSIS3 into components/
- [ ] Copy RSISB into components/

## Phase 1 — Shared Infrastructure

- [ ] Unified Sentry watcher for all components
- [ ] Shared CI/CD workflow (GitHub Actions)
- [ ] Shared deployment scripts
- [ ] Centralized logging

## Phase 2 — Orchestrator CLI

- [ ] `cosmos status` — check all components
- [ ] `cosmos start/stop` — control component servers
- [ ] `cosmos logs` — tail component logs
- [ ] `cosmos build/test` — build and test all
- [ ] Install via `cosmos/install.sh`

## Phase 3 — Dashboard

- [ ] Status panel (Sentry data)
- [ ] Component cards with quick links
- [ ] System health metrics
- [ ] Embedded meta viewer

## Phase 4 — Integration

- [ ] SPACE → myKB spec export
- [ ] myRSISKB bridge wiring
- [ ] Cross-component data flows
