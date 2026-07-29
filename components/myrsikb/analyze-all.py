#!/usr/bin/env python3
"""Full analysis of every file across RSIS3, mykb, and myrsikb.
Reads each file, traces imports/uses, and generates a relationship-aware inventory."""

import os, re, ast, json, sys
from pathlib import Path
from collections import defaultdict
import fnmatch

HOME = Path.home()
PROJECTS = {
    "rsis3":  HOME / "dev" / "codex" / "rsis3",
    "mykb":   HOME / "dev" / "codex" / "mykb",
    "myrsikb": HOME / "dev" / "codex" / "myrsikb",
}

SKIP_DIRS = {
    "__pycache__", ".git", ".pytest_cache", ".hypothesis",
    "node_modules", ".okf-skill", ".obsidian",
    "rack", "buffers", ".agents",
}
SKIP_PATTERNS = {"*.pyc", "*.db", "*.db-*", "*.pyo", "*.db-wal", "*.db-shm", "*.npz"}
CODE_EXTS = {".py", ".js", ".css", ".html", ".sh", ".yml", ".yaml", ".json", ".toml", ".j2", ".mjs"}

OUT_PATH = HOME / "dev" / "codex" / "myrsikb" / "INVENTORY.md"

def is_code_file(rel_path):
    parts = rel_path.replace("\\", "/").split("/")
    name = Path(rel_path).name
    if name in {"package-lock.json", ".dash.log"}:
        return False
    for pat in SKIP_PATTERNS:
        if fnmatch.fnmatch(name, pat):
            return False
    if any(p in SKIP_DIRS for p in parts[:-1]):
        return False
    ext = Path(rel_path).suffix.lower()
    return ext in CODE_EXTS or name == ".gitignore"

def parse_py_imports(text):
    """Extract import relationships from Python source."""
    imports = set()
    try:
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])
    except:
        pass
    return imports

def parse_js_imports(text):
    js_imports = set()
    for m in re.finditer(r'(?:import|require)\s*\(?\s*[\'"]([^\'"]+)[\'"]', text):
        mod = m.group(1)
        if not mod.startswith(".") and not mod.startswith("/"):
            js_imports.add(mod.split("/")[0])
    return js_imports

def get_classes(text):
    classes = []
    try:
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                bases = []
                for base in node.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        bases.append(base.attr)
                classes.append((node.name, bases))
    except:
        pass
    return classes

def get_functions(text):
    funcs = []
    try:
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                funcs.append(node.name)
    except:
        pass
    return funcs

# ── Scan everything ────────────────────────────────────────

all_files = []  # (project, rel_path, full_path)
proj_files = {}  # project -> [(rel_path, full_path)]
proj_imports = {}  # project -> {rel_path: {imported_names}}

