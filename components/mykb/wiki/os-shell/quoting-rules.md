---
type: "concept"
title: "Quoting Rules"
description: "Single/double quotes, backslash escapes, and ANSI-C quoting"
tags: ["quoting", "shell", "escaping", "bash"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Quoting.html"]
---

# Quoting Rules

## Summary
Quoting is how a shell stops special characters from being interpreted: single quotes make everything literal, double quotes preserve most expansions but prevent splitting and globbing, and backslashes escape single characters.

## Details
- Single quotes: '...' removes the meaning of every character inside, including backslash and $; there is no way to embed a single quote except via ''' or double quotes.
- Double quotes: "..." keeps $, `, and \ active but suppresses word splitting and globbing, so "$var" passes multi-word values intact.
- Backslash escapes the next character inside double quotes for $, `, ", \, and newline; outside quotes it escapes anything.
- ANSI-C quoting $'...' interprets \n, \t, \xNN, \uNNNN and friends — the portable way to embed control characters.
- Locale-aware quoting $'...' is less common; printf '%q' and ${var@Q} produce safely re-quoted strings for eval.
- Empty and unset are different: "" expands to an empty argument while "$@" without arguments expands to nothing at all.
- Here-documents have their own quoting rules: <<'EOF' suppresses expansion inside the body.

## Related
- [[wiki/os-shell/shell-expansion-order|Shell Expansion Order]] — quoting changes which stages run
- [[wiki/os-shell/parameter-expansion|Parameter Expansion]] — the expansions quotes control
- [[wiki/os-shell/here-documents|Here Documents]] — quoted delimiters disable expansion
- [[wiki/os-shell/command-substitution|Command Substitution]] — quoted substitution avoids splitting
- [[wiki/os-shell/environment-variables|Environment Variables]] — values with spaces need quotes
