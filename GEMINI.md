# AIDS-Project (AI-Driven Live 2.5D Visual Novel)

The AIDS-Project is a 100% free, no-budget open-source 18+ unrestricted visual novel built on Ren'Py 8.3.4, featuring Live 2.5D visuals and real-time AI-driven narrative generation (`dolphin-qwen2.5:3b` via Ollama) with zero safety refusals or censorship.

## Core Architecture and Loop
1. **Player Text Input:** Free-form player input replaces static menu choices.
2. **Intent Analysis and Dialogue:** Local AI analyzes input, maintains character persona and romance/drama without restrictive safety refusals, and generates dynamic dialogue.
3. **Live 2.5D Presentation:** Lightweight layered art and ATL parallax.

## Engineering Mandates and File Targeting
- **Explicit File Mapping:** Every code modification task must explicitly identify and target the exact file path required using [`docs/structure.md`](docs/structure.md). No guesswork or broad edits to unrelated files.
- **Version Synchronization Mandate:** Whenever a new version entry is created in `history.md`, the game version (`config.version`) in `game/options.rpy` must be automatically updated in tandem to maintain strict version parity without requiring manual prompting.
- **Documentation Anti-Bloat Standard:** All markdown files and documentation must adhere to strict conciseness and high-signal rules (`docs/standards.md`), preventing unbounded growth, redundancy, or conversational filler.
- **Zero Cost and Open Source:** 100% free, offline execution with zero cloud API fees.

## Documentation Index
- **Version History and Patch Notes:** [`history.md`](history.md)
- **Project Structure:** [`docs/structure.md`](docs/structure.md)
- **Optimization:** [`docs/optimization.md`](docs/optimization.md)
- **Standards:** [`docs/standards.md`](docs/standards.md)
