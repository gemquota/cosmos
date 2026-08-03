---
type: "concept"
title: "Forward Chaining"
description: "Reasoning from known facts toward a goal by applying rules"
tags: ["forward-chaining", "reasoning", "inference", "rules"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Forward Chaining

## Summary
Forward chaining starts with known facts and repeatedly applies rules whose conditions are satisfied, deriving new facts until the goal is reached or no rule applies. It matters because it is complete, data-driven, and easy to implement — the engine of many expert systems. It is also how agents can reason from observations.

## Details
- Data-driven: all rules fire as their conditions become true. The inference engine maintains a working memory of facts; each cycle it matches rule conditions against the facts, picks a rule whose conditions are satisfied, fires it, and adds the derived fact to working memory. The process continues until the goal is derived, no rules fire, or a conflict-resolution strategy chooses among simultaneously applicable rules (by specificity, recency, or priority). Because it starts from what is known and derives everything derivable, it is complete — every consequence of the facts and rules is eventually found.
- Used in production-rule systems and RETE-based engines. The RETE algorithm precompiles the rule conditions into a discrimination network so that pattern matching is incremental: when one fact changes, only the affected partial matches are updated instead of re-matching every rule against every fact. This made forward chaining practical for large production systems (the XCON configurer fired tens of thousands of rules) and remains the standard architecture for business-rule engines.
- Contrast with backward chaining, which is goal-driven. Backward chaining starts from the goal and works back to facts, asking "what conditions would prove this?"; forward chaining starts from facts and works toward the goal. Forward chaining is better when there are few facts and many possible goals (you want to see everything that follows); backward chaining is better when the goal is known and the fact space is large. The same rule base supports both modes.
- Failure modes: combinatorial explosion — deriving huge numbers of irrelevant facts when rules are too generative; loops from cyclic rules that keep re-deriving facts; and conflict-resolution choices that chase the wrong path. All are tamed by rule discipline: restrict rule firing, bound the working memory, and design rules to terminate.
- RSIS3 relevance: a retrieval pipeline that starts from a query's known facts and fans out through the wiki graph until evidence saturates is forward chaining over the knowledge base — and its explosion risk is exactly why retrieval needs pruning.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — observations feed forward reasoning
- [[wiki/concepts/production-rules|Production Rules]] — the rule formalism
- [[wiki/concepts/backward-chaining|Backward Chaining]] — the goal-driven counterpart
- [[wiki/concepts/expert-systems|Expert Systems]] — the classic consumer
- [[wiki/concepts/constraint-satisfaction|Constraint Satisfaction]] — propagation as forward inference