for proj_name, proj_root in PROJECTS.items():
    proj_files[proj_name] = []
    proj_imports[proj_name] = {}
    for root, dirs, files in os.walk(proj_root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in sorted(files):
            full = Path(root) / f
            rel = str(full.relative_to(proj_root))
            if not is_code_file(rel):
                continue
            proj_files[proj_name].append((rel, full))
            all_files.append((proj_name, rel, full))

# Build reverse dependency maps
# For each project, map filename -> set of files that import it
rev_deps = {}  # proj -> {module_name: [(importer_rel, typ)]}
for proj_name, files in proj_files.items():
    deps = defaultdict(set)
    imports_map = {}
    for rel, full in files:
        try:
            text = full.read_text(encoding="utf-8", errors="replace")
        except:
            text = ""
        if rel.endswith(".py"):
            imported = parse_py_imports(text)
        elif rel.endswith(".js") or rel.endswith(".mjs"):
            imported = parse_js_imports(text)
        else:
            imported = set()
        imports_map[rel] = imported
        # Map module names back to files
        for imp in imported:
            deps[imp].add(rel)
    proj_imports[proj_name] = imports_map
    rev_deps[proj_name] = deps

# ── Generate descriptions ──────────────────────────────────

def fmt_size(size):
    return f"{size}B" if size < 1024 else f"{size/1024:.1f}KB"

def describe_file(proj_name, rel_path, full_path):
    """Read the file and write a proper analysis."""
    try:
        text = full_path.read_text(encoding="utf-8", errors="replace")
    except:
        text = ""
    
    lines = text.split("\n")
    ext = Path(rel_path).suffix.lower()
    name = Path(rel_path).name
    size = full_path.stat().st_size
    sz = fmt_size(size)
    
    paragraphs = []
    
    # Shebang
    shebang = ""
    if lines and lines[0].startswith("#!"):
        shebang = lines[0]
    
    # Docstring (Python)
    docstring = ""
    if ext == ".py":
        try:
            tree = ast.parse(text)
            if isinstance(tree, ast.Module) and tree.body:
                first = tree.body[0]
                if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                    docstring = first.value.value.strip()
        except:
            pass
    
    # Imports
    my_imports = proj_imports[proj_name].get(rel_path, set())
    
    # What imports this file
    # Map the filename (without ext) to rev_deps
    stem = Path(rel_path).stem
    imported_by = rev_deps[proj_name].get(stem, set())
    # Also check for full module paths
    for k, v in rev_deps[proj_name].items():
        if k.endswith(stem) or stem.endswith(k):
            imported_by |= v
    
    # Remove self-references
    imported_by = {r for r in imported_by if r != rel_path}
    
    # Classes
    classes = []
    funcs = []
    if ext == ".py":
        classes = get_classes(text)
        funcs = [f for f in get_functions(text) if not f.startswith("_")]
    
    # ═══════════════════════════════════════════════════════
    # Now write the analysis
    # ═══════════════════════════════════════════════════════
    
    # Paragraph 1: Identity — what is this file
    if ext == ".py":
        if shebang:
            if docstring:
                p1 = docstring.split("\n")[0]
            else:
                p1 = f"Python script. Defines {len(classes)} class(es) and {len(funcs)} function(s)." if classes or funcs else "Python module."
            paragraphs.append(p1)
        else:
            if docstring:
                p1 = docstring.split("\n")[0]
            else:
                p1 = f"Python module. {'Defines ' + ', '.join(c[0] for c in classes[:4]) + '.' if classes else ''} {'Exports ' + ', '.join(funcs[:4]) + '.' if funcs and not classes else ''}"
            paragraphs.append(p1)
    
    elif ext == ".js":
        paragraphs.append("JavaScript module for the RSIS3 dashboard frontend.")
    
    elif ext == ".sh":
        paragraphs.append("Shell script. Launches or manages RSIS3 components.")
    
    elif ext == ".html":
        title_m = re.search(r"<title>(.*?)</title>", text)
        if title_m:
            paragraphs.append(f"HTML page: **{title_m.group(1)}**.")
        else:
            paragraphs.append("HTML template.")
    
    elif ext == ".json":
        try:
            data = json.loads(text)
            if isinstance(data, dict):
                keys = list(data.keys())[:5]
                paragraphs.append(f"JSON configuration. Contains keys: `{', '.join(keys)}`.")
            elif isinstance(data, list):
                paragraphs.append(f"JSON array with {len(data)} entries.")
        except:
            paragraphs.append("JSON data.")
    
    elif ext == ".toml":
        n_m = re.search(r'^name\s*=\s*"([^"]+)"', text, re.MULTILINE)
        paragraphs.append(f"TOML config{' for ' + n_m.group(1) if n_m else ''}.")
    
    elif ext == ".css":
        paragraphs.append("Dashboard stylesheet.")
    
    elif ext == ".j2":
        paragraphs.append("Jinja2 template for surgical code generation.")
    
    elif ext in (".yml", ".yaml"):
        paragraphs.append("YAML configuration.")
    
    # Paragraph 2: Dependencies — what it imports
    if my_imports:
        local_imports = {i for i in my_imports if not i.startswith(("src.", "memory_bridge."))}
        project_imports = {i for i in my_imports if i.startswith("src.") or i.startswith("memory_bridge.") or i in rev_deps.get(proj_name, {})}
        
        if project_imports:
            sorted_imp = sorted(project_imports)[:6]
            paragraphs.append(f"Imports from within {proj_name}: `{', '.join(sorted_imp)}`." + (f" and {len(project_imports)-6} more" if len(project_imports) > 6 else ""))
    
    # Paragraph 3: What depends on it
    if imported_by:
        sorted_deps = sorted(imported_by)[:6]
        paragraphs.append(f"Used by {len(imported_by)} file(s) in {proj_name}: `{', '.join(sorted_deps)}`." + (f" and {len(imported_by)-6} more" if len(imported_by) > 6 else ""))
    
    # Paragraph 3b: Classes and their bases
    if classes:
        cls_detail = []
        for cname, bases in classes[:4]:
            if bases:
                cls_detail.append(f"**{cname}**({', '.join(bases)})")
            else:
                cls_detail.append(f"**{cname}**")
        if classes:
            paragraphs.append(f"Defines: {', '.join(cls_detail)}." + (f" and {len(classes)-4} more" if len(classes) > 4 else ""))
    
    if not paragraphs:
        paragraphs.append(f"{ext.upper()} file in {proj_name}.")
    
    # Ensure at least 1 paragraph, at most 3
    return "\n\n".join(paragraphs[:3]), sz, classes, funcs, my_imports

# ── Write Inventory ────────────────────────────────────────

def write_inventory():
    print("Writing INVENTORY.md...")
    out = []
    
    total_files = len(all_files)
    out.append("# RSIS3 + mykb + myrsikb — Complete Code Inventory")
    out.append("")
    out.append(f"**{total_files} files** across **3 projects**, each analyzed for purpose,")
    out.append("dependencies, dependents, classes, and functions.")
    out.append("")
    out.append("---")
    out.append("")
    
    for proj_name in ["rsis3", "mykb", "myrsikb"]:
        proj_root = PROJECTS[proj_name]
        files = [(r, f) for p, r, f in all_files if p == proj_name]
        
        out.append(f"# {proj_name}")
        out.append("")
        out.append(f"**{len(files)} files** — `{proj_root}`")
        out.append("")
        out.append("---")
        out.append("")
        
        # Group by directory
        dir_map = defaultdict(list)
        for rel, full in files:
            d = str(Path(rel).parent) if Path(rel).parent != Path(".") else "."
            dir_map[d].append((rel, full))
        
        for directory in sorted(dir_map.keys()):
            dir_files = sorted(dir_map[directory], key=lambda x: x[0])
            display_dir = directory if directory != "." else "`root`"
            
            # Directory description
            dd = gen_dir_desc(proj_name, directory, dir_files)
            out.append(f"## 📁 {display_dir}/")
            out.append("")
            out.append(dd)
            out.append("")
            
            for rel_path, full_path in dir_files:
                desc, sz, classes, funcs, imports = describe_file(proj_name, rel_path, full_path)
                name = Path(rel_path).name
                
                out.append(f"### `{rel_path}`")
                out.append("")
                out.append(f"*{sz}*")
                out.append("")
                out.append(desc)
                out.append("")
        
        out.append("---")
        out.append("")
    
    text = "\n".join(out)
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"  → {OUT_PATH} ({OUT_PATH.stat().st_size/1024:.0f}KB)")
    print("Done.")

