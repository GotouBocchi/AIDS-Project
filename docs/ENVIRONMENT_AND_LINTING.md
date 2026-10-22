# Environment & Linting Standards

## 1. Engine & Runtime Requirements
- **Ren'Py Version:** **Ren'Py 8+** (Mandatory for modern Python 3 support).
- **Python Runtime:** Embedded Python 3 (matching Ren'Py's internal runtime environment for compatibility).
- **AI Core:** Local LLM integration (Ollama running Gemma 2B) with strict system prompt domain restrictions.

## 2. Code Quality & Linting Standards ("The ESLint Equivalent")
To maintain clean, type-safe, and bug-free code across Python and Ren'Py:
- **Python Linting & Formatting:** Use **Ruff** or **Flake8** for fast, modern Python linting and formatting across custom modules in `game/python_modules/`.
- **Ren'Py Linting:** Use Ren'Py's built-in lint tool (`renpy.linter` / command-line lint) to validate script syntax, label references, and dialogue consistency before every release.
- **Coding Standards:** 
  - Keep AI logic strictly decoupled from Ren'Py's display logic.
  - Use asynchronous calls (`threading` with daemon threads) to prevent UI freezing during LLM generation.
  - Prioritize local performance, memory bounds, and efficient prompt engineering.
