---
type: "entity"
title: "RuntimeError"
resource: ""
---
description: "A generic runtime failure indicating invalid state or an unhandled condition"
tags: ["android", "api", "ast", "auth", "authentication", "bash", "entity", "errors"]
timestamp: "2026-07-19T22:41:43Z"

# RuntimeError

## Summary
A runtime error is a failure that occurs while a program is executing, indicating invalid state or a condition the code did not anticipate. It matters because most runtime errors are symptoms of a logic or state bug, not random events. Clear handling and reporting turn them from mysterious crashes into diagnosable problems, and prevention keeps them rare.

## Details
- **Definition** — a runtime error signals that execution hit an invalid state, such as an impossible value, a missing precondition, or an unhandled branch.
- **Distinction** — runtime errors differ from input-validation errors: validation rejects bad input; runtime errors mean the code itself reached a bad state.
- **Exception hygiene** — catching broad exception types hides bugs; handlers should be as specific as the situation allows.
- **Context** — a useful runtime error message includes what was attempted, the offending values, and the state that made it invalid.
- **Wrapping** — low-level errors should be wrapped in domain-meaningful exceptions while preserving the original cause for debugging.
- **Testing** — exercising error paths with bad state finds runtime errors before users do; error-guessing and property tests help.
- **Common failure modes** — swallowing exceptions, converting them into empty results, and logging only the message without a traceback.
- **Worked example** — a formatter receives an unexpected null date; instead of crashing opaquely, it raises a runtime error naming the field and value, which a test catches.
- **Practical relevance** — disciplined runtime error handling keeps failures visible, specific, and fixable.

- **Recovery** — some runtime errors allow safe recovery paths, such as resetting state or falling back, but recovery must be explicit.
- **Prevention** — assertions and state validation at boundaries catch the conditions that become runtime errors later.
## Related
- [[wiki/testing/error-guessing|Error Guessing]] — finding failure cases
- [[wiki/software-engineering/logging-strategies|Logging Strategies]] — capturing context
- [[wiki/testing/unit-testing|Unit Testing]] — covering error paths
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — structured errors
- [[wiki/testing/mutation-testing|Mutation Testing]] — probing robustness
- [[wiki/software-engineering/debugging-methodology|Debugging Methodology]] — root-cause analysis
