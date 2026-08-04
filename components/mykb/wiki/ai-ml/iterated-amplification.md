---
type: "concept"
title: "Iterated Amplification"
description: "Building superhuman judgments from human-level ones through recursive question decomposition"
tags: ["alignment", "oversight", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Iterated Amplification

## Summary
Iterated amplification is a scalable oversight proposal that builds superhuman judgments from human-level ones by recursively decomposing hard questions into easier subtasks. It matters because evaluating models on tasks harder than humans is an open alignment problem, and amplification offers a path from human judgment to capable oversight. Its core assumption is that decomposition errors do not compound catastrophically. Amplification is a bet that decomposition can preserve oversight quality.

## Details
- **Definition** — amplification answers a hard question by breaking it into subtasks that are answered and then combined, recursively applying human oversight at each level.
- **Mechanism** — a human judges subtask answers, a model or system aggregates them, and the aggregate guides the next level of decomposition.
- **Key assumption** — the method works only if errors at each decomposition level stay small and do not multiply into large final errors.
- **Variants** — recursive-reward-modeling applies the idea to reward signals, and debate-protocols use competition instead of cooperation.
- **Relation to oversight** — amplification is one of the main scalable-oversight proposals under oversight-mechanisms.
- **Worked example** — answering a complex policy question, the system splits it into research, analysis, and drafting subtasks, each verified by humans before combination.
- **Failure modes** — decomposition that loses context, systematic human errors, and aggregation mistakes undermine the approach.
- **Practical relevance** — the idea directly motivates practical techniques like self-reflection-agents and hierarchical verification in agent systems.
- **Decomposition design** — subtasks must be genuinely easier than the whole question.
- **Aggregation** — combination methods must avoid compounding small errors.
- **Worked example** — a hard evaluation question is split into fact-checking and synthesis subtasks, each overseen separately.
- **Failure example** — a decomposition that hides the hardest judgment in one opaque subtask does not actually amplify oversight.

## Related
- [[wiki/ai-ml/recursive-reward-modeling|Recursive Reward Modeling]] — the reward-based variant
- [[wiki/ai-ml/debate-protocols|Debate Protocols]] — the competitive variant
- [[wiki/ai-ml/oversight-mechanisms|Oversight Mechanisms]] — the umbrella concept
- [[wiki/ai-ml/alignment-and-values|Alignment and Values]] — the research family
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — a practical echo
