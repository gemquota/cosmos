#!/usr/bin/env bash
# Consolidate answers from all 7 series into a final specification artifact.
# Usage: ./consolidate-spec.sh <answers-dir> <output-dir>
# Fixed: proper JSON merging (original had broken concatenation)

set -euo pipefail

ANSWERS_DIR="${1:-./answers}"
OUTPUT_DIR="${2:-./specification}"

mkdir -p "$OUTPUT_DIR"

echo "Consolidating specification from $ANSWERS_DIR..."

cp -r "$ANSWERS_DIR" "$OUTPUT_DIR/answers" 2>/dev/null || true

# Generate summary
cat > "$OUTPUT_DIR/SUMMARY.md" << 'EOF'
# Specification Summary

Generated from the SPACE — Structured Prompt Creation Framework.

## Series Completed
EOF

for series_dir in "$ANSWERS_DIR"/*/; do
    [ -d "$series_dir" ] || continue
    series_name=$(basename "$series_dir")
    echo "- $series_name" >> "$OUTPUT_DIR/SUMMARY.md"
done

cat >> "$OUTPUT_DIR/SUMMARY.md" << 'EOF'

## Key Artifacts
EOF

# Build decisions dictionary using proper JSON merge (python3)
python3 -c "
import json, glob, os, sys

artifacts = {}
answers_dir = sys.argv[1]
output_dir = sys.argv[2]

for series_json in sorted(glob.glob(os.path.join(answers_dir, '*/series-answers.json'))):
    try:
        with open(series_json) as f:
            data = json.load(f)
        if isinstance(data, dict):
            artifacts.update(data)
    except (json.JSONDecodeError, IOError) as e:
        print(f'Warning: skipping {series_json}: {e}', file=sys.stderr)

# Write valid merged JSON
with open(os.path.join(output_dir, 'decisions.json'), 'w') as f:
    json.dump(artifacts, f, indent=2)

# Write artifact dictionary
with open(os.path.join(output_dir, 'artifact-dictionary.json'), 'w') as f:
    json.dump(artifacts, f, indent=2)

print(f'Artifact dictionary written with {len(artifacts)} entries.')
" "$ANSWERS_DIR" "$OUTPUT_DIR"

echo ""
echo "Done! Specification consolidated at: $OUTPUT_DIR"
