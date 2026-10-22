# AIDS-Project (AI-Driven Live 2.5D Story)

The AIDS-Project is a dynamically generated visual novel featuring **Live 2.5D visuals** where AI creates the scenario, climax, and ending in real-time. It leverages the Ren'Py engine to provide a structured yet flexible framework for storytelling and immersive pseudo-3D presentation.

## Core Objective & Narrative Flow
The primary goal is to move away from static, pre-written branching narratives and flat sprites. Instead, the game operates on a fully dynamic loop:
1. **Player Text Input:** The player types free-form text input rather than choosing from static menu options.
2. **Intent Analysis & Story Generation:** The local AI analyzes the player's input to determine intent, context, and narrative direction.
3. **AI-Crafted Dialogue & Live 2.5D Direction:** The AI generates context-aware dialogue and emotional cues, keeping the narrative flowing toward a dynamic climax.

## Local LLM Guardrails & Domain Restriction
To ensure stability and prevent out-of-scope hallucinations on weak hardware:
- **System Prompts & Constraints:** Strict role-playing system prompts restrict the local LLM (e.g., Gemma 2B) to its trained domain (narrative storytelling, character dialogue, emotional tone mapping).
- **Output Validation:** Fallback mechanisms and regex/structural parsing ensure the AI response adheres to expected dialogue formats and does not wander off-script.

## Technical Context for AI Agents
- **Engine:** Ren'Py (Python-based DSL).
- **AI Core:** **Python** integration with a **Local LLM** (Ollama running Gemma).
- **Visuals:** Live 2.5D layered composition, lightweight ATL (Animation and Transformation Language) parallax, and modular expression mapping.
- **Architecture:** 
  - `game/script.rpy`: Main entry point and story flow logic.
  - `game/python_modules/`: (Planned) Dedicated directory for AI logic, intent parsing, and LLM interfacing.
  - `game/screens.rpy`: UI definitions and text input screens.
- **Resolution:** 1920x1080 (standard HD).
- **Coding Standards:** 
  - Keep AI logic decoupled from Ren'Py's display logic.
  - Use asynchronous calls where possible to prevent UI freezing during LLM generation.
  - Prioritize local performance and efficient prompt engineering.

## Performance & Optimization (Weak PC Mandate)
- **Constraint:** Target hardware includes systems with limited RAM, older CPUs, and modest integrated GPUs running both local LLMs and Live 2.5D graphics.
- **Mandate:** Every feature must be evaluated and restricted by the **Optimization Agent** protocol.
- **Guidelines:** Refer to `docs/LOW_END_OPTIMIZATION.md` for strict hardware restrictions, asynchronous execution rules, memory bounds, and lightweight 2.5D asset budgets.
