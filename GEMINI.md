# AIDS-Project (AI-Driven Live 2.5D Story)

The AIDS-Project is a dynamic visual novel built on **Ren'Py 8.3.4**, featuring **Live 2.5D visuals** and real-time AI-driven narrative generation (`gemma2:2b-instruct-q4_K_M` via Ollama).

## Core Architecture & Loop
1. **Player Text Input:** Free-form player input replaces static menu choices.
2. **Intent Analysis & Dialogue:** Local AI analyzes input, respects strict domain guardrails (constrained to storytelling), and generates dynamic dialogue.
3. **Live 2.5D Presentation:** Lightweight layered art and ATL parallax.

## Documentation Index
- **Optimization:** [`docs/Optimization.md`](docs/Optimization.md)
- **Standards:** [`docs/Standards.md`](docs/Standards.md)
