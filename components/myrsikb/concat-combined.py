#!/usr/bin/env python3
"""Combine all three project concatenations into one master file.

Runs the individual concat scripts for RSIS3, mykb, and myrsikb,
then merges all 6 output files into a single hierarchical markdown.

Usage:
  python3 concat-combined.py [--outdir OUTPUT_DIR]
  
Output:
  combined-code.md      — Code from all 3 projects
  combined-content.md   — Content from all 3 projects
  combined-all.md       — Everything in one file
"""

import os
import sys
import subprocess
from pathlib import Path

HOME = Path.home()
PROJECTS = {
    "rsis3":  HOME / "dev" / "codex" / "rsis3",
    "mykb":   HOME / "dev" / "codex" / "mykb",
    "myrsikb": Path(__file__).resolve().parent,
}

OUT_DIR = PROJECTS["myrsikb"]
if len(sys.argv) > 2 and sys.argv[1] == "--outdir":
    OUT_DIR = Path(sys.argv[2])


def run_concat(name: str, root: Path):
    """Run a project's concat script if present."""
    print(f"  {name}...", end=" ", flush=True)
    
    # Determine the concat script
    if name == "rsis3":
        script = root / "scripts" / "concat_project.py"
    elif name == "mykb":
        script = root / "build-export.py"
        # mykb's build-export always writes to its own root, so run there
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("OK")
            for line in result.stdout.strip().split("\n"):
                if line.strip():
                    print(f"    {line.strip()}")
            # Copy the output files to OUT_DIR
            for fn in ["mykb-code.md", "mykb-content.md"]:
                src = root / fn
                dst = OUT_DIR / fn
                if src.exists():
                    import shutil
                    shutil.copy2(src, dst)
        else:
            print("FAILED")
            print(result.stderr[:500])
        return
    elif name == "myrsikb":
        script = root / "build-export.py"
    else:
        print("skipped (no script)")
        return
    
    if not script.exists():
        print("skipped (not found)")
        return
    
    result = subprocess.run(
        [sys.executable, str(script), "--outdir", str(OUT_DIR)],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print("OK")
        for line in result.stdout.strip().split("\n"):
            if line.strip():
                print(f"    {line.strip()}")
    else:
        print("FAILED")
        print(result.stderr[:500])


def merge_file(combined_lines: list, header: str, source_path: Path):
    """Append a project's export file to the combined output."""
    if not source_path.exists():
        print(f"    {source_path.name}: not found, skipping")
        return
    
    size = source_path.stat().st_size
    print(f"    {source_path.name} ({size/1024:.0f}KB)")
    
    content = source_path.read_text(encoding="utf-8", errors="replace")
    
    # Split into lines, skip the original title (we use our own header)
    lines = content.split("\n")
    
    # Find where the content really starts (after the first --- separator)
    # or skip the first heading
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "---" and i < 10:
            start = i + 1
            break
    
    combined_lines.append("")
    combined_lines.append(f"## {header}")
    combined_lines.append("")
    combined_lines.extend(lines[start:])
    combined_lines.append("")


def main():
    print("=== Combined Project Export ===")
    print("")
    
    # Step 1: Run individual concat scripts
    print("Step 1: Generating individual exports...")
    for name, root in PROJECTS.items():
        run_concat(name, root)
    
    print("")
    
    # Step 2: Merge code files
    print("Step 2: Merging into combined exports...")
    
    code_sources = [
        ("RSIS3 — Code", OUT_DIR / "rsis3-code.md"),
        ("mykb — Code", OUT_DIR / "mykb-code.md"),
        ("myrsikb — Code", OUT_DIR / "myrsikb-code.md"),
    ]
    
    content_sources = [
        ("RSIS3 — Content", OUT_DIR / "rsis3-content.md"),
        ("mykb — Content", OUT_DIR / "mykb-content.md"),
        ("myrsikb — Content", OUT_DIR / "myrsikb-content.md"),
    ]
    
    def fmt_size(path: Path) -> str:
        return f"{path.stat().st_size/1024:.0f}KB" if path.exists() else "0KB"
    
    # ── Combined Code ──────────────────────────────────────
    print("\n  Combined Code:")
    code_lines = [
        "# Combined Code — RSIS3 + mykb + myrsikb",
        "",
        "> All source code from the RSIS3 cognitive architecture, mykb knowledge operating system,",
        "> and their memory bridge integration layer. Combined into one hierarchical document.",
        "",
    ]
    
    # Summary table
    code_lines.append("| Project | File | Size |")
    code_lines.append("|---------|------|------|")
    for name, path in code_sources:
        code_lines.append(f"| {name.split('—')[0].strip()} | `{path.name}` | {fmt_size(path)} |")
    code_lines.append("")
    
    for header, path in code_sources:
        merge_file(code_lines, header, path)
    
    code_path = OUT_DIR / "combined-code.md"
    code_path.write_text("\n".join(code_lines), encoding="utf-8")
    print(f"  → {code_path} ({code_path.stat().st_size/1024:.0f}KB)")
    
    # ── Combined Content ────────────────────────────────────
    print("\n  Combined Content:")
    content_lines = [
        "# Combined Content — RSIS3 + mykb + myrsikb",
        "",
        "> All documentation, wiki articles, and text content from all three projects.",
        "",
    ]
    
    content_lines.append("| Project | File | Size |")
    content_lines.append("|---------|------|------|")
    for name, path in content_sources:
        content_lines.append(f"| {name.split('—')[0].strip()} | `{path.name}` | {fmt_size(path)} |")
    content_lines.append("")
    
    for header, path in content_sources:
        merge_file(content_lines, header, path)
    
    content_path = OUT_DIR / "combined-content.md"
    content_path.write_text("\n".join(content_lines), encoding="utf-8")
    print(f"  → {content_path} ({content_path.stat().st_size/1024:.0f}KB)")
    
    # ── Combined All ────────────────────────────────────────
    print("\n  Combined All:")
    all_lines = [
        "# Combined — RSIS3 + mykb + myrsikb",
        "",
        "> Complete export of all code and content from the RSIS3 autonomous cognitive architecture,",
        "> mykb personal knowledge operating system, and their memory bridge integration.",
        "",
        "## Contents",
        "",
        "1. [Combined Code](#combined-code)",
        "2. [Combined Content](#combined-content)",
        "",
    ]
    
    # Code section
    all_lines.append("---")
    all_lines.append("")
    all_lines.append("# Combined Code")
    all_lines.append("")
    for header, path in code_sources:
        merge_file(all_lines, header, path)
    
    # Content section
    all_lines.append("---")
    all_lines.append("")
    all_lines.append("# Combined Content")
    all_lines.append("")
    for header, path in content_sources:
        merge_file(all_lines, header, path)
    
    all_path = OUT_DIR / "combined-all.md"
    all_path.write_text("\n".join(all_lines), encoding="utf-8")
    print(f"  → {all_path} ({all_path.stat().st_size/1024:.0f}KB)")
    
    total = sum(
        p.stat().st_size for _, p in code_sources + content_sources if p.exists()
    )
    print(f"\n  Total source: {total/1024:.0f}KB across 6 individual exports")
    combined_total = (
        code_path.stat().st_size + content_path.stat().st_size + all_path.stat().st_size
    )
    print(f"  Combined outputs: {combined_total/1024:.0f}KB (3 files)")
    print("\nDone.")


if __name__ == "__main__":
    main()
