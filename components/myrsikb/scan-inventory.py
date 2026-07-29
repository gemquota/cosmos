#!/usr/bin/env python3
"""Generate a comprehensive inventory of all code files across RSIS3, mykb, and myrsikb."""

import os
import re
import ast
from pathlib import Path

HOME = Path.home()
PROJECTS = {
    "rsis3":  HOME / "dev" / "codex" / "rsis3",
    "mykb":   HOME / "dev" / "codex" / "mykb",
    "myrsikb": Path(__file__).resolve().parent,
}

INVENTORY_PATH = HOME / "dev" / "codex" / "myrsikb" / "INVENTORY.md"

SKIP_DIRS = {
    "__pycache__", ".git", ".pytest_cache", ".hypothesis",
    "node_modules", ".okf-skill", ".obsidian",
    "rack", ".agents", "buffers", "templates",
}
SKIP_FILES = {
    "package-lock.json", ".dash.log",
}
SKIP_PATTERNS = {"*.pyc", "*.db", "*.db-*", "*.pyo", "*.db-wal", "*.db-shm", "*.npz"}

CODE_EXTS = {".py", ".js", ".css", ".html", ".sh", ".yml", ".yaml", ".json", ".toml", ".j2", ".mjs"}


def should_include(rel_path: str, root: Path) -> bool:
    parts = rel_path.replace("\\", "/").split("/")
    name = Path(rel_path).name
    if name in SKIP_FILES:
        return False
    for pat in SKIP_PATTERNS:
        import fnmatch
        if fnmatch.fnmatch(name, pat):
            return False
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return False
    ext = Path(rel_path).suffix.lower()
    if ext in CODE_EXTS:
        return True
    if name == ".gitignore":
        return True
    return False


def extract_docstring(path: Path) -> str:
    """Extract the module-level docstring from a Python file."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content)
        if isinstance(tree, ast.Module) and tree.body:
            first = tree.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
                doc = first.value.value
                return doc.strip()
    except Exception:
        pass
    return ""


def extract_jsdoc(path: Path) -> str:
    """Extract top comment block from a JS file."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        lines = content.strip().split("\n")
        if lines and lines[0].startswith("#!/"):
            lines = lines[1:]
        comment_lines = []
        for line in lines[:20]:
            if line.strip().startswith("//") or line.strip().startswith("/*") or line.strip().startswith("*"):
                comment_lines.append(line.strip().lstrip("/*").lstrip("*").lstrip("//").strip())
                if "*/" in line:
                    break
            elif comment_lines and not line.strip().startswith(("//", "/*", "*")):
                break
        return " ".join(comment_lines) if comment_lines else ""
    except Exception:
        return ""


def extract_shebang(path: Path) -> str:
    """Get the shebang line."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        first = content.strip().split("\n")[0]
        if first.startswith("#!"):
            return first
    except Exception:
        pass
    return ""


def get_first_imports(path: Path) -> str:
    """Get the key imports from a Python file."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content)
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
                    if len(imports) >= 3:
                        break
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
                    if len(imports) >= 3:
                        break
            if len(imports) >= 3:
                break
        return ", ".join(imports)
    except Exception:
        return ""


def get_top_classes(path: Path) -> list[str]:
    """Get the top-level class names from a Python file."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content)
        return [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
            and not node.name.startswith("_")
        ][:5]
    except Exception:
        return []


def get_top_functions(path: Path) -> list[str]:
    """Get the top-level function names."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(content)
        return [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
            and not node.name.startswith("_")
        ][:5]
    except Exception:
        return []


