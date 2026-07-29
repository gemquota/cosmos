#!/usr/bin/env python3
"""Concatenate the myrsikb (memory_bridge) project into markdown.

Outputs:
  myrsikb-code.md     — All source code files
  myrsikb-content.md  — Documentation files

Usage:
  python3 build-export.py [--outdir OUTPUT_DIR]
"""

import os
import sys
import fnmatch
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

EXCLUDE_DIRS = {"__pycache__", ".git"}
EXCLUDE_PATTERNS = {"*.pyc", "*.md"}  # exclude generated markdown outputs
CODE_EXTENSIONS = {".py", ".json", ".toml"}
CONTENT_EXTENSIONS = {".md", ".txt"}


def classify_file(rel_path: str):
    name = Path(rel_path).name
    ext = Path(rel_path).suffix.lower()

    for pat in EXCLUDE_PATTERNS:
        if fnmatch.fnmatch(name, pat):
            return None

    if name == "build-export.py":
        return None

    if ext in CODE_EXTENSIONS:
        return "code"
    if ext in CONTENT_EXTENSIONS:
        return "content"
    return None


def fmt_size(size: int) -> str:
    if size < 1024:
        return f"{size}B"
    elif size < 1024 * 1024:
        return f"{size/1024:.1f}KB"
    return f"{size/1024/1024:.1f}MB"


def file_lang(path: str) -> str:
    ext = Path(path).suffix.lower()
    return {".py": "python", ".json": "json", ".toml": "toml", ".md": "markdown", ".txt": "text"}.get(ext, "")


def generate_markdown(files, title, description):
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"> {description}")
    lines.append("")
    lines.append(f"**{len(files)} files**")
    if files:
        total = sum(os.path.getsize(str(PROJECT_ROOT / f)) for f in files)
        lines.append(f"**{fmt_size(total)}**")
    lines.append("")
    lines.append("---")
    lines.append("")

    by_dir = {}
    for f in files:
        d = str(Path(f).parent)
        by_dir.setdefault(d, []).append(f)

    for directory in sorted(by_dir.keys()):
        dir_files = sorted(by_dir[directory])
        header = directory if directory != "." else "root"
        lines.append(f"## `{header}/`")
        lines.append("")

        for f in dir_files:
            full_path = PROJECT_ROOT / f
            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                content = f"*[Error: {e}]*"

            lang = file_lang(f)
            size_str = fmt_size(os.path.getsize(str(full_path)))

            lines.append(f"### `{f}`")
            lines.append("")
            lines.append(f"*{size_str}*")
            lines.append("")
            lines.append(f"```{lang}")
            lines.append(content.rstrip("\n"))
            lines.append("```")
            lines.append("")

    return "\n".join(lines)


def main():
    outdir = PROJECT_ROOT
    if len(sys.argv) > 2 and sys.argv[1] == "--outdir":
        outdir = Path(sys.argv[2])

    print(f"Scanning {PROJECT_ROOT}...")
    all_files = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if any(fnmatch.fnmatch(f, p) for p in EXCLUDE_PATTERNS):
                continue
            full = Path(root) / f
            rel = str(full.relative_to(PROJECT_ROOT))
            all_files.append(rel)

    code_files = sorted(f for f in all_files if classify_file(f) == "code")
    content_files = sorted(f for f in all_files if classify_file(f) == "content")

    print(f"  Code: {len(code_files)}, Content: {len(content_files)}")

    code_md = generate_markdown(
        code_files,
        "myrsikb — Code Files",
        "memory_bridge: RSIS3 ↔ mykb integration layer",
    )
    code_path = outdir / "myrsikb-code.md"
    code_path.write_text(code_md, encoding="utf-8")
    print(f"  → {code_path} ({fmt_size(code_path.stat().st_size)})")

    content_md = generate_markdown(
        content_files,
        "myrsikb — Content Files",
        "Documentation for the memory bridge",
    )
    content_path = outdir / "myrsikb-content.md"
    content_path.write_text(content_md, encoding="utf-8")
    print(f"  → {content_path} ({fmt_size(content_path.stat().st_size)})")

    print("Done.")


if __name__ == "__main__":
    main()
