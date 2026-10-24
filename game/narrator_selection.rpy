################################################################################
## Narrator Selection Screen (AIDS-Project)
## Displays persona options and rich details before starting the story.
################################################################################

screen narrator_selection():
    default current_key = "optimistic"

    frame:
        background "#030712f8"
        xfill True
        yfill True
        padding (70, 50)

        vbox:
            spacing 30
            xfill True

            # Title & Subtitle with generous spacing and readable sizes
            vbox:
                spacing 8
                xalign 0.5
                text "CHOOSE NARRATOR PERSONA" size 42 color "#00f0ff" bold True xalign 0.5
                text "Select the narrative director framework that will shape your story's tone, pacing, and outcome." size 20 color "#94a3b8" xalign 0.5 text_align 0.5

            null height 10

            hbox:
                spacing 45
                xfill True
                yfill True

                # Left side: List of Personas (scrollable/spacious buttons)
                vbox:
                    spacing 16
                    xsize 520

                    python:
                        from story_personas import NARRATOR_PERSONAS
                        personas_list = list(NARRATOR_PERSONAS.values())

                    for p in personas_list:
                        button:
                            xfill True
                            padding (25, 22)
                            background ("#cc006655" if current_key == p.key else "#0f172acc")
                            hover_background "#cc006699"
                            action SetScreenVariable("current_key", p.key)
                            
                            vbox:
                                spacing 6
                                text p.name size 24 color "#ffffff" bold True
                                text p.genre_setting size 15 color "#38bdf8"

                # Right side: Persona Details Panel
                python:
                    active_persona = NARRATOR_PERSONAS.get(current_key)

                frame:
                    background "#0f172aee"
                    padding (50, 45)
                    xfill True
                    yfill True
                    
                    vbox:
                        spacing 25
                        xfill True

                        text active_persona.name size 32 color "#cc0066" bold True
                        
                        vbox:
                            spacing 6
                            text "GENRE SETTING" size 14 color "#64748b" bold True
                            text active_persona.genre_setting size 18 color "#f8fafc"

                        vbox:
                            spacing 6
                            text "ENDING BIAS" size 14 color "#64748b" bold True
                            text active_persona.ending_bias size 18 color "#38bdf8"

                        vbox:
                            spacing 6
                            text "DESCRIPTION & MANDATE" size 14 color "#64748b" bold True
                            text active_persona.description size 18 color "#e2e8f0" line_spacing 6

                        null height 15

                        # Prominent, highly clickable confirmation button
                        textbutton "CONFIRM SELECTION":
                            xalign 0.5
                            padding (50, 18)
                            background "#cc0066"
                            hover_background "#ff1a8c"
                            text_color "#ffffff"
                            text_bold True
                            text_size 20
                            action Return(current_key)
