# The script of the game goes in this file.

init python:
    import sys
    import os
    # Add python_modules to sys.path to enable imports from that directory
    python_modules_path = os.path.join(config.gamedir, "python_modules")
    if python_modules_path not in sys.path:
        sys.path.insert(0, python_modules_path)

    from story_personas import get_narrator_persona

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# Default narrator persona key
default narrator_persona_key = "optimistic"

label splashscreen:
    # Check if the player has already verified their age in a previous session
    if not persistent.is_adult:
        call screen age_warning
    return


# The game starts here.

label start:

    # Persona Selection Screen Call
    # Displays the custom narrator selection UI, allowing players to preview details and confirm.
    scene black with dissolve
    
    call screen narrator_selection
    $ narrator_persona_key = _return

    $ current_persona = get_narrator_persona(narrator_persona_key)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "You have chosen [current_persona.name]."

    e "You've created a new Ren'Py game with a dynamic narrator!"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
