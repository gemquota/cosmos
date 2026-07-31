import { describe, it, expect } from 'vitest';
import {
  resolveTemplate,
  resolveDocument,
  resolveContextLines,
  isResolved,
  getUnresolvedKeys,
} from '../../src/template/resolver.js';
import { extractTemplateVars, hasTemplateVars } from '../../src/template/patterns.js';
import type { ArtifactDictionary } from '../../src/types/index.js';

const ARTIFACTS: ArtifactDictionary = {
  domain: {
    value: 'Machine learning',
    source_question_id: '1.1.1',
    source_series_id: 1,
    confidence: 0.9,
    last_updated: '',
  },
  audience_level: {
    value: 'Practitioners',
    source_question_id: '1.1.2',
    source_series_id: 1,
    confidence: 0.8,
    last_updated: '',
  },
  nested: {
    value: 'For {domain} practitioners',
    source_question_id: '1.1.3',
    source_series_id: 1,
    confidence: 0.7,
    last_updated: '',
  },
};

describe('Template Patterns', () => {
  it('extracts template variables from text', () => {
    const keys = extractTemplateVars('This is for {domain} at {audience_level} level');
    expect(keys).toEqual(['domain', 'audience_level']);
  });

  it('returns empty array for text with no vars', () => {
    expect(extractTemplateVars('No vars here')).toEqual([]);
  });

  it('deduplicates keys', () => {
    const keys = extractTemplateVars('{domain} and {domain}');
    expect(keys).toEqual(['domain']);
  });

  it('hasTemplateVars detects variables', () => {
    expect(hasTemplateVars('Hello {domain}')).toBe(true);
    expect(hasTemplateVars('Hello world')).toBe(false);
  });
});

describe('Template Resolver', () => {
  it('resolves known artifact keys', () => {
    const result = resolveTemplate('Working in {domain}', ARTIFACTS);
    expect(result).toBe('Working in Machine learning');
  });

  it('shows placeholder for unknown keys', () => {
    const result = resolveTemplate('Working in {unknown_key}', ARTIFACTS);
    expect(result).toBe('Working in [Not yet determined: unknown_key]');
  });

  it('handles mixed resolved and unresolved', () => {
    const result = resolveTemplate('{domain} for {audience_level} at {unknown}', ARTIFACTS);
    expect(result).toBe('Machine learning for Practitioners at [Not yet determined: unknown]');
  });

  it('resolves nested template variables', () => {
    const result = resolveTemplate('{nested}', ARTIFACTS);
    expect(result).toBe('For Machine learning practitioners');
  });

  it('handles no template variables', () => {
    const result = resolveTemplate('Plain text', ARTIFACTS);
    expect(result).toBe('Plain text');
  });

  it('handles object artifact values', () => {
    const artifacts: ArtifactDictionary = {
      config: {
        value: { lang: 'ts', target: 'es2022' },
        source_question_id: '5.1.1',
        source_series_id: 5,
        confidence: 0.8,
        last_updated: '',
      },
    };
    const result = resolveTemplate('{config}', artifacts);
    expect(result).toContain('ts');
    expect(result).toContain('es2022');
  });
});

describe('Document Resolver', () => {
  it('resolves across multiple lines', () => {
    const doc = `# Spec\n\nDomain: {domain}\nAudience: {audience_level}`;
    const result = resolveDocument(doc, ARTIFACTS);
    expect(result).toBe('# Spec\n\nDomain: Machine learning\nAudience: Practitioners');
  });
});

describe('Context Lines Resolver', () => {
  it('resolves context lines from MD files', () => {
    const lines = [
      '> Context: This specification is for the {domain} domain.',
      '> Target audience: {audience_level}',
      '> No variables here',
    ];
    const result = resolveContextLines(lines, ARTIFACTS);
    expect(result[0]).toBe('> Context: This specification is for the Machine learning domain.');
    expect(result[1]).toBe('> Target audience: Practitioners');
    expect(result[2]).toBe('> No variables here');
  });
});

describe('isResolved', () => {
  it('returns true for resolved keys', () => {
    expect(isResolved('domain', ARTIFACTS)).toBe(true);
  });

  it('returns false for unresolved keys', () => {
    expect(isResolved('missing_key', ARTIFACTS)).toBe(false);
  });
});

describe('getUnresolvedKeys', () => {
  it('returns only unresolved keys', () => {
    const unresolved = getUnresolvedKeys('{domain} and {missing1} and {audience_level} and {missing2}', ARTIFACTS);
    expect(unresolved).toEqual(['missing1', 'missing2']);
  });

  it('returns empty for fully resolved text', () => {
    const unresolved = getUnresolvedKeys('{domain} and {audience_level}', ARTIFACTS);
    expect(unresolved).toEqual([]);
  });
});
