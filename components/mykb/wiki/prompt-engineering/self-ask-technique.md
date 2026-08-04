---
type: "concept"
title: "Self-Ask Technique"
description: "Prompting method where the model asks and answers follow-up questions before the final answer"
tags: ["self-ask", "prompting", "reasoning", "questions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Self-Ask Technique

## Summary

The self-ask technique prompts the model to ask itself follow-up questions and answer them before producing a final answer, decomposing complex queries into sub-questions. Each answer provides context for the next, building a reasoning chain that mirrors how a careful analyst works. The technique matters because it improves accuracy on multi-hop questions that require assembling information across steps. Self-ask is most valuable when answers to sub-questions genuinely gate the final answer rather than merely restating it.

## Details

- **Definition** — self-ask instructs the model to generate and answer intermediate questions until the original question is resolvable.
- **Decomposition** — complex questions are split into smaller, independently answerable pieces, reducing the load on a single inference.
- **Explicit reasoning** — the generated questions and answers form a visible trace, aiding debugging and trust.
- **Retrieval integration** — each sub-question can drive its own retrieval, supporting multi-hop knowledge access.
- **Relation to chain-of-thought** — self-ask is a structured variant that turns private reasoning into explicit question-answer steps.
- **Relation to least-to-most** — both decompose tasks, but self-ask focuses on question decomposition for answering.
- **Worked example** — for "Which country's capital has a metro named after a composer?", the model first asks which composer, then which country's capital, then answers.
- **Failure modes** — invented sub-answers, unnecessary decomposition, and compounding errors across steps reduce gains.
- **Practical relevance** — self-ask is a building block for agent planning and retrieval-augmented question answering.
- **Evaluation** — performance is measured on multi-hop benchmarks where single-pass answers often fail.
- **Verification pass** — checking that each intermediate answer is consistent with the final answer catches compounding errors early.


## Related

- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the reasoning baseline
- [[wiki/prompt-engineering/least-to-most-prompting|Least-to-Most Prompting]] — the decomposition family
- [[wiki/ai-ml/query-decomposition|Query Decomposition]] — the general technique
- [[wiki/agent-systems/agent-planning-systems|Agent Planning Systems]] — planning in agents
- [[wiki/prompt-engineering/step-back-prompting|Step-Back Prompting]] — abstraction-based reasoning
- [[wiki/questions/clarifying-questions|Clarifying Questions]] — the human analog

