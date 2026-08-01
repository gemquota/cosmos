---
type: "concept"
title: "Here Documents"
description: "Feeding a command's stdin from literal text embedded in the script"
tags: ["heredoc", "stdin", "shell", "scripting"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Here Documents

## Summary
A here-document (`<<EOF`) feeds literal text into a command's stdin, enabling multi-line input without files: `cat <<EOF > file`. It is how scripts embed configs, SQL, and templates.

## Details
- Quoting the delimiter (`<<'EOF'`) disables expansion inside the body.
- `<<-` strips leading tabs; `<<<` (here-string) feeds a single line.
- RSIS3 relevance: wiki article templates are often generated via heredocs.

## Related
- [[wiki/os-shell/stdin-stdout-stderr|Stdin Stdout Stderr]] — heredocs are a stdin source
- [[wiki/os-shell/shell-scripting|Shell Scripting]] — the scripting idiom heredocs serve
- [[wiki/dev-tools/markdown-authoring|Markdown Authoring]] — heredocs can write markdown
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — heredocs build portable knowledge files
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — heredocs write frontmatter blocks
