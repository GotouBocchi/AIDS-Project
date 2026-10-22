# AIDS-Project: AI-Driven Live 2.5D Story

**AIDS-Project** is an experimental visual novel framework built on the Ren'Py engine. It combines **free-form player text input**, **dynamic AI-driven intent and dialogue generation**, and **Live 2.5D visual presentation** into a cohesive, living narrative experience.

## Project Vision & Gameplay Loop
- **Free-Form Player Input:** Players type their own actions and responses rather than selecting from rigid menus.
- **Dynamic AI Direction:** The local LLM interprets player intent and generates context-aware dialogue and story progression.
- **Domain Guardrails:** Strict system prompts restrict the local model (e.g., Hermes 3) to narrative roleplay and storytelling, ensuring predictable, high-quality output on weak hardware.
- **Live 2.5D Presentation:** Layered character assets and subtle parallax depth bring characters to life without performance lag.

## Technical Overview
- **Engine:** [Ren'Py](https://www.renpy.org/)
- **Core Technology:** Local LLM integration (Hermes 3 via Ollama) with intent analysis and strict prompt guardrails.
- **Architecture:** Modular Python/Ren'Py hybrid designed for real-time text processing and lightweight pseudo-3D rendering.

## Getting Started
(Initial setup and installation instructions will be added as the project develops.)
