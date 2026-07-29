#!/usr/bin/env python3
"""Git-Backed Temporal History Engine (Epic 3)
Auto-commits file changes with standardized timestamps.
Provides "time-travel" file retrieval and audit-log APIs.

Usage:
  python3 .wiki-daemon/temporal_engine.py status        # show repo state
  python3 .wiki-daemon/temporal_engine.py commit <path>  # commit a specific file
  python3 .wiki-daemon/temporal_engine.py commit-all     # commit all changes
  python3 .wiki-daemon/temporal_engine.py history <path>  # show file history
  python3 .wiki-daemon/temporal_engine.py snapshot <path> <timestamp>  # get file at time
"""
import os, sys, json, shutil
from datetime import datetime, timezone

BUNDLE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    import git
except ImportError:
    print("GitPython required: pip install GitPython")
    sys.exit(1)

REPO_PATH = BUNDLE
COMMIT_AUTHOR = "mykb-daemon <daemon@mykb.local>"

def get_repo():
    try:
        repo = git.Repo(REPO_PATH)
        return repo
    except git.InvalidGitRepositoryError:
        print("Not a git repository. Run: git init")
        sys.exit(1)

def format_ts(dt=None):
    dt = dt or datetime.now(timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')

def parse_ts(ts_str):
    """Parse ISO 8601 or UNIX timestamp."""
    try:
        # Try UNIX timestamp (float)
        return datetime.fromtimestamp(float(ts_str), tz=timezone.utc)
    except (ValueError, TypeError):
        pass
    try:
        return datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
    except:
        return None

def cmd_status():
    repo = get_repo()
    if not repo.head.is_valid():
        print("Repo initialized — no commits yet")
        return
    
    print(f"Branch: {repo.active_branch.name}")
    print(f"Last commit: {repo.head.commit.hexsha[:12]} ({datetime.fromtimestamp(repo.head.commit.authored_date, tz=timezone.utc).isoformat()[:19]})")
    print(f"Files changed: {len([f for f in repo.index.diff(None)])} unstaged, {len(repo.index.diff('HEAD'))} staged")
    print(f"Untracked: {len(repo.untracked_files)}")

def cmd_commit(target_path=None):
    """Auto-commit a file or all changes."""
    repo = get_repo()
    ts = format_ts()
    author = git.Actor(*COMMIT_AUTHOR.split(' <'))
    
    if target_path == '--all' or target_path is None:
        # Stage all tracked changes + new files
        repo.index.add('*')
        # Don't commit if nothing to do
        if repo.is_dirty(untracked_files=True) or repo.untracked_files:
            repo.index.commit(f"auto-commit: {ts}", author=author, committer=author)
            print(f"Committed all changes at {ts}")
        else:
            print("Nothing to commit")
    else:
        # Resolve path
        abs_path = os.path.join(BUNDLE, target_path) if not os.path.isabs(target_path) else target_path
        if not os.path.exists(abs_path):
            print(f"File not found: {target_path}")
            return
        rel = os.path.relpath(abs_path, BUNDLE)
        repo.index.add([rel])
        repo.index.commit(f"auto-commit [{rel}]: {ts}", author=author, committer=author)
        print(f"Committed {rel} at {ts}")

def cmd_history(filepath):
    """Return commit history for a file as JSON."""
    repo = get_repo()
    abs_path = os.path.join(BUNDLE, filepath) if not os.path.isabs(filepath) else filepath
    rel = os.path.relpath(abs_path, BUNDLE)
    
    if not os.path.exists(abs_path):
        print(json.dumps({'error': f'File not found: {filepath}'}))
        return
    
    try:
        commits = []
        for c in repo.iter_commits(paths=rel):
            commits.append({
                'hash': c.hexsha[:12],
                'author': str(c.author),
                'date': datetime.fromtimestamp(c.committed_date, tz=timezone.utc).isoformat(),
                'message': c.message.strip(),
                'committed_date': c.committed_date,
            })
        print(json.dumps(commits, indent=2))
    except:
        print(json.dumps([]))

def cmd_snapshot(filepath, timestamp):
    """Get file content at a specific point in time."""
    repo = get_repo()
    abs_path = os.path.join(BUNDLE, filepath) if not os.path.isabs(filepath) else filepath
    rel = os.path.relpath(abs_path, BUNDLE)
    
    dt = parse_ts(timestamp)
    if not dt:
        print(json.dumps({'error': f'Invalid timestamp: {timestamp}'}))
        return
    
    try:
        # Find commit closest to the given timestamp
        target_ts = dt.timestamp()
        best_commit = None
        best_diff = float('inf')
        
        for c in repo.iter_commits(paths=rel):
            diff = abs(c.committed_date - target_ts)
            if diff < best_diff:
                best_diff = diff
                best_commit = c
        
        if not best_commit:
            print(json.dumps({'error': 'No commits found for this file'}))
            return
        
        # Get file content at that commit
        content = best_commit.tree[rel].data_stream.read().decode('utf-8', errors='replace')
        result = {
            'file': rel,
            'timestamp': timestamp,
            'restored_from': best_commit.hexsha[:12],
            'committed_at': datetime.fromtimestamp(best_commit.committed_date, tz=timezone.utc).isoformat(),
            'content': content,
            'size': len(content),
        }
        print(json.dumps(result, indent=2))
    except KeyError:
        print(json.dumps({'error': f'File {rel} not in commit history'}))
    except Exception as e:
        print(json.dumps({'error': str(e)}))

def cmd_diff(filepath=None):
    """Show diff for a file or all changes."""
    repo = get_repo()
    
    if filepath:
        abs_path = os.path.join(BUNDLE, filepath)
        rel = os.path.relpath(abs_path, BUNDLE)
        diff_text = repo.git.diff(rel)
    else:
        diff_text = repo.git.diff()
    
    if diff_text:
        print(diff_text)
    else:
        print("No differences")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == 'status':
        cmd_status()
    elif cmd == 'commit':
        target = sys.argv[2] if len(sys.argv) > 2 else '--all'
        cmd_commit(target)
    elif cmd == 'commit-all':
        cmd_commit('--all')
    elif cmd == 'history':
        if len(sys.argv) < 3:
            print("Usage: temporal_engine.py history <filepath>")
            sys.exit(1)
        cmd_history(sys.argv[2])
    elif cmd == 'snapshot':
        if len(sys.argv) < 4:
            print("Usage: temporal_engine.py snapshot <filepath> <timestamp>")
            sys.exit(1)
        cmd_snapshot(sys.argv[2], sys.argv[3])
    elif cmd == 'diff':
        target = sys.argv[2] if len(sys.argv) > 2 else None
        cmd_diff(target)
    else:
        print(f"Unknown command: {cmd}")
