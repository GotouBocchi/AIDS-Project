################################################################################
## Narrator Selection Screen (AIDS-Project)
## Displays persona options and rich details before starting the story.
################################################################################

screen narrator_selection():
    default current_key = "optimistic"

    frame:
        background "#05050fee"
        xfill True
        yfill True
        padding (80, 60)

        vbox:
            spacing 25
            xfill True

            # Title & Subtitle
            text "CHOOSE NARRATOR PERSONA" size 36 color "#00f0ff" bold True xalign 0.5
            text "Select the narrative director framework that will shape your story's tone, pacing, and outcome." size 18 color "#94a3b8" xalign 0.5

            null height 15

            hbox:
                spacing 40
                xfill True
                yfill True

                # Left side: List of Personas
                vbox:
                    spacing 12
                    xsize 550

                    python:
                        from story_personas import NARRATOR_PERSONAS
                        personas_list = list(NARRATOR_PERSONAS.values())

                    for p in personas_list:
                        button:
                            xfill True
                            padding (20, 18)
                            background ("#ff007f44" if current_key == p.key else "#0f172acc")
                            hover_background "#ff007f66"
                            action SetScreenVariable("current_key", p.key)
                            
                            vbox:
                                spacing 4
                                text p.name size 20 color "#ffffff" bold True
                                text p.genre_setting size 13 color "#00f0ff"

                # Right side: Persona Details Panel
                python:
                    active_persona = NARRATOR_PERSONAS.get(current_key)

                frame:
                    background "#0f172aee"
                    padding (40, 35)
                    xfill True
                    yfill True
                    
                    vbox:
                        spacing 20
                        xfill True

                        text active_persona.name size 28 color "#ff007f" bold True
                        
                        vbox:
                            spacing 4
                            text "GENRE SETTING" size 13 color "#64748b" bold True
                            text active_persona.genre_setting size 16 color "#f8fafc"

                        vbox:
                            spacing 4
                            text "ENDING BIAS" size 13 color "#64748b" bold True
                            text active_persona.ending_bias size 16 color "#38bdf8"

                        vbox:
                            spacing 4
                            text "DESCRIPTION & MANDATE" size 13 color "#64748b" bold True
                            text active_persona.description size 16 color "#e2e8f0"

                        null height 20

                        textbutton "CONFIRM SELECTION":
                            xalign 0.5
                            padding (35, 15)
                            background "#ff007f"
                            hover_background "#db2777"
                            text_color "#ffffff"
                            text_bold True
                            text_size 18
                            action Return(current_key)
