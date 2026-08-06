---
type: "index"
hub: true
title: "Syntheses Index"
description: "Listing of the syntheses/ folder (54 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Syntheses

Part of [[wiki/index|Wiki Index]]. 54 pages.

## Pages
- [[wiki/syntheses/acquisition-pass-snapshot-ordering|Acquisition Passes & Snapshot Ordering]] — Durable rules for multi-worker acquisition rounds: stage untracked notes before regenerating files.json (it counts tracked files only), generators are idempotent and safe to re-run, and threshold buckets move predictably because fulls are capped at 400 words
- [[wiki/syntheses/ao-agent-os-integration-assessment|AO (Agent OS) Integration Assessment — Selective Harvest Rules]] — Durable rules from assessing the Agent OS codebase for COSMOS: harvest infrastructure (sandbox, HITL approvals, scheduler guards, cost ledger) into RSIS3, never duplicate memory/dashboard/telemetry surfaces; Phase A sync tool-layer port patterns (allowlist + containment + audit triad, stub-planner argument discipline, config gates) and Phase B cost-ledger + semantic-search patterns (persistent ledger replay, two-stage budget enforcement, hashed n-gram embeddings, test hygiene); Phase C scheduler patterns (budget-bounded fan-out, immutable-evaluator fan-in, re-dispatch-after-settle deadlock guard, scheduler-guarded review waves, DAG-shape telemetry, CLI-over-config / env-over-config)
- [[wiki/syntheses/assurance-cases|Assurance Cases]] — Structured arguments that a system meets safety goals
- [[wiki/syntheses/audit-frameworks-ai|AI Audit Frameworks]] — Structured methods for auditing AI systems
- [[wiki/syntheses/bug-bounty-ai|Bug Bounties for AI]] — Rewarding external researchers for finding AI vulnerabilities
- [[wiki/syntheses/containment-strategies|Containment Strategies]] — Isolating AI systems to bound their impact
- [[wiki/syntheses/coordinated-disclosure|Coordinated Disclosure]] — Structured multi-party vulnerability disclosure
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]] — Durable engineering patterns for the static-hosted dashboard↔wiki integration: lazy iframes, bounded client-side search, repo-relative snapshots, read-only validation, verification-first changes
- [[wiki/syntheses/dead-link-repair|Dead-Link Repair]] — Finding and fixing links that point nowhere
- [[wiki/syntheses/deployment-safety|Deployment Safety]] — Practices for shipping AI systems without harm
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — Open threads on claims, sources, and version history so syntheses stay auditable
- [[wiki/syntheses/external-red-teams|External Red Teams]] — Independent adversarial testers for AI systems
- [[wiki/syntheses/fallback-plans|Fallback Plans]] — Prepared responses when systems fail
- [[wiki/syntheses/feedback-integration-loops|Feedback Integration Loops]] — Mechanisms that convert feedback into durable system changes
- [[wiki/syntheses/gradual-deployment|Gradual Deployment]] — Rolling out AI systems in stages
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]] — Automated checks that verify a knowledge graph's structural integrity
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow: Open Threads]] — Open threads on how captures become curated concepts, sources, and syntheses
- [[wiki/syntheses/knowledge-graph-maintenance|Knowledge Graph Maintenance]] — Keeping a knowledge graph consistent, connected, and current
- [[wiki/syntheses/knowledge-synthesis-pipelines|Knowledge Synthesis Pipelines]] — Automated pipelines that turn raw captures into linked knowledge
- [[wiki/syntheses/knowledge-synthesis|Knowledge Synthesis]] — Integrating multiple sources or concepts into a coherent new conclusion, framework, or insight
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]]
- [[wiki/syntheses/lessons-to-actions|Lessons to Actions]] — Converting lessons learned into concrete implemented changes
- [[wiki/syntheses/loop-closure|Loop Closure]] — Ensuring improvement loops terminate with durable change
- [[wiki/syntheses/model-updates-risks|Model Update Risks]] — Risks introduced when models are updated
- [[wiki/syntheses/monitored-deployment|Monitored Deployment]] — Running systems under active observation
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement]] — Durable rules for acquiring concept notes into MyKB, curating hash-named junk entity pages, and enforcing RSIS3 workspace hygiene with check-practices
- [[wiki/syntheses/nested-loop-graph-and-zoom-fix|Nested-Loop Graph & Zoom Direction Fix]] — Durable patterns for the interactive Ω graphs: viewBox-width zoom inversion (f>1 zooms in), re-projecting only the loop family onto concentric rings at the semantic centroid, and keeping generator scripts + index cards in sync
- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]] — Durable patterns for completing the L1–L9 loop stack (meta-tuners observe target-loop history, not params), outcome-window signal driving in tests, and static snapshot wiring for the dashboard Loops tab
- [[wiki/syntheses/orphan-detection|Orphan Detection]] — Finding nodes with no inbound links in a knowledge graph
- [[wiki/syntheses/parallel-agent-acquisition|Parallel Agent Acquisition (5×100) & Writer Reliability]] — Durable rules for running multi-agent knowledge-acquisition passes: a gated define→confirm→generate flow with programmatic uniqueness checks, write-immediately batching to survive silent writer stalls, and independent post-verification instead of trusting agent self-reports
- [[wiki/syntheses/pass3-integration-depth-wave|Pass 3 — Integration & Depth Wave (8×400)]] — Eight parallel workers deepened and grew mykb by 3,200 files across AI, systems, data, cognition, dev culture, RSI/RSIS3 integration, curation, and frontend clusters — with the goal of making mykb fully integrated into RSIS3's decision-making
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — Processes for fixing vulnerabilities across AI systems
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — Settling a work pass into durable structure before the next one
- [[wiki/syntheses/recursive-self-improvement-spec-2026-08-06|Recursive Self-Improvement Specification — SPACE v2 Export]] — The completed 326-probe SPACE session (67/67 questions, 67 artifacts) that fixes what recursive self-improvement is and how RSIS3 should be built
- [[wiki/syntheses/responsible-disclosure-ai|Responsible Disclosure for AI]] — Norms for disclosing AI vulnerabilities safely
- [[wiki/syntheses/restricted-deployment|Restricted Deployment]] — Limiting where or how an AI system can be used
- [[wiki/syntheses/rsis3-l3-cycle-1-cross-session-memory-consolidation-2026-08-06|RSIS3 L3 cycle 1 — cross-session memory consolidation]] — L3 cycle 1 consolidated workspace telemetry into durable MyKB memory (self-written via the gateway)
- [[wiki/syntheses/rsis3-l3-cycle-2-cross-session-memory-consolidation-2026-08-06|RSIS3 L3 cycle 2 — cross-session memory consolidation]] — L3 cycle 2 consolidated workspace telemetry into durable MyKB memory (self-written via the gateway)
- [[wiki/syntheses/rsis3-l3-cycle-3-cross-session-memory-consolidation-2026-08-06|RSIS3 L3 cycle 3 — cross-session memory consolidation]] — L3 cycle 3 consolidated workspace telemetry into durable MyKB memory (self-written via the gateway)
- [[wiki/syntheses/rsis3-l3-cycle-4-cross-session-memory-consolidation-2026-08-06|RSIS3 L3 cycle 4 — cross-session memory consolidation]] — L3 cycle 4 consolidated workspace telemetry into durable MyKB memory (self-written via the gateway)
- [[wiki/syntheses/rsis3-l3-cycle-5-cross-session-memory-consolidation-2026-08-06|RSIS3 L3 cycle 5 — cross-session memory consolidation]] — L3 cycle 5 consolidated workspace telemetry into durable MyKB memory (self-written via the gateway)
- [[wiki/syntheses/rsis3-pass-6-2026-08-06|RSIS3 Pass 6 — five full cycles across L1–L9]] — Running 5 full cycles (40 loop executions) under a 99.6%-full disk: RSIS_DISK_USAGE_PCT override for the resource enforcer, module-logger discipline in scheduler callbacks, checkpoint git-add sweep behavior, and the even-telemetry full-cycle cadence
- [[wiki/syntheses/rsis3-pass-7-2026-08-06|RSIS3 Pass 7 — ecosystem data contracts, validated at both gates]] — One documented contract per shared shape (OKF, files.json, ecosystem.json, loops.json, telemetry JSONL, SPACE framework) enforced by a stdlib-only validator wired into gen-static-data --check and check-practices; disk-override semantics (RSIS_DISK_USAGE_PCT=100 on full disks) and the freshness-vs-shape split in the deploy gate
- [[wiki/syntheses/rsis3-pass-8-2026-08-06|RSIS3 Pass 8 — MyKB memory link: loops read and write the wiki]] — Durable rules from pass 8: L3 consolidation is self-writing through the MyKB gateway, loops read syntheses for context, cycle ordinals from durable counts
- [[wiki/syntheses/safety-case-approach|Safety Case Approach]] — Structuring safety justification as explicit cases
- [[wiki/syntheses/security-advisories-ai|Security Advisories]] — Official notices about AI security vulnerabilities
- [[wiki/syntheses/third-party-audits|Third-Party Audits]] — Independent external reviews of AI systems
- [[wiki/syntheses/transparency-reports|Transparency Reports]] — Regular public reports on AI system behavior and incidents
- [[wiki/syntheses/tripwires|Tripwires]] — Triggers that halt a system when thresholds are crossed
- [[wiki/syntheses/update-regression|Update Regression]] — New versions performing worse on old capabilities
- [[wiki/syntheses/vulnerability-reports-ai|Vulnerability Reports]] — Formal channels for reporting AI security flaws
- [[wiki/syntheses/weekly-review|Weekly Review]]
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]] — A knowledge base that improves its own structure and coverage
- [[wiki/syntheses/wiki-stats-hub|Wiki Stats Hub Architecture & Snapshot Hygiene]] — Durable patterns for the MyKB stats hub: one generator emitting embedded JSON plus a self-contained Chart.js page, graceful degradation when the CDN is unavailable, and the snapshot-regeneration pipeline (graph → files.json → --check) that must run after every wiki change

