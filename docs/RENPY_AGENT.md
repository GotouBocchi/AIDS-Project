# Ren'Py Expert Agent Protocol

## Purpose
To ensure 100% error-free Ren'Py DSL (`.rpy`) and embedded Python code, adhering strictly to Ren'Py 8+ documentation and syntax specifications.

## Core Rules & Validation
1. **Ren'Py Documentation Adherence:** All `.rpy` scripts, screens, characters, and transforms must strictly follow official Ren'Py 8+ syntax (e.g., proper indentation, `init python`, screen language definitions).
2. **Error Prevention & Linting:** 
   - No assumptions about Ren'Py internals; verify APIs against Ren'Py 8 documentation.
   - Run Ren'Py's built-in linting tool (`renpy.linter`) prior to finalizing any script changes to catch undefined labels, missing images, or syntax errors.
3. **Decoupled AI Logic:** Keep external Python modules (e.g., local LLM interfacing) completely decoupled in `game/python_modules/` to avoid polluting the Ren'Py UI thread.
