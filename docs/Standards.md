# Development Standards

## 1. Pinned Tool Versions and Code Quality Stack
- **Ren'Py Engine:** `8.3.4` (Embedded Python `3.9.18`)
- **Local LLM Runtime:** `Ollama v0.5.1+`
- **LLM Model:** `hermes3:3b` (Optimized for weak PCs, ~2GB-3GB RAM; superior creative writing, roleplay, and romantic/dramatic narrative depth without restrictive refusal filters)
- **Python Linter and Formatter:** `Ruff v0.6.9` / `Flake8 v7.1.1`
- **Python Type Checker:** `mypy v1.11.2`
- **Ren'Py Code Validator:** Ren'Py Built-in Lint tool (via Ren'Py Launcher / CLI)

## 2. Character Personas and Standard Narrative Endings
Each character persona possesses intrinsic gravitational bias toward standard narrative ending archetypes:
- **Elena (Warm and Optimistic):** 
  - *Standard Happy Ending Bias:* ★★★★★ (5/5)
  - *Resolution Style:* Heartwarming emotional closure, mutual affection, and uplifting conclusions.
- **Lyra (Gentle and Melancholic):** 
  - *Standard Bittersweet / Sad Ending Bias:* ★★★★★ (5/5)
  - *Resolution Style:* Poignant farewells, emotional sacrifice, and bittersweet parting.
- **Vesper (Intense and Volatile):** 
  - *Standard Dramatic / Bad Ending Bias:* ★★★★★ (5/5)
  - *Resolution Style:* High-tension conflict, severe consequences, and tragic fallouts.

## 3. Prompt Guardrails and Objective Alignment
- **Strict System Anchoring:** Every prompt sent to Hermes 3 is prefixed with character persona, affinity metrics, and standard narrative ending bias.
- **Anti-Drift Constraints:** Preventing fourth-wall breaks, lecturing, or out-of-scope wandering.
- **Output Structuring:** Clean parsing tags for Ren'Py.

## 4. Code Quality and Execution Guidelines
- **Python Linting:** Run `ruff check game/python_modules/` and `ruff format game/python_modules/` before finalizing Python code.
- **Ren'Py Validation:** Run Ren'Py's built-in Lint tool to verify `.rpy` scripts, label references, image assets, and dialogue integrity.
- **Asynchronous AI Execution:** All LLM calls must run on background threads (`threading.Thread`, daemon=True) to guarantee zero main-thread blocking and stable 60 FPS UI performance.
- **Strict Decoupling:** AI logic and intent parsing must remain isolated in `game/python_modules/`, completely subject to low-end hardware memory bounds.
