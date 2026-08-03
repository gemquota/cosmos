---
type: "concept"
title: "Production Rules"
description: "Condition-action rules that fire when their conditions match state"
tags: ["production-rules", "rules", "expert-systems", "inference"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Production Rules

## Summary
Production rules are IF condition THEN action rules evaluated against working memory; when a condition matches, the action fires, possibly changing state and enabling other rules. They matter because they model reactive, modular behavior and are the substrate of classic expert systems. They are also how agents can encode policies.

## Details
- The structure is simple and powerful: each rule is an independent unit — "IF the temperature exceeds 90 AND the device is idle THEN shut it down" — and the system's behavior emerges from the interactions of many such units firing as their conditions become true. Working memory holds the current facts; the recognize-act cycle repeatedly matches rule conditions against working memory, selects a rule, fires its action, and updates working memory, which may enable or disable other rules. This is exactly the architecture of the classic production systems (OPSS, SOAR) and modern rule engines.
- Rule engines (e.g., RETE) match many rules efficiently. The RETE algorithm compiles the rule conditions into a shared discrimination network, so when one fact changes, only the affected partial matches are updated rather than re-testing every rule against every fact. This is what makes production systems with thousands of rules practical: the matching cost is incremental, not recomputed. The RETE design is why rule engines remain the standard for business-rule systems (Drools, CLIPS) that must evaluate large rule sets on every state change.
- Conflict resolution decides which matching rule fires first. When several rules match, the engine must choose: by specificity (more conditions wins), by recency (rules matching the newest facts win), by priority, or by a domain-specific strategy. The choice is not cosmetic — different conflict-resolution strategies produce different behaviors from the same rule base, so the strategy is part of the system's semantics. Getting it wrong produces the classic production-system failure: the right rules firing in the wrong order.
- Strengths: modular, explainable — each rule is inspectable and its firing is traceable, which is why production systems remain the gold standard for auditable policy. Weakness: interaction surprises — the behavior of many independent rules is emergent, and subtle interactions (two rules that both fire, a rule that undoes another's effect) are hard to predict from reading the individual rules.
- RSIS3 relevance: constraint and policy rules bound tool use — the practices and invariants are naturally production rules, and the checker is the recognize-act cycle over them.

## Related
- [[wiki/agent-systems/action-observation-loop|Action-Observation Loop]] — the loop rule firing drives
- [[wiki/concepts/forward-chaining|Forward Chaining]] — the inference strategy
- [[wiki/concepts/expert-systems|Expert Systems]] — the classic host
- [[wiki/concepts/procedural-memory|Procedural Memory]] — rules as compiled skill
- [[wiki/agent-systems/behavior-trees|Behavior Trees]] — a structured alternative
