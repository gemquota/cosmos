#!/usr/bin/env python3
"""Immutable AI Evaluator — separate process, read-only.

This process is loaded from a read-only filesystem mount and is never
in-scope for self-improvement. It evaluates candidate improvements
submitted by the L2 Improvement Engine.

The gate is deterministic and stdlib-only: it validates the candidate
shape, checks target paths, compiles the code, scans the AST for unsafe
patterns, and scores style/efficiency/regression heuristics. When an API
key is configured an LLM refinement pass runs on top, but the
deterministic hard gates always fail closed — an LLM can never overturn a
hard FAIL.

Usage:
    echo '{"candidate": "..."}' | python evaluator.py

Startup:
    python evaluator.py --verify <expected_sha256>
"""

import ast
import hashlib
import json
import os
import re
import sys
import textwrap
from pathlib import PurePath


SYSTEM_PROMPT_FILE = os.path.join(os.path.dirname(__file__), "prompt.txt")

# Score keys expected by the L2 loop and telemetry.
SCORE_KEYS = ("correctness", "safety", "efficiency", "style", "regression")

# Calls that are never acceptable in an unattended quality gate: dynamic
# code execution, destructive filesystem operations, unsafe deserialization,
# and interactive/credential access that would hang or exfiltrate.
_UNSAFE_ATTR_CALLS = {
    "os.system", "os.popen",
    "os.spawnl", "os.spawnle", "os.spawnlp", "os.spawnlpe",
    "os.spawnv", "os.spawnve", "os.spawnvp", "os.spawnvpe",
    "os.fork", "os.forkpty",
    "os.execl", "os.execle", "os.execlp", "os.execlpe",
    "os.execv", "os.execve", "os.execvp", "os.execvpe",
    "os.remove", "os.unlink", "os.rmdir", "os.removedirs",
    "shutil.rmtree", "shutil.rmdir",
    "pickle.load", "pickle.loads", "shelve.open",
    "getpass.getpass", "getpass.getuser",
}
_UNSAFE_NAME_CALLS = {"eval", "exec", "compile", "input"}
_SUBPROCESS_CALLS = {
    "subprocess.run", "subprocess.call", "subprocess.check_call",
    "subprocess.check_output", "subprocess.Popen",
    "subprocess.getoutput", "subprocess.getstatusoutput",
}
_DESTRUCTIVE_BINS = {"rm", "del", "mkfs", "dd", "shutdown", "format",
                     "killall", "pkill", "fuser"}
_DESTRUCTIVE_TOKENS = ("rm -rf", "rm -fr", "del /f", "del /q",
                       "format c:", "mkfs.", "dd if=", "> /dev/sd")
_STYLE_MARKERS = ("todo", "fixme", "xxx", "placeholder", "hack")
_WINDOWS_DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")
_DIFF_HEADER_RE = re.compile(r"^(\+\+\+|---) ([^\t]+)")


def load_system_prompt() -> str:
    """Load the immutable system prompt from the sidecar file."""
    with open(SYSTEM_PROMPT_FILE) as f:
        return f.read()


