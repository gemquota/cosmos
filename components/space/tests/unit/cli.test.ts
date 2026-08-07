import { describe, it, expect } from 'vitest';
import { configFromEnv, validateConfig, listEnvVars } from '../../src/config/validation.js';

describe('CLI Configuration', () => {
  it('configFromEnv returns default config', () => {
    const config = configFromEnv();
    expect(config.llm_provider).toBe('none');
    expect(config.locale).toBe('en');
    expect(config.projects_dir).toContain('.space');
  });

  it('validateConfig accepts valid config', () => {
    const result = validateConfig({ llm_provider: 'openai', llm_model: 'gpt-4o' });
    expect(result.valid).toBe(true);
  });

  it('validateConfig rejects invalid provider', () => {
    const result = validateConfig({ llm_provider: 'invalid-provider' as any });
    expect(result.valid).toBe(false);
    expect(result.errors.length).toBeGreaterThan(0);
  });

  it('validateConfig warns on missing API key', () => {
    const result = validateConfig({ llm_provider: 'openai', llm_api_key: '' });
    expect(result.warnings.length).toBeGreaterThanOrEqual(1);
  });

  it('validateConfig warns on extreme temperature', () => {
    const result = validateConfig({ llm_temperature: 10 });
    expect(result.warnings.length).toBeGreaterThanOrEqual(1);
  });

  it('listEnvVars returns all config fields', () => {
    const envVars = listEnvVars();
    expect(Object.keys(envVars).length).toBeGreaterThanOrEqual(10);
    expect(envVars.llm_provider).toBeDefined();
    expect(envVars.llm_api_key).toBeDefined();
    expect(envVars.locale).toBeDefined();
  });

  it('configFromEnv overrides from env', () => {
    process.env.SPACE_LLM_PROVIDER = 'anthropic';
    process.env.SPACE_LOCALE = 'es';
    const config = configFromEnv();
    expect(config.llm_provider).toBe('anthropic');
    expect(config.locale).toBe('es');
    delete process.env.SPACE_LLM_PROVIDER;
    delete process.env.SPACE_LOCALE;
  });
});

describe('SpaceInstance API', () => {
  it('createSpace returns valid instance', async () => {
    const { createSpace } = await import('../../src/engine/core.js');
    const space = createSpace();
    expect(space.config).toBeDefined();
    expect(space.framework).toBeDefined();
    expect(space.framework.series.length).toBe(7);
  });
});