def gen_dir_desc(proj_name, directory, files):
    """Generate a directory description based on what's in it."""
    names = [Path(r).name for r, _ in files]
    
    descs = {
        "rsis3": {
            ".": "Project root. Entry points and configuration.",
            "scripts": "Build and maintenance scripts for RSIS3. Concat for prompt context, tooltip injection.",
            "src": "Core cognitive architecture. All RSIS3 subsystems live here.",
            "src/identity": "The system's sense of self. SelfModel tracks layer scores, purpose, narrative, and values across 9 cognitive layers. CrisisMonitor detects threshold breaches. SnapshotManager persists identity state over time. ValueReinforcementTracker records axiom reinforcement.",
            "src/rrp": "Reasoning and Resolution Protocol — RSIS3's structured deliberation engine. Multi-round protocol with ambiguity vectors, constraint tracking, decision trees, session persistence, and multi-session coordination for branching deliberations.",
            "src/pulse": "Pulse cycle system — the heartbeat of recursive improvement. Scheduler runs periodic cycles. Writer persists pulse data as JSON. Each pulse captures system state, layer scores, evaluation decisions, and patch outcomes.",
            "src/codegen": "AST-targeted code generation. Finds stub coordinates in source files, renders Jinja2 templates, validates surgical patches (same line count, same structure). Every successful mutation is recorded in mykb.",
            "src/l3_self_direction": "Level 3 self-direction — the meta-cognitive layer. SignalWatcher polls for changes. GoalGenerator ranks goals by priority, now including knowledge gaps from mykb. QueueManager orchestrates execution. Evolution handles strategy refinement.",
            "src/dashboard": "FastAPI server on port 8765 with 10 tab views. Serves real-time system metrics, cycle history, RRP sessions, identity state, and the new knowledge explorer. Static frontend uses vanilla JS with Chart.js for system graph visualization.",
            "src/dashboard/static": "Dashboard frontend assets. HTML entry point with 19 script tags, CSS with cargo-cult theme system, and modular JS architecture.",
            "src/dashboard/static/js": "Dashboard JavaScript — API client, tab renderers, UI components, and the new knowledge explorer tab.",
            "src/dashboard/static/js/components": "Reusable widgets: tooltips, modal dialogs, accordion panels, skeleton loaders, chart.js wrapper, navigator bar, and the force-directed system graph.",
            "src/dashboard/static/js/tabs": "Ten tab views: overview, cycles, telemetry, RRP, identity, scheduler, db, explore, **knowledge** (new — mykb explorer), and errors.",
            "src/db": "SQLite persistence layer. Thread-safe connection manager with singleton pattern. Versioned schema migrations (forward-only). Stores RRP sessions, cycles, telemetry, identity snapshots, KG nodes/edges, goals, and signals.",
            "src/evaluator": "Evaluation client for pulse cycles. Validates goal analysis, constraint extraction, ambiguity assessment, and produces structured evaluation reports.",
            "src/tools": "Tool suite that RSIS3's cognitive layers call. KnowledgeGraph (now delegates to mykb), PulseEngine (orchestrates the 9-phase protocol), RecoveryManager (apply-and-verify with auto-commit), TestRunner, StateMachine, and utilities.",
            "src/state_machine": "Nested state machine for RSIS3's lifecycle. Manages cognitive layer states, transitions between thinking/acting/reflecting modes, and the recovery lifecycle.",
            "src/recovery": "Recovery system — applies patches, runs tests, and auto-commits when everything passes. Implements defensive recovery patterns for identity crisis resolution.",
        },
        "mykb": {
            ".": "Project root. Server, index builder, export script, and startup shell script.",
            ".wiki-daemon": "The daemon and all its analysis engines. Session extraction, vector embedding, hybrid search, graph engine, gap detection, backlinks, temporal analysis, curation, consolidation, QA API, and domain article writing.",
            "hooks": "Codex tool-use hooks. Post-tool-use and session-stop handlers that write session buffers for the wiki daemon to process.",
            "wiki": "The knowledge base itself. 2298 OKF-format markdown files in typed subdirectories: sessions, entities, decisions, tools, topics, daily notes, communities, identity, questions, clusters.",
        },
        "myrsikb": {
            ".": "Integration project root. Memory bridge package plus concat/analysis scripts.",
            "memory_bridge": "The RSIS3 ↔ mykb integration layer. Standalone Python package that lets RSIS3 treat mykb as its semantic memory, knowledge graph, temporal memory, and gap detector. MemoryClient is the single-entry facade.",
        },
    }
    
    if proj_name in descs and directory in descs[proj_name]:
        return descs[proj_name][directory]
    
    # Auto-generate
    exts = defaultdict(int)
    for n in names:
        e = Path(n).suffix.lower()
        exts[e] += 1
    ext_desc = ", ".join(f"{ext}: {count}" for ext, count in sorted(exts.items(), key=lambda x: -x[1]))
    return f"Contains {len(files)} file(s) — {ext_desc}."

if __name__ == "__main__":
    write_inventory()
