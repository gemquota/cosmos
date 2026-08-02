---
type: "concept"
title: "Arrays in Bash/Zsh"
description: "Indexed and associative arrays and common patterns"
tags: ["arrays", "bash", "zsh", "scripting"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.gnu.org/software/bash/manual/html_node/Arrays.html"]
---

# Arrays in Bash/Zsh

## Summary
Bash and zsh arrays store multiple values in one variable. Bash uses zero-based indexed arrays plus associative arrays (declare -A); zsh arrays are one-based by default and its associative arrays use associative syntax from day one.

## Details
- Build indexed arrays with arr=(a "b c" d); elements with spaces must be quoted, or they split on IFS at assignment time.
- Read all elements safely with "${arr[@]}" — one word per element; "${arr[*]}" joins with the first IFS character and is for display.
- ${#arr[@]} is the element count, ${!arr[@]} the indices, and arr+=(x) appends; slicing ${arr[@]:1:2} mirrors string slicing.
- Associative arrays (declare -A map) use map[key]=value, with "${map[@]}" values and "${!map[@]}" keys — a hash map for counters and lookups.
- mapfile/readarray -t arr < file slurps lines; IFS= read -r for line-at-a-time processing with control.
- zsh differences: indices start at 1, ${(k)map} and ${(v)map} flags access keys/values, and ${arr[@]:1} has different semantics.
- Pitfalls: forgetting quotes around "${arr[@]}" silently collapses elements; for loops over unquoted arrays split on spaces.

## Related
- [[wiki/os-shell/parameter-expansion|Parameter Expansion]] — expansion operators over arrays
- [[wiki/os-shell/quoting-rules|Quoting Rules]] — element boundaries depend on quotes
- [[wiki/os-shell/shell-functions|Shell Functions]] — passing arrays by nameref
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — feeding files into arrays
- [[wiki/os-shell/zsh-configuration|Zsh Configuration]] — zsh's differing array model
