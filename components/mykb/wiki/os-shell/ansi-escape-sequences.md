---
type: "concept"
title: "ANSI Escape Sequences"
description: "SGR colors, cursor control, and terminal rendering"
tags: ["ansi", "escape-sequences", "terminal", "sgr", "colors"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://invisible-island.net/xterm/ctlseqs/ctlseqs.html", "https://man7.org/linux/man-pages/man4/console_codes.4.html"]
---

# ANSI Escape Sequences

## Summary
Escape sequences are the control protocol between applications and terminals: a stream starting with the ESC character tells the terminal to move the cursor, change colors, or clear the screen. The SGR (Select Graphic Rendition) sequences control text attributes and color.

## Details
- CSI sequences begin with ESC [ and end with a final byte: ESC [ 2 J clears the screen, ESC [ H homes the cursor, ESC [ n A/B/C/D move it.
- SGR colors: 30-37 foreground, 40-47 background, 90-97 bright foreground; 0 resets, 1 bold, 3 italic, 4 underline, 7 reverse.
- 256-color mode uses ESC [ 38 ; 5 ; n m; truecolor uses 38 ; 2 ; r ; g ; b m — support varies across emulators.
- Cursor visibility and shape (ESC [ ? 25 l hides), scroll regions, and the alternate screen (ESC [ ? 1049 h) matter for full-screen apps.
- OSC sequences (ESC ] ... BEL/ST) set window titles, hyperlinks (OSC 8), and clipboard (OSC 52) — some are a security risk.
- Terminals interpret these per the terminfo entry named by TERM; tput generates the right codes for the configured terminal.
- Tools echo colors with printf '[31mred[0m' or tput setaf 1; color output in pipes needs explicit opt-in to avoid control garbage.

## Related
- [[wiki/os-shell/terminal-emulators|Terminal Emulators]] — the interpreter of escape sequences
- [[wiki/os-shell/pty-and-pseudo-terminals|PTYs & Pseudo-Terminals]] — the channel they travel on
- [[wiki/os-shell/head-tail-and-less|head, tail & less]] — less -R renders ANSI colors
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]] — color-aware filtering
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]] — the multiplexer that must relay sequences
