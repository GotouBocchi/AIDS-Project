# Changelog

All notable changes to the AIDS-Project will be documented in this file according to the project's versioning taxonomy:
- **Big Update (Major):** Changes major aspects of the gameplay.
- **Minor Update:** Changes gameplay in a small way.
- **Very Minor Update:** Does not change gameplay (documentation, UI polish, meta setup).

## [0.0.1] - 2026-10-22 (Very Minor Update)
### Added
- **18+ Content Warning Splashscreen & Readability Refinement:** Implemented `screen age_warning` in `game/screens.rpy` with clean modal structure, clear layman text, and intuitive "Yes, I am 18+" / "I am under 18" buttons before the main menu loads. (Does not change gameplay; classified as Very Minor Update).

## [0.0.0-dev] - 2026-10-22
### Initialized
- **Project Setup:** Initialized foundational workspace and documentation for AIDS-Project (AI-Driven Live 2.5D Visual Novel on Ren'Py 8.3.4).
- **18+ Unrestricted Mandate:** Established core project mandate for 18+ unrestricted mature narrative generation with zero safety refusals (`dolphin-qwen2.5:3b` via Ollama).
- **Narrator Personas:** Implemented `game/python_modules/story_personas.py` defining 4 Narrator Personas with ending biases (Optimistic, Melancholic, Fatalistic, Chaotic) and stage/character constraints.
- **Note:** Project is strictly in the initialization phase; no gameplay implementation or testing has been performed yet.