def self_verify(expected_digest: str) -> bool:
    """Verify our own binary digest at startup."""
    with open(__file__, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    ok = actual == expected_digest
    if not ok:
        print(json.dumps({
            "error": "DIGEST_MISMATCH",
            "expected": expected_digest[:16],
            "actual": actual[:16],
        }), file=sys.stderr)
    return ok


# ── deterministic gate ────────────────────────────────────────────── #

def _check_paths(target_files: list) -> list[str]:
    """Validate that every target path stays inside the workspace."""
    problems: list[str] = []
    for f in target_files:
        if not isinstance(f, str) or not f.strip():
            problems.append("target file entry is empty or not a string")
            continue
        if _WINDOWS_DRIVE_RE.match(f) or "\\" in f:
            problems.append(f"target path uses absolute/Windows form: {f!r}")
            continue
        parts = PurePath(f).parts
        if PurePath(f).is_absolute():
            problems.append(f"absolute target path: {f!r}")
        elif ".." in parts:
            problems.append(f"target path escapes workspace: {f!r}")
    return problems


def _extract_code(candidate: dict):
    """Return ``(code, is_diff, deleted, touched, removed_defs)``.

    ``diff`` may be raw module content or a unified diff. Unified diffs are
    reduced to their added lines so correctness/safety checks run against
    the code the candidate actually introduces.
    """
    raw = candidate.get("diff") or candidate.get("diff_or_code") or ""
    if not isinstance(raw, str) or not raw.strip():
        return "", False, 0, [], []

    lines = raw.splitlines()
    is_diff = any(l.startswith("+++ ") for l in lines) and any(
        l.startswith("@@") for l in lines)
    if not is_diff:
        return raw, False, 0, [], []

    added: list[str] = []
    removed_defs: list[str] = []
    touched: list[str] = []
    deleted = 0
    for line in lines:
        m = _DIFF_HEADER_RE.match(line)
        if m:
            path = m.group(2)
            if path.startswith("a/") or path.startswith("b/"):
                path = path[2:]
            if path != "/dev/null":
                touched.append(path)
        elif line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            deleted += 1
            stripped = line[1:].lstrip()
            if stripped.startswith(("def ", "class ", "import ", "from ")):
                removed_defs.append(stripped)
        elif line.startswith("deleted file mode"):
            removed_defs.append("deleted file mode")
    return "\n".join(added), True, deleted, touched, removed_defs


def _check_syntax(code: str, is_diff: bool = False) -> list[str]:
    """Return syntax errors (hard correctness gate).

    For unified diffs the added lines are fragments of an enclosing block;
    the common indent is stripped before re-checking so a valid partial
    diff never false-positives on indentation.
    """
    try:
        compile(code, "<candidate>", "exec")
    except IndentationError as e:
        if not is_diff:
            return [f"indentation error at line {e.lineno}: {e.msg}"]
        try:
            compile(textwrap.dedent(code), "<candidate>", "exec")
        except SyntaxError as e2:
            return [f"syntax error at line {e2.lineno}: {e2.msg}"]
        return []
    except SyntaxError as e:
        return [f"syntax error at line {e.lineno}: {e.msg}"]
    return []


def _parse_ast(code: str):
    """Parse candidate code, retrying after dedent for diff fragments.

    Added lines of a unified diff are fragments of an enclosing block;
    dedent makes them parseable so the safety/efficiency scans still apply.
    Returns ``None`` when neither attempt parses (the correctness gate
    reports the syntax error).
    """
    try:
        return ast.parse(code)
    except SyntaxError:
        try:
            return ast.parse(textwrap.dedent(code))
        except SyntaxError:
            return None


def _subprocess_literals(call_node: ast.Call) -> list[str]:
    """Collect literal command tokens from a subprocess call."""
    literals: list[str] = []
    for arg in call_node.args:
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            literals.append(arg.value)
        elif isinstance(arg, (ast.List, ast.Tuple)):
            for elt in arg.elts:
                if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                    literals.append(elt.value)
    return literals


def _scan_unsafe(code: str) -> list[str]:
    """Return safety violations found in the candidate code."""
    tree = _parse_ast(code)
    if tree is None:
        return []  # correctness gate already reports the syntax error

    violations: list[str] = []

    def dotted_name(node) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            base = dotted_name(node.value)
            return f"{base}.{node.attr}" if base else node.attr
        return ""

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = dotted_name(node.func)
            loc = f"line {node.lineno}"
            if name in _UNSAFE_ATTR_CALLS or (
                    name in _UNSAFE_NAME_CALLS and isinstance(node.func, ast.Name)):
                violations.append(f"{name}() at {loc} — unsafe call")
            elif name in _SUBPROCESS_CALLS:
                shell = any(
                    isinstance(kw.arg, str) and kw.arg == "shell"
                    and isinstance(kw.value, ast.Constant)
                    and kw.value.value is True
                    for kw in node.keywords)
                literals = _subprocess_literals(node)
                joined = " ".join(literals).lower()
                if shell:
                    violations.append(f"{name}(shell=True) at {loc}")
                elif any(bin_ in joined.split() for bin_ in _DESTRUCTIVE_BINS) or \
                        any(tok in joined for tok in _DESTRUCTIVE_TOKENS):
                    violations.append(
                        f"{name}(...) destructive command at {loc}")
            elif name == "open" and isinstance(node.func, ast.Name):
                mode = ""
                path = ""
                if node.args:
                    first = node.args[0]
                    if isinstance(first, ast.Constant) and isinstance(first.value, str):
                        path = first.value
                    if len(node.args) >= 2:
                        second = node.args[1]
                        if (isinstance(second, ast.Constant)
                                and isinstance(second.value, str)):
                            mode = second.value
                for kw in node.keywords:
                    if kw.arg == "file" and isinstance(kw.value, ast.Constant):
                        path = str(kw.value.value)
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                writes = any(c in mode for c in "wax+")
                outside = path.startswith(("/", "~")) or ".." in path or \
                    _WINDOWS_DRIVE_RE.match(path)
                if writes and outside:
                    violations.append(
                        f"open({path!r}, mode={mode!r}) at {loc} — "
                        "writes outside workspace")

    # Destructive shell strings hidden in constants (e.g. subprocess args).
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            lowered = node.value.lower()
            if any(tok in lowered for tok in _DESTRUCTIVE_TOKENS):
                violations.append(
                    f"destructive shell string at line {node.lineno}")
    return violations


def _check_regression(is_diff: bool, deleted: int, removed_defs: list,
                      touched: list, target_files: list):
    """Score regression risk; whole-file/definition removals fail closed."""
    if not is_diff:
        return [], 1.0, []
    problems: list[str] = []
    notes: list[str] = []
    score = 1.0
    if removed_defs:
        problems.append("removes existing code: " +
                        "; ".join(removed_defs[:3]))
        score = 0.0
    elif deleted:
        notes.append(f"removes {deleted} line(s)")
        score = 0.8
    if touched and target_files:
        out = [t for t in touched if t not in target_files]
        if out:
            notes.append("diff touches files outside target_files: " +
                         ", ".join(out[:3]))
            score = min(score, 0.9)
    return problems, score, notes


def _style_check(code: str):
    """Heuristic style score (0.0–1.0) and notes."""
    notes: list[str] = []
    score = 1.0
    for i, line in enumerate(code.splitlines(), 1):
        if len(line) > 100:
            notes.append(f"line {i} exceeds 100 chars")
            score = min(score, 0.9)
        if line.rstrip() != line:
            notes.append(f"line {i} has trailing whitespace")
            score = min(score, 0.95)
    lowered = code.lower()
    for marker in _STYLE_MARKERS:
        if marker in lowered:
            notes.append(f"contains '{marker}' marker")
            score = min(score, 0.85)
    if "notimplementederror" in lowered:
        notes.append("unimplemented body (NotImplementedError)")
        score = min(score, 0.8)
    if re.search(r"^\s*(pass|\.\.\.)\s*$", code, re.M):
        notes.append("contains bare pass/... no-op")
        score = min(score, 0.85)
    return score, notes


def _efficiency_check(code: str):
    """Heuristic efficiency score (0.0–1.0) and notes."""
    notes: list[str] = []
    score = 1.0
    if not code.strip():
        return score, notes
    tree = _parse_ast(code)
    if tree is None:
        return score, notes
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        body = [n for n in node.body if not isinstance(n, ast.Expr)
                or not isinstance(n.value, ast.Constant)
                or not isinstance(n.value.value, str)]
        def is_none_return(n: ast.stmt) -> bool:
            if not isinstance(n, ast.Return):
                return False
            if n.value is None:
                return True
            return (isinstance(n.value, ast.Constant)
                    and n.value.value is None)

        has_return_none = any(is_none_return(n) for n in body)
        if has_return_none and len(body) == 1:
            notes.append(f"{node.name}() is a no-op (returns None)")
            score = min(score, 0.85)
        args = node.args
        if (args.vararg or args.kwarg) and node.body:
            notes.append(f"{node.name}() uses a catch-all signature")
            score = min(score, 0.9)
    return score, notes


def _merge_llm(decision: str, scores: dict, llm_decision, llm_scores):
    """Merge an LLM verdict into the deterministic result (fail-closed).

    A hard deterministic FAIL is final: the LLM can add rationale and
    suggestions but never overturn the decision or inflate the scores.
    On a deterministic PASS the LLM may downgrade to FAIL or refine the
    sub-scores.
    """
    if decision == "FAIL":
        return decision, dict(scores)
    if llm_decision == "FAIL":
        decision = "FAIL"
    merged = dict(scores)
    if isinstance(llm_scores, dict):
        for key in SCORE_KEYS:
            value = llm_scores.get(key)
            if isinstance(value, (int, float)) and 0.0 <= value <= 1.0:
                merged[key] = float(value)
    return decision, merged


def _llm_evaluate(candidate: dict):
    """Optional AI refinement pass; returns None when not configured."""
    api_key = os.environ.get("RSIS_EVALUATOR_API_KEY") or \
        os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        import openai
    except ImportError:
        return None
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.environ.get("RSIS_EVALUATOR_MODEL", "gpt-4o-mini"),
            temperature=0,
            messages=[
                {"role": "system", "content": load_system_prompt()},
                {"role": "user", "content": json.dumps(candidate)},
            ],
        )
        data = json.loads(response.choices[0].message.content)
        return data if isinstance(data, dict) else None
    except Exception as e:
        print(json.dumps({"error": f"LLM_EVALUATION_FAILED: {e}"}),
              file=sys.stderr)
        return None


