#!/usr/bin/env python3
"""Static Knowledge Base Linter (Epic 4)
Scans all .md files for broken [[wikilinks]], orphan notes, and integrity issues.

Usage:
  python3 .wiki-daemon/kb_linter.py           # full scan, print report
  python3 .wiki-daemon/kb_linter.py --json     # JSON output for API
  python3 .wiki-daemon/kb_linter.py --fix      # auto-fix: add orphan header
  python3 .wiki-daemon/kb_linter.py --watch    # one-shot scan (for pre-commit hook style)
"""
import os, re, sys, json
from collections import defaultdict

BUNDLE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def find_all_md_files(base):
    """Return set of all .md file paths relative to base."""
    files = set()
    for root, dirs, fns in os.walk(base):
        # Skip hidden dirs and non-content dirs
        skip = {'.git', '__pycache__', 'node_modules', '.okf-skill', '.obsidian'}
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith('.')]
        for fn in fns:
            if fn.endswith('.md'):
                rel = os.path.relpath(os.path.join(root, fn), base)
                files.add(rel)
    return files

def extract_wikilinks(text):
    """Extract all [[wikilink]] targets from text. Returns set of filenames."""
    links = set()
    # [[target|label]] or [[target]]
    for m in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', text):
        target = m.group(1).strip()
        # Normalize: remove leading ./ or /
        if target.startswith('./'):
            target = target[2:]
        if target.startswith('/'):
            target = target[1:]
        # Add .md if missing
        if not target.endswith('.md'):
            target += '.md'
        links.add(target)
    return links

def extract_tags(text):
    """Extract all #tags from text (but not ## headings or ###)."""
    tags = set()
    for m in re.finditer(r'(?<!\w)#([a-zA-Z][a-zA-Z0-9_/-]*)', text):
        tag = m.group(1)
        tags.add(tag)
    return tags

def lint(return_json=False):
    """Run linter and return report dict or print to stdout."""
    md_files = find_all_md_files(BUNDLE)
    
    # Build: file → wikilinks, file → tags, file → backlinks
    file_links = {}       # file -> set of wikilinks
    file_tags = {}        # file -> set of tags
    backlinks = defaultdict(set)  # target -> set of files that link to it
    
    for f in md_files:
        path = os.path.join(BUNDLE, f)
        try:
            with open(path, encoding='utf-8', errors='replace') as fh:
                text = fh.read()
        except:
            continue
        
        links = extract_wikilinks(text)
        file_links[f] = links
        file_tags[f] = extract_tags(text)
        
        for target in links:
            backlinks[target].add(f)
    
    # ── Broken links ──
    broken = {}
    for f, links in file_links.items():
        bad = []
        for target in links:
            # Resolve relative wikilinks
            # If the target contains a /, try relative to the linking file's dir
            if '/' in target:
                # Try as-is first (relative to root)
                if target in md_files:
                    continue
                # Try relative to the linking file's directory
                link_dir = os.path.dirname(f)
                resolved = os.path.normpath(os.path.join(link_dir, target))
                if resolved in md_files:
                    continue
                bad.append(target)
            else:
                # Simple name — could be anywhere
                # Search all files for a match
                found = False
                for mf in md_files:
                    if os.path.basename(mf) == target or mf == target:
                        found = True
                        break
                if not found:
                    bad.append(target)
        
        if bad:
            broken[f] = bad
    
    # ── Orphan detection ──
    orphans = []
    for f in md_files:
        # Root files like index.md, Home.md, README.md are not orphans
        basename = os.path.basename(f)
        if basename in ('index.md', 'README.md', 'Home.md', 'AGENTS.md', 'log.md'):
            continue
        # Check if any other file links to this one
        linked_from = backlinks.get(f, set())
        # Also check if the file links to itself (ignore self-refs)
        linked_from = {lf for lf in linked_from if lf != f}
        if not linked_from:
            orphans.append(f)
    
    # ── Stats ──
    total_links = sum(len(v) for v in file_links.values())
    total_broken = sum(len(v) for v in broken.values())
    
    report = {
        'status': 'ok' if not broken else 'issues_found',
        'summary': {
            'total_files': len(md_files),
            'total_links': total_links,
            'broken_links': total_broken,
            'orphan_notes': len(orphans),
            'files_with_broken_links': len(broken),
        },
        'broken_links': {f: sorted(b) for f, b in sorted(broken.items())},
        'orphans': sorted(orphans),
        'tags': {},
    }
    
    # Top tags
    all_tags = defaultdict(int)
    for tags in file_tags.values():
        for t in tags:
            all_tags[t] += 1
    report['tags'] = dict(sorted(all_tags.items(), key=lambda x: -x[1])[:30])
    
    if return_json:
        return report
    
    # Pretty print
    print(f"\n{'='*50}")
    print(f"  KB Linter Report — {len(md_files)} files scanned")
    print(f"{'='*50}")
    print(f"  Total [[wikilinks]]: {total_links}")
    print(f"  Broken links:       {total_broken}")
    print(f"  Orphan notes:       {len(orphans)}")
    print(f"  Files with issues:  {len(broken)}")
    print()
    
    if broken:
        print(f"  ── Broken [[wikilinks]] ──")
        for f, links in sorted(broken.items())[:10]:
            print(f"    {f}:")
            for l in links[:5]:
                print(f"      → {l}")
        if len(broken) > 10:
            print(f"    ... and {len(broken) - 10} more files")
        print()
    
    if orphans:
        print(f"  ── Orphan Notes (0 inbound links) ──")
        for f in orphans[:15]:
            print(f"    {f}")
        if len(orphans) > 15:
            print(f"    ... and {len(orphans) - 15} more")
        print()
    
    if not broken and not orphans:
        print("  ✓ No issues found — all links valid, no orphans.")
    
    return report

if __name__ == '__main__':
    if '--json' in sys.argv:
        report = lint(return_json=True)
        print(json.dumps(report, indent=2))
    elif '--fix' in sys.argv:
        report = lint(return_json=True)
        # Auto-fix: add orphan note header to orphan files
        for f in report['orphans'][:5]:  # Limit to 5 to avoid overwhelm
            path = os.path.join(BUNDLE, f)
            with open(path) as fh:
                content = fh.read()
            if not content.startswith('---'):
                # Add orphan marker in frontmatter
                content = f"---\nstatus: orphan\n---\n\n{content}"
                with open(path, 'w') as fh:
                    fh.write(content)
                print(f"  Marked orphan: {f}")
        print(f"  Fixed {min(len(report['orphans']), 5)} orphans")
    else:
        lint(return_json=False)
