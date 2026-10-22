# Project Structure and File Map

Maps out every file and directory to ensure precise file targeting without repository-wide scans.

| Path | Purpose / Responsibility |
| :--- | :--- |
| `gemini.md` | Core project index and architecture overview. |
| `README.md` | Public-facing player overview and project vision. |
| `CHANGELOG.md` | Version history and patch notes. |
| `docs/structure.md` | This file map. |
| `docs/optimization.md` | Low-end PC hardware constraints and 2.5D asset budgets. |
| `docs/standards.md` | Pinned versions, prompt guardrails, and dating sim ending architecture. |
| `game/script.rpy` | Ren'Py entry point and story flow. |
| `game/screens.rpy` | UI definitions and player text input screens. |
| `game/options.rpy` | Game configuration and resolution settings. |
| `game/gui.rpy` | Visual styling and font configurations. |
| `game/python_modules/` | AI intent parsing, Ollama (`dolphin-qwen2.5:3b`) client, and ending state tracking. |