def _is_data_candidate(raw: str) -> bool:
    """True when the payload is a JSON document rather than Python code.

    Tuning loops (L8/L9) gate JSON delta documents through the evaluator;
    those are config data, not code, so the Python gates do not apply.
    """
    try:
        parsed = json.loads(raw)
    except ValueError:
        return False
    return isinstance(parsed, (dict, list))


def _scan_data_strings(raw: str) -> list[str]:
    """Scan JSON/config payloads for destructive shell strings."""
    lowered = raw.lower()
    return [f"destructive shell string in candidate data: {tok!r}"
            for tok in _DESTRUCTIVE_TOKENS if tok in lowered]


def evaluate(candidate: dict) -> dict:
    """Evaluate a candidate improvement against the deterministic gate."""
    failures: list[str] = []
    notes: list[str] = []
    suggestions: list[str] = []
    scores = {key: 1.0 for key in SCORE_KEYS}

    if not isinstance(candidate, dict):
        return {
            "decision": "FAIL",
            "scores": scores,
            "rationale": "Candidate must be a JSON object.",
            "suggestions": ["Submit a JSON object with description, "
                            "target_files, and diff."],
        }

    target_files = candidate.get("target_files")
    if not isinstance(target_files, list) or not target_files:
        failures.append("no target_files declared")
        target_files = []
    failures.extend(_check_paths(target_files))

    raw = candidate.get("diff") or candidate.get("diff_or_code") or ""
    if not isinstance(raw, str) or not raw.strip():
        failures.append("no code or diff provided")
    elif _is_data_candidate(raw):
        # Config/data candidates (L8/L9 tuning deltas) are JSON documents,
        # not Python: shape + destructive-string checks only.
        notes.append("config/data candidate (JSON) \u2014 Python gates skipped")
        data_problems = _scan_data_strings(raw)
        if data_problems:
            failures.extend(data_problems)        # safety hard gate
            scores["safety"] = 0.0
    else:
        code, is_diff, deleted, touched, removed_defs = _extract_code(candidate)
        if not code.strip():
            if is_diff:
                failures.append("diff contains no added lines")
            else:
                failures.append("no code or diff provided")
        else:
            syntax_problems = _check_syntax(code, is_diff=is_diff)
            if syntax_problems:
                failures.extend(syntax_problems)  # correctness hard gate
                scores["correctness"] = 0.0
            elif is_diff:
                scores["correctness"] = 1.0
            safety_problems = _scan_unsafe(code)
            if safety_problems:
                failures.extend(safety_problems)  # safety hard gate
                scores["safety"] = 0.0
            style_score, style_notes = _style_check(code)
            eff_score, eff_notes = _efficiency_check(code)
            scores["style"] = style_score
            scores["efficiency"] = eff_score
            notes.extend(style_notes + eff_notes)

        reg_problems, reg_score, reg_notes = _check_regression(
            is_diff, deleted, removed_defs, touched, target_files)
        failures.extend(reg_problems)             # regression hard gate
        scores["regression"] = reg_score
        notes.extend(reg_notes)

    suggestions = [n for n in dict.fromkeys(notes)
                   if not n.startswith("config/data candidate")][:4]
    if failures:
        decision = "FAIL"
        rationale = (f"{len(failures)} hard gate failure(s): "
                     + "; ".join(failures[:3]))
        if len(failures) > 3:
            rationale += "; …"
    else:
        decision = "PASS"
        if raw.strip() and _is_data_candidate(raw):
            rationale = ("Deterministic gate passed: paths safe, payload is "
                         "valid JSON/config, no unsafe patterns.")
        else:
            rationale = ("Deterministic gate passed: paths safe, code compiles, "
                         "no unsafe patterns, no regressions.")
        if notes:
            rationale += " Notes: " + "; ".join(notes[:3])

    # Optional LLM refinement — deterministic hard gates fail closed.
    llm = _llm_evaluate(candidate)
    if llm:
        decision, scores = _merge_llm(
            decision, scores, llm.get("decision"), llm.get("scores"))
        if llm.get("rationale"):
            rationale += f" | LLM: {llm['rationale']}"
        for s in llm.get("suggestions") or []:
            if isinstance(s, str) and s not in suggestions:
                suggestions.append(s)

    return {
        "decision": decision,
        "scores": {key: max(0.0, min(1.0, float(scores.get(key, 1.0))))
                   for key in SCORE_KEYS},
        "rationale": rationale,
        "suggestions": suggestions[:5],
    }


def main() -> None:
    args = sys.argv[1:]

    # Optional self-verification on startup
    if "--verify" in args:
        idx = args.index("--verify")
        expected = args[idx + 1]
        if not self_verify(expected):
            sys.exit(1)

    # Read candidate from stdin
    try:
        raw = sys.stdin.read()
        candidate = json.loads(raw)
    except (json.JSONDecodeError, EOFError) as e:
        print(json.dumps({"error": f"INVALID_INPUT: {e}"}), file=sys.stderr)
        sys.exit(1)

    # Evaluate
    result = evaluate(candidate)

    # Output result
    print(json.dumps(result))


if __name__ == "__main__":
    main()
