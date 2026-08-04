---
type: "concept"
title: "Grammar-Constrained Generation"
description: "Decoding restricted to tokens valid under a formal grammar"
tags: ["grammar-constrained", "grammar", "decoding", "structured"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Grammar-Constrained Generation

## Summary

Grammar-constrained generation restricts decoding so that every token sequence is valid under a formal grammar, such as JSON, SQL, or LaTeX. It turns structure from a hope into a guarantee at token-selection time. The technique matters because it eliminates whole classes of parsing failures and enables reliable machine-readable output from language models. Grammar constraints guarantee syntax, leaving semantics as the remaining evaluation problem.

## Details

- **Definition** — a grammar defines the set of valid token sequences; constrained decoding masks out tokens that cannot continue a valid parse.
- **Mechanism** — at each decoding step, a parser tracks the grammar state and blocks tokens that would produce invalid output.
- **Hard guarantee** — unlike prompting, constraints cannot be violated by the model, providing deterministic structural compliance.
- **Grammar types** — context-free grammars cover many formats; specialized decoders exist for JSON schemas, regex, and programming languages.
- **Tradeoffs** — constraints add decoding overhead and can slightly reduce output quality by restricting the model's token choices.
- **Use cases** — JSON schema decoding, SQL generation, LaTeX output, and tool-call arguments are common applications.
- **Worked example** — a code-generation pipeline uses a SQL grammar so the model cannot emit syntactically invalid queries, leaving only semantic validation.
- **Failure modes** — incomplete grammars reject valid outputs, while overly permissive grammars fail to catch real errors.
- **Practical relevance** — grammar constraints are a core structured-output technique used by inference engines and agent frameworks.
- **Relation to constrained decoding** — grammar-constrained generation is a specialization of general constrained decoding.
- **Semantic validation** — valid output can still be wrong, so grammar constraints are paired with business-rule checks rather than replacing them.


## Related

- [[wiki/prompt-engineering/constrained-decoding|Constrained Decoding]] — the general technique
- [[wiki/prompt-engineering/json-schema-decoding|JSON Schema Decoding]] — the schema variant
- [[wiki/ai-ml/structured-output-generation|Structured Output Generation]] — the goal
- [[wiki/prompt-engineering/latex-generation|LaTeX Generation]] — a grammar application
- [[wiki/llm-agents/tool-use-function-calling|Tool Use and Function Calling]] — the caller context
- [[wiki/prompt-engineering/xml-output-parsing|XML Output Parsing]] — the XML variant

