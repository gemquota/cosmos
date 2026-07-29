import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { existsSync, rmSync, mkdirSync, writeFileSync, readFileSync } from 'fs';
import { join } from 'path';
import { execSync } from 'child_process';

const TEST_DIR = '/data/data/com.termux/files/home/dev/space/.test-consolidate-' + Date.now();
const SCRIPT = '/data/data/com.termux/files/home/dev/space/scripts/consolidate-spec.mjs';

describe('Consolidation Script', () => {
  const inputDir = join(TEST_DIR, 'answers');
  const outputDir = join(TEST_DIR, 'output');

  beforeEach(() => {
    mkdirSync(join(inputDir, 'series-1'), { recursive: true });
    mkdirSync(join(inputDir, 'series-2'), { recursive: true });
    writeFileSync(
      join(inputDir, 'series-1', 'series-answers.json'),
      JSON.stringify(
        {
          '1.1.1': { text: 'Machine learning', choice: 'Single domain' },
          '1.1.2': { text: 'Practitioners', choice: 'Professionals' },
        },
        null,
        2,
      ),
    );
    writeFileSync(
      join(inputDir, 'series-2', 'series-answers.json'),
      JSON.stringify(
        {
          '2.1.1': { text: 'Entities', choice: 'Core entities' },
        },
        null,
        2,
      ),
    );
  });

  afterEach(() => {
    if (existsSync(TEST_DIR)) rmSync(TEST_DIR, { recursive: true });
  });

  it('produces valid JSON output', () => {
    execSync(`node ${SCRIPT} "${inputDir}" "${outputDir}"`, { encoding: 'utf-8' });

    expect(existsSync(join(outputDir, 'decisions.json'))).toBe(true);
    expect(existsSync(join(outputDir, 'artifact-dictionary.json'))).toBe(true);
    expect(existsSync(join(outputDir, 'SUMMARY.md'))).toBe(true);

    const decisions = JSON.parse(readFileSync(join(outputDir, 'decisions.json'), 'utf-8'));
    expect(decisions['1.1.1']).toBeDefined();
    expect(decisions['1.1.1'].text).toBe('Machine learning');
    expect(decisions['2.1.1']).toBeDefined();
  });

  it('handles malformed JSON gracefully', () => {
    mkdirSync(join(inputDir, 'series-3'), { recursive: true });
    writeFileSync(join(inputDir, 'series-3', 'series-answers.json'), 'not json at all');

    execSync(`node ${SCRIPT} "${inputDir}" "${outputDir}"`, { encoding: 'utf-8' });
    expect(existsSync(join(outputDir, 'decisions.json'))).toBe(true);
  });

  it('handles empty answers directory', () => {
    rmSync(inputDir, { recursive: true });
    mkdirSync(inputDir, { recursive: true });

    execSync(`node ${SCRIPT} "${inputDir}" "${outputDir}"`, { encoding: 'utf-8' });
    const decisions = JSON.parse(readFileSync(join(outputDir, 'decisions.json'), 'utf-8'));
    expect(Object.keys(decisions)).toHaveLength(0);
  });
});
