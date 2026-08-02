---
type: "concept"
title: "Terminal Emulators"
description: "Terminfo/termcap, the TERM variable, and emulator families"
tags: ["terminal", "terminfo", "term", "emulator"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://invisible-island.net/ncurses/ncurses.faq.html", "https://man7.org/linux/man-pages/man5/terminfo.5.html"]
---

# Terminal Emulators

## Summary
A terminal emulator renders a character-cell screen and translates keyboard input into escape sequences, standing in for the hardware terminals of the past. The TERM variable names the emulator's capabilities, and the terminfo database tells programs like ncurses which sequences to emit.

## Details
- Families: xterm-compatible (xterm, GNOME Terminal, Konsole, Windows Terminal), modern GPU-accelerated (alacritty, kitty, foot), and multiplexer-embedded (tmux, screen).
- TERM=xterm-256color is the common modern value; programs query terminfo for cursor movement, color, and clear-screen sequences.
- terminfo entries live under /usr/share/terminfo (one file per terminal) and describe capabilities like colors, insert/delete lines, and function keys.
- tput colors, tput cup r c, and tput setaf n let scripts use terminal features without hardcoding sequences.
- Emulators differ in truecolor support, Unicode width handling, and escape handling; mismatch causes artifacts like broken colors in tmux.
- The DEC Special Graphics and VT100 lineage still shapes everything: most emulators answer ANSI/DEC queries identically.
- Clipboard, font, and scrollback live in the emulator, not the shell; multiplexers add panes and sessions on top.

## Related
- [[wiki/os-shell/pty-and-pseudo-terminals|PTYs & Pseudo-Terminals]] — the kernel plumbing under every emulator
- [[wiki/os-shell/ansi-escape-sequences|ANSI Escape Sequences]] — the protocol emulators speak
- [[wiki/os-shell/tmux-sessions|Tmux Sessions]] — the multiplexer layer
- [[wiki/os-shell/readline-and-line-editing|Readline & Line Editing]] — editing inside the emulator
- [[wiki/os-shell/dotfiles|Dotfiles]] — where TERM and terminal prefs are set
