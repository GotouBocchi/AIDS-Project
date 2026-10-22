# Optimization & Performance

Target hardware includes systems with limited RAM, older multi-core/single-core CPUs, and modest integrated GPUs running both local LLMs and Live 2.5D visual layers. 

## 1. The Optimization Protocol
- **Resource Auditing:** Every new script, asset layer, or background process must be audited for memory and GPU/CPU footprint.
- **Strict Veto Power:** Any architectural addition that causes noticeable input lag, memory leaks, texture bloat, or freezes on low-end hardware must be rejected or refactored before merging.

## 2. Core Restrictions for Low-End Hardware
- **Zero Main-Thread Blocking:** LLM queries, network requests, and heavy computations *must* run asynchronously (background threads/workers). The Ren'Py UI must remain responsive at 60 FPS with visual loading indicators.
- **Memory Bounds & Caching Limits:** State history and prompt context windows must be strictly bounded (e.g., sliding window of recent turns) to prevent exponential RAM growth during long gameplay sessions.
- **Live 2.5D Asset Optimization:** 
  - Use lightweight Ren'Py ATL (Animation and Transformation Language) for parallax and subtle motion rather than heavy external shaders or continuous particle systems.
  - Keep character layer count minimal (e.g., base, eyes, mouth, hair) and purge unused textures promptly from VRAM.
- **Local LLM Efficiency:** Prompt lengths must be optimized, and generation parameters (e.g., token limits, quantization profiles) configured conservatively to suit local inference speeds (e.g., Ollama running Gemma 2B).
