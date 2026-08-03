---
type: "index"
hub: true
title: "Syntheses Index"
description: "Listing of the syntheses/ folder (44 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Syntheses

Part of [[wiki/index|Wiki Index]]. 44 pages.

## Pages
- [[wiki/syntheses/acquisition-pass-snapshot-ordering|Acquisition Passes & Snapshot Ordering]] — Durable rules for multi-worker acquisition rounds: stage untracked notes before regenerating files.json (it counts tracked files only), generators are idempotent and safe to re-run, and threshold buckets move predictably because fulls are capped at 400 words
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
- [[wiki/syntheses/responsible-disclosure-ai|Responsible Disclosure for AI]] — Norms for disclosing AI vulnerabilities safely
- [[wiki/syntheses/restricted-deployment|Restricted Deployment]] — Limiting where or how an AI system can be used
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