def generate_description(path: Path, rel_path: str, ext: str) -> str:
    """Generate a multi-paragraph description of the file."""
    paras = []

    if ext == ".py":
        doc = extract_docstring(path)
        shebang = extract_shebang(path)
        classes = get_top_classes(path)
        funcs = get_top_functions(path)
        imports = get_first_imports(path)

        if shebang:
            paras.append(f"Executable script. {shebang[2:]}")

        if doc:
            # Split docstring into sentences, take first 2-3
            sentences = [s.strip() for s in doc.replace("\n", " ").split(".") if s.strip()]
            p1 = ". ".join(sentences[:2]) + "." if len(sentences) >= 2 else sentences[0] + "." if sentences else ""
            if p1:
                paras.append(p1)

        if classes:
            cls_line = ", ".join(classes[:4])
            extra = f" Also defines: {', '.join(classes[4:])}" if len(classes) > 4 else ""
            paras.append(f"Defines classes: **{cls_line}**." + extra)

        if funcs and not classes:
            func_line = ", ".join(funcs[:4])
            paras.append(f"Provides functions: `{func_line}`.")

        if imports and not doc:
            paras.append(f"Key dependencies: `{imports}`.")

    elif ext == ".js":
        jdoc = extract_jsdoc(path)
        shebang = extract_shebang(path)
        if shebang:
            paras.append(f"Executable. {shebang[2:]}")
        if jdoc:
            paras.append(jdoc)

    elif ext == ".sh":
        shebang = extract_shebang(path)
        if shebang:
            paras.append(f"Shell script. {shebang[2:]}")

        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            for line in content.split("\n")[:10]:
                if line.strip().startswith("#") and "!" not in line:
                    paras.append(line.strip().lstrip("# "))
                    break
        except Exception:
            pass

    elif ext == ".json":
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            data = content.strip()
            if data.startswith("{"):
                keys = list(json.loads(data).keys())[:5]
                paras.append(f"JSON data. Top-level keys: `{', '.join(keys)}`.")
            elif data.startswith("["):
                paras.append("JSON array.")
            else:
                paras.append("JSON data.")
        except Exception:
            paras.append("JSON data.")

    elif ext in (".yml", ".yaml"):
        paras.append("YAML configuration.")

    elif ext == ".html":
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            title_match = re.search(r"<title>(.*?)</title>", content)
            if title_match:
                paras.append(f"HTML page. Title: **{title_match.group(1)}**.")
            else:
                paras.append("HTML template.")
        except Exception:
            paras.append("HTML file.")

    elif ext == ".css":
        paras.append("Stylesheet.")

    elif ext == ".toml":
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            name_match = re.search(r'^name\s*=\s*"([^"]+)"', content, re.MULTILINE)
            if name_match:
                paras.append(f"Project configuration. Package: **{name_match.group(1)}**.")
            else:
                paras.append("TOML configuration.")
        except Exception:
            paras.append("TOML configuration.")

    elif ext == ".j2":
        paras.append("Jinja2 template.")

    if not paras:
        paras.append(f"{ext.upper()} file.")

    return "\n\n".join(paras[:3])


def describe_directory(paths_by_dir: dict) -> dict[str, str]:
    """Generate directory descriptions based on content."""
    descs = {}

    # Hard-coded directory descriptions for known packages
    hardcoded = {
        "src": "Core source code for RSIS3. Contains all cognitive subsystems, tools, and the dashboard.",
        "src/identity": "Identity subsystem — self-model, crisis monitoring, value reinforcement, and state snapshots. RSIS3's sense of self.",
        "src/rrp": "Reasoning and Resolution Protocol — structured deliberation with ambiguity assessment, constraint tracking, and multi-session coordination.",
        "src/pulse": "Pulse cycle scheduler and writer. The heartbeat of RSIS3's recursive improvement loops.",
        "src/codegen": "AST-targeted code generation engine. Finds stubs, renders Jinja2 templates, validates surgical patches.",
        "src/knowledge_graph": "Knowledge Graph facade — now delegates to mykb via memory_bridge.",
        "src/l3_self_direction": "Level 3 self-direction — signal watching, goal generation, queue management, and evolutionary planning.",
        "src/dashboard": "FastAPI dashboard server and static frontend. Charts, tabs, knowledge explorer, and system monitoring.",
        "src/db": "SQLite database connection manager, schema, and versioned migrations.",
        "src/evaluator": "Evaluator client — validates pulse cycle phases and produces evaluation reports.",
        "src/tools": "Tool suite — knowledge graph, pulse engine, recovery manager, test runner, state machine, and utility scripts.",
        "src/state_machine": "Core state machine — manages system states, transitions, and lifecycles.",
        "src/recovery": "Recovery manager — applies patches, verifies with tests, commits when passing.",
        "src/dashboard/static": "Dashboard frontend — HTML, CSS, and JavaScript. Served by FastAPI.",
        "src/dashboard/static/js": "JavaScript modules for the dashboard — tabs, components, API client, tooltips.",
        "src/dashboard/static/js/components": "Reusable dashboard UI components — tooltips, modal, accordion, skeleton, charts, navigator, system graph.",
        "src/dashboard/static/js/tabs": "Dashboard tab views — overview, cycles, telemetry, RRP, identity, scheduler, DB, explore, knowledge, errors.",
        "src/dashboard/static/css": "Dashboard stylesheets.",
        ".wiki-daemon": "mykb daemon scripts — session extraction, vector DB, graph engine, gap detection, QA API, backlinks, temporal analysis, curation.",
        "hooks": "Codex hooks for mykb — post-tool-use and session-stop handlers that write session buffers.",
        "wiki": "mykb wiki bundle — OKF-format markdown articles, entities, sessions, daily notes, community pages.",
        "scripts": "Build and maintenance scripts.",
        "memory_bridge": "RSIS3 ↔ mykb integration layer. Standalone Python package that lets RSIS3 treat mykb as its semantic memory, knowledge graph, and gap detector.",
    }

    for d, paths in paths_by_dir.items():
        # Try hardcoded first
        parts = d.split("/")
        for depth in range(len(parts), 0, -1):
            prefix = "/".join(parts[:depth])
            if prefix in hardcoded:
                descs[d] = hardcoded[prefix]
                break
        if d not in descs:
            # Generate from file list
            files = ", ".join(Path(p).name for p in paths[:6])
            if len(paths) > 6:
                files += f" and {len(paths) - 6} more"
            descs[d] = f"Contains {len(paths)} file(s): {files}."

    return descs


