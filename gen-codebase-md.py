#!/usr/bin/env python3
"""Generate CODEBASE.md — a combined, hierarchical concatenation of the
COSMOS codebase for context injection and review.

Rules (kept in sync with the header of the generated file):
  - include source/config/docs: .py .mjs .js .cjs .ts .tsx .html .css
    .sh .yml .yaml .json .md (md only from selected dirs) plus
    extensionless executable scripts (e.g. cli/cosmos) and .github workflows
  - exclude generated/runtime/data: node_modules, dist, auto, exports,
    .rsis, wiki content, telemetry, jsonl, maps, images, zips, snapshots,
    audit-suite reports, package-lock, and the output file itself
  - per-file cap: 250 KB (larger files are skipped and reported)

Usage: python3 gen-codebase-md.py [--out CODEBASE.md]
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = "CODEBASE.md"
MAX_FILE_BYTES = 250 * 1024

INCLUDE_EXT = {".py", ".mjs", ".js", ".cjs", ".ts", ".tsx", ".html", ".css",
               ".sh", ".yml", ".yaml", ".json", ".md"}

LANG = {
    ".py": "python", ".mjs": "javascript", ".js": "javascript",
    ".cjs": "javascript", ".ts": "typescript", ".tsx": "tsx",
    ".html": "html", ".css": "css", ".sh": "bash", ".yml": "yaml",
    ".yaml": "yaml", ".json": "json", ".md": "markdown",
}

EXCLUDED_DIRS = {
    ".git", "node_modules", "dist", "auto", "exports", ".rsis", "__pycache__",
    ".pytest_cache", ".vercel", "wiki", "raw", "buffers", "cycles", "telemetry",
    "proposals", "sessions", "reports", "audit-suite", "superpowers",
}
EXCLUDED_DIR_PARTS = {"__pycache__", ".pytest_cache"}
EXCLUDED_NAMES = {
    # generated snapshots / heavy artifacts
    "catalog.json", "files.json", "graph.json", "index.json", "log.json",
    "stub-index.json", "stub-review.json", "stub_created_dates.json",
    "guidance.json", "dashboard-data.json", "loops.json", "ecosystem.json",
    "package-lock.json", "mykb-code.md", "mykb-content.md", "log.md",
    "CODEBASE.md", "gen-codebase-md.py",
    "data.json",  # vercel-deploy app payload (generated)
}
# markdown is only included from these roots (content dirs stay out)
MD_ROOTS = {
    ROOT,
    ROOT / "components/rsis3",
    ROOT / "components/rsis3/docs",
    ROOT / "components/mykb",
    ROOT / "components/space",
    ROOT / "components/space/docs",
    ROOT / "components/space/meta",
    ROOT / "components/space/prompt-framework",
    ROOT / "contracts",
    ROOT / "vercel-deploy",
    ROOT / "docs",
}
SKIP_DIRS = {"diagrams", "ops"}  # images + report content


def excluded_path(p: Path) -> bool:
    rel = p.relative_to(ROOT)
    parts = set(rel.parts)
    if EXCLUDED_DIRS & parts or EXCLUDED_DIR_PARTS & parts:
        return True
    if p.name in EXCLUDED_NAMES:
        return True
    if rel.parts[:3] == ("components", "mykb", "ops"):
        return True  # mykb ops reports/assessments are content, not code
    if rel.parts[:2] == ("components", "rsis3") and "lifecycles" in rel.parts:
        return True  # rebirth archives are runtime state
    if rel.parts[:2] == ("components", "rsis3") and rel.parts[2:3] == ("rack",) \
            and rel.parts[3:4] == ("pulses",) and p.name == "dashboard-data.json":
        return True  # generated snapshot (also in EXCLUDED_NAMES)
    for d in SKIP_DIRS:
        if rel.parts and rel.parts[0] == d:
            return True
    return False


def is_script(p: Path) -> bool:
    """Extensionless executable source scripts (e.g. cli/cosmos)."""
    if p.suffix or not (p.stat().st_mode & 0o111):
        return False
    try:
        with open(p, "rb") as fh:
            return fh.read(2) == b"#!"
    except OSError:
        return False


def lang_for(p: Path) -> str:
    lang = LANG.get(p.suffix.lower(), "")
    return "bash" if not lang and is_script(p) else lang


def collect() -> list[Path]:
    files: list[Path] = []
    skipped_big: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS
                       and (not d.startswith(".") or d == ".github")]
        cur = Path(dirpath)
        if excluded_path(cur) and cur != ROOT:
            continue
        for name in sorted(filenames):
            p = cur / name
            if excluded_path(p):
                continue
            ext = p.suffix.lower()
            if ext not in INCLUDE_EXT and not is_script(p):
                continue
            if ext == ".md" and not any(
                    p.is_relative_to(r) for r in MD_ROOTS):
                continue
            size = p.stat().st_size
            if size > MAX_FILE_BYTES:
                skipped_big.append(f"{p.relative_to(ROOT)} ({size // 1024}KB)")
                continue
            files.append(p)
    files.sort(key=lambda p: str(p.relative_to(ROOT)))
    if skipped_big:
        print(f"  skipped >{MAX_FILE_BYTES // 1024}KB: {len(skipped_big)} files "
              f"({', '.join(skipped_big[:5])}{'…' if len(skipped_big) > 5 else ''})",
              file=sys.stderr)
    return files


def anchor(rel: str) -> str:
    return "file-" + "".join(c if c.isalnum() else "-" for c in rel.lower())


def tree_lines(files: list[Path]) -> list[str]:
    """Prune a directory tree from the included relative paths."""
    tree: dict = {}
    for p in files:
        node = tree
        for part in p.relative_to(ROOT).parts[:-1]:
            node = node.setdefault(part, {})
        node[p.name] = None

    lines: list[str] = []
    def walk(node: dict, prefix: str):
        entries = sorted(node.items())
        for i, (name, child) in enumerate(entries):
            last = i == len(entries) - 1
            branch = "└─" if last else "├─"
            lines.append(f"{prefix}{branch} {name}")
            if child:
                walk(child, prefix + ("   " if last else "│  "))
    walk(tree, "")
    return lines


def render(files: list[Path]) -> str:
    total = sum(p.stat().st_size for p in files)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out: list[str] = []
    out.append("# COSMOS — Combined Codebase (hierarchical concatenation)")
    out.append("")
    out.append(f"Generated: {ts} · files: {len(files)} · total: "
               f"{total / 1024 / 1024:.2f} MB · script: `gen-codebase-md.py`")
    out.append("")
    out.append("## Inclusion rules")
    out.append("")
    out.append("- Source, config, and docs: `.py .mjs .js .cjs .ts .tsx "
               ".html .css .sh .yml .yaml .json` plus markdown from the "
               "repo/component/doc roots, extensionless executable scripts "
               "(`cli/cosmos`), and `.github/` CI workflows. (MyKB `wiki/` "
               "content is data, not code, and stays out.)")
    out.append("- Excluded: `.git`, `node_modules`, `dist/`, `auto/`, "
               "`exports/`, `.rsis/` state, telemetry/cycles/sessions, "
               "generated snapshots (`graph.json`, `files.json`, "
               "`catalog.json`, `dashboard-data.json`, …), images, zips, "
               "`docs/audit-suite`/`docs/superpowers` reports, "
               "`package-lock.json`, and this file.")
    out.append(f"- Per-file cap: {MAX_FILE_BYTES // 1024} KB "
               "(larger files are skipped).")
    out.append("")
    out.append("## Repository tree")
    out.append("")
    out.append("```text")
    out.extend(tree_lines(files))
    out.append("```")
    out.append("")
    out.append("## Table of contents")
    out.append("")
    for p in files:
        rel = str(p.relative_to(ROOT))
        out.append(f"- [{rel}](#{anchor(rel)})")
    out.append("")

    # group by top-level: root files first, then top dirs alphabetically
    by_top: dict[str, list[Path]] = {}
    for p in files:
        rel = p.relative_to(ROOT)
        top = "" if len(rel.parts) == 1 else rel.parts[0]
        by_top.setdefault(top, []).append(p)

    def sort_key(top: str):
        return (top != "", top)  # root files first

    for top in sorted(by_top, key=sort_key):
        group = by_top[top]
        if top:
            out.append(f"## {top}/")
            out.append("")
        else:
            out.append("## / (repo root)")
            out.append("")
        for p in group:
            rel = str(p.relative_to(ROOT))
            size = p.stat().st_size
            out.append(f"### `{rel}`  [{size // 1024}KB]")
            out.append("")
            lang = lang_for(p)
            out.append(f"```{lang}")
            out.append(p.read_text(encoding="utf-8", errors="replace").rstrip("\n"))
            out.append("```")
            out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT)
    args = ap.parse_args()
    files = collect()
    dest = ROOT / args.out
    dest.write_text(render(files), encoding="utf-8")
    print(f"CODEBASE.md written: {len(files)} files, "
          f"{dest.stat().st_size / 1024 / 1024:.2f} MB → {dest.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
