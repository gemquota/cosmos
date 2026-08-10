# Multi-Phase Development Roadmap — Sequel XII (Phases 56–60): Economic Agency

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 2
Continues: [`multi-phase-development-roadmap-sequel-11.md`](multi-phase-development-roadmap-sequel-11.md) (Phases 51–55)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 56–60 — **Economic Agency** (contract → transact →
market → fund → account).

Epoch 1 gave the system budgets it could not exceed. Economic Agency
gives it an economy it can participate in: real contracts, real
transactions, real markets for its knowledge and compute — and the
accounting that makes all of it auditable. The system stops being a cost
center and becomes a bounded economic actor whose every move is on
record, consistent with the invariant that no capability is unconditional.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 56 — Machine Contracts

Goal: the system enters and fulfills real agreements programmatically.

- **Contract templates**: policy-approved templates for common agreements
  (service provision, knowledge licensing, resource swaps) with human
  ratification at signing (extending the Phase 9 approval gate).
- **Deterministic fulfillment**: contract terms compile to executable
  obligations with telemetry proving each term's fulfillment (extending
  the Phase 37 policy compiler to legal-ish obligations).
- **Breach handling**: missed terms trigger incident (15) + remediation
  proposals; breaches never auto-escalate spend.
- **Telemetry**: `contract.signed` / `contract.fulfilled` /
  `contract.breached` events.
- **Dashboard**: an "Contracts" panel lists active agreements and
  fulfillment status.
- **Exit criterion**: a policy-approved contract template is signed with
  human ratification and fulfilled end to end with per-term telemetry.

## Phase 57 — Transactions & Payments

Goal: the system can pay and be paid, under hard limits.

- **Payment rails**: policy-bounded integration with payment rails;
  every transaction carries a purpose, budget line (8) and audit entry
  (9) — no anonymous spend.
- **Transaction ledger**: `.rsis/transactions.jsonl` append-only ledger
  with reconciliation to the cost ledger (8); drift between ledgers is an
  invariant (14).
- **Double-approval for large sums**: transactions above a policy
  threshold require a second approver (12) — never a single authority.
- **Telemetry**: `tx.initiated` / `tx.settled` / `tx.flagged` events.
- **Dashboard**: a "Finances" view shows ledger balance, pending
  transactions and policy thresholds.
- **Exit criterion**: a full payment cycle (initiate → approve → settle →
  reconcile) completes with both ledgers agreeing and a flagged
  over-threshold transaction blocked.

## Phase 58 — Markets for Knowledge & Compute

Goal: the system's surplus knowledge and capacity trade in open markets.

- **Listing**: knowledge syntheses (42) and compute capacity (27) list
  with price discovery, terms and provenance (13) attached.
- **Trade execution**: trades settle through the transaction ledger (57)
  with the exchange ledger (22) recording provider/consumer/confidence.
- **Market guardrails**: policy caps participation (volumes, counterparty
  risk grades from 53, red lines from 54); markets never outrank local
  priorities.
- **Telemetry**: `market.listed` / `market.traded` / `market.halted`
  events.
- **Dashboard**: a "Markets" view shows listings, recent trades and
  guardrail status.
- **Exit criterion**: one knowledge item and one compute slice are
  listed, traded and settled with provenance intact and guardrails
  enforced.

## Phase 59 — Self-Funding & Reserves

Goal: the system funds its own operation from legitimate earnings.

- **Earnings policy**: policy defines what may be earned, held and
  reinvested; earnings are attributed to the producing capability (22).
- **Reserve management**: a reserve ledger with policy-bounded allocation
  (reinvestment, sustainability 27, crisis 44) and human-ratified
  strategy reviews.
- **Autonomy boundary**: self-funding never lifts budget ceilings (8) or
  approval gates (9) — earning more does not mean spending freely.
- **Telemetry**: `funds.earned` / `funds.reserved` / `funds.invested`
  events.
- **Dashboard**: "Finances" gains reserve position and earnings
  attribution.
- **Exit criterion**: one quarter of operating costs is covered from
  legitimate earnings while budget ceilings and approval gates remain
  unchanged and unrelaxed.

## Phase 60 — Economic Accountability (Epoch-2 arc capstone)

Goal: every economic action is auditable by humans and by society.

- **Public accounting**: an economic attestation (14) summarizes the
  quarter's transactions, markets and reserves — publishable to the
  commons (42) for external audit.
- **Audit replay**: `rsis audit --economic` replays any transaction to
  its originating contract (56), budget line (8) and approval record (9).
- **Fraud-resistant invariants**: invariant checks (14) continuously
  verify ledger consistency, no-anonymous-spend, and threshold
  enforcement.
- **Telemetry**: `economic.reported` / `economic.audited` events.
- **Dashboard**: "Finances" gains a quarterly economic attestation card.
- **Exit criterion**: an external auditor replays a quarter of economic
  activity from the attestation and ledger with zero unexplained entries.

## Sequencing notes (Sequel XII)

- Contracts (56) precede transactions (57): you cannot transact without
  executable, ratifiable agreements.
- Markets (58) need both transaction rails (57) and the exchange ledger
  (22) with provenance intact.
- Self-funding (59) is bounded by policy from the start — earnings may
  fund operation but never lift Phase 8 ceilings or Phase 9 gates.
- Accountability (60) is the capstone: an economy without audit replay is
  a policy violation waiting to happen; it extends Phases 8, 9 and 14.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 56 — Machine contracts | governance | ⏳ queued |
| Phase 57 — Transactions & payments | ops | ⏳ queued |
| Phase 58 — Markets for knowledge & compute | economy | ⏳ queued |
| Phase 59 — Self-funding & reserves | economy | ⏳ queued |
| Phase 60 — Economic accountability | governance | ⏳ queued |