def main():
    import json, fnmatch

    print("Scanning projects...")
    all_files = []  # list of (project, rel_path, full_path)

    tree_structure = {}  # project -> {dir: [files]}

    for proj_name, proj_root in PROJECTS.items():
        print(f"  {proj_name}...")
        project_files = []
        dir_map = {}

        for root, dirs, files in os.walk(proj_root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

            for f in sorted(files):
                full = Path(root) / f
                rel = str(full.relative_to(proj_root))
                if not should_include(rel, proj_root):
                    continue

                d = str(Path(rel).parent)
                if d not in dir_map:
                    dir_map[d] = []
                dir_map[d].append(rel)
                project_files.append((rel, full))

        tree_structure[proj_name] = dir_map
        all_files.extend((proj_name, rel, full) for rel, full in project_files)

    total = len(all_files)
    print(f"\nTotal code files: {total}")

    # Generate directory descriptions
    dir_descs = {}
    for proj_name, dir_map in tree_structure.items():
        dir_descs[proj_name] = describe_directory(dir_map)

    # Write inventory
    print(f"Writing inventory...")

    lines = []
    lines.append("# RSIS3 + mykb + myrsikb — Complete Code Inventory")
    lines.append("")
    lines.append(f"**{total} files** across **3 projects** — RSIS3 (cognitive architecture),")
    lines.append("mykb (knowledge operating system), and myrsikb (memory bridge).")
    lines.append("")
    lines.append("---")
    lines.append("")

    for proj_name in ["rsis3", "mykb", "myrsikb"]:
        proj_root = PROJECTS[proj_name]
        proj_files = [(rel, full) for p, rel, full in all_files if p == proj_name]
        dir_map = tree_structure[proj_name]

        lines.append(f"# {proj_name}")
        lines.append("")
        lines.append(f"**{len(proj_files)} files** — `{proj_root}`")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Group by directory, sorted
        for directory in sorted(dir_map.keys()):
            dir_files = sorted(dir_map[directory])
            display_dir = directory if directory != "." else "`root`"

            # Directory description
            dd = dir_descs[proj_name].get(directory, "")
            lines.append(f"## 📁 {display_dir}/")
            lines.append("")
            if dd:
                lines.append(dd)
                lines.append("")
            lines.append("")

            for rel_path in dir_files:
                full = proj_root / rel_path
                ext = Path(rel_path).suffix.lower()
                name = Path(rel_path).name
                size = full.stat().st_size

                sz_str = f"{size}B" if size < 1024 else f"{size/1024:.1f}KB"

                lines.append(f"### `{rel_path}`")
                lines.append("")
                lines.append(f"*{sz_str}*")
                lines.append("")

                desc = generate_description(full, rel_path, ext)
                for para in desc.split("\n\n"):
                    lines.append(para)
                    lines.append("")

                lines.append("")

        lines.append("---")
        lines.append("")

    # Write
    output = "\n".join(lines)
    INVENTORY_PATH.write_text(output, encoding="utf-8")
    print(f"  → {INVENTORY_PATH} ({INVENTORY_PATH.stat().st_size / 1024:.0f}KB)")
    print("Done.")


if __name__ == "__main__":
    main()
