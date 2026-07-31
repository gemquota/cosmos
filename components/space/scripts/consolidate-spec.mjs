#!/usr/bin/env node
/**
 * Consolidate answers from all 7 series into a final specification artifact.
 * Robust replacement for the broken consolidate-spec.sh.
 *
 * Usage: node scripts/consolidate-spec.mjs <answers-dir> <output-dir>
 */

import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'fs';
import { join } from 'path';

const ANSWERS_DIR = process.argv[2] || './answers';
const OUTPUT_DIR = process.argv[3] || './specification';

if (!existsSync(ANSWERS_DIR)) {
  console.error(`✗ Answers directory not found: ${ANSWERS_DIR}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });

console.log(`Consolidating specification from ${ANSWERS_DIR}...`);

const decisions = {};
const errors = [];
let totalEntries = 0;

const subdirs = readdirSync(ANSWERS_DIR, { withFileTypes: true })
  .filter(d => d.isDirectory())
  .map(d => d.name);

for (const dir of subdirs) {
  const jsonPath = join(ANSWERS_DIR, dir, 'series-answers.json');
  if (!existsSync(jsonPath)) {
    const dirPath = join(ANSWERS_DIR, dir);
    const jsonFiles = readdirSync(dirPath).filter(f => f.endsWith('.json'));
    for (const jf of jsonFiles) {
      try {
        const data = JSON.parse(readFileSync(join(dirPath, jf), 'utf-8'));
        if (typeof data === 'object' && data !== null) {
          Object.assign(decisions, data);
          totalEntries += Object.keys(data).length;
        }
      } catch (e) {
        errors.push(`${dir}/${jf}: ${e.message}`);
      }
    }
    continue;
  }

  try {
    const data = JSON.parse(readFileSync(jsonPath, 'utf-8'));
    if (typeof data === 'object' && data !== null) {
      Object.assign(decisions, data);
      totalEntries += Object.keys(data).length;
    }
  } catch (e) {
    errors.push(`${dir}/series-answers.json: ${e.message}`);
  }
}

writeFileSync(join(OUTPUT_DIR, 'decisions.json'), JSON.stringify(decisions, null, 2));
writeFileSync(join(OUTPUT_DIR, 'artifact-dictionary.json'), JSON.stringify(decisions, null, 2));

const summary = [
  '# Specification Summary',
  '',
  'Generated from the Structured Prompt Creation Framework.',
  '',
  '## Series Completed',
  ...subdirs.map(d => `- ${d}`),
  '',
  '## Key Artifacts',
  `Total entries: ${totalEntries}`,
  '',
  '## Errors',
  errors.length > 0 ? errors.map(e => `- ${e}`).join('\n') : 'None',
].join('\n');

writeFileSync(join(OUTPUT_DIR, 'SUMMARY.md'), summary);

console.log(`✓ decisions.json (${totalEntries} entries)`);
console.log(`✓ artifact-dictionary.json`);
console.log(`✓ SUMMARY.md`);
if (errors.length > 0) {
  console.warn(`⚠ ${errors.length} errors:`);
  errors.forEach(e => console.warn(`  - ${e}`));
}
console.log(`Done: ${OUTPUT_DIR}`);
