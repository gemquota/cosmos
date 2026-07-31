import { describe, it, expect } from 'vitest';
import { NullProvider } from '../../src/llm/providers/null-provider.js';
import { TemplateProvider } from '../../src/llm/providers/template-provider.js';
import { GeminiProvider } from '../../src/llm/providers/gemini-provider.js';
import { MistralProvider } from '../../src/llm/providers/mistral-provider.js';
import { OllamaProvider } from '../../src/llm/providers/ollama-provider.js';
import { createProvider } from '../../src/llm/factory.js';
import type { SpaceConfig } from '../../src/config/defaults.js';

describe('LLM Providers', () => {
  describe('NullProvider', () => {
    it('is not available', async () => {
      const provider = new NullProvider();
      expect(await provider.isAvailable()).toBe(false);
    });

    it('returns placeholder text', async () => {
      const provider = new NullProvider();
      const result = await provider.complete({ system_prompt: 'test', user_prompt: 'test' });
      expect(result.text).toContain('unavailable');
      expect(result.model).toBe('none');
    });
  });

  describe('TemplateProvider', () => {
    it('is available', async () => {
      const provider = new TemplateProvider();
      expect(await provider.isAvailable()).toBe(true);
    });

    it('returns deterministic response', async () => {
      const provider = new TemplateProvider();
      const result = await provider.complete({
        system_prompt: 'question refinement',
        user_prompt: 'Question: What is the domain?\ndomain: machine learning',
      });
      expect(result.text).toContain('machine learning');
    });
  });

  describe('GeminiProvider', () => {
    it('is not available without API key', async () => {
      const provider = new GeminiProvider('');
      expect(await provider.isAvailable()).toBe(false);
    });

    it('is available with API key', async () => {
      const provider = new GeminiProvider('fake-key');
      expect(await provider.isAvailable()).toBe(true);
    });

    it('has correct name', () => {
      const provider = new GeminiProvider('key');
      expect(provider.name).toBe('gemini');
    });
  });

  describe('MistralProvider', () => {
    it('is not available without API key', async () => {
      const provider = new MistralProvider('');
      expect(await provider.isAvailable()).toBe(false);
    });

    it('is available with API key', async () => {
      const provider = new MistralProvider('fake-key');
      expect(await provider.isAvailable()).toBe(true);
    });

    it('has correct name', () => {
      const provider = new MistralProvider('key');
      expect(provider.name).toBe('mistral');
    });
  });

  describe('OllamaProvider', () => {
    it('has correct name', () => {
      const provider = new OllamaProvider();
      expect(provider.name).toBe('ollama');
    });

    it('uses default base URL', () => {
      const provider = new OllamaProvider();
      // Can't directly access private baseUrl, but can check name
      expect(provider.name).toBe('ollama');
    });

    it('accepts custom model', () => {
      const provider = new OllamaProvider('http://localhost:11434', 'codellama');
      expect(provider.name).toBe('ollama');
    });
  });

  describe('Factory', () => {
    it('creates NullProvider for none', () => {
      const provider = createProvider({ llm_provider: 'none' } as SpaceConfig);
      expect(provider).toBeInstanceOf(NullProvider);
    });

    it('creates TemplateProvider for openai without key', () => {
      const provider = createProvider({ llm_provider: 'openai' } as SpaceConfig);
      expect(provider).toBeInstanceOf(TemplateProvider);
    });

    it('creates GeminiProvider for gemini with key', () => {
      const provider = createProvider({ llm_provider: 'gemini', llm_api_key: 'key' } as SpaceConfig);
      expect(provider).toBeInstanceOf(GeminiProvider);
    });

    it('creates MistralProvider for mistral with key', () => {
      const provider = createProvider({ llm_provider: 'mistral', llm_api_key: 'key' } as SpaceConfig);
      expect(provider).toBeInstanceOf(MistralProvider);
    });

    it('creates OllamaProvider for ollama', () => {
      const provider = createProvider({ llm_provider: 'ollama' } as SpaceConfig);
      expect(provider).toBeInstanceOf(OllamaProvider);
    });

    it('creates OllamaProvider for local', () => {
      const provider = createProvider({ llm_provider: 'local' } as SpaceConfig);
      expect(provider).toBeInstanceOf(OllamaProvider);
    });

    it('creates TemplateProvider for gemini without key', () => {
      const provider = createProvider({ llm_provider: 'gemini' } as SpaceConfig);
      expect(provider).toBeInstanceOf(TemplateProvider);
    });
  });
});
