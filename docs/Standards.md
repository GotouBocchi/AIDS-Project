# Development Standards

## 1. Pinned Tool Versions and Code Quality Stack
- **Ren'Py Engine:** `8.3.4` (Embedded Python `3.9.18`)
- **Local LLM Runtime:** `Ollama v0.5.1+`
- **LLM Model:** `dolphin-qwen2.5:3b` (Optimized for 8GB+ PCs, ~2GB RAM footprint; superior creative writing, roleplay, and romantic/dramatic narrative depth without restrictive refusal filters)
- **Python Linter and Formatter:** `Ruff v0.6.9` / `Flake8 v7.1.1`
- **Python Type Checker:** `mypy v1.11.2`
- **Ren'Py Code Validator:** Ren'Py Built-in Lint tool (via Ren'Py Launcher / CLI)

## 2. Narrator Personas (Narrative Director Frameworks)
Focusing exclusively on narrator personas (`game/python_modules/story_personas.py`), each narrator persona drives the story tone, pacing, and gravitational ending bias while maintaining strict constraints tied to character state and stage background feelings (lighting, ambiance, weather):
- **The Optimistic Chronicler (`optimistic`):** 
  - *Ending Bias:* Happy Ending Bias (★★★★★)
  - *Resolution Style:* Heartwarming emotional closure, mutual affection, and uplifting conclusions.
- **The Melancholic Archivist (`melancholic`):** 
  - *Ending Bias:* Bittersweet / Sad Ending Bias (★★★★★)
  - *Resolution Style:* Poignant farewells, emotional sacrifice, and quiet parting.
- **The Fatalistic Director (`fatalistic`):** 
  - *Ending Bias:* Bad / Dramatic Ending Bias (★★★★★)
  - *Resolution Style:* High-tension conflict, severe consequences, and tragic fallouts.
- **The Chaotic Wildcard (`chaotic`):** 
  - *Ending Bias:* Chaotic / Randomized Bias (★★★★★)
  - *Resolution Style:* Unpredictable plot twists, surreal shifts, and erratic narrative turns.

## 3. 18+ Unrestricted Content Mandate
- **Unrestricted Narrative Generation:** The AIDS-Project is strictly an 18+ adult project. All narrative generation powered by `dolphin-qwen2.5:3b` operates with zero safety refusals, censorship filters, or moralizing lectures.
- **Mature & Intimate Exploration:** Fully unrestricted exploration of romance, drama, dark themes, and adult content is fully supported and anchored directly into the narrator persona system prompts.

## 4. Prompt Guardrails and Objective Alignment
- **Strict System Anchoring:** Every prompt sent to Dolphin-Qwen2.5 is prefixed with character persona, affinity metrics, and standard narrative ending bias.
- **Anti-Drift Constraints:** Preventing fourth-wall breaks, lecturing, or out-of-scope wandering.
- **Output Structuring:** Clean parsing tags for Ren'Py.

## 5. Code Quality and Execution Guidelines
- **Python Linting:** Run `ruff check game/python_modules/` and `ruff format game/python_modules/` before finalizing Python code.
- **Ren'Py Validation:** Run Ren'Py's built-in Lint tool to verify `.rpy` scripts, label references, image assets, and dialogue integrity.
- **Asynchronous AI Execution:** All LLM calls must run on background threads (`threading.Thread`, daemon=True) to guarantee zero main-thread blocking and stable 60 FPS UI performance.
- **Strict Decoupling:** AI logic and intent parsing must remain isolated in `game/python_modules/`, completely subject to low-end hardware memory bounds.
- **Logical Code Placement:** New functions, UI screens, variables, or script blocks must be placed within their logically appropriate section inside existing files (e.g., UI screens near related menu screens in `game/screens.rpy`, script labels in `game/script.rpy`) rather than blindly appending them to the end of files.