## Concepts

- [Acquisition Passes & Snapshot Ordering](acquisition-pass-snapshot-ordering.md) — Acquisition Passes & Snapshot Ordering
- [Adversarial Review Pass 1 — Stub Promotion Wave Cleanup (2026-08)](adversarial-review-pass-1-2026-08.md) — Adversarial Review Pass 1 — Stub Promotion Wave Cleanup (2026-08)
- [Adversarial Review Pass 3 — Claims Grounding, Link Hygiene & Near-Duplicate Merges (2026-08)](adversarial-review-pass-3-2026-08.md) — Adversarial Review Pass 3 — Claims Grounding, Link Hygiene & Near-Duplicate Merges (2026-08)
- [AO (Agent OS) Integration Assessment — Selective Harvest Rules](ao-agent-os-integration-assessment.md) — AO (Agent OS) Integration Assessment — Selective Harvest Rules
- [Assurance Cases](assurance-cases.md) — Assurance Cases
- [AI Audit Frameworks](audit-frameworks-ai.md) — AI Audit Frameworks
- [Bug Bounties for AI](bug-bounty-ai.md) — Bug Bounties for AI
- [Containment Strategies](containment-strategies.md) — Containment Strategies
- [Coordinated Disclosure](coordinated-disclosure.md) — Coordinated Disclosure
- [Cosmos Dashboard & MyKB Integration Patterns](cosmos-dashboard-mykb-integration.md) — Cosmos Dashboard & MyKB Integration Patterns
- [Dead-Link Repair](dead-link-repair.md) — Dead-Link Repair
- [Deployment Safety](deployment-safety.md) — Deployment Safety
- [Evidence and Provenance: Open Threads](evidence-and-provenance.md) — Evidence and Provenance: Open Threads
- [External Red Teams](external-red-teams.md) — External Red Teams
- [Fallback Plans](fallback-plans.md) — Fallback Plans
- [Feedback Integration Loops](feedback-integration-loops.md) — Feedback Integration Loops
- [Gradual Deployment](gradual-deployment.md) — Gradual Deployment
- [Graph Health Checks](graph-health-checks.md) — Graph Health Checks
- [Knowledge Acquisition Workflow: Open Threads](knowledge-acquisition-workflow.md) — Knowledge Acquisition Workflow: Open Threads
- [Knowledge Graph Maintenance](knowledge-graph-maintenance.md) — Knowledge Graph Maintenance
- [Knowledge Synthesis Pipelines](knowledge-synthesis-pipelines.md) — Knowledge Synthesis Pipelines
- [Knowledge Synthesis](knowledge-synthesis.md) — Knowledge Synthesis
- [Knowledge System Overview](knowledge-system.md) — Knowledge System Overview
- [Lessons to Actions](lessons-to-actions.md) — Lessons to Actions
- [Loop Closure](loop-closure.md) — Loop Closure
- [Loop & Graph Engineering Wave — 14-Source Ingest](loop-graph-engineering-wave-2026-08.md) — Loop & Graph Engineering Wave — 14-Source Ingest
- [Model Update Risks](model-updates-risks.md) — Model Update Risks
- [Monitored Deployment](monitored-deployment.md) — Monitored Deployment
- [MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement](mykb-acquisition-curation-and-practices.md) — MyKB Acquisition/Curation Pass & RSIS3 Usage-Practice Enforcement
- [Nested-Loop Graph & Zoom Direction Fix](nested-loop-graph-and-zoom-fix.md) — Nested-Loop Graph & Zoom Direction Fix
- [Nine-Loop Stack Implementation & Dashboard Wiring](nine-loop-stack-implementation.md) — Nine-Loop Stack Implementation & Dashboard Wiring
- [Orphan Detection](orphan-detection.md) — Orphan Detection
- [Parallel Agent Acquisition (5×100) & Writer Reliability](parallel-agent-acquisition.md) — Parallel Agent Acquisition (5×100) & Writer Reliability
- [Pass 3 — Integration & Depth Wave (8×400)](pass3-integration-depth-wave.md) — Pass 3 — Integration & Depth Wave (8×400)
- [Patch Management for AI](patch-management-ai.md) — Patch Management for AI
- [Post-Pass Consolidation](post-pass-consolidation.md) — Post-Pass Consolidation
- [Recursive Self-Improvement Specification — SPACE v2 Export](recursive-self-improvement-spec-2026-08-06.md) — Recursive Self-Improvement Specification — SPACE v2 Export
- [Responsible Disclosure for AI](responsible-disclosure-ai.md) — Responsible Disclosure for AI
- [Restricted Deployment](restricted-deployment.md) — Restricted Deployment
- [Safety Case Approach](safety-case-approach.md) — Safety Case Approach
- [Security Advisories](security-advisories-ai.md) — Security Advisories
- [500-Stub Expansion Pass (2026-08-03)](stub-expansion-pass-500-2026-08.md) — 500-Stub Expansion Pass (2026-08-03)
- [Stub Promotion Wave — 1,098 stubs → growing (2026-08)](stub-promotion-wave-2026-08.md) — Stub Promotion Wave — 1,098 stubs → growing (2026-08)
- [Third-Party Audits](third-party-audits.md) — Third-Party Audits
- [Transparency Reports](transparency-reports.md) — Transparency Reports
- [Tripwires](tripwires.md) — Tripwires
- [Update Regression](update-regression.md) — Update Regression
- [Vulnerability Reports](vulnerability-reports-ai.md) — Vulnerability Reports
- [Weekly Review](weekly-review.md) — Weekly Review
- [Wiki Self-Improvement](wiki-self-improvement.md) — Wiki Self-Improvement
- [Wiki Stats Hub Architecture & Snapshot Hygiene](wiki-stats-hub.md) — Wiki Stats Hub Architecture & Snapshot Hygiene
