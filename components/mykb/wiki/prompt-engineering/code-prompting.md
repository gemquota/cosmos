---
type: "concept"
title: "Code Prompting"
description: "Prompting techniques specialized for code generation, repair, and explanation"
tags: ["code-prompting", "code", "prompting", "generation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Code Prompting

## Summary

Code prompting is the set of prompting techniques specialized for code generation, repair, explanation, and conversion. It leverages the fact that code is structured, executable, and testable, so prompt quality can be measured by compilation and test outcomes. Code prompting matters because it is the interface through which developers and agents get working programs from language models. The best code prompts encode the contract of the function — inputs, outputs, errors — so success can be verified automatically.

## Details

- **Definition** — code prompting frames requests so the model produces correct, idiomatic, and runnable code in the target language.
- **Specification quality** — precise function signatures, input-output examples, and edge-case descriptions reduce wrong implementations.
- **Structured output** — requiring code blocks, tests, or explanation alongside code makes results parseable and verifiable.
- **Test-driven prompting** — asking the model to write tests with the implementation, or providing tests in the prompt, improves correctness.
- **Repair workflows** — feeding error messages and failing tests back into the prompt turns code prompting into a repair loop.
- **Worked example** — a developer prompts "write a Python function parse_date(s) -> datetime handling ISO and 'YYYY-MM-DD', raising ValueError otherwise" and verifies with unit tests.
- **Failure modes** — ambiguous specs, missing imports, silent assumptions, and plausible-but-wrong logic are the main failure classes.
- **Practical relevance** — code prompting underpins pair programmers, code agents, and automation of boilerplate and migration work.
- **Relation to reasoning techniques** — program-of-thoughts and structured reasoning extend code prompting beyond generation to problem solving.
- **Evaluation** — code prompts are scored by compilation success, test pass rates, and human review of style and efficiency.
- **Verification loop** — pairing generation with automated tests converts prompt quality into a measurable, improvable quantity.


## Related

- [[wiki/prompt-engineering/program-of-thoughts|Program of Thoughts]] — code as reasoning
- [[wiki/agent-systems/code-generation-agents-revisited|Code Generation Agents]] — the agent context
- [[wiki/ai-ml/code-benchmarks|Code Benchmarks]] — the evaluation standard
- [[wiki/prompt-engineering/tool-schema-design|Tool Schema Design]] — structured interfaces
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — parseable results
- [[wiki/prompt-engineering/grammar-constrained-generation|Grammar-Constrained Generation]] — valid syntax

