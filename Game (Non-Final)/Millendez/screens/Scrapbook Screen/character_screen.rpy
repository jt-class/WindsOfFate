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
                    idle "gui/button/chapter_button.png"
                    hover "gui/button/chapter_button_hover.png"         
                text "Mari" style "text_pos"
            
            if persistent.aurora:
                vbox:
                    imagebutton action ShowMenu("info_aurora"):
                        idle "gui/button/chapter_button.png"
                        hover "gui/button/chapter_button_hover.png"         
                    text "Aurora" style "text_pos"
            
            

screen info_mari():

    tag menu
    use scrapbook (character_info = False)

    hbox:
        xalign 0.1
        yalign 1.0
        add "images/Characters/Mari/mc_mari.png" at Transform (xsize=715, ysize= 880)

    hbox style "frame_pos":
        vbox:
            add "gui/frame.png" at Transform (ysize = 514)
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
        add "images/Characters/Mari/mc_mari.png" at Transform (xsize=715, ysize= 880)

    hbox style "frame_pos":
        vbox:
            add "gui/frame.png" at Transform (ysize = 514)
            text "Aurora Averill" style "info_font"
            text "Age: 18" style "info_font"
            text mari_info style "info_font" size 24
            


    textbutton _("Back") action ShowMenu("character_info"):
        xalign 0.9
        xoffset 10
        yalign 0.9




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

define mari_info = "Background: A bright and curious young woman from the Philippines.\nShe lives with her single mother and has a close relationship with her\nfriends. She shares a deep, unspoken affection for her best friend,\nAurora, and dreams of one day confessing her feelings.\nPersonality: Kind, compassionate, and determined. She's often seen\nas quiet and reserved, but she has a strong sense of justice and will\ndo anything to protect those she loves. Her newfound power has made\nher even more resolute and driven."
