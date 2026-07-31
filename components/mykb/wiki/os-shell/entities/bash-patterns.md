---
type: "entity"
title: "Bash Scripting Patterns"
tags: ["shell", "bash", "scripting", "terminal", "automation"]
source: ["sessions/"]
---

# Bash Scripting Patterns

Shell scripting patterns observed across the ecosystem — from Termux automation to build pipelines.

## Common Patterns

### Colorized Output
echo "═══ TITLE ═══"
echo "✓ Success"
echo "✗ Failure"

### Port Detection (Android-safe)
port=8091
while nc -z 127.0.0.1 $port 2>/dev/null; do port=$((port + 1)); done

### Process Management
PID=$!
sleep 2
kill $PID 2>/dev/null
wait $PID 2>/dev/null

See also: [[wiki/shell-environment/index|Shell Environment]], [[wiki/os-shell/index|OS & Shell]]
