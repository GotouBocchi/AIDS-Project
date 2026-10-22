# AIDS-Project (AI-Driven Live 2.5D Story)

The AIDS-Project is a dynamic visual novel built on **Ren'Py 8+**, featuring **Live 2.5D visuals** and real-time AI-driven narrative generation (local Gemma LLM).

## Core Architecture & Loop
1. **Player Text Input:** Free-form player input replaces static menu choices.
2. **Intent Analysis & Dialogue:** Local AI analyzes input, respects strict domain guardrails (constrained to storytelling), and generates dynamic dialogue.
3. **Live 2.5D Presentation:** Lightweight layered art and ATL parallax.

## Engineering Mandates & Documentation Index
- **Precision & Anti-Bloat:** All documentation and code must be strictly surgical, high-signal, and free of redundant information.
- **Tool & Dependency Version Control:** See [`docs/TOOL_VERSIONS.md`](docs/TOOL_VERSIONS.md).
- **Ren'Py Expert Protocol:** See [`docs/RENPY_AGENT.md`](docs/RENPY_AGENT.md).
- **Weak PC Optimization:** See [`docs/LOW_END_OPTIMIZATION.md`](docs/LOW_END_OPTIMIZATION.md).
- **Environment & Linting:** See [`docs/ENVIRONMENT_AND_LINTING.md`](docs/ENVIRONMENT_AND_LINTING.md).
