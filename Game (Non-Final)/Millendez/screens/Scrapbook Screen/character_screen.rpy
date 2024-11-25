screen character_info():
    tag menu
    use scrapbook

    hbox:
        xalign 0.5
        yalign 0.5

        grid 6 2:

            spacing 37

            vbox:
                imagebutton action ShowMenu("info_mari"):
                    idle chap_button_idle
                    hover chap_button_hover      
                text "Mari" style "text_pos"
            
            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Aurora" style "text_pos"

            if persistent.bellatrix:
                vbox:
                    imagebutton action ShowMenu("info_bellatrix"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Bellatrix" style "text_pos"
            
            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Ian" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Mary" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Noel" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover        
                    text "Aluna" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Josh" style "text_pos"
            
            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Kurt" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Jennie" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Larry" style "text_pos"

            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle chap_button_idle
                        hover chap_button_hover         
                    text "Victoria" style "text_pos"
                
            
screen info_mari():

    tag menu
    use scrapbook (character_info = False)

    hbox:
        xalign 0.1
        yalign 1.0
        add mari_profile at Transform (xsize=715, ysize= 880)

    hbox style "frame_pos":
        vbox:
            add frame_info at Transform (ysize = 514)
            text "Mari Luzviminda" style "info_font"
            text "Age: 18" style "info_font"
            text mari_info style "info_font" size 24

    textbutton _("Back") action ShowMenu("character_info"):
        xalign 0.9
        xoffset 10
        yalign 0.9


screen info_aurora():

    tag menu
    use scrapbook (character_info = False)

    hbox:
        xalign 0.1
        yalign 1.0
        add mari_profile at Transform (xsize=715, ysize= 880)

    hbox style "frame_pos":
        vbox:
            add frame_info at Transform (ysize = 514)
            text "Aurora Averill" style "info_font"
            text "Age: 18" style "info_font"
            text aurora_info style "info_font" size 24
            
    textbutton _("Back") action ShowMenu("character_info"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen info_bellatrix():

    tag menu
    use scrapbook (character_info = False)

    hbox:
        xalign 0.1
        yalign 1.0
        add mari_profile at Transform (xsize=715, ysize= 880)

    hbox style "frame_pos":
        vbox:
            add frame_info at Transform (ysize = 514)
            text "Bellatrix Wilkes" style "info_font"
            text "Age: 18" style "info_font"
            text bellatrix_info style "info_font" size 24
            
    textbutton _("Back") action ShowMenu("character_info"):
        xalign 0.9
        xoffset 10
        yalign 0.9

screen info_ian():

    tag menu
    use scrapbook (character_info = False)

screen info_mary():

    tag menu
    use scrapbook (character_info = False)

screen info_noel():

    tag menu
    use scrapbook (character_info = False)

screen info_aluna():

    tag menu
    use scrapbook (character_info = False)

screen info_josh():

    tag menu
    use scrapbook (character_info = False)

screen info_kurt():

    tag menu
    use scrapbook (character_info = False)

screen info_jennie():

    tag menu
    use scrapbook (character_info = False)

screen info_larry():

    tag menu
    use scrapbook (character_info = False)

screen info_victoria():
    
    tag menu
    use scrapbook (character_info = False)

screen info_nathan():

    tag menu
    use scrapbook (character_info = False)

screen info_emma():

    tag menu
    use scrapbook (character_info = False)

screen info_dylan():

    tag menu
    use scrapbook (character_info = False)

screen info_corazon():

    tag menu
    use scrapbook (character_info = False)



style info_pos:
    xoffset -280
    yoffset -200
    spacing 25

style frame_pos:
    xalign 0.8
    xoffset 25
    yoffset 300

style info_font:
    font gui.interface_text_font
    color "#000000"
    xoffset 50
    yoffset -450

define mari_info = "Background: A bright and curious young woman from the Philippines.\nShe lives with her single mother and has a close relationship with her\nfriends. She shares a deep, unspoken affection for her best friend,\nAurora, and dreams of one day confessing her feelings.\n\nPersonality: Kind, compassionate, and determined. She's often seen\nas quiet and reserved, but she has a strong sense of justice and will\ndo anything to protect those she loves. Her newfound power has made\nher even more resolute and driven."
define aurora_info = "Background: Mari's best friend and confidante. She comes from a \nsupportive family and is known for her intelligence and level-\nheadedness. She reciprocates Mari's feelings, but is hesitant to admit \nthem due to fear of rejection and the complexities of their friendship.\n\nPersonality: Loyal, empathetic, and analytical. She's always there \nfor Mari, offering support and advice. Aurora's intelligence and \nquick thinking often help Mari navigate challenging situations."
define bellatrix_info = "Background: A manipulative and ambitious young woman who harbors \nresentment towards Mari and her friends. She's often seen as a loner\nand is known for her cruel and cunning nature.\n\nPersonality: Jealous, vindictive, and power-hungry. Bellatrix will\nstop at nothing to get what she wants, and she's willing to use her \ncunning to manipulate others."
define ian_info = "Background: A bully who often targets Mari and her friends. He's known \nfor his aggressive behavior and lack of empathy\n\nPersonality: Arrogant, cruel, and impulsive. Ian is often driven\n by his own desires and will resort to violence to get his way."