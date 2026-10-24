# Project Structure and File Map

Maps out every file and directory to ensure precise file targeting without repository-wide scans.

| Path | Purpose / Responsibility |
| :--- | :--- |
| `GEMINI.md` | Core project index, architecture overview, and agent guidelines. |
| `README.md` | Public-facing player overview, version status, and project vision. |
| `history.md` | Version history and patch notes (changelog). |
| `docs/structure.md` | This file map. |
| `docs/optimization.md` | Low-end PC hardware constraints, non-blocking threading, and asset budgets. |
| `docs/standards.md` | Pinned tool versions, prompt guardrails, and narrator personas architecture. |
| `game/script.rpy` | Ren'Py entry point, splashscreen age check (`age_warning`), and story flow. |
| `game/screens.rpy` | UI definitions, player text input screens, and 18+ content warning modal. |
| `game/narrator_selection.rpy` | Dedicated UI screen for previewing and confirming Narrator Persona selection. |
| `game/options.rpy` | Game configuration, window properties, and version tracking (`config.version`). |
| `game/gui.rpy` | Visual styling, fonts, and UI component parameters. |
| `game/libs/libs.txt` | Third-party library loading configuration and preload rules. |
| `game/python_modules/` | AI intent parsing, Ollama (`dolphin-qwen2.5:3b`) client, and ending state tracking. |
| `game/python_modules/story_personas.py` | Narrator Personas (Narrative Director frameworks) defining ending biases (Happy, Sad, Bad, Chaotic) and contextual constraints tied to character state and stage background feelings. |
