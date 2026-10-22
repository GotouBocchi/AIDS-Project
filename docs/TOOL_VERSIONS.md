# Tool & Dependency Version Control (Pinned & Specific)

This document tracks the exact pinned and specific toolchains, engines, and library versions authorized for the AIDS-Project to ensure compatibility and stability across low-end target systems.

| Tool / Component | Specific Version | Purpose |
| :--- | :--- | :--- |
| **Ren'Py Engine** | `8.3.4` | Core visual novel engine runtime. |
| **Python** | `3.9.18` (Embedded) | Scripting and background worker execution. |
| **Local LLM Runtime** | `Ollama v0.5.1+` | Local model execution daemon. |
| **LLM Model** | `gemma2:2b-instruct-q4_K_M` | Dynamic narrative & dialogue generation (optimized for 2GB-4GB RAM). |
| **Python Linter** | `Ruff v0.6.9` / `Flake8 v7.1.1` | Code quality and formatting for `game/python_modules/`. |
| **Ren'Py Linter** | Built-in (`renpy.linter` in v8.3.4) | Script syntax, label, and asset validation. |
