---
type: "concept"
title: "Grammar-Based Testing"
description: "Generating parser and compiler inputs from grammars"
tags: ["grammar-based-testing", "testing", "parsers", "generation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.antlr.org/", "https://hypothesis.readthedocs.io/en/latest/"]
---

# Grammar-Based Testing

## Summary
Grammar-based testing generates inputs from formal grammars, lexer and parser descriptions, producing valid, varied, and malformed-but-parseable data. It is powerful for parsers, compilers, and input validation layers.

## Details
- Grammars: BNF or EBNF, ANTLR grammars, and regex-based generators.
- Generators: Hypothesis from-regex strategies, ANTLR-based generators, and custom builders.
- Syntactically valid inputs exercise deep parsing paths.
- Mutate valid inputs for negative coverage, grammar-aware fuzzing.
- Use for compilers, SQL parsers, configuration files, and protocol messages.
- Combine with property-based testing for semantic invariants.
- Grammar rules double as coverage targets for generated cases.
- Keep grammars in sync with the parser to avoid generating inputs the system never accepts.

## Related
- [[wiki/testing/fuzzing|Fuzz Testing]] — grammar-aware mutation of inputs
- [[wiki/testing/model-based-testing|Model-Based Testing]] — grammars as generation models
- [[wiki/testing/property-based-testing|Property-Based Testing]] — semantic checks on generated inputs
- [[wiki/testing/negative-testing|Negative Testing]] — malformed grammar inputs
- [[wiki/testing/test-oracles|Test Oracles]] — expected parse outcomes
- [[wiki/testing/unit-testing|Unit Testing]] — hand-written parser cases
