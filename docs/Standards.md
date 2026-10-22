# Development Standards

## 1. Pinned Tool Versions & Code Quality Stack
- **Ren'Py Engine:** `8.3.4` (Embedded Python `3.9.18`)
- **Local LLM Runtime:** `Ollama v0.5.1+`
- **LLM Model:** `hermes3:3b` (Optimized for weak PCs, ~2GB-3GB RAM; superior creative writing, roleplay, and romantic/dramatic narrative depth without restrictive refusal filters)
- **Python Linter & Formatter:** `Ruff v0.6.9` / `Flake8 v7.1.1`
- **Python Type Checker:** `mypy v1.11.2`
- **Ren'Py Code Validator:** Ren'Py Built-in **Lint** tool (via Ren'Py Launcher / CLI)

## 2. Code Quality & Execution Guidelines
- **Python Linting:** Run `ruff check game/python_modules/` and `ruff format game/python_modules/` before finalizing Python code.
- **Ren'Py Validation:** Run Ren'Py's built-in **Lint** tool to verify `.rpy` scripts, label references, image assets, and dialogue integrity.
- **Asynchronous AI Execution:** All LLM calls must run on background threads (`threading.Thread`, daemon=True) to guarantee zero main-thread blocking and stable 60 FPS UI performance.
- **Strict Decoupling:** AI logic and intent parsing must remain isolated in `game/python_modules/`, completely subject to low-end hardware memory bounds.
