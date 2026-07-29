#!/usr/bin/env bash
# Consolidate answers from all 7 series into a final specification artifact.
# Usage: ./consolidate-spec.sh <answers-dir> <output-dir>

set -euo pipefail

ANSWERS_DIR="${1:-./answers}"
OUTPUT_DIR="${2:-./specification}"

mkdir -p "$OUTPUT_DIR"

echo "Consolidating specification from $ANSWERS_DIR..."

cp -r "$ANSWERS_DIR" "$OUTPUT_DIR/answers" 2>/dev/null || true

# Generate summary
cat > "$OUTPUT_DIR/SUMMARY.md" << 'EOF'
# Specification Summary

Generated from the Structured Prompt Creation Framework.

## Series Completed
EOF

for series_dir in "$ANSWERS_DIR"/*/; do
    series_name=$(basename "$series_dir")
    echo "- $series_name" >> "$OUTPUT_DIR/SUMMARY.md"
done

cat >> "$OUTPUT_DIR/SUMMARY.md" << 'EOF'

## Key Artifacts
EOF

# Build decisions dictionary
echo "{" > "$OUTPUT_DIR/decisions.json"
first=true
for series_json in "$ANSWERS_DIR"/*/series-answers.json; do
    [ -f "$series_json" ] || continue
    [ "$first" = false ] && echo "," >> "$OUTPUT_DIR/decisions.json"
    first=false
    cat "$series_json" >> "$OUTPUT_DIR/decisions.json"
done
echo "}" >> "$OUTPUT_DIR/decisions.json"

# Generate artifact dictionary
python3 -c "
import json
artifacts = {}
try:
    with open('$OUTPUT_DIR/decisions.json') as f:
        artifacts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    pass
with open('$OUTPUT_DIR/artifact-dictionary.json', 'w') as f:
    json.dump(artifacts, f, indent=2)
print(f'Artifact dictionary written with {len(artifacts)} entries.')
"

echo ""
echo "Done! Specification consolidated at: $OUTPUT_DIR"
