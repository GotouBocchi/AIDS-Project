# AIDS-Project (AI Driven Story)

The AIDS-Project is a dynamically generated visual novel where AI creates the scenario, climax, and ending in real-time. It leverages the Ren'Py engine to provide a structured yet flexible framework for storytelling.

## Core Objective
The primary goal is to move away from static, pre-written branching narratives. Instead, the game uses AI to:
- Generate unique story scenarios.
- Build tension towards a dynamic climax.
- Conclude with a satisfying, context-aware ending.

## Technical Context for AI Agents
- **Engine:** Ren'Py (Python-based DSL).
- **AI Core:** **Python** integration with a **Local LLM** (e.g., via Ollama, LocalAI, or custom Python modules).
- **Architecture:** 
  - `game/script.rpy`: Main entry point and story flow logic.
  - `game/python_modules/`: (Planned) Dedicated directory for AI logic and LLM interfacing.
  - `game/screens.rpy`: UI definitions.
- **Dynamic Integration:** Story beats, dialogue, and choices will be fetched from a local Python service or module that interfaces with the LLM.
- **Resolution:** 1920x1080 (standard HD).
- **Coding Standards:** 
  - Keep AI logic decoupled from Ren'Py's display logic.
  - Use asynchronous calls where possible to prevent UI freezing during LLM generation.
  - Prioritize local performance and efficient prompt engineering.
