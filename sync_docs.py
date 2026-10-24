"""
Documentation Synchronization Utility for AIDS-Project
Automatically checks and synchronizes project version, README.md, and docs/structure.md
based on empirical file scanning and game/options.rpy configuration.
"""

import os
import re
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_game_version() -> str:
    options_path = os.path.join(ROOT_DIR, "game", "options.rpy")
    if not os.path.exists(options_path):
        print(f"Error: {options_path} not found.")
        sys.exit(1)
    
    with open(options_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    match = re.search(r'define\s+config\.version\s*=\s*["\']([^"\']+)["\']', content)
    if match:
        return match.group(1)
    print("Error: config.version not found in game/options.rpy")
    sys.exit(1)


def sync_readme(version: str) -> None:
    readme_path = os.path.join(ROOT_DIR, "README.md")
    if not os.path.exists(readme_path):
        print(f"Warning: {readme_path} not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update version header and status badge
    updated = re.sub(r'\(v[0-9]+\.[0-9]+\.[0-9]+\)', f'(v{version})', content)
    updated = re.sub(r'Active Development \(`v[0-9]+\.[0-9]+\.[0-9]+`\)', f'Active Development (`v{version}`)', updated)

    if updated != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"SUCCESS: Synchronized README.md to version {version}")
    else:
        print("README.md is already up to date.")


def scan_game_files() -> list:
    game_dir = os.path.join(ROOT_DIR, "game")
    files_found = []
    for root, _, files in os.walk(game_dir):
        # Ignore cache, tl, saves, compiled rpyc, images
        if any(exc in root for exc in [".cache", "tl", "saves", ".mypy_cache", "cache"]):
            continue
        for file in files:
            if file.endswith((".rpyc", ".png", ".jpg", ".ogg", ".mp3")):
                continue
            rel_path = os.path.relpath(os.path.join(root, file), ROOT_DIR)
            files_found.append(rel_path.replace("\\", "/"))
    return sorted(files_found)


def auto_update_structure_doc() -> None:
    struct_path = os.path.join(ROOT_DIR, "docs", "structure.md")
    if not os.path.exists(struct_path):
        print(f"Warning: {struct_path} not found.")
        return

    with open(struct_path, "r", encoding="utf-8") as f:
        content = f.read()

    files = scan_game_files()
    added_count = 0
    
    for f in files:
        if f not in content:
            # Generate a descriptive placeholder based on file path/extension
            purpose = "Project source module or UI screen."
            if f.endswith(".rpy"):
                purpose = "Ren'Py script or screen definition file."
            elif f.endswith(".py"):
                purpose = "Python backend module."
            elif f.endswith(".txt"):
                purpose = "Configuration or text asset."

            new_row = f"| `{f}` | {purpose} |\n"
            
            # Insert before the last line or append right before python modules section
            if "| `game/python_modules/` |" in content:
                content = content.replace("| `game/python_modules/` |", f"{new_row}| `game/python_modules/` |")
            else:
                content = content.strip() + f"\n{new_row}"
            
            added_count += 1
            print(f"AUTO-DOC: Added missing file to docs/structure.md -> {f}")

    if added_count > 0:
        with open(struct_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"SUCCESS: Automatically updated docs/structure.md with {added_count} new files.")
    else:
        print("SUCCESS: docs/structure.md is fully up to date with all game files.")


def main() -> None:
    print("=== AIDS-Project Documentation Synchronizer ===")
    version = get_game_version()
    print(f"Detected game version: {version}")
    
    sync_readme(version)
    auto_update_structure_doc()
    print("=== Synchronization Complete ===")


if __name__ == "__main__":
    main()
