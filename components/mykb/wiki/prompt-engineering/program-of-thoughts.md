---
type: "concept"
title: "Program of Thoughts"
description: "Reasoning technique that expresses reasoning steps as executable program code"
tags: ["program-of-thoughts", "prompting", "code", "reasoning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Program of Thoughts

## Summary

Program of thoughts is a reasoning technique in which the model expresses its reasoning steps as executable program code, then runs the code to obtain the answer. By moving arithmetic and logic out of the model's head and into a runtime, it reduces computation errors in multi-step problems. The technique matters because it combines the structure of chain-of-thought with the exactness of execution. The technique shifts trust from the model's arithmetic to the interpreter's, but the model still writes the program, so verification remains necessary.

## Details

- **Definition** — the model writes a program that computes the answer, and the program's output grounds the final response.
- **Error reduction** — arithmetic, list manipulation, and bookkeeping are delegated to an interpreter, eliminating a major error class.
- **Executable trace** — the code provides a verifiable reasoning trace that can be inspected and debugged.
- **Runtime requirement** — safe code execution is required; sandboxing and resource limits protect the host.
- **Relation to chain-of-thought** — verbal reasoning remains useful for planning the program, while execution replaces fallible mental math.
- **Bridges to tool use** — program execution behaves like a tool call, connecting reasoning techniques to agent tooling.
- **Worked example** — for a compound probability problem, the model writes a short script computing the product and sum of probabilities, then reports the printed result.
- **Failure modes** — syntactically broken programs, unsafe execution, and logic errors in the code itself still require verification.
- **Practical relevance** — the technique improves accuracy on calculation-heavy tasks and is a building block of code-driven agents.
- **Evaluation** — correctness is measured against ground truth, with code validity and execution success as intermediate checks.
- **Hybrid strategy** — using verbal reasoning to plan and code to compute combines the strengths of both while limiting each one's failure modes.


## Related

- [[wiki/prompt-engineering/code-prompting|Code Prompting]] — the code-generation craft
- [[wiki/agent-systems/code-execution-environments|Code Execution Environments]] — the runtime requirement
- [[wiki/llm-agents/chain-of-thought|Chain of Thought]] — the verbal baseline
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — capturing results
- [[wiki/agent-systems/verifier-agents|Verifier Agents]] — checking outputs
- [[wiki/prompt-engineering/self-ask-technique|Self-Ask Technique]] — question-driven reasoning

