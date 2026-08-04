---
type: "concept"
title: "Senior Dev"
description: "Senior dev: experience-based judgment in architecture, review, mentoring, and ownership"
tags: ["entity", "ast", "cli", "ide", "queue", "terminal", "seniority"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Senior Dev

## Summary

Senior Dev captures the experience-based practices of a senior developer: architectural judgment, code review, mentoring, and ownership of outcomes. Seniority is less about knowing more syntax and more about making sound tradeoffs under uncertainty. It matters because these practices multiply the effectiveness of everyone around them. Senior practice is largely about where attention goes: risks, interfaces, and the team around the code.

## Details

- **Definition** — A senior developer applies accumulated judgment to design, review, and delivery decisions, including the judgment to know what not to build.
- **Architecture** — Seniors balance short-term delivery with long-term maintainability, choosing the simplest design that survives likely change.
- **Code review** — Review at senior level focuses on contracts, failure modes, and clarity, not just style; it protects the codebase's long-term health.
- **Mentoring** — Explaining reasoning, not just answers, grows the team's capability and reduces single points of failure.
- **Ownership** — Seniors own outcomes end to end, including deployment, monitoring, and clean-up, rather than stopping at the merge.
- **Judgment vs rules** — Guidelines are defaults, not laws; senior judgment decides when to deviate and records why.
- **Failure modes** — Bus-factor concentration, over-engineering, and review bottleneck are the risks of seniority without process.
- **Practical relevance** — Agent tooling increasingly encodes senior practices, so capturing them in the wiki makes them executable guidance.
- **Risk focus** — Seniors spend effort where failure is expensive, not where it is merely possible.
- **Interface thinking** — Stable, well-named interfaces outlive implementations; design effort concentrates there.
- **Teaching** — Explaining decisions in review comments and docs spreads judgment instead of hoarding it.
- **Long-term lens** — Senior decisions weigh the cost of tomorrow's maintenance, not just the speed of today's merge.

## Related

- [[wiki/development/categories/cli-tools/dev|Dev]] — the workflow seniors steer
- [[wiki/development/categories/cli-tools/cognitive|Cognitive]] — judgment under load
- [[wiki/development/categories/cli-tools/reality|Reality]] — evidence-based decision making
- [[wiki/development/categories/cli-tools/sovereign-orchestrator|Sovereign Orchestrator]] — autonomous ownership patterns
