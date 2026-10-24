# AIDS-Project: AI-Driven Interactive Story Game (v0.0.4)

AIDS-Project is a 100% free, open-source 18+ unrestricted AI-driven visual novel framework built on Ren'Py 8.3.4. 

> **Status:** **Active Development (`v0.0.4`)**. Features mandatory 18+ age verification, modular narrator selection screen (`game/narrator_selection.rpy`), narrator personas framework, and local LLM runtime (`dolphin-qwen2.5:3b` via Ollama) architecture.

## Project Vision & Architecture
- **18+ Unrestricted Mandate:** Unconstrained narrative generation (`dolphin-qwen2.5:3b` via Ollama) with zero safety refusals, censorship filters, or moralizing lectures.
- **Free-Form Player Input:** Designed to replace static menu choices with player text input.
- **Mandatory Age Verification:** Built-in modal age warning screen (`age_warning`) ensuring compliant 18+ access upon launch.
- **Narrator Selection & Personas (`game/narrator_selection.rpy`, `game/python_modules/story_personas.py`):** Interactive UI for previewing and confirming narrative director frameworks (Optimistic, Melancholic, Fatalistic, Chaotic) with distinct ending biases and behavioral rules.
- **Low-End PC Optimization:** Built to run locally on modest hardware with zero cloud API fees and asynchronous non-blocking inference.

## Quick Facts
- **100% Free & Offline:** No internet required, no subscriptions, and zero ads.
- **Engine:** Ren'Py 8.3.4 (Embedded Python 3.9.18).
- **AI Runtime:** Ollama with `dolphin-qwen2.5:3b`.

## Documentation & History
- **Version History & Status:** [`history.md`](history.md)
- **Project Structure:** [`docs/structure.md`](docs/structure.md)
- **Development Standards:** [`docs/standards.md`](docs/standards.md)
- **Optimization Guidelines:** [`docs/optimization.md`](docs/optimization.md)
