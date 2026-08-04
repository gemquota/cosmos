---
type: "concept"
title: "Agent Consensus"
description: "Mechanisms for multiple agents to agree on decisions or outputs"
tags: ["consensus", "agents", "multi-agent", "agreement"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Agent Consensus

## Summary
Agent consensus covers the mechanisms by which multiple agents agree on a decision or output, from simple voting to structured debate. It matters because single-agent judgments are noisy, and aggregating diverse opinions improves reliability on high-stakes outputs. The cost, however, grows with the number of participants. Consensus is most valuable when errors are independent and the cost of failure is high.

## Details
- **Definition** — consensus is any procedure that combines individual agent outputs into a single agreed result, usually to reduce error and increase confidence.
- **Mechanisms** — common approaches include majority voting, weighted voting, quorum rules, sequential debate, and confidence-weighted aggregation.
- **Diversity first** — consensus only helps when the participants are independently useful; identical agents just multiply the same mistake.
- **Cost model** — each participant adds latency, tokens, and orchestration complexity, so consensus should be reserved for decisions where errors are expensive.
- **Worked example** — a code-review panel of three critics votes on whether a patch is safe; a quorum of two rejections blocks the merge.
- **Failure modes** — correlated errors, sycophantic agreement, and systematic bias in the shared base model can make consensus look confident while being wrong.
- **Variants** — market-based coordination prices disagreement instead of voting on it, and hierarchical supervision replaces consensus with authority.
- **Evaluation** — consensus quality is measured against ground truth on held-out decisions, including how often the group beats its best member.
- **Practical relevance** — consensus powers voting-agents and critic panels in production, and it is a core building block of multi-agent reliability.
- **Limits** — consensus cannot fix absent information; if every agent shares the same blind spot, agreement is not evidence.
- **Quorum rules** — fixed quorums, supermajorities, and unanimous requirements make consensus tunable to the stakes of the decision.
- **Worked example** — a moderation panel requires two of three agents to agree before approving borderline content.
- **Limits** — consensus adds latency and compute, so it should be bypassed for trivial decisions where the error cost is low.

## Related
- [[wiki/agent-systems/voting-agents|Voting Agents]] — the voting mechanism in practice
- [[wiki/agent-systems/critic-agents|Critic Agents]] — the critical inputs a panel aggregates
- [[wiki/agent-systems/agent-ensembling|Agent Ensembling]] — the diversity source behind useful consensus
- [[wiki/agent-systems/supervisor-pattern-swarm|Supervisor Pattern and Swarm]] — hierarchy as an alternative to consensus
