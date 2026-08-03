---
type: "index"
hub: true
title: "Ml Frameworks Index"
description: "Listing of the ml-frameworks/ folder (75 pages)."
tags: ["index"]
timestamp: "2026-08-03T00:00:00Z"
---

# Ml Frameworks

Part of [[wiki/index|Wiki Index]]. 75 pages.

## Pages
- [[wiki/ml-frameworks/anthropic-api|Anthropic API]] — Anthropic's hosted API for Claude models, with emphasis on safety, long contexts, and tool use
- [[wiki/ml-frameworks/anthropic-sdk|Anthropic SDK]] — Official client libraries for the Claude API including Messages, streaming, and tool use
- [[wiki/ml-frameworks/batching-strategies|Batching Strategies]] — Scheduling policies that group requests to maximize serving efficiency
- [[wiki/ml-frameworks/bf16-training|BF16 Training]] — Training in bfloat16, which keeps the FP32 exponent range while halving memory footprint
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The chat endpoint pattern (messages in, assistant message out) that most LLM APIs standardize on
- [[wiki/ml-frameworks/checkpointing-training|Checkpointing During Training]] — Saving model state periodically so training can resume after interruption or failure
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — Compile-time transformations that optimize model graphs for target hardware
- [[wiki/ml-frameworks/context-distillation|Context Distillation]] — Compressing a long context or retrieved knowledge into a model via fine-tuning
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — Serving technique that schedules token generation across requests at every step
- [[wiki/ml-frameworks/data-loaders-and-pipelines|Data Loaders and Pipelines]] — Infrastructure that streams, shuffles, and preprocesses training data into the training loop
- [[wiki/ml-frameworks/deepspeed|DeepSpeed]] — Microsoft library for distributed training and inference of very large models
- [[wiki/ml-frameworks/dense-vs-sparse-models|Dense vs Sparse Models]] — Trade-offs between dense models that use all parameters per token and sparse MoE models
- [[wiki/ml-frameworks/distillation-vs-quantization|Distillation vs Quantization]] — Comparing two model-compression approaches: teaching a smaller model versus compressing weights
- [[wiki/ml-frameworks/dspy-autogen-crewai|DSPy, AutoGen, and CrewAI]] — Programmatic and multi-agent frameworks: DSPy optimizes prompts, AutoGen and CrewAI orchestrate agent teams
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — Running models on user-adjacent devices or servers to cut latency and preserve privacy
- [[wiki/ml-frameworks/embeddings-api|Embeddings API]] — Hosted endpoints that convert text into dense vectors for search, clustering, and classification
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — Running held-out evaluations on checkpoints while training is still in progress
- [[wiki/ml-frameworks/flash-attention|Flash Attention]] — IO-aware attention algorithm that avoids materializing the full attention matrix
- [[wiki/ml-frameworks/google-gemini|Google Gemini]] — Google's hosted API for Gemini models via the Generative Language API and Vertex AI
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — Training technique that sums gradients over several micro-batches before applying an optimizer step
- [[wiki/ml-frameworks/haystack|Haystack]] — Open-source framework for building production RAG and search pipelines with modular components
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — The hub, libraries, and community platform that standardizes model sharing and ML tooling
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — Runtime software that loads trained LLM weights and serves token generation efficiently
- [[wiki/ml-frameworks/jax|JAX]] — Google's numerical library with autodiff and XLA compilation, popular for ML research and TPU training
- [[wiki/ml-frameworks/kernels-and-inference-optimization|Kernels and Inference Optimization]] — Low-level GPU kernel techniques that speed up model forward passes
- [[wiki/ml-frameworks/langchain-framework|LangChain Framework]] — Popular framework for composing LLM calls with tools, retrievers, and memory into chains and agents
- [[wiki/ml-frameworks/langchain|LangChain]] — A framework for composing LLM applications: chains, agents, retrieval, and integrations
- [[wiki/ml-frameworks/langgraph-llamaindex|LangGraph and LlamaIndex]] — Frameworks for graph-structured agent state and data-centric RAG pipelines respectively
- [[wiki/ml-frameworks/litellm|LiteLLM]] — Proxy and SDK that normalizes hundreds of LLM providers behind one OpenAI-compatible interface
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — A C/C++ inference engine for running quantized LLMs efficiently on CPU and GPU
- [[wiki/ml-frameworks/llamaindex|LlamaIndex]] — A data framework for connecting LLMs to enterprise and personal data via indexing and retrieval
- [[wiki/ml-frameworks/long-context-techniques|Long Context Techniques]] — Methods for extending or effectively using very long model contexts
- [[wiki/ml-frameworks/lora-adapters|LoRA Adapters]] — The small trainable matrices that LoRA adds to each layer for parameter-efficient tuning
- [[wiki/ml-frameworks/low-rank-adaptation|Low-Rank Adaptation (LoRA)]] — Parameter-efficient fine-tuning that trains small low-rank update matrices instead of full weights
- [[wiki/ml-frameworks/mixed-precision-training|Mixed Precision Training]] — Training that stores some tensors in low precision and others in full precision to save memory and speed up compute
- [[wiki/ml-frameworks/mlflow-model-registry|MLflow Model Registry]] — Central catalog for versioned models with stage transitions from staging to production
- [[wiki/ml-frameworks/model-composition|Model Composition]] — Building systems from multiple models or adapters rather than a single monolithic model
- [[wiki/ml-frameworks/model-merging|Model Merging]] — Combining weights from multiple fine-tuned models into one capable model
- [[wiki/ml-frameworks/moe-architectures|Mixture-of-Experts Architectures]] — Model architecture that routes tokens through a subset of expert networks per layer
- [[wiki/ml-frameworks/ollama|Ollama]] — A local-first runtime for serving open-weight models with a simple API and CLI
- [[wiki/ml-frameworks/on-device-llm|On-Device LLMs]] — Language models that run locally on phones, laptops, or embedded hardware
- [[wiki/ml-frameworks/onnx-runtime|ONNX Runtime]] — Cross-platform inference engine that runs models in the Open Neural Network Exchange format
- [[wiki/ml-frameworks/onnx|ONNX]] — Open Neural Network Exchange: an open model format for interoperability across frameworks and runtimes
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — OpenAI's hosted API surface: chat completions, embeddings, fine-tuning, and tool calling
- [[wiki/ml-frameworks/openai-sdk|OpenAI SDK]] — Official client libraries for calling OpenAI chat, completion, embedding, and assistant APIs
- [[wiki/ml-frameworks/openrouter-prompt-caching|OpenRouter and Prompt Caching]] — Multi-provider API gateway plus automatic caching of shared prompt prefixes to cut cost and latency
- [[wiki/ml-frameworks/paged-attention|Paged Attention]] — Attention memory manager that stores KV cache in non-contiguous pages like virtual memory
- [[wiki/ml-frameworks/peft-methods|PEFT Methods]] — Parameter-efficient fine-tuning techniques including LoRA, prefix tuning, and adapters
- [[wiki/ml-frameworks/pipeline-parallelism|Pipeline Parallelism]] — Distributed training that splits model layers across devices and streams micro-batches through them
- [[wiki/ml-frameworks/prefill-and-decode|Prefill and Decode]] — LLM inference splits each request into a parallel prefill phase and a token-by-token decode phase
- [[wiki/ml-frameworks/prefill-decode-disaggregation|Prefill/Decode Disaggregation]] — Separating the prefill and decode phases onto different serving resources
- [[wiki/ml-frameworks/pruning-and-sparsity|Pruning and Sparsity]] — Removing or zeroing model weights to reduce size and compute
- [[wiki/ml-frameworks/pytorch|PyTorch]] — Meta's Python deep-learning framework, the de facto standard for training and serving LLMs
- [[wiki/ml-frameworks/qlora-adapter-merging|QLoRA and Adapter Merging]] — Quantized LoRA training and the practice of merging adapters into base weights for deployment
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — Designing request and token limits that protect services while allowing legitimate traffic
- [[wiki/ml-frameworks/rope-embeddings-sliding-window|RoPE and Sliding Window Attention]] — Positional encoding and attention-window techniques that enable long-context models
- [[wiki/ml-frameworks/routing-models|Routing Models]] — Systems that dispatch each request to the most suitable model or adapter
- [[wiki/ml-frameworks/runs|Training Runs]] — A single execution of a training or fine-tuning job tracked with config, metrics, and artifacts
- [[wiki/ml-frameworks/semantic-kernel|Semantic Kernel]] — Microsoft SDK for building AI applications with plugins, planners, and memory across languages
- [[wiki/ml-frameworks/server-sent-events|Server-Sent Events]] — HTTP streaming transport that pushes model tokens to clients as they are generated
- [[wiki/ml-frameworks/serverless-inference|Serverless Inference]] — On-demand LLM inference where capacity scales automatically and you pay per use
- [[wiki/ml-frameworks/sharding-data-parallel|Sharded Data Parallelism]] — Distributed training strategy that replicates the model while sharding optimizer state across GPUs
- [[wiki/ml-frameworks/small-language-models|Small Language Models]] — Compact models tuned for efficiency, speed, and on-device deployment
- [[wiki/ml-frameworks/sparse-experts|Sparse Experts]] — The expert modules in MoE models that activate only for a subset of tokens
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — Incrementally delivering LLM output as tokens are generated, reducing perceived latency
- [[wiki/ml-frameworks/tensor-parallelism|Tensor Parallelism]] — Distributed training and inference that splits individual weight tensors across multiple GPUs
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — Google's ML framework with production serving focus, used across Google's model stack
- [[wiki/ml-frameworks/tensorrt-llm|TensorRT-LLM]] — NVIDIA toolkit that compiles LLMs into highly optimized TensorRT engines for GPU serving
- [[wiki/ml-frameworks/tgi|Text Generation Inference]] — Hugging Face serving stack for LLMs with continuous batching and tensor parallelism built in
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — Measuring token consumption and spend per request, user, and model
- [[wiki/ml-frameworks/tool-schemas|Tool Schemas]] — JSON Schema declarations describing a tool's name, description, and typed arguments for LLM tool calling
- [[wiki/ml-frameworks/tvm-and-llvm|TVM and LLVM]] — Compiler infrastructure used to generate and optimize machine code for ML workloads
- [[wiki/ml-frameworks/vllm|vLLM]] — A high-throughput inference and serving engine for LLMs, optimized with PagedAttention
- [[wiki/ml-frameworks/wandb-and-experiment-tracking|W&B and Experiment Tracking]] — Platforms that log metrics, artifacts, and hyperparameters for training experiments
- [[wiki/ml-frameworks/zero-stage|ZeRO Stages]] — DeepSpeed optimization levels that shard optimizer state, gradients, and parameters across GPUs
